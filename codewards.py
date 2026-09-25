def printer_error(s):
    # your code
    other_letter = ""
    for letter in s:
        if letter not in "abcdefghijklm":
            other_letter += letter
    return f"{len(other_letter)}/{len(s)}"


print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))
