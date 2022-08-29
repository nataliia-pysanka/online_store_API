## REST API with Django-rest-framework.
An online store  was created. CRUD endpoints were implemented for the following models: Product, Order. 
List GET endpoints should are paginated. All endpoints return JSON. 

____

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


Clone this repository using git
```bash
git clone git@github.com:nataliia-pysanka/online_store_API.git
```
Change dir
```bash
cd online_store_API
```
Build the container
```bash
make up
```
Find container's name
```bash
sudo docker ps -a
```
Open container's bash
```bash
sudo docker exec -i -t <container_name> /bin/sh
```
Make migrations
```bash
make migrate
```
Populate database
```bash
make seed
```
Navigate to (http://localhost)


### Destroy

```bash
make down
```

