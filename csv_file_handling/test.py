import csv

# open the file in read mode
file_path = r'D:\Coding_Vs_Code\Mini_Projects\csv_file_handling\data.csv'
# with open(file_path, 'r', newline='') as csv_file:
#     # create a reader object
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     # loop through the rows
#     for row in csv_reader:
#         # print the row as a list
#         print(row)

# with open(file_path, 'a', newline='') as csv_file:
#     # create a writer object
#     csv_writer = csv.writer(csv_file)
#     # write some data rows
#     csv_writer.writerow(['Saif', 25,])

# with open(file_path, 'r') as f:
#     f_reader = csv.DictReader(f)
#     for row in f_reader:
#         print(row)

# I want to read third row data
# with open(file_path, 'r') as f:
#     f_reader = csv.reader(f)
#     pos = f_reader.line_num
#     print(pos)
#     row = next(f_reader)
#     print(row)
#     pos = f_reader.line_num
#     print(pos)


# open the file in read mode
with open(file_path, 'r', newline='') as csv_file:
    # create a reader object
    csv_reader = csv.reader(csv_file)
    # get the current position of the cursor
    pos = csv_file.tell()
    # print the position
    print(pos)
    # read the first row
    row = next(csv_reader)
    # print the row as a list
    print(row)
    # get the current position of the cursor
    pos = csv_file.tell()
    # print the position
    print(pos)
