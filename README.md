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

## HTTPS STATUS CODES

HTTP (Hypertext Transfer Protocol) status codes are three-digit numbers returned by a server in response to a client's request made to the server. They indicate the outcome of the request and provide information about the status of the server or the requested resource. The status codes are grouped into five classes:

1xx Informational:

1. 100 Continue
2. 101 Switching Protocols
3. 102 Processing (WebDAV)

2xx Success:

1. 200 OK
2. 201 Created
3. 202 Accepted
4. 203 Non-Authoritative Information
5. 204 No Content
6. 205 Reset Content
7. 206 Partial Content
8. 207 Multi-Status (WebDAV)
9. 208 Already Reported (WebDAV)
10. 226 IM Used

3xx Redirection:

1. 300 Multiple Choices
2. 301 Moved Permanently
3. 302 Found
4. 303 See Other
5. 304 Not Modified
6. 305 Use Proxy (deprecated)
7. 307 Temporary Redirect
8. 308 Permanent Redirect

4xx Client Errors:

1. 400 Bad Request
2. 401 Unauthorized
3. 402 Payment Required
4. 403 Forbidden
5. 404 Not Found
6. 405 Method Not Allowed
7. 406 Not Acceptable
8. 407 Proxy Authentication Required
9. 408 Request Timeout
10. 409 Conflict
11. 410 Gone
12. 411 Length Required
13. 412 Precondition Failed
14. 413 Payload Too Large
15. 414 URI Too Long
16. 415 Unsupported Media Type
17. 416 Range Not Satisfiable
18. 417 Expectation Failed
19. 418 I'm a teapot
20. 421 Misdirected Request
21. 422 Unprocessable Entity (WebDAV)
22. 423 Locked (WebDAV)
23. 424 Failed Dependency (WebDAV)
24. 425 Too Early
25. 426 Upgrade Required
26. 428 Precondition Required
27. 429 Too Many Requests
28. 431 Request Header Fields Too Large
29. 451 Unavailable For Legal Reasons

5xx Server Errors:

1. 500 Internal Server Error
2. 501 Not Implemented
3. 502 Bad Gateway
4. 503 Service Unavailable
5. 504 Gateway Timeout
6. 505 HTTP Version Not Supported
7. 506 Variant Also Negotiates
8. 507 Insufficient Storage (WebDAV)
9. 508 Loop Detected (WebDAV)
10. 510 Not Extended
11. 511 Network Authentication Required

These status codes provide information to the client about the success or failure of their request and guide further actions. Developers and administrators use these codes for troubleshooting and improving the performance and reliability of web applications.
