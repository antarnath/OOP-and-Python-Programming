def full_name(f_name, l_name):
    name = f"{f_name} {l_name}"
    return name

name = full_name(l_name="Nath", f_name="Antar")
# print(name)

def long_name(**kargs):
    print(kargs)
# long_name(first="Antar",last="Nath",middle="Chandra")


def all_type(first, *args, **kargs):
    print(first)
    for word in args:
        print(word)
    for key, value in kargs.items():
        print(key, value)
all_type("Antar", "aa", "bb", "cc", last="Nath", middle="Chandra",fast="Antar")