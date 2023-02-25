def concatenate(*args, **kwargs):
    text = "".join(args)

    for key in kwargs:
        text = text.replace(key, kwargs[key])#if key in text replace with value of kwargs with key

    return text

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))