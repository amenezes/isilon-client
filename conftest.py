import re

import pytest
from cleo import Application
from aioresponses import aioresponses

from isilon.client import IsilonClient
from isilon.commands import AccountsCommand, ContainersCommand, DiscoverabilityCommand, EndpointsCommand, ObjectsCommand
from isilon.exceptions import TokenRetrieveException


@pytest.fixture
def token_exeption(mock_aioresponse):
    mock_aioresponse.get(
        "http://localhost:8080/auth/v1.0", exception=TokenRetrieveException
    )

@pytest.fixture
def mock_aioresponse():
    with aioresponses() as m:
        yield m

@pytest.fixture
def api_mock(mock_aioresponse):
    pattern = re.compile(r'^http://localhost:8080/v1/AUTH_test.*$')
    mock_aioresponse.get('http://localhost:8080/auth/v1.0', headers={"X-Auth-Token": "abc123lkj"})
    mock_aioresponse.get('http://localhost:8080/info', payload='')
    mock_aioresponse.get('http://localhost:8080/v1/endpoints', body='')
    mock_aioresponse.get(pattern, status=200, payload='')
    mock_aioresponse.post(pattern, payload='')
    mock_aioresponse.head(pattern, headers={"X-Object-Meta": "test"})
    mock_aioresponse.delete(pattern, payload='')
    mock_aioresponse.put(pattern, status=200)


@pytest.fixture
def isilon_client_mock(api_mock):
    client = IsilonClient()
    return client


@pytest.fixture
def cmd_app(api_mock):
    application = Application()
    application.add(AccountsCommand())
    application.add(ContainersCommand())
    application.add(DiscoverabilityCommand())
    application.add(EndpointsCommand())
    application.add(ObjectsCommand())
    return application
