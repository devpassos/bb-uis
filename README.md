# User Image System
The User Image System - UIS is a simple CRUD that recieves clients names and images from the endpoint API and store it into a datababase.

## Iniciando a Aplcação
- Para iniciar a aplicação, basta clonar no projeto e, na raiz, executar o seguinte comando:
  ```
  docker compose up
  ```

## Testes
- O framework de testes utilizado foi o pytest.
- Certifique-se de ter o pytest instalado e na pasta `app` executar:
  ```
  python -m pytest
  ```
  - Em distribuições Ubuntu pode ser necessário executar:
    ```
    python3 -m pytest
    ```
- Veja um exemplo da saída abaixo:
   ![pytest_exemple](https://github.com/devpassos/bb-uis/assets/45983543/0ea19e6c-6e61-4de2-b7d8-f94f97d2e906)


## Diagrams
### Application Diagram:
  <img width="734" alt="Application Diagram" src="https://github.com/devpassos/bb-uis/assets/45983543/66fcc838-751f-48de-9039-e60b32d15184">

### E-R Diagram:
  ![Modelo ER - UIS](https://github.com/devpassos/bb-uis/assets/45983543/3825b8f9-061b-4c4e-b113-aabb97f387c7)

## Estrutura do projeto
```
├── app -> Pasta Raiz da aplicação. É o conteúdo que é copiado para o container docker
│   
│   ├── api -> Arquivos 
│   │   
│   │   ├── v1
│   │   │   └── enpoints
│   │   │       ├── root.py
│   │   │       ├── user.py
│   │   │       ├── user_image.py
│   │   │       └── user_image_thumb.py
│   │   └── api.py
│   ├── core
│   │   ├── configs.py
│   │   ├── database.py
│   │   ├── deps.py
│   │   └── util.py
│   ├── db -> Pasta que guarda o bando de dados sqlite (é criado no momento do deploy da aplicação)
│   │   └── uis.sqlite
│   ├── models
│   │   ├── all_models.py
│   │   ├── images_model.py
│   │   └── users_model.py
│   ├── resources
│   │   ├── img
│   │   │   ├── exemplo-jpg.jpg
│   │   │   └── img_teste.jpg
│   │   └── txt
│   │       └── base64_img_teste.txt
│   ├── schemas
│   │   ├── images_schema.py
│   │   └── users_schema.py
│   ├── test -> Guarda o código para aexecução do framework pytest
│   │   └── test_api.py
│   ├── Dockerfile -> instruções de build do aplicação fastAPI.
│   ├── criar_tabelas.py -> Arquivo que pode ser executado separadamente para criar o bando da aplicação e suas respectivas tabelas.
│   ├── main.py -> Arquivo principal da aplicação.
│   └── requirements.txt
├── diagrams -> Diretório com os diagramas e modelos da aplicação.
│   ├── Application Diagram.png
│   ├── Modelo ER - UIS.pdf
│   └── Modelo ER - UIS.png
├── Docker-compose.yml
```
