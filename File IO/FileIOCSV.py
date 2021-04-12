import csv
#reading csv file
with open('TestFileForCSV.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Total lines processed: {line_count}.')

#writing in csv
with open('CSVTestFile2.csv', mode='w') as CSVTestFile2:
    employee_writer = csv.writer(CSVTestFile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['Rahul', 'Accounting', 'November'])
    employee_writer.writerow(['Sarvesh', 'IT', 'March'])