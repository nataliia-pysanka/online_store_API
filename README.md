## REST API with Django-rest-framework.
An online store  was created. CRUD endpoints were implemented for the following models: Product, Order. 
List GET endpoints should are paginated. All endpoints return JSON. 

____

## How  to test application works:
1. Clone repository: `git@github.com:nataliia-pysanka/online_store_API.git`
2. Change dir: `cd online_store_API`
3. Install virtual enviroment: `python -m venv venv`
4. Activate virtual env: `source venv/bin/activate`
5. Update: `pip install --upgrade pip`
6. Install dependencies for the project in the virtual environment python:
   `python -m pip install --no-cache-dir -r requirements.txt`
7. Make migrations for creating DB:
   `make migrate`
8. Populate the database:
   `make seed`
9. Launch local server: `python manage.py runserver`


### Routes:
```bash
{URI}/api/products/<pk>
{URI}/api/orders/<pk>
{URI}/api/stats/?date_start=<year-month>&date_end==<year-month>&metric=<[price|count]>
```

## Installation

### Requirements

Docker-compose (https://docs.docker.com/compose/)

### Deploy

```bash
# Clone this repository using git
`git@github.com:nataliia-pysanka/online_store_API.git`
# Change dir
`sudo cd services`
# Build the container
`make up`
# Make migrations
`make migrate
# Populate database
`make seed`
# Navigate to http://localhost
```

### Destroy

```bash
`make down`
```

