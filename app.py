__author__ = 'Adrian Au-Yeung'

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# for login
app.secret_key = 'adrian'
api = Api(app)


# Flask decorator to create the db
# looks at the elements create in the model classes
@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()


# JWT creates the /auth endpoint
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


# this makes sure app.run is only runned if we direct run app.py and not
# app.run is not runned on import
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
