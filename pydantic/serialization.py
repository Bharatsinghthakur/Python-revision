# to covert our pydantic models into python dictionaries -- we have -- model_dump()
# to convert our pydantic models into json we have -- model_dump_json()
# python keep dictionares in { } with single quote fields -- type -- class 'dict'
# python keep json in { } with double quote fields -- type -- class 'str'

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:str
    
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    
address_dict = {'city':'new delhi','state':'delhi','pincode':'20222'}
address1 = Address(**address_dict)

patient_dict = {'name':'Bharat','gender':"male",'age':'25','address':address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()

temp1 = patient1.model_dump(exclude_unset=True)

print(patient1)
print(type(patient1))
print(temp)
print(type(temp))