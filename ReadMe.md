# Address Book API using FastAPI

## Project Overview

This project is a simple Address Book REST API built using FastAPI and SQLite.

The application allows users to:

- Create addresses
- Retrieve addresses
- Update addresses
- Delete addresses
- Retrieve nearby addresses using latitude, longitude, and distance

The project uses:
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

---

# Project Structure

```text
address_book/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils.py
│
├── requirements.txt
├── README.md


Installation

Step 1: Clone Repository
git clone https://github.com/kirubhashree03-cmyk/address-book-api.git
cd address-book-api

Step 2: Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac/Linux
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt
Run the Application
uvicorn app.main:app --reload

Application will run at:

http://127.0.0.1:8000
Swagger Documentation

Open:

http://127.0.0.1:8000/docs

API Endpoints

Method	Endpoint	Description
POST	/addresses	Create address
GET	/addresses	Get all addresses
PUT	/addresses/{id}	Update address
DELETE	/addresses/{id}	Delete address
GET	/addresses/nearby	Get nearby addresses


Sample POST Request
{
  "name": "Chennai Office",
  "latitude": 13.0827,
  "longitude": 80.2707
}

Nearby Search Example

GET /addresses/nearby?lat=13.0827&lon=80.2707&distance=5

This returns all addresses within 5 KM radius.

Validation Rules

Latitude must be between -90 and 90
Longitude must be between -180 and 180

Database

The project uses SQLite database.

Database file:

address.db

Author

Kirubha Shree P
