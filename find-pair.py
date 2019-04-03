import itertools

import sys
import csv

items = {}
item_names = {}


# read price csv file
def read_file(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            #print(row[0],row[1])
            items[row[0]]=int(row[1])
            item_names.setdefault(int(row[1]),[]).append(row[0])


# finding the closest sum of two below balance
def finding_closest_two(numbers, balance):
    closest = []
    for i in itertools.combinations(numbers, 2):
        if sum(i) == balance:
            return i
        else:
            if sum(i) < balance:
                closest.append((balance - sum(i), i))

    if closest == []:
        return None
    else:
        return min(closest)[1]


# finding the closest sum of three below balance
def finding_closest_three(numbers, balance):
    closest = []
    for i in itertools.combinations(numbers, 3):
        if sum(i) == balance:
            return i
        else:
            if sum(i) < balance:
                closest.append((balance - sum(i), i))

    if closest == []:
        return None
    else:
        return min(closest)[1]


# main function
def main():

    if len(sys.argv) != 3:
        print("This command has wrong input parameters")
        print("python3 find-pair.py filename.txt balance")
        return

    read_file(sys.argv[1])

    balance = int(sys.argv[2])

    result = finding_closest_two(items.values(), balance)
    print("Choose Two:")
    if result is None:
        print("Not Possible")
        return

    coma = True
    for i in result:
        item = item_names[i][0]
        item_names[i].remove(item)
        if coma:
            print(item, i, end =", ")
            coma = False
        else:
            print(item, i)

    print("Choose Three: (Bonus Question)")
    items.clear()
    item_names.clear()
    read_file(sys.argv[1])
    result = finding_closest_three(items.values(), balance)
    if result is None:
        print("Not Possible")
        return

    coma = 2
    for i in result:
        item = item_names[i][0]
        item_names[i].remove(item)
        if coma>0:
            print(item, i, end=", ")
            coma = coma-1
        else:
            print(item, i)


if __name__ == "__main__":
    main()
