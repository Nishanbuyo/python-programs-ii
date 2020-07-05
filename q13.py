import csv
def list_to_csv(filename, data):
    with open(filename, 'w') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(['name', 'address', 'age'])
        for row in data:
            csv_file.writerow(row)
        

data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

list_to_csv('file.csv', data)
