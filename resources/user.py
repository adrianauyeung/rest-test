import sqlite3
from flask_restful import Resource, request, reqparse
__author__ = 'Adrian Au-Yeung'
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Must include username"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Must include password"
                        )


    def post(self):
        data = UserRegister.parser.parse_args()

        # make sure user does not exist
        if UserModel.find_by_username(data['username']):
            return {"message": "user already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user created successfully"}, 201