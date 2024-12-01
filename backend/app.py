from models.blacklist import Blacklist
from flask import Flask  # type: ignore
from routes import register_routes
from models.db import db
from configs.config import Config
from flask_migrate import Migrate  # type: ignore
from flask_jwt_extended import JWTManager  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET
app.config['JWT_BLACKLIST_ENABLED'] = Config.JWT_BLACKLIST_ENABLED
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = Config.JWT_BLACKLIST_TOKEN_CHECKS
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    token = Blacklist.query.filter_by(jti=jti).first()
    return token is not None


def create_tables():
    if app.config['ENV'] == 'development':
        db.create_all()

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
