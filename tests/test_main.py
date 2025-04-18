# tests/test_main.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_note():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First, get token
        token_resp = await ac.post("/token", data={"username": "testuser", "password": "password"})
        assert token_resp.status_code == 200
        token = token_resp.json()["access_token"]

        # Create a new note
        headers = {"Authorization": f"Bearer {token}"}
        note_data = {"title": "Test Note", "content": "This is a test."}
        response = await ac.post("/notes", json=note_data, headers=headers)

        assert response.status_code == 200
        assert response.json()["title"] == note_data["title"]

@pytest.mark.asyncio
async def test_get_notes():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token_resp = await ac.post("/token", data={"username": "testuser", "password": "password"})
        assert token_resp.status_code == 200
        token = token_resp.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        response = await ac.get("/notes", headers=headers)

        assert response.status_code == 200
        assert isinstance(response.json(), list)