# CSV MODULE 
import csv

# with context manager 

# csv reader method now in background is using something called as 
# dilect that has come present parameters for what is expects the format 
# of our csv file to be so by default .


# Read the file as read more csv with reader
with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)

    # next(csv_reader) 
    # next help us to step over our value in iterable 
    # we can use diffrent delimeter
    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')
        
        for line in csv_reader:
           csv_writer.writerow(line)


with open('new_names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file,)
    for line in csv_reader:
        print(line)
