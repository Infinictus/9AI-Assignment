##Instructions:

###Prerequisites:

Python 3.7 or higher
MongoDB installed and running


###Setup:

Clone the repository: git clone https://github.com/your-repo/blog-api.git
Navigate to the project directory: cd blog-api
Create a virtual environment: python -m venv env
Activate the virtual environment:

On Windows: env\Scripts\activate
On Unix or macOS: source env/bin/activate


Install the required dependencies: pip install -r requirements.txt


###Configuration:

Create a .env file in the project root directory.
Add the following environment variables:

MONGODB_URI: The connection URI for your MongoDB instance (e.g., mongodb://localhost:27017/blog-api)


###Running the API:

Start the FastAPI server: uvicorn main:app --reload
The API will be available at http://localhost:8000.


###API Documentation:

The API documentation is available at http://localhost:8000/docs.
