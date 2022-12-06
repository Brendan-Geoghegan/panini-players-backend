def test_register(api):
    pass


def test_login(api):
    pass


def test_logout(api):
    resp = api.get('/logout')
    assert b'message": "See you soon!' in resp.data
