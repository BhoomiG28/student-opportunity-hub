from flask import Flask
from config import Config
from models import db
from routes.auth import auth
from flask_login import LoginManager
from flask_login import login_required, current_user

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)

@app.route("/")
def home():
    return "Student Opportunity Hub is Running!"

@app.route("/dashboard")
@login_required
def dashboard():
    return f"Welcome {current_user.name}"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)  