import tempfile

import pytest


@pytest.mark.asyncio
async def test_get(http):
    resp = await http.get("https://httpbin.org/get")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_get_large_object(http):
    with tempfile.TemporaryDirectory() as tmpdir:
        resp = await http.get_large_object(
            "https://httpbin.org/robots.txt", f"{tmpdir}/testfile"
        )
    assert resp.status == 200


@pytest.mark.asyncio
async def test_post(http):
    resp = await http.post("https://httpbin.org/post")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_put(http):
    resp = await http.put("https://httpbin.org/put")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_send_large_object(http):
    resp = await http.send_large_object("https://httpbin.org/put", "LICENSE")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_delete(http):
    resp = await http.delete("https://httpbin.org/delete")
    assert resp.status == 200


@pytest.mark.asyncio
async def test_head(http):
    resp = await http.head("https://httpbin.org/get")
    assert resp.status == 200
