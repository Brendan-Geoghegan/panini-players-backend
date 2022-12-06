from flask_mail import Mail

def mail_config(app):
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '26914877c00786'
    app.config['MAIL_PASSWORD'] = '267519f7d51a04'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    return Mail(app)
