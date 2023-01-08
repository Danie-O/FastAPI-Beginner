from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel


app = FastAPI() # initialise FastAPI app


students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}


class Student(BaseModel):
    """
    A class representing a student.
    
    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        year (str): The year the student is in.
    """
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    """
    A class representing updates to a student's information.
    
    Attributes:
        name (Optional[str]): The updated name of the student.
        age (Optional[int]): The updated age of the student.
        year (Optional[int]): The updated year the student is in.
    """
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None


# Base route
@app.get("/")
def index():
    """
    Base route that returns the name "First Data".
    
    Returns:
        Dict: A dictionary containing the name "First Data".
    """
    return {"name": "First Data"}


# Path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view ", gt=0)):
    """
    A route that returns a student with the given ID.
    This function retrieves a student from a dictionary of students using the provided student ID as the key. 
    If the student is not found in the dictionary, a 404 error is returned.
    
    Args:
        student_id (int): The ID of the student to retrieve.
        
    Returns:
        Dict: A dictionary representing the student with the given ID.
        
    Raises:
        HTTPException: 404 If the student with the given ID is not found.
    """
    try:
        return students[student_id]
    except KeyError:
        raise HTTPException(status_code=404, detail="Student not found")


# Using Query parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        
        return {"Data": "Not found"}


# Combining path and query params
# @app.get("/get-by-name/{student_id}")
# def get_student(*, student_id: int, name: Optional[str] = None, test: int):
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
        
#         return {"Data": "Not found"}


# Create a new student
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    """
    Create a new student.
    
    This route creates a new student and adds it to a dictionary of students using the provided student ID as the key. If a student with the given ID already exists, an error message is returned.
    
    Args:
        student_id (int): The ID of the student to create.
        student (Student): A dictionary containing the student's information.
        
    Returns:
        Dict: A dictionary representing the created student.
        Dict: A dictionary containing an error message if the student already exists.
    """
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student
    return students[student_id]


# Update student records
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    """
    Update a student's information.
    
    This route updates the information for a student with the given ID using the provided update information. If a student with the given ID does not exist, an error message is returned.
    
    Args:
        student_id (int): The ID of the student to update.
        student (UpdateStudent): A dictionary containing the updated student information.
        
    Returns:
        Dict: A dictionary representing the updated student.
        Dict: A dictionary containing an error message if the student does not exist.
    """
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


#Delete a student's record
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    """
    Delete a student.
    
    This route deletes a student with the given ID from a dictionary of students. If a student with the given ID does not exist, an error message is returned.
    
    Args:
        student_id (int): The ID of the student to delete.
        
    Returns:
        Dict: A dictionary containing a success message if the student was deleted.
        Dict: A dictionary containing an error message if the student does not exist.
    """
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}