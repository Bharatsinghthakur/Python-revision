# pyadantic
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

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
    # name: str = Field(max_length=50)
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the name of the patient in less than 50 chars",
            examples=["niko", "neo"],
        ),
    ]
    age: int = Field(gt=0, lt=120)
    email: Optional[EmailStr] = None
    linkedIn: Optional[AnyUrl] = None
    # weight: float = Field(gt=0)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None, description="is the patient married")]
    # allergies: Optional[List[str]] = None
    allergies: Annotated[Optional[List[str]], Field(default=None, maxlength=5)]
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

