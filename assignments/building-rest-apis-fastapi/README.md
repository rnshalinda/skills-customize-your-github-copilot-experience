# 📘 Assignment: Building REST APIs with FastAPI framework

## 🎯 Objective

Build a RESTful web API using FastAPI. Students will define endpoints, request and response models, and handle basic CRUD operations for a simple collection of items.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a FastAPI application with endpoints to list items, retrieve a single item, create new items, and update existing items.

#### Requirements
Completed program should:

- Use FastAPI to define a web API
- Implement the following endpoints:
  - `GET /items`
  - `GET /items/{item_id}`
  - `POST /items`
  - `PUT /items/{item_id}`
- Store items in an in-memory collection such as a list or dictionary
- Return JSON-formatted responses

### 🛠️ Add Validation and Documentation

#### Description
Use Pydantic models to validate incoming request data and define response schemas.

#### Requirements
Completed program should:

- Define Pydantic models for item data
- Validate input for `POST` and `PUT` requests
- Raise appropriate HTTP errors for invalid requests or missing items
- Include endpoint summaries or docstrings to improve API documentation

### 🛠️ Run and Explore the API Docs

#### Description
Start the FastAPI server and confirm the interactive documentation works as expected.

#### Requirements
Completed program should:

- Be runnable with `uvicorn starter-code:app --reload`
- Provide OpenAPI docs at `/docs`
- Allow testing of the API through the Swagger UI
