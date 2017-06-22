__author__ = 'Adrian Au-Yeung'
from app import app
from db import db

db.init_app(app)

# Flask decorator to create the db
# looks at the elements create in the model classes
@app.before_first_request
def create_tables():
    db.create_all()