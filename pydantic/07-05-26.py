# pyadantic
from pydantic import BaseModel , EmailStr
from typing import List, Dict, Optional

# ty

# def inserted_patient_data(name:str,age:int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect Data types')

# def update_patient_data(name:str,age:int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise ValueError('Incorrect Value types')


# pydantic model -- which needs to create a schema
class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr[Optional] =
    weight: float
    married: bool = False
    allergies:Optional[List[str]] = None
    contact_details: Dict[str, str]  # key and value - both are string


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
    "age": "26",
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "bharat@mail.com", "mobile": "1234567891"},
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)

# steps for pydantic

# 1- build model that is class
# 2 - use that model to create a object
# 3 - then pass that model to your function
