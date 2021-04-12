import pandas
#reading data
df = pandas.read_csv('CSVTestFile2.csv')
print(df)

#writing data

#reading from file2
df = pandas.read_csv('CSVTestFile2.csv', 
            index_col='Employee', 
            header=0, #header line
            names=['Employee', 'Dept', 'Birth_month']) #headers
#writing to another csv file
df.to_csv('CSVTestFile3.csv')