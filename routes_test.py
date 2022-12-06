def test_home(api):
    """Prediction page initially loads with 0 pieces"""
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'LegOh!' in resp.data

def test_get_prediction(api):
    """Prediction page initially loads with 0 pieces and no estimate"""
    resp = api.get('/prediction')
    assert resp.status == '200 OK'
    assert b'What\'s the damage?' in resp.data
    assert b'LegOh! | Predict' in resp.data
    assert b'<input type="number" id="piece_count" name="piece_count" value="0" min=0 onkeyup="validateSubmission()">' in resp.data
    assert b'<span id="result">0</span>' in resp.data

def test_post_prediction(api):
    """Renders result page with piece count and estimation"""
    form_data = {'piece_count': '150'}
    resp = api.post('/prediction', data=form_data)
    assert resp.status == '200 OK'
    assert b'LegOh! | Result' in resp.data
    assert b'<input type="number" id="piece_count" name="piece_count" value="150" min=0 onkeyup="validateSubmission()">' in resp.data
    assert b'<span id="result">0</span>' not in resp.data

def test_get_reminder(api):
    """Does not allow GET requests to /reminder"""
    resp = api.get('/reminder')
    assert resp.status == '405 METHOD NOT ALLOWED'

def test_post_reminder(api):
    """Shows thank you page after sending receipt"""
    # Get a unique test email account at https://generator.email/ and visit https://generator.email/<generated-email-address> to see incoming mail
    form_data = {'piece_count': '150', 'result': '24.99', 'to_email': 'testymctestface@gmailup.com'}
    resp = api.post('/reminder', data=form_data)
    assert resp.status == '200 OK'
    assert b'LegOh! | Thank you' in resp.data
