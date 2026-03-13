# CSV MODULE 
import csv

# with context manager 

# csv reader method now in background is using something called as 
# dilect that has come present parameters for what is expects the format 
# of our csv file to be so by default .

# Read the file as read more csv with reader
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)

    # next(csv_reader) 
    # next help us to step over our value in iterable 
    # we can use diffrent delimeter
    # with open('new_names.csv','w') as new_file:
    #     csv_writer = csv.writer(new_file,delimiter='\t')
        
    #     for line in csv_reader:
    #        csv_writer.writerow(line)


# with open('new_names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter='\t')
   
#     for line in csv_reader:
#         print(line)


# with open('names.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['email'])

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
## we have to specify the filednames in dictionary for write 
    with open('new_names.csv','w',newline="") as new_file:
        fieldnames = ['first_name','last_name','email']
        # if you want to remove the email 
        
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')
       
        # we can specify the header name as well
        
        csv_writer.writeheader()
        
        for line in csv_reader:
           # we can remove the email as well
            # del line['email']
            csv_writer.writerow(line)


