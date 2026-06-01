import csv
def opencsv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        output = []
        for i in reader:
            output.append(i)
        return output

def writecsv(filename, the_list):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)