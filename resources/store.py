__author__ = 'Adrian Au-Yeung'
from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return{'message': 'store {} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error has occurred'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'store {} deleted'.format(name)}
        return {'message': 'unable to find store'}, 400


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}, 200
