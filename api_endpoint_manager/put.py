from flask_jwt_auth import APIAuth
from flask_restplus import Resource
from http_request_args.validation import RequestArgsValidator
from http_request_response import RequestUtilities

from .api_endpoint import APIEndpoint


class PutEndpoint(APIEndpoint):
    def __init__(self, api, route, qs_args_def, body_args_def, business_class, authentication_required=True, authorization_object=None):
        if '_id' in route:
            @api.route(route)
            class ItemPut(Resource):

                @RequestUtilities.try_except
                @RequestArgsValidator.args_validation(qs_args_def, body_args_def)
                @APIAuth.auth_required(authentication_required=authentication_required, authorization_object=authorization_object)
                def put(self, _id):
                    return business_class.run()
        else:
            @api.route(route)
            class ItemPut(Resource):

                @RequestUtilities.try_except
                @RequestArgsValidator.args_validation(qs_args_def, body_args_def)
                @APIAuth.auth_required(authentication_required=authentication_required, authorization_object=authorization_object)
                def put(self):
                    return business_class.run()