from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class student(BaseModel):
    name: str = 'Nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field (gt=0, lt=10, default=5, description="A decimal value representing the CGPA of the student")
   
new_student = {'age':32, 'email':'nitish@example.com', 'cgpa':8.5}

student = student(**new_student)

#print in pydantic model format 
print(student)

#print in dict format
student_dict = student.dict()
# student_dict = dict(student)

print(student_dict['age'] )
print(student_dict['email'] )
print(student_dict['cgpa'] )

#print in json format
student_json = student.json()
print(student_json)