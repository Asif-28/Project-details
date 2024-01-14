import pytest
import requests
from faker import Faker

fake = Faker()

endpoint = "http://localhost:8000/client"

data = {
    "client_name": fake.name(),
    "client_email": fake.email(),
    "client_project_manager": fake.name(),
}


def test_create_client():
    url = f"{endpoint}/create"  # replace with your actual server URL
    response = requests.post(url, json=data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["message"] == "Client created successfully"


def test_list_client():
    url = f"{endpoint}/list"  # replace with your actual server URL
    response = requests.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0

    match = False

    # check if data is valid
    for client in response.json():
        if client["client_name"] == data["client_name"]:
            if client["client_email"] == data["client_email"]:
                match = True
                break

    assert match == True

        # add other required fields here


# st run --checks all http://localhost:8000/openapi.json
