# computed field - when we dont want to take the input from the user 
# on the go we want to calculate from the fileds already exist
from pydantic import BaseModel , EmailStr , computed_field
from typing import List , Dict 

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float #kg
    height:float #mtr
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi
    

    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.calculate_bmi)
    print("updated")
    
    
patient_info = {
    "name": "bharat",
    'email':"bharat@hdfc.com",
    "age": "26", # we are provding age as string intentionally 
    "height":1.54,
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"email": "bharat@gmail.com", "mobile": "1234567891"},
}

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)