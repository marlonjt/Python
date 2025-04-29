from datetime import datetime, date


date_now = datetime.now()

print(type(date_now), date_now)

myBirthday = datetime.strptime("03-02-2000-12:10:02-548513", "%d-%m-%Y-%I:%M:%S-%f")
formatted_birthday = myBirthday.strftime("%d-%m-%Y-%I:%M:%S-%f")

print(type(myBirthday), myBirthday)
print(type(myBirthday), formatted_birthday)


def calculate_birthday(myBirthday):
    act_year = date_now.year
    my_year = myBirthday.year

    years = int(act_year) - int(my_year)

    return years


print(f"Han pasado {calculate_birthday(myBirthday)} años")


"""
extra
"""

myBirthday = datetime.strptime("03-02-2000-12:10:02-548513", "%d-%m-%Y-%I:%M:%S-%f")

print(f"Year:{myBirthday.year}")
print(f"Mont:{myBirthday.month}")
print(f"Day:{myBirthday.day}")
print(f"Hour:{myBirthday.hour}")
print(f"Minute:{myBirthday.minute}")
print(f"Second:{myBirthday.second}")
print(f"Microsecond:{myBirthday.microsecond}")
