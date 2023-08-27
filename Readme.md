# File Upload Project - RapidFort
This is a simple web application built with Flask that allows users to upload files and receive information about the uploaded files.

## Features
1. Upload any file via the web interface.
2. Retrieve information about the uploaded file, such as filename, size, path, timestamp and other metadata.

## Setup and Installation

### Running with Python
1. **Clone the repository**
```python
git clone https://github.com/coutaditya/fileupload.git
```
2. **Install the requirements**
```python
pip install -r requirements.txt
```
3. **Run Flask App**
```python
python fileupload.py
```
4. **Access the web-app at:** ` http://localhost:5000`

### Running with Docker
1. **Clone the repository**
```python
git clone https://github.com/coutaditya/fileupload.git
```
2. **Download and Install Docker**
3. **Build Docker Image**
```python
docker build -t file-upload-app .
```
4. **Run the container**
```python
docker run -p 5000:5000 file-upload-app
```
5. **Access the web-app at:** ` http://localhost:5000`
6. **Stopping the App**
    1. In the terminal where the container is running, use Ctrl+C.
    2. Run the following docker command to delete the docker image:
    ```python
    docker image rm file-upload-app
    ```

## How to use
1. Access the web app in your browser.
2. Use the provided UI to upload a file.
3. Submit the form to receive information about the uploaded file.

## API Definition
When a client communicates with a server over the web, this process is enabled by the Hypertext Transfer Protocol (HTTP). HTTP is a request-response protocol between a client and a server.
The GET and POST methods are the two most common HTTP request methods. They are used to retrieve or send data to a server.

### GET Requests
1. GET request is one of the HTTP methods used to retrieve data from a server. 
2. It's a request made by a client to the server to fetch a representation of a resource identified by a specific URI (Uniform Resource Identifier).
3. GET requests are intended for retrieving data and should not cause any side effects on the server. They should not modify or change any data on the server.
4. Here's an example of a simple GET request for a REST API:
```python
GET /api/users/123 HTTP/1.1
Host: example.com
```
5. For a GET request, common status codes are:
    1. 200: Success
    2. 404: Not Found
    3. 400: Bad Request


### POST Requests
1. In a RESTful API, a POST request is an HTTP method used to submit data to be processed by the server.
2. Unlike GET requests that retrieve data, POST requests are used to create new resources on the server or perform actions that cause a change in the server's state.
3. POST requests include a payload (data) in the request body, which the server processes and responds to accordingly.
4. In a POST request, data is not visible on the URL like in GET request. Instead, we pass our data inside the body of the POST request.
5. Here's an example of a POST request to create a new user in a hypothetical user management API:
```python
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "username": "adityaadi",
  "email": "grand@nitj.com",
  "password": "aditya123"
}

6. For a POST request, common status codes are:
    1. 201: Created
    2. 202: Accepted
    3. 204: No content
    3. 240: Bad Request

```
### Project Live Link: http://34.131.206.154:5000/

