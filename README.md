# ClearStream
ClearStream is software for monitoring and managing a home wastewater treatment plant.

## Project Structure

The project is organized as follows:

### Files and Directories:

- **app/**: Main application directory containing the source code.
  - **crud.py**: Contains CRUD (Create, Read, Update, Delete) functions for database operations.
  - **database.py**: Database configuration and function to obtain database sessions.
  - **endpoints/**: Directory containing API endpoint definitions.
    - **sewage.py**: Defines API endpoints related to sewage management.
  - **main.py**: Main FastAPI application file, initializes the app and registers routers.
  - **models.py**: Defines data models used in the application.
  - **schemas.py**: Defines data schemas used for validation and serialization.

- **LICENSE**: Project license file (MIT License).
- **README.md**: Project description file.
- **requirements.txt**: Project dependencies file.
- **tests/**: Directory containing unit tests.
  - **test_sewage.py**: Unit tests for sewage management endpoints.

### Functionality Description:

- **CRUD**: The `crud.py` file contains functions for creating, reading, updating, and deleting data in the database.
- **Database**: The `database.py` file configures the SQLite database connection and provides a function to obtain database sessions.
- **Endpoints**: The `sewage.py` file in the `endpoints` directory defines API endpoints for managing sewage, such as creating, reading lists, and individual records.
- **Models**: The `models.py` file defines the `Sewage` data model used in the database.
- **Schemas**: The `schemas.py` file defines data schemas used for validation and serialization in the API.
- **Main Application**: The `main.py` file initializes the FastAPI application, creates database tables, and registers routers with endpoints.
- **Tests**: The `test_sewage.py` file contains unit tests for the API endpoints related to sewage management.

### Dependencies:

- **requirements.txt**: Contains the list of project dependencies, such as `fastapi`, `sqlmodel`, `sqlite3`, and `uvicorn`.

### License:

- **LICENSE**: The project is licensed under the MIT License.

### Documentation:

- **README.md**: Contains a basic description of the ClearStream project.
