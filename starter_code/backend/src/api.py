import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from sqlalchemy.sql.functions import user
from werkzeug.exceptions import Aborter
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth
import sys


def create_app(test_config=None):
    # create and configure the apps
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {'origins': '*'}})

    # CORS Rules
    @app.after_request
    def after_request(response):

        # Allow only used methods
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Origin',
                             '*')

        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,DELETE,PATCH,OPTIONS')
        return response

    db_drop_and_create_all()

    # ROUTES

# -------------  Public --------- Getting drinks ---------------------------
    @app.route('/drinks', methods=["GET"])
    def retrieve_drinks():
        # Getting user data

        drinks = drink_getter(public=True)

        # Get Questions with helper function
        return jsonify({"success": True, "drinks": drinks})

# -------------------- Private -------------------------------------
    @app.route('/drinks-detail', methods=["GET"])
    @requires_auth("get:drinks-detail")
    def retrieve_drinks_detail(self):
        # Getting user data
        drinks = drink_getter(public=False)

        # Get Questions with helper function
        return jsonify({"success": True, "drinks": drinks})

# ---------------------- Drink oprations --------------------------------
    @app.route('/drinks', methods=["POST"])
    @requires_auth("post:drinks")
    def post_drinks(self):
        # Getting user data and making sure it's the same data-type as DB MODEL
        try:
            json_data = dict(request.json)

            user_title = json_data['title']
            user_recipe = ""
            if type(json_data['recipe']) == str:
                user_recipe = json_data['recipe']
            else:
                user_recipe = json.dumps(json_data['recipe'])


            the_drink = Drink(
                title=user_title,
                recipe=user_recipe
            )
        except:
            abort(422)

        try:
            the_drink.insert()

            return jsonify({'success': True, 'drink': the_drink.long()})
        except:
            abort(500)
        # Get Questions with helper function

    @app.route('/drinks/<drink_id>', methods=["PATCH"])
    @requires_auth("patch:drinks")
    def modify_drinks(self, drink_id):
        # Getting user data
        drink_data = dict(request.json)

        if drink_data is None:
            abort(422)

        user_title = drink_data.get('title'),
        user_title = ''.join(user_title)

        user_recipe = (drink_data.get('recipe')
                       if type(drink_data.get('recipe')) == str
                       else json.dumps(drink_data.get('recipe')))

        # Data not correct, UNPROCESSABLE
        if(user_title is None or user_title == ""):
            abort(422)

        drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

        if drink is not None:
            drink.title = user_title

            if user_recipe is not None:
                drink.recipe = user_recipe

            drink.update()
        else:
            abort(404)

        return jsonify({"success": True, "drinks": [drink.title]})

    @app.route('/drinks/<drink_id>', methods=["DELETE"])
    @requires_auth("delete:drinks")
    def delete_drinks(self, drink_id):

        the_drink = Drink.query.filter(
            Drink.id == drink_id).one_or_none()

        if the_drink is not None:
            the_drink.delete()
        else:
            abort(404)
        return jsonify({"success": True,  "delete": drink_id})

    # Helper function to get drinks based on request

    def drink_getter(public):
        # on the parameters  from the calling function
        try:
            if(public):
                drinks = Drink.query.all()

                drinks = [drink.short() for drink in drinks]
                return drinks

            else:
                drinks = Drink.query.all()
                drinks = [drink.long() for drink in drinks]

                return drinks

        except os.error as eeee:
            print("E")
            print(eeee)

    # Error Handling

    @app.errorhandler(400)
    def bad_request(error):
        print(sys.exc_info())
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        print(sys.exc_info())
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        print(sys.exc_info())
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable_entity(error):
        print(sys.exc_info())
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable entity"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        print(sys.exc_info())
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app
