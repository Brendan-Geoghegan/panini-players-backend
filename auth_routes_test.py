import json
from panini.helper import id_generator


def test_valid_register(api):
    random_id = id_generator()
    register_data = {
        "id": random_id,
        "email": 'test@test.com',
        "username": 'test',
        "location": 'Manchester',
        "password_1": 'password',
        "password_2": 'password'
    }
    resp = api.post('/register', data=json.dumps(register_data),
                    headers={"Content-Type": "application/json"})
    assert resp.status == '201 CREATED'
    assert b'New user created' in resp.data


def test_invalid_register_username_already_exists(api):
    random_id = id_generator()
    register_data = {
        "id": random_id,
        "email": 'test@test.com',
        "username": 'Sean',
        "location": 'London',
        "password_1": 'password',
        "password_2": 'password'
    }
    resp = api.post('/register', data=json.dumps(register_data),
                    headers={"Content-Type": "application/json"})
    assert resp.status == '400 BAD REQUEST'
    assert b'Username already in database' in resp.data


def test_invalid_register_email_already_exists(api):
    random_id = id_generator()
    register_data = {
        "id": random_id,
        "email": 'test@test.com',
        "username": 'george@123.com',
        "location": 'London',
        "password_1": 'password',
        "password_2": 'password'
    }
    resp = api.post('/register', data=json.dumps(register_data),
                    headers={"Content-Type": "application/json"})
    assert resp.status == '400 BAD REQUEST'
    assert b'Email already in database' in resp.data


def test_invalid_register_passwords_dont_match(api):
    random_id = id_generator()
    register_data = {
        "id": random_id,
        "email": 'test1@test.com',
        "username": 'george@123.com',
        "location": 'London',
        "password_1": 'password',
        "password_2": 'password1'
    }
    resp = api.post('/register', data=json.dumps(register_data),
                    headers={"Content-Type": "application/json"})
    assert resp.status == '400 BAD REQUEST'
    assert b'Passwords have to be the same' in resp.data


def test_invalid_login_user_not_found(api):
    invalid_credentials = {
        'username': 'user_not_found',
        'password': 'password123'
    }
    resp = api.post('/login', data=json.dumps(invalid_credentials),
                    headers={"Content-Type": "application/json"})
    assert resp.status == "404 NOT FOUND"
    assert b'{\n  "error": "404 Not Found: User not found"\n}\n' in resp.data


def test_invalid_login_incorrect_password(api):
    invalid_credentials = {
        'username': 'Sean',
        'password': 'incorrect_password'
    }
    resp = api.post('/login', data=json.dumps(invalid_credentials),
                    headers={"Content-Type": "application/json"})
    assert resp.status == "400 BAD REQUEST"
    assert b'{\n  "error": "400 Bad Request: Incorrect password"\n}\n' in resp.data


def test_logout(api):
    resp = api.get('/logout')
    assert b'message": "See you soon!' in resp.data
