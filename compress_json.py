#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import zipfile
from datetime import date
from glob import glob
from pathlib import Path

if os.name == "nt":
    import ctypes
    from ctypes import windll, wintypes
    from uuid import UUID

    # ctypes GUID copied from MSDN sample code
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8),
        ]

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            (
                self.Data1,
                self.Data2,
                self.Data3,
                self.Data4[0],
                self.Data4[1],
                rest,
            ) = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest >> (8 - i - 1) * 8 & 0xFF

    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID),
        wintypes.DWORD,
        wintypes.HANDLE,
        ctypes.POINTER(ctypes.c_wchar_p),
    ]

    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value

    FOLDERID_Download = "{374DE290-123F-4565-9164-39C4925E467B}"

    def get_download_folder():
        return _get_known_folder_path(FOLDERID_Download)

else:
    from gi.repository import GLib

    def get_download_folder():
        return GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOWNLOAD)


home_path = Path.home()
download_path = get_download_folder()
save_dir = f"{home_path}/session"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

file_list = glob(f"{download_path}/*.json")

if file_list:
    zip_name = f"session_data_{date.today().strftime('%Y%m%d')}"
    zip_file = f"{save_dir}/{zip_name}.zip"
    with zipfile.ZipFile(zip_file, "w") as zip:
        for file_name in file_list:
            zip.write(file_name, os.path.basename(file_name))
            os.remove(file_name)
