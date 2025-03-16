
# Firestore Integration with FastAPI

This project demonstrates how to integrate Firestore with FastAPI, including exception handling using Python's match-case and serialization similar to Django REST Framework.

## Features

- Firestore Integration: Seamlessly connect and perform CRUD operations with Firestore.

- Exception Handling: Uses Python's match-case for clean and structured error handling.

- Serialization: Implements a custom serialization system inspired by Django REST Framework, making data handling more efficient and structured.

## Prerequisites

- Python 3.10.x (support match-case)

- FastAPI
## Run Locally

Clone the repository or download the project directly from GitHub

```bash
  git clone https://github.com/komikodok/integrate-firestore-fastapi
```

Create a virtual environment

```bash
  python -m venv .venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Serialization

```bash
class UserSerializer(BaseSerializer):

    class Meta:
        fields = ["id", "email", "phone_number", "hobby"]
```