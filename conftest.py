from panini import server
import pytest

@pytest.fixture
def api():
    client = server.test_client()
    return client