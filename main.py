#!/usr/bin/python3.7
import csv

#
# with open('test1.csv') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)


def load_csv(filename):
    dataSet=[]
    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            dataSet.append(dict(row))
    return dataSet

data=load_csv('csv/test1.csv')
for row in data:
    print(row)


# def loadCSV(filename):
#     dataSet=[]
#     with open(filename,'r') as file:
#         csvReader=csv.reader(file)
#         for line in csvReader:
#             dataSet.append(line)
#     return dataSet
# data = loadCSV('csv/test1.csv')
# for row in data:
#     print(row)

#
# for row in data:
#     print(data)

# with open('space.csv') as file:
#     reader=csv.reader(file, delimiter=' ')
#     for row in reader:
#         print(row)

# with open('dollor.csv') as file:
#     reader=csv.reader(file, delimiter='$')
#     for row in reader:
#         print(row)


# with open('csv/test1.csv') as file:
#     print(type(file))
#     reader = csv.DictReader(file)
#     print(type(reader))
#
#     for row in reader:
#
#         # print(row)
#          print(dict(row))


    #input and then output
# with open('test1.csv') as f:
#     reader = csv.reader(f)
#     with open('inout', 'w', newline='') as file:
#         thewriter = csv.writer(file)
#         for row in reader:
#
#             thewriter.writerow(row)

# with open('test1.csv') as f:
#     reader=csv.DictReader(f)
#     reader1=csv.reader(f)
#     with open('inoutDic.csv', 'w', newline='') as file:
#         fields = ['Monday', ' Tuesday', ' Wednesday', ' Thursday', ' Friday', ' Saturday', ' Sunday']
#
#         thewriter = csv.DictWriter(file, fieldnames=fields)
#         thewriter.writeheader()
#         for row in reader:
#
#             thewriter.writerow(row)