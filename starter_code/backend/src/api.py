import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
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

        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,DELETE,PATCH')
        return response

    db_drop_and_create_all()

    # ROUTES
    @app.route('/drinks', methods=["GET"])
    def retrieve_drinks():
        # Getting user data

        drinks = drink_getter(public=True)

        # Get Questions with helper function
        return jsonify({"success": True, "drinks": drinks})

    @app.route('/drinks-detail', methods=["GET"])
    @requires_auth("get:drinks-detail")
    def retrieve_drinks_detail(self):
        # Getting user data
       # print("You're authoed ")
      #  drinks = drink_getter(public=False)

        # Get Questions with helper function
        return jsonify({"success": True, "drinks": "drinks"})

    @app.route('/drinks', methods=["POST"])
    @requires_auth("post:drinks")
    def post_drinks(self):
        # Getting user data and making sure it's the same data-type as DB MODEL

        drink_data = request.json
        if drink_data is None:
            abort(422)

        try:
            user_title = str(drink_data['title'])
            user_recipe = str(drink_data['recipe'])
        except:
            abort(422)
        # Checking if there's an input error and handling it as entry error   # Data not correct, UNPROCESSABLE

        if(user_title is not None and
           user_recipe is not None
           ):

            # Instace of DB object with our Data
            the_Drink = Drink(
                title=user_title,
                recipe=user_recipe)

            # Try inserting into DB
            try:
                the_Drink.insert()
                return jsonify(
                    {"success": True, "drinks": [the_Drink]}
                )
            # Server error from SQL Alchemy
            except:
                print(sys.exc_info())
                abort(500)
        else:
            abort(422)

        # Get Questions with helper function

    @app.route('/drinks/<drink_id>', methods=["PATCH"])
    @requires_auth("patch:drinks")
    def modify_drinks(self,drink_id):
        # Getting user data
        drink_data = request.json
        if drink_data is None:
            abort(422)
        drink_title = str(drink_data['title'])

        # Data not correct, UNPROCESSABLE
        if(drink_title is None or drink_title == ""):
            abort(422)

        drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

        if drink is not None:
            drink.title = drink_title
            drink.update()
        else:
            abort(404)

        return jsonify({"success": True, "drinks": [drink]})

    @app.route('/drinks/<drink_id>', methods=["DELETE"])
    @requires_auth("delete:drinks")
    def delete_drinks(self,drink_id):

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

                if(drinks is not None or drinks is not None):
                    return drinks
                else:
                    abort(500)
            else:
                drinks = Drink.query.all()
                drinks = [drink.long() for drink in drinks]

                if(drinks is not None or drinks is not None):
                    return drinks
                else:
                    abort(500)

        except:
            print(sys.exc_info())
            abort(500)

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
