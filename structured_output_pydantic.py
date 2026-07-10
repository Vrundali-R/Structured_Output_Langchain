from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Person(BaseModel):
    name: str
    age: int
    email: EmailStr  # Field for email with validation
    phone: str = "123-456-7890"  # Default value for phone
    Address: Optional[str] = None  # Optional field for address
    cgpa: float = Field(ge=0.0, le=4.0, description="Cumulative Grade Point Average")  # Field for CGPA with validation for range between 0.0 and 4.0

new_person = {"name": "Alice", "age": 30, "email": "alice@example.com", "cgpa": 4} # here if you provide str instead of int for age, it will raise a validation error.
person = Person(**new_person)  # ** is used to unpack the dictionary and pass its items as keyword arguments to the Person constructor.
print(person)

person_dict = dict(person)  # Convert the Pydantic model instance to a dictionary
print(person_dict)