def increment_string(string):

    stripped = string.rstrip("1234567890")
    ints = string[len(stripped) :]

    if len(ints) == 0:
        return string + "1"
    else:
        length = len(ints)
        new_ints = 1 + int(ints)
        new_ints = str(new_ints).zfill(length)
        return stripped + new_ints


print(increment_string("foo"))  # foo1
print(increment_string("foobar23"))  # foobar24
print(increment_string("foo099"))  # foo100
