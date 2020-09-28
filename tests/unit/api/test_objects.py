import pytest


@pytest.mark.asyncio
async def test_get_object(isilon_client_mock):
    resp = await isilon_client_mock.objects.get("container", "obj")
    assert resp is not None


@pytest.mark.asyncio
async def test_create_object(isilon_client_mock):
    resp = await isilon_client_mock.objects.create("container", "obj2", "mycontent")
    assert resp == 200


@pytest.mark.asyncio
async def test_copy_object(isilon_client_mock):
    with pytest.raises(NotImplementedError):
        await isilon_client_mock.objects.copy("container", "obj2")


@pytest.mark.asyncio
async def test_delete_object(isilon_client_mock):
    resp = await isilon_client_mock.objects.delete("container", "obj2")
    assert resp == 200


@pytest.mark.asyncio
async def test_show_metadata(isilon_client_mock):
    resp = await isilon_client_mock.objects.show_metadata("container", "obj2")
    assert "X-Object-Meta" in resp


@pytest.mark.asyncio
async def test_update_metadata(isilon_client_mock):
    resp = await isilon_client_mock.objects.update_metadata("container", "obj2")
    assert resp == 200
