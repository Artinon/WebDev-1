with open("data.csv") as row:
    content = row.readlines()
    for line in content:
        row_data = line.split(",")
        print("{0} is {1} years old and {2}.".format(str(row_data[0]), str(row_data[1]), str(row_data[2])))