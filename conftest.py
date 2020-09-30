import json

import pytest
from cleo import Application

from isilon.client import IsilonClient
from isilon.creds import Credentials
from isilon.http import Http
from isilon.api.base import BaseAPI
from isilon.commands import AccountsCommand, ContainersCommand, DiscoverabilityCommand, EndpointsCommand, ObjectsCommand


@pytest.fixture
def http():
    return Http()


@pytest.fixture
def isilon_client():
    return IsilonClient()


@pytest.fixture
def creds(http):
    return Credentials(http, "account", "user", "pass")


@pytest.fixture
def isilon_client_mock(monkeypatch):
    monkeypatch.setattr(BaseAPI, 'get_token', token_mock)
    monkeypatch.setattr(BaseAPI, 'base_request', request_success_mock)
    return IsilonClient()


@pytest.fixture
def cmd_app(monkeypatch):
    monkeypatch.setattr(BaseAPI, 'get_token', token_mock)
    monkeypatch.setattr(BaseAPI, 'base_request', request_success_mock)

    application = Application()
    application.add(AccountsCommand())
    application.add(ContainersCommand())
    application.add(DiscoverabilityCommand())
    application.add(EndpointsCommand())
    application.add(ObjectsCommand())
    return application


async def token_mock(*args, **kwargs):
    return {"X-Auth-Token": "abc123lkj"}


async def request_success_mock(*args, **kwargs):
    return ResponseMock()


class ResponseMock:
    def __init__(self, *args, **kwargs):
        self.status = kwargs.get('status', 200)
        self.headers = {"X-Object-Meta": "mock"}

    async def json(self):
        return json.dumps({"message": "ok"})
