## Instructions:

### Prerequisites:

Python 3.7 or higher
MongoDB installed and running

### Setup:

Clone the repository: git clone https://github.com/your-repo/blog-api.git
Navigate to the project directory: cd blog-api
Create a virtual environment: python -m venv env
Activate the virtual environment:

On Windows: env\Scripts\activate
On Unix or macOS: source env/bin/activate

Install the required dependencies: pip install -r requirements.txt

### Configuration:

Create a .env file in the project root directory.
Add the following environment variables:

MONGODB_URI: The connection URI for your MongoDB instance (e.g., mongodb://localhost:27017/blog-api)

### Running the API:

Start the FastAPI server: uvicorn main:app --reload
The API will be available at http://localhost:8000.

### API Documentation:

The API documentation is available at http://localhost:8000/docs.

### Code Structure:

blog-api/
├── main.py
├── models/
│   ├── __init__.py
│   ├── blog.py
│   ├── comment.py
│   ├── user.py
├── repositories/
│   ├── __init__.py
│   ├── blog_repository.py
│   ├── comment_repository.py
│   ├── user_repository.py
├── routers/
│   ├── __init__.py
│   ├── blog_router.py
│   ├── comment_router.py
│   ├── user_router.py
├── services/
│   ├── __init__.py
│   ├── blog_service.py
│   ├── comment_service.py
│   ├── user_service.py
├── .env
├── requirements.txt
└── README.md

### Models:

blog.py: Defines the Blog model representing a blog post.
comment.py: Defines the Comment model representing a comment on a blog post.
user.py: Defines the User model representing a user.

### Repositories:

blog_repository.py: Handles CRUD operations for Blog objects in the MongoDB database.
comment_repository.py: Handles CRUD operations for Comment objects in the MongoDB database.
user_repository.py: Handles CRUD operations for User objects in the MongoDB database.

### Routers:

blog_router.py: Defines the routing and API endpoints for blog-related operations.
comment_router.py: Defines the routing and API endpoints for comment-related operations.
user_router.py: Defines the routing and API endpoints for user-related operations.

### Services:

blog_service.py: Contains business logic and validation for blog-related operations.
comment_service.py: Contains business logic and validation for comment-related operations.
user_service.py: Contains business logic and validation for user-related operations.
main.py: The entry point of the application, where the FastAPI app is created and configured.
Requirements:

The requirements.txt file lists all the required Python packages for the project.

### Documentation:
The API documentation is available at http://localhost:8000/docs when the server is running. It provides detailed information about the available endpoints, request/response formats, and example payloads.
API Endpoints:

### Blogs:

GET /blogs: Retrieve a list of all blog posts.
GET /blogs/{blog_id}: Retrieve a specific blog post by ID.
POST /blogs: Create a new blog post.
PUT /blogs/{blog_id}: Update an existing blog post by ID.
DELETE /blogs/{blog_id}: Delete a blog post by ID.

### Comments:

GET /blogs/{blog_id}/comments: Retrieve all comments for a specific blog post.
POST /blogs/{blog_id}/comments: Add a new comment to a blog post.
PUT /comments/{comment_id}: Update an existing comment by ID.
DELETE /comments/{comment_id}: Delete a comment by ID.

### Users:

GET /users: Retrieve a list of all users.
GET /users/{user_id}: Retrieve a specific user by ID.
POST /users: Create a new user.
PUT /users/{user_id}: Update an existing user by ID.
DELETE /users/{user_id}: Delete a user by ID.

### Error Handling and Input Validation:

The API includes robust error handling and input validation mechanisms.
Request payloads are validated using Pydantic models.
Appropriate HTTP status codes and error messages are returned for various error scenarios.

### Code Quality and Organization:

The codebase follows object-oriented programming principles and adheres to RESTful API design guidelines.
The code is organized into separate modules and packages for better maintainability and scalability.
Docstrings and comments are provided throughout the codebase for better understanding and documentation.
