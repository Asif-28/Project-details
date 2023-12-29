from fastapi import FastAPI, status

from models import Project, Client
from database import db
import pymongo
from constants import message, JSONResponse

# from constants import Message

app = FastAPI()

"""
Project
"""


@app.post("/project/create")
async def create_project(project: Project) -> JSONResponse:
    """
    Create a new project
    """

    db_projects = db["Projects"]
    db_projects.create_index(project.index_key(), unique=True)

    try:
        db_projects.insert_one(project.model_dump())
        return message.success(text="Project created")
    except pymongo.errors.DuplicateKeyError:
        return message.error(text=f"Project {project.projectName} already exists.")


@app.get("/project/list")
async def list_projects() -> list[Project]:
    """
    List all projects
    """

    db_projects = db["Projects"]
    projects = db_projects.find()
    return [Project(**project) for project in projects]


"""
Client
"""


@app.post("/client/create")
async def create_client(client: Client) -> JSONResponse:
    """
    Create a new client
    """

    db_clients = db["Clients"]
    db_clients.create_index(client.index_key(), unique=True)

    try:
        db_clients.insert_one(client.model_dump())
        return message.success(text="Client created")
    except pymongo.errors.DuplicateKeyError:
        return message.error(text="Client already exists")


@app.get("/client/list")
async def list_clients() -> list[Client]:
    """
    List all clients
    """

    db_clients = db["Clients"]
    clients = db_clients.find()
    print(clients)
    return [Client(**client) for client in clients]
