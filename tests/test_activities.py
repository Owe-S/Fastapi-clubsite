import os
import sys
# Legg til prosjektrot i path slik at vi kan importere database, models, osv.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, engine
from auth import get_current_user


# Dummy bruker for å slippe JWT i tester
def override_get_current_user():
    class DummyUser:
        userName = "test_user"
    return DummyUser()

# Sett override før TestClient
app.dependency_overrides[get_current_user] = override_get_current_user
client = TestClient(app)

# Sett opp og tear down testdatabase
@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    try:
        Base.metadata.drop_all(bind=engine)
    except Exception:
        pass


def test_list_activities_empty():
    response = client.get("/activities/?skip=0&limit=5")
    assert response.status_code == 200
    assert response.json() == []


def test_create_and_list_activity():
    new_data = {
        "listID": 1,
        "boolShow": True,
        "activityName": " Test Activity",
        "actAlias": None,
        "location": "Test",
        "maxParticipants": 5,
        "boolWaitlist": False,
        "partReserved": 0,
        "date_start": "2025-01-01T10:00:00",
        "time_from": "1000",
        "time_to": "1200",
        "boolOnlinePay": False,
        "boolOnlineSignup": True,
        "formID": None,
        "priceGroupID": None,
        "signup_from": None,
        "signup_to": None,
        "actDescription": "",
        "boolSignupToMail": False,
        "signupMailTo": None,
        "boolVTG": False,
        "boolVTGforward": False,
        "payAccount": None,
        "boolMemberRequired": False,
        "actLocation": None,
        "field_borrowEquipment": False
    }
    post_resp = client.post("/activities/", json=new_data)
    assert post_resp.status_code == 200
    created = post_resp.json()
    assert created["activityName"] == " Test Activity"

    list_resp = client.get("/activities/?skip=0&limit=5")
    assert list_resp.status_code == 200
    data = list_resp.json()
    assert len(data) == 1
    assert data[0]["activityName"] == " Test Activity"


def test_crud_lifecycle():
    # 1) starts empty
    r = client.get("/activities")
    assert r.status_code == 200 and isinstance(r.json(), list)

    # 2) create
    new = {"activityName":"Golf 101"}
    r = client.post("/activities", json=new)
    assert r.status_code == 200
    data = r.json()
    assert data["activityName"] == "Golf 101"
    aid = data["activityID"]

    # 3) read single
    r = client.get(f"/activities/{aid}")
    assert r.json()["activityName"] == "Golf 101"

    # 4) update
    r = client.put(f"/activities/{aid}", json={"activityName":"Golf 102"})
    assert r.json()["activityName"] == "Golf 102"

    # 5) delete
    r = client.delete(f"/activities/{aid}")
    assert r.status_code == 200
