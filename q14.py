import csv

def read_csv(filename):
    with open(filename) as csv_file:
        out_dict = [{k: v for k, v in row.items()} for row in csv.DictReader(csv_file)]
    print(out_dict)
    



read_csv('file.csv')