from flask import Flask

from src.main.routes.user_routes import users_route_bp

app = Flask(__name__)

app.register_blueprint(users_route_bp)
