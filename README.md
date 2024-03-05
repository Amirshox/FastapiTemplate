# FastAPI Template Project

Welcome to the FastAPI Template Project! This project is designed to provide a solid foundation for building scalable and maintainable web applications using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- **FastAPI Framework**: Leverages FastAPI for building APIs, offering automatic Swagger documentation, request validation, and more.
- **Database Integration**: Utilizes SQLAlchemy for ORM, with Alembic for database migrations, supporting asynchronous database operations.
- **User Management**: Includes a basic user model and API endpoints for user management, such as creating, retrieving, updating, and deleting users.
- **Dependency Injection**: Implements dependency injection for database sessions and other services, making the code more modular and testable.
- **Pre-configured Development Tools**: Comes with pre-commit hooks configured for code formatting and linting, ensuring code quality and consistency.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PostgreSQL (or you can adjust the database settings for your preferred database)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Amirshox/FastapiTemplate.git
   cd FastapiTemplate


### Install the required dependencies:

```bash
pip install -r requirements.txt
```
- Copy the .env.example file to .env and adjust the database settings and any other environment variables as needed.

### Running the Application
To run the application in development mode with live reloading:

```bash
make run-dev
```
- This command uses uvicorn to serve the application, which will reload automatically on code changes.

### Database Migrations
#### To create and apply database migrations:

```bash
alembic revision --autogenerate -m "Your message here"
alembic upgrade head
```

### API Documentation
#### Once the application is running, you can visit http://localhost:8000/docs to view the Swagger UI documentation for the API. This provides an interactive interface to explore and test the API endpoints.

### Project Structure
- `src/`: Source code for the application.
- - `api/`: API route definitions.
- - `core/`: Core application configurations and services.
- - `db/`: Database models and session management.
- `migrations/`: Alembic migrations scripts.
- `requirements.txt`: Project dependencies.
- `.env.example`: Example environment variables file.

### Contributing
#### Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.
