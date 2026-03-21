# print("hello")
# message = 'hello world'
# print(message)
message = "bharat's world"
print(message)
print(message[1])



## Methods 
#lower
message = "Hello World"
print(message.lower())

#upper
print(message.upper())

#count
print(message.count("Hello"))

#find
print(message.find('World'))

# replace

message = print(message.replace("World","Universe"))
print(message)

# string contcatenation 

greeting = "namaste"
name = "Bharat"

print(greeting + ", " + name + ". Welcome!" )

message = '{}, {}.Welcome'.format(greeting,name)
reply = "i am pretty good"
mess = f'hey buddy how are you ? {reply.upper()}'
print(message)
print(mess)
# print(dir(mess))


# print(help(str))