# FIELD VALIDATOR

# It is used to validate the custom level of validation according to client needs - for eg we have email where
# we have to check weather the employee is from certain company or not from his email
# as well as we can you use tranformation as well


from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.capitalize()
    
        
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
    
    
patient_info = {
    "name": "bharat",
    'email':"bharat@hdfc.com",
    "age": "26",
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "bharat@gmail.com", "mobile": "1234567891"},
}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)