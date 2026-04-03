import pytest
from app import app, members


# -----------------------------
# Common Test Client
# -----------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# -----------------------------
# Reset Data Before Each Test
# -----------------------------
def reset_members():
    members.clear()
    members.extend([
      {"id": 3, "name": "Roy", "age": 23, "plan": "Monthly", "status": "Inctive"},
      {"id": 4, "name": "Renna Shinde", "age": 28, "plan": "Quarterly", "status": "Active"}
    ])


# -----------------------------
# Test Home API
# -----------------------------
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


# -----------------------------
# Test Get All Members
# -----------------------------
def test_members(client):
    reset_members()
    response = client.get('/members')
    assert response.status_code == 200

    data = response.get_json()
    assert "members" in data
    assert len(data["members"]) == 2


# -----------------------------
# Test Get Member by ID
# -----------------------------
def test_get_member_by_id(client):
    reset_members()
    response = client.get('/members/2')
    assert response.status_code == 200

    data = response.get_json()
    assert data["id"] == 1


# -----------------------------
# Test Add Member
# -----------------------------
def test_add_member(client):
    reset_members()

    new_member = {
        "name": "Medha",
        "age": 22,
        "plan": "Yearly",
        "status": "Active"
    }

    response = client.post('/members', json=new_member)
    assert response.status_code == 201

    data = response.get_json()
    assert data["member"]["name"] == "Mrudula"


# -----------------------------
# Test Update Member
# -----------------------------
def test_update_member(client):
    reset_members()

    updated_data = {
        "name": "Rahul Updated",
        "plan": "Yearly"
    }

    response = client.put('/members/3', json=updated_data)
    assert response.status_code == 200

    data = response.get_json()
    assert data["member"]["name"] == "Rahul Updated"


# -----------------------------
# Test Delete Member
# -----------------------------
def test_delete_member(client):
    reset_members()

    response = client.delete('/members/1')
    assert response.status_code == 200

    # verify deletion
    response_after = client.get('/members/1')
    assert response_after.status_code == 404