"""
You are working on an authentication system and there is a set of rules the users have to follow when picking a new password:

I. It has to be at least 16 characters long.
II. The password cannot contain the word "password". This rule is not case-sensitive.
III. The same character cannot be used more than 4 times. This rule is case-sensitive, meaning "a" and "A" are considered different characters.
IV. The password has to contain at least one uppercase and one lowercase letter.
V. The password has to contain at least one of the following special characters: "*", "#", "@".

Task:

Write a function that takes in a password and returns a collection of any rule numbers that are not met.

Example Test Cases:
password_1 = "Strongpwd9999#ac" => []
password_2 = "Aess10#" => [1]
password_3 = "Password@" => [1,2]
password_4 = "#PassWord011111112222223x" => [2,3]
password_5 = "PASSWORDz#1111111" => [2,3]
password_6 = "aaaapassword$$" => [1,2,3,4,5]
password_7 = "LESS10#" => [1,4]
password_8 = "sSSSSt#passWord" => [1,2]
password_9 = "SsSSSt#passWordpassword" => [2,3]
password_10 = "aZ*" => [1]
password_11 = "123pa$s#s@WORD" => [1]
All test Cases:
validate(password_1) => []
validate(password_2) => [1]
validate(password_3) => [1,2]
validate(password_4) => [2,3]
validate(password_5) => [2,3]
validate(password_6) => [1,2,3,4,5]
validate(password_7) => [1,4]
validate(password_8) => [1,2]
9. validate(password_9) => [2,3]
10. validate(password_10) => [1]
11. validate(password_11) => [1]

"""
from collections import Counter


def validate(password):
    failed = []

    # At least 16 characters 

    if len(password) < 16:
        failed.append(1)
    
    # Cannot contain password
    if "password" in password.lower():
        failed.append(2)

    # no character appears more than 4 times

    counts = Counter(password)
    if any(count > 4 for count in counts.values()):
        failed.append(3)
    
    # must contain at least one uppercase and lowercase
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)

    if not(has_upper and has_lower):
        failed.append(4)
    
    # must contain atleast one special character(*,#,@)

    if not any(c in "@#*" for c in password):
        failed.append(5)
    
    return failed

password_1 = "Strongpwd9999#ac"
password_2 = "Aess10#"
password_3 = "Password@" 
password_4 = "#PassWord011111112222223x" 
password_5 = "PASSWORDz#1111111"
password_6 = "aaaapassword$$"
password_7 = "LESS10#"
password_8 = "sSSSSt#passWord"
password_9 = "SsSSSt#passWordpassword" 
password_10 = "aZ*" 
password_11 = "123pa$s#s@WORD"

print(validate(password_1))
print(validate(password_2))
print(validate(password_3))
print(validate(password_4))
print(validate(password_5))
print(validate(password_6))
print(validate(password_7))
print(validate(password_8))
print(validate(password_9))
print(validate(password_10))
print(validate(password_11))

