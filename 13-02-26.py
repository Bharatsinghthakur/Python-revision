# try and except block 

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

try:
    f = open('test.txt')
    # if f.name == "test.txt":
    #     raise Exception               ## if we want to raise exception by our own
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e,"exception has been raised")
else:
    print(f.read())
    f.close()
finally:
    print('This is the block where we should close the db connections')
