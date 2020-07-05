list_of_tuples = [
    ('Ram', 'Suwal', 22),
    ('Hari', 'Gilbert', 55),
    ('Gita', 'Taylor', 21),
    ('Sita', 'Nelson', 33),
    ('Jeremy', 'Watson', None),
    ('Penny', 'Swift', 61),
    ('Bruce', 'Doe', None)
]

def calculate_average(list_of_tuples):
    mean_age =0
    for tup in list_of_tuples:
        if tup[2] is not None:
            mean_age+=tup[2]
    return mean_age

average_age = int(calculate_average(list_of_tuples)/len(list_of_tuples))
print(average_age)

for tup in list_of_tuples:
    if tup[2] is None:
        print(tup[0], "Unknown age")
    elif tup[2]> average_age:
        print(tup[0], "old")
    else:
        print(tup[0], "young")
    
