import pytest


@pytest.mark.asyncio
async def test_objects(isilon_client_mock):
    objects = await isilon_client_mock.containers.objects("test")
    assert isinstance(objects, str)


@pytest.mark.asyncio
async def test_create(isilon_client_mock):
    resp = await isilon_client_mock.containers.create("teste2")
    assert resp == 200


@pytest.mark.asyncio
async def test_update_metadata(isilon_client_mock):
    resp = await isilon_client_mock.containers.update_metadata("teste2")
    assert resp == 200


@pytest.mark.asyncio
async def test_show_metadata(isilon_client_mock):
    resp = await isilon_client_mock.containers.metadata("teste2")
    assert "X-Object-Meta" in resp


@pytest.mark.asyncio
async def test_delete(isilon_client_mock):
    resp = await isilon_client_mock.containers.delete("teste2")
    assert resp == 200
