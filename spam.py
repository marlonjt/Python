def reverse_words(text):
    r = []
    for res in text.split(" "):
        r.append(res[::-1])
    return " ".join(r), type(r)


print(reverse_words("  double  spaced  words  "))
