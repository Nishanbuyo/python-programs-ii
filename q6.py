def search(list1):
    for name in list1:
        if name == "John":
            return "Found"

    return "Not Found"

list1 = ["Stephen", "Elena", "Jeremy", "Taylor"]
list2 = ["Stephen", "Elena", "John", "Jeremy", "Taylor"]
print(search(list1))
print(search(list2))