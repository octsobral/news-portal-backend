#News Portal Backend

---

##Introduction
News portal backend using fastapi and mongodb. In this repository you will also find a docker-compose that can be used to execute all services necessary for this application.

---
##Executing with docker-compose
You will need docker installed in your machine. After that, you can simply execute the commands below:
````
docker-compose build
docker-compose up
````
The first command will create the image of our News Portal application. The second one will turn our appplication and our database service.

---
##Using Swagger and/or Redoc
Once the application is up, you can check and test the endpoints of the application using Swagger or Redoc. For this, you will need to open a browser, go to _localhost:8000/docs_ (for Swagger documentation) or _localhost:8000/redoc_ (for Redoc documentation).

---
##Structure
The structure os our application can be seen below (only folders):

- news-portal-backend (root)
    - src (source directory of our application)
      - config (stores environment configuration file)
      - database (stores models, repository and db definitions)
        - model (stores models of documents in our db)
        - repository (definitions of our repository access)
      - schema (stores the intermediate schemas used between db and services)
      - service (bridge between endpoints and repository)

