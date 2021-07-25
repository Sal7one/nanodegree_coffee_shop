import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth
import sys


app = Flask(__name__)
setup_db(app)

CORS(app, resources={r"/api/*": {'origins': '*'}})

db_drop_and_create_all()


def create_app(test_config=None):
    # create and configure the apps
    app = Flask(__name__)
    setup_db(app)

    # CORS Rules
    @app.after_request
    def after_request(response):

        # Allow only used methods
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,DELETE,PATCH')
        return response

    '''
    @TODO uncomment the following line to initialize the datbase
    # !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    # !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    # !! Running this funciton will add one
    '''

    # ROUTES
    '''
    @TODO implement endpoint
        GET /drinks
            it should be a public endpoint
            it should contain only the drink.short() data representation
        returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
            or appropriate status code indicating reason for failure
            jsonify()
            jsonify()
            jsonify()
            jsonify()
    '''

    @app.route('/drinks', methods=["GET"])
    def retrieve_drinks():
        # Getting user data
        drinks = []

        # Get Questions with helper function
        return jsonify({"success": True, "drinks": drinks})

    '''
    @TODO implement endpoint
        GET /drinks-detail
            it should require the 'get:drinks-detail' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
            or appropriate status code indicating reason for failure
            jsonify({"success": True, "drinks": drinks})

    '''
    @requires_auth("get:drinks-detail")
    @app.route('/drinks-detail', methods=["GET"])
    def retrieve_drinks():
        # Getting user data
        drinks = []

        # Get Questions with helper function

        return jsonify({"success": True, "drinks": drinks})

    '''
    @TODO implement endpoint
        POST /drinks
            it should create a new row in the drinks table
            it should require the 'post:drinks' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
            or appropriate status code indicating reason for failure
                    jsonify({"success": True, "drinks": drinks})


    '''

    '''
    @TODO implement endpoint
        PATCH /drinks/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should update the corresponding row for <id>
            it should require the 'patch:drinks' permission
            it should contain the drink.long() data representation
        returns status code 200 and json {"success": True, "drinks": drink}
        where drink an array containing only the updated drink
            or appropriate status code indicating reason for failure

                    jsonify({"success": True, "drinks": drinks})

    '''

    '''
    @TODO implement endpoint
        DELETE /drinks/<id>
            where <id> is the existing model id
            it should respond with a 404 error if <id> is not found
            it should delete the corresponding row for <id>
            it should require the 'delete:drinks' permission
        returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
            or appropriate status code indicating reason for failure
                    jsonify({"success": True, "delete": id})

    '''

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''

    @app.errorhandler(400)
    def bad_request(error):
        print(error)
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

    '''
    @TODO implement error handlers using the @app.errorhandler(error) decorator
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''

    '''
    @TODO implement error handler for 404
        error handler should conform to general task above
    '''

    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above
    '''
