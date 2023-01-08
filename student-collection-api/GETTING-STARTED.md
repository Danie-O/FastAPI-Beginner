# **My First API**

Welcome to my first API! This API provides a way to manage a collection of students, allowing you to create, view, update, and delete student records.

## **Getting Started**
To get the API up and running, follow these steps:

1. Clone the repository to your local machine: 
```git clone https://github.com/<your-username>/my-first-api.git

2. Navigate to the repository directory: 
``` cd my-first-api

3. Install the required packages: 
``` pip install -r requirements.txt

4. Run the API: 
``` uvicorn main:app --reload

The app should now be running at <a href="http://localhost:8000"></a>


## **Accessing the API **
To view and interact with the API, you can use the OpenAPI documentation page. To access this page, visit <a href="http://localhost:8000/docs"></a> in your web browser.

On the documentation page, you will see a list of available endpoints and their parameters. You can use the "Try it out" buttons to send requests to the API and see the responses.

## **Examples**
Here are a few examples of how you can use the API:

### **Create a new student**
To create a new student, send a POST request to the /create-student/{student_id} endpoint. Provide the student's ID and information in the request body.

Here is an example using cURL: 
```curl -X POST "http://localhost:8000/create-student/2" -H "Content-Type: application/json" -d '{"name": "Jane", "age": 18, "year": "year 13"}'

This will create a new student with the ID 2, and return the student's information.

### **View a student**
To view a student's information, send a GET request to the /get-student/{student_id} endpoint. Provide the student's ID in the path parameter.

Here is an example using cURL: 
```curl "http://localhost:8000/get-student/2"

This will return the student's information for the student with ID 2.

### **Update a student's information**
To update a student's information, send a PUT request to the /update-student/{student_id} endpoint. Provide the student's ID and updated information in the request body.

Here is an example using cURL: 
```curl -X PUT "http://localhost:8000/update-student/2" -H "Content-Type: application/json" -d '{"age": 19}'

This will update the age of the student with ID 2, and return the updated student's information.

### **Delete a student**
To delete a student, send a DELETE request to the /delete-student/{student_id} endpoint. Provide the student's ID in the path parameter.

Here is an example using cURL: 
```curl -X DELETE "http://localhost:8000/delete


