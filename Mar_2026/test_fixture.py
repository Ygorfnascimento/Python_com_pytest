import pytest
import requests
import sqlalchemy
from unittest.mock import MagicMock
from sqlalchemy.sql import text

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_length(sample_list):
    assert len(sample_list) == 5

@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}
    return mock

def test_api_call_with_mock(mock_response):
    assert mock_response.status_code == 200
    assert mock_response.json() == {"message": "Success"}


def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

def test_contador():
    assert list(contador(5)) == [0, 1, 2, 3, 4]

@pytest.fixture
def database_connection():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    connection = engine.connect()
    yield connection
    connection.close()

def test_database_connection(database_connection):
    result = database_connection.execute(text("SELECT 1"))
    assert result.fetchone()[0] == 1