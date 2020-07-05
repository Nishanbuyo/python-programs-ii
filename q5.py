my_tuple = ('John', 'Doe', 34)

people = []
people.append(my_tuple)
print(people)


def append_colleagues():
    colleagues = (('Sam', 'Taylor', 43), ('Mark', 'Gilbert', 20),
                  ('Bishal', 'Suwal', 23), ('Daisy', 'Johnson', 22))
    for tup in colleagues:
        people.append(tup)
    return people


def sort(people):
    sort_fname = sorted(people, key=lambda x: x[0])
    sort_lname = sorted(people, key=lambda x: x[1])
    sort_age = sorted(people, key=lambda x: x[2])
    print("Sorted on the basis of first name: \n", sort_fname)
    print("Sorted on the basis of last name: \n", sort_lname)
    print("Sorted on the basis of age: \n", sort_age)


people = append_colleagues()
print("After appending colleagues: \n", people)
print("Sorting ...")
sort(people)
