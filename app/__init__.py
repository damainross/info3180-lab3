#from flask import Flask

#app = Flask(__name__)
#from app import views

from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'foojjjjfffs'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '08d52e65acd168'
app.config['MAIL_PASSWORD'] = 'a8a3a69c4d8114'
mail = Mail(app)
from app import views