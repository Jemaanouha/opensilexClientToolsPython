# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.2-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from typing import List
from opensilexClientToolsPython.models import *
from datetime import date
import inspect
from opensilexClientToolsPython.api_client import ApiClient


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        
    def authenticate(
        self,
        body : 'AuthenticationDTO' = None,
        **kwargs
    ):  # noqa: E501
        """Authenticate a user and return an access token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationDTO body: User authentication informations
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(body, AuthenticationDTO) and body != None:
            raise ValueError("Invalid value for parameter `body`. This parameter couldn't be cast to type `AuthenticationDTO`")
                 


        if kwargs.get('async_req'):
            return self.authenticate_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.authenticate_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def authenticate_with_http_info(self, **kwargs):  # noqa: E501
        """Authenticate a user and return an access token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticationDTO body: User authentication informations
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authenticate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenGetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def authenticate_open_id(
        self,
        code : 'str' = None,
        **kwargs
    ):  # noqa: E501
        """Authenticate a user and return an access token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_open_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Authorization code
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(code, str) and code != None:
            raise ValueError("Invalid value for parameter `code`. This parameter couldn't be cast to type `str`")
                 


        if kwargs.get('async_req'):
            return self.authenticate_open_id_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.authenticate_open_id_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def authenticate_open_id_with_http_info(self, **kwargs):  # noqa: E501
        """Authenticate a user and return an access token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_open_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Authorization code
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authenticate_open_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/openid', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenGetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def authenticate_saml(
        self,
        **kwargs
    ):  # noqa: E501
        """Authenticate a user and return an access token from SAML response  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_saml(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        


        if kwargs.get('async_req'):
            return self.authenticate_saml_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.authenticate_saml_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def authenticate_saml_with_http_info(self, **kwargs):  # noqa: E501
        """Authenticate a user and return an access token from SAML response  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_saml_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authenticate_saml" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/saml', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def forgot_password(
        self,
        identifier : 'str',
        **kwargs
    ):  # noqa: E501
        """Send an e-mail confirmation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: User e-mail or uri (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["identifier", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(identifier, str) and identifier != None:
            raise ValueError("Invalid value for parameter `identifier`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.forgot_password_with_http_info(identifier, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.forgot_password_with_http_info(identifier, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def forgot_password_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Send an e-mail confirmation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: User e-mail or uri (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `forgot_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/forgot-password', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_credentials_groups(
        self,
        **kwargs
    ):  # noqa: E501
        """Get list of existing credentials indexed by Swagger @API concepts in the application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_credentials_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CredentialsGroupDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        


        if kwargs.get('async_req'):
            return self.get_credentials_groups_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_credentials_groups_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_credentials_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of existing credentials indexed by Swagger @API concepts in the application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_credentials_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CredentialsGroupDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_credentials_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CredentialsGroupDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def logout(
        self,
        **kwargs
    ):  # noqa: E501
        """Logout by discarding a user token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        


        if kwargs.get('async_req'):
            return self.logout_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.logout_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def logout_with_http_info(self, **kwargs):  # noqa: E501
        """Logout by discarding a user token  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.logout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/logout', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def renew_password(
        self,
        renew_token : 'str',
        check_only : 'bool' = None,
        password : 'str' = None,
        **kwargs
    ):  # noqa: E501
        """Update user password  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_password(renew_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str renew_token: User renew token (required)
        :param bool check_only: Check only renew token
        :param str password: User password
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["renew_token", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(renew_token, str) and renew_token != None:
            raise ValueError("Invalid value for parameter `renew_token`. This parameter couldn't be cast to type `str`")
             
        if not isinstance(check_only, bool) and check_only != None:
            raise ValueError("Invalid value for parameter `check_only`. This parameter couldn't be cast to type `bool`")
                 
        if not isinstance(password, str) and password != None:
            raise ValueError("Invalid value for parameter `password`. This parameter couldn't be cast to type `str`")
                 


        if kwargs.get('async_req'):
            return self.renew_password_with_http_info(renew_token, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.renew_password_with_http_info(renew_token, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def renew_password_with_http_info(self, renew_token, **kwargs):  # noqa: E501
        """Update user password  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_password_with_http_info(renew_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str renew_token: User renew token (required)
        :param bool check_only: Check only renew token
        :param str password: User password
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['renew_token', 'check_only', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method renew_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'renew_token' is set
        if ('renew_token' not in params or
                params['renew_token'] is None):
            raise ValueError("Missing the required parameter `renew_token` when calling `renew_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'renew_token' in params:
            query_params.append(('renew_token', params['renew_token']))  # noqa: E501
        if 'check_only' in params:
            query_params.append(('check_only', params['check_only']))  # noqa: E501
        if 'password' in params:
            query_params.append(('password', params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/renew-password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenGetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def renew_token(
        self,
        **kwargs
    ):  # noqa: E501
        """Send back a new token if the provided one is still valid  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in [] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        


        if kwargs.get('async_req'):
            return self.renew_token_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.renew_token_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def renew_token_with_http_info(self, **kwargs):  # noqa: E501
        """Send back a new token if the provided one is still valid  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.renew_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: TokenGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method renew_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/security/renew-token', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenGetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
