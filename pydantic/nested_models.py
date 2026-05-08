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

print(patient1.address)
print(patient1.address.pincode)



# better organziation of releated (eg:vitals,address,insuracne)

# resuablity: Use vitals in multiple models (eg:patient,Medical Record)

# validation : Nested Models are validated automatically - no extra work needed
