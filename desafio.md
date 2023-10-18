# User Image System

You are responsible for the design and implementation of a User Image System.

This system should store the users' images and be developed using Python and the FastAPI framework.

Below, are some high level definitions of what should be created:

 
## `user-image-api`

Create an API to manage Users Images

### Endpoints:
## Criado corpo das rotas
- /add-user -
  - request : receives a User Name
  - response: returns the new User ID.

- /update-user
  - request : receives a User ID and new User Name
  - response: returns the User ID.      

- /add-user-image
  - request : receives a User ID and an image (Base 64 Format).
  - response: returns the new image ID.

- /get-user-image
  - request : receives a User ID and an Image ID.
  - response: returns requested image (Base 64 Format)

- /list-user-images-thumbnails
  - request : receives a User ID
  - response: return a list of user's images ID and (Base 64 Format) on maximum size of 100x100, and preserving aspect ratio.

- /update-user-image
  - request : receives a User ID, an Image ID, and a new image (Base 64 Format)
  - response : no response body needed

- /delete-user-image
  - request : receives a User ID and an Image ID
  - response: no response body needed

## nomes dentro da conveção
Obs.: Adapt the endpoints' names by following REST API URI naming conventions

## What should be delivered?

- Solution Architecture Diagram

- Database Entity-Relationship Diagram

- Application code on Git Repository with unit/integration tests to ensure conformity

- Docker-compose / Dockerfile for local deployment with database;


## What will be evaluated?

- Code Structure/Organization

- Exception Handling

- Database Modeling
