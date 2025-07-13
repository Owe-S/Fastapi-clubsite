# tests/test_news.py

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from main import app
from routers.news import get_session

class DummySession:
    """A no-op async session that returns no rows."""
    async def execute(self, *args, **kwargs):
        class R:
            def scalars(self_inner):
                return self_inner
            def all(self_inner):
                return []
        return R()

    async def commit(self): ...
    async def refresh(self, obj): ...
    async def close(self): ...

@pytest_asyncio.fixture(autouse=True)
def override_db_session():
    """Override get_session to yield our DummySession in all tests."""
    async def _override():
        yield DummySession()
    app.dependency_overrides[get_session] = _override
    yield
    app.dependency_overrides.clear()

@pytest_asyncio.fixture
async def client():
    """AsyncClient wired to FastAPI via ASGITransport."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        yield ac

@pytest.mark.asyncio
async def test_healthcheck(client):
    r = await client.get("/healthcheck")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_list_news_unauth(client):
    r = await client.get("/news/")
    assert r.status_code == 401

@pytest.mark.asyncio
async def test_token_and_list_news(client):
    # 1) Obtain a JWT
    data = {"username": "API-Test", "password": "UtvidetTest2025!"}
    r = await client.post("/token", data=data)
    assert r.status_code == 200
    token = r.json().get("access_token")
    assert token, "Expected access_token"

    # 2) Call /news/ with that token
    headers = {"Authorization": f"Bearer {token}"}
    r2 = await client.get("/news/", headers=headers)
    assert r2.status_code == 200
    assert r2.json() == []  # our dummy session always returns empty list
