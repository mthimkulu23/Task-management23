from flask_jwt_extended import JWTManager
from flask import jsonify


jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_lookup(user):
    # Assuming 'user' is an instance of User_admin
    return user.get('username')

@jwt.user_claims_loader
def add_claims_to_access_token(user):
    # Assuming 'user' is an instance of User_admin
    return {"role": user.get('role')}

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'The token is invalid.',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401







