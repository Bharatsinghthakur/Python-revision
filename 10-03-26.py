# file Objects

f = open('text.txt','r')
print(f.mode)

f.close()

# context manager  -- we need to work for file in this only
with open('text.txt','r') as f:
    f_contents = f.read()
    print(f_contents,end='')

with open('text.txt','r') as f:
    f_contents = f.readline()
    print(f_contents,end='')

with open('text.txt','r') as f:
    f_contents = f.readlines()
    print(f_contents,end='')

# we have access for this variable here but we cannot read or write this file
# print(f.closed)
# print(f.read())


# if line has thousands of line and if we go through that 
# we can run out of memory for that we can read in efficent way like this

with open('text.txt','r') as f:
    for line in f:
        print(line, end="")

with open('text.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0 :
        print(f_contents, end='') 
        f_contents = f.read(size_to_read)

with open('text.txt','r') as f:
        size_to_read = 10
        f_contents = f.read(size_to_read)
        print(f_contents, end ="")
        f_contents = f.read(size_to_read)
        print(f_contents)


        # print(f.tell())  this will tell where is our cursor 


with open('text2.txt','w') as f:
     f.write('test')
     f.seek(0)
     f.write('R')


with open('text.txt','r') as rf:
     with open('text_copy.txt','w') as wf:
          for line in rf:
               wf.write(line)



with open('text.txt','rb') as rf:
     with open('text_copy.txt','wb') as wf:
          for line in rf:
               wf.write(line)


# This is for chunk size of ours as we want more control of filke by not going line by line

# with open('text.txt','rb') as rf:
#      with open('text_copy.txt','wb') as wf:
#           chunk_size = 4096
#           rf_chunk = rf.read(chunk_size)
#           while len(rf_chunk) > 0 :
#                wf.write(rf_chunk)
#                rf_chunk = rf.read(chunk_size)