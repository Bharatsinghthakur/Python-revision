# Model Validator
# sometimes we have to validate or mandate some conditions like if patient age is more than 60 it should have the
# emergency contact number  - value of validation is on two field age and contact


from pydantic import BaseModel, EmailStr , model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return self
    


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
    "email": "bharat@gmail.com",
    "age": "26",  # we are provding age as string intentionally
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "bharat@gmail.com", "mobile": "1234567891"},
}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)
