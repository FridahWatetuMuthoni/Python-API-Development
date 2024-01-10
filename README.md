# API DEVELOPMENT IN PYTHON USING FASTAPI

## How to create a virtual environment

> > > python -m venv venv

## Installing fastapi

> > > pip install fastapi[all]

## Putting all the requirements to a text file

> > > pip freeze > requirements.txt

## How to run the uvicorn server

> > > uvicorn the_entry_file:the_name_of_the_fastapi_instance --reload(reloads your server when the code changes)

> > > uvicorn main:app --reload

## HTTP METHODS

HTTP (Hypertext Transfer Protocol) defines a set of methods (sometimes referred to as verbs) to indicate the desired action to be performed on a resource. Each HTTP request typically includes a method, which tells the server what action to perform. Here are some commonly used HTTP methods:

1. GET: Retrieve data from the server. The URL contains all the necessary information for the server to locate and return the requested resource.

2. POST: Submit data to be processed to a specified resource. It's often used to create a new resource on the server.

3. PUT: Update a resource on the server. The request typically includes the updated representation of the resource.

4. DELETE: Request that a resource be removed. It is used to delete a specified resource.

5. PATCH: Apply partial modifications to a resource. It is used to apply partial updates to a resource.

6. HEAD: Similar to GET but without the response body. It's used to retrieve metadata about a resource without the actual data.

7. OPTIONS: Retrieve information about the communication options available for the target resource. It's often used to check what HTTP methods and other features are supported by the server.

8. TRACE: Echoes the received request so that a client can see what (if any) changes or additions have been made by intermediate servers.

9. CONNECT: Establish a network connection to a server over HTTP for the purpose of tunneling. It's often used for secure SSL/TLS connections.

These methods provide a way for clients to interact with resources on the web server in various ways. The choice of method depends on the desired action, and each method has its own specific semantics.

## APIS HTTP METHODS

| CRUD METHOD | HTTP METHOD | URL ROUTE  | FASTAPI ROUTE             |
| ----------- | ----------- | ---------- | ------------------------- |
| Create      | POST        | /posts     | @app.post("/posts)        |
| Read        | GET         | /posts     | @app.get("/posts")        |
| Read        | GET         | /posts/:id | @app.get("/posts/{id})    |
| Update      | PUT/PATCH   | /posts/:id | @app.put("/posts/{id})    |
| Delete      | DELETE      | /posts/:id | @app.delete("/posts/{id}) |
