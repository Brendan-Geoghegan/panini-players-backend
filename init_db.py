from panini import db, server
from panini.models.main import User
import string, random

cards = "FWC1-0 FWC2-0 FWC3-0 FWC4-0 FWC5-0 FWC6-0 FWC7-0 FWC8-0 FWC9-0 FWC-0 FWC11-0 FWC12-0 FWC13-0 FWC14-0 FWC15-0 FWC16-0 FWC17-0 FWC18-0 QAT-0 QAT2-0 QAT3-0 QAT4-0 QAT5-0 QAT6-0 QAT7-0 QAT8-0 QAT9-0 QAT-0 QAT11-0 QAT12-0 QAT13-0 QAT14-0 QAT15-0 QAT16-0 QAT17-0 QAT18-0 QAT19-0 QAT-0 ECU1-0 ECU2-0 ECU3-0 ECU4-0 ECU5-0 ECU6-0 ECU7-0 ECU8-0 ECU9-0 ECU-0 ECU11-0 ECU12-0 ECU13-0 ECU14-0 ECU15-0 ECU16-0 ECU17-0 ECU18-0 ECU19-0 ECU20-0 SEN1-0 SEN2-0 SEN3-0 SEN4-0 SEN5-0 SEN6-0 SEN7-0 SEN8-0 SEN9-0 SEN-0 SEN11-0 SEN12-0 SEN13-0 SEN14-0 SEN15-0 SEN16-0 SEN17-0 SEN18-0 SEN19-0 SEN20-0"

users = [
    {'username': 'Sean', 'password': 'password123', 'email': 'sean@123.com', 'location': 'Lodon', 'cards': cards},
    {'username': 'Kornelia', 'password': 'password234', 'email': 'kornelia@123.com', 'location': 'Lodon', 'cards': cards},
    {'username': 'George', 'password': 'password345', 'email': 'george@123.com', 'location': 'Lodon', 'cards': cards},
    {'username': 'Brendan', 'password': 'password456', 'email': 'Brendan@123.com', 'location': 'Lodon', 'cards':cards},
]



# list = [
#     {'user': 'afjonivew', 'panini': 0, 'FWC1': 1},
#     {'user': 'fnaadvo', 'panini': 1, 'FWC1': 1},
#     {'user': 'fmvidfjsd', 'panini': 1, 'FWC1': 0},
#     {'user': 'mfnvrlkf', 'panini': 0, 'FWC1': 0},
# ]

def id_generator():
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(10))
    return id

with server.app_context():
    db.drop_all()
    db.create_all()
    for user in users:
        db.session.add(User(id=id_generator(), username=user['username'], password=user['password'], email=user['email'], location=user['location'], cards=user['cards']))
        db.session.commit()

    # for cards in list:
    #     db.session.add(List(user=cards['user'], panini=cards['panini'], fwc1=cards['FWC1'] ))
    #     db.session.commit()

