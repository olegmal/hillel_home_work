
def trimmed_str(my_str: str):
    new_str = ""

    for char in my_str[:25]:
        if char.isupper():
            new_str += char
    print(new_str)
    return new_str


trimmed_str("hdkdfkffOhdxbdjncLhjcdclOhs176U")
print(trimmed_str)
