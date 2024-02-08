# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
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


class VueJsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        
    def get_config(
        self,
        **kwargs
    ):  # noqa: E501
        """Return the current configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Request accepted language
        :return: FrontConfigDTO
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
            return self.get_config_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_config_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_config_with_http_info(self, **kwargs):  # noqa: E501
        """Return the current configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Request accepted language
        :return: FrontConfigDTO
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
                    " to method get_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FrontConfigDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_extension(
        self,
        module : 'str',
        **kwargs
    ):  # noqa: E501
        """Return the front Vue JS extension file to include  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extension(module, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module: Module identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["module", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(module, str) and module != None:
            raise ValueError("Invalid value for parameter `module`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.get_extension_with_http_info(module, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_extension_with_http_info(module, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_extension_with_http_info(self, module, **kwargs):  # noqa: E501
        """Return the front Vue JS extension file to include  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extension_with_http_info(module, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module: Module identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extension" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module' is set
        if ('module' not in params or
                params['module'] is None):
            raise ValueError("Missing the required parameter `module` when calling `get_extension`")  # noqa: E501

        if 'module' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['module']):  # noqa: E501
            raise ValueError("Invalid value for parameter `module` when calling `get_extension`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'module' in params:
            path_params['module'] = params['module']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/extension/js/{module}.js', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_extension_style(
        self,
        module : 'str',
        **kwargs
    ):  # noqa: E501
        """Return the front Vue JS extension css file to include  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extension_style(module, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module: Module identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["module", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(module, str) and module != None:
            raise ValueError("Invalid value for parameter `module`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.get_extension_style_with_http_info(module, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_extension_style_with_http_info(module, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_extension_style_with_http_info(self, module, **kwargs):  # noqa: E501
        """Return the front Vue JS extension css file to include  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_extension_style_with_http_info(module, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module: Module identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extension_style" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module' is set
        if ('module' not in params or
                params['module'] is None):
            raise ValueError("Missing the required parameter `module` when calling `get_extension_style`")  # noqa: E501

        if 'module' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['module']):  # noqa: E501
            raise ValueError("Invalid value for parameter `module` when calling `get_extension_style`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'module' in params:
            path_params['module'] = params['module']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/extension/css/{module}.css', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_theme_config(
        self,
        module_id : 'str',
        theme_id : 'str',
        **kwargs
    ):  # noqa: E501
        """Return the front Vue JS theme configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_config(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :return: ThemeConfigDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["module_id", "theme_id", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(module_id, str) and module_id != None:
            raise ValueError("Invalid value for parameter `module_id`. This parameter couldn't be cast to type `str`")
             
        if not isinstance(theme_id, str) and theme_id != None:
            raise ValueError("Invalid value for parameter `theme_id`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.get_theme_config_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_theme_config_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_theme_config_with_http_info(self, module_id, theme_id, **kwargs):  # noqa: E501
        """Return the front Vue JS theme configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_config_with_http_info(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :return: ThemeConfigDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module_id', 'theme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_theme_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module_id' is set
        if ('module_id' not in params or
                params['module_id'] is None):
            raise ValueError("Missing the required parameter `module_id` when calling `get_theme_config`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if ('theme_id' not in params or
                params['theme_id'] is None):
            raise ValueError("Missing the required parameter `theme_id` when calling `get_theme_config`")  # noqa: E501

        if 'module_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['module_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `module_id` when calling `get_theme_config`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        if 'theme_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['theme_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `theme_id` when calling `get_theme_config`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'module_id' in params:
            path_params['moduleId'] = params['module_id']  # noqa: E501
        if 'theme_id' in params:
            path_params['themeId'] = params['theme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/theme/{moduleId}/{themeId}/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ThemeConfigDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_theme_css(
        self,
        module_id : 'str',
        theme_id : 'str',
        **kwargs
    ):  # noqa: E501
        """Return the theme css file  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_css(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["module_id", "theme_id", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(module_id, str) and module_id != None:
            raise ValueError("Invalid value for parameter `module_id`. This parameter couldn't be cast to type `str`")
             
        if not isinstance(theme_id, str) and theme_id != None:
            raise ValueError("Invalid value for parameter `theme_id`. This parameter couldn't be cast to type `str`")
             


        if kwargs.get('async_req'):
            return self.get_theme_css_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_theme_css_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_theme_css_with_http_info(self, module_id, theme_id, **kwargs):  # noqa: E501
        """Return the theme css file  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_css_with_http_info(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module_id', 'theme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_theme_css" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module_id' is set
        if ('module_id' not in params or
                params['module_id'] is None):
            raise ValueError("Missing the required parameter `module_id` when calling `get_theme_css`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if ('theme_id' not in params or
                params['theme_id'] is None):
            raise ValueError("Missing the required parameter `theme_id` when calling `get_theme_css`")  # noqa: E501

        if 'module_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['module_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `module_id` when calling `get_theme_css`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        if 'theme_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['theme_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `theme_id` when calling `get_theme_css`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'module_id' in params:
            path_params['moduleId'] = params['module_id']  # noqa: E501
        if 'theme_id' in params:
            path_params['themeId'] = params['theme_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/theme/{moduleId}/{themeId}/style.css', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_theme_resource(
        self,
        module_id : 'str',
        theme_id : 'str',
        file_path : 'str' = None,
        accepted_extensions : 'List[str]' = None,
        **kwargs
    ):  # noqa: E501
        """Return the theme requested resource  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_resource(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :param str file_path: Resource path
        :param list[str] accepted_extensions: List of supported file extensions
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        frame = inspect.currentframe()
        keys, _, _, values = inspect.getargvalues(frame)
        passed_arguments = {}
        for key in keys:
            if key != 'self' and key not in ["module_id", "theme_id", ] and values[key] != None:
                passed_arguments[key] = values[key]
        kwargs['_return_http_data_only'] = True

        
        
        if not isinstance(module_id, str) and module_id != None:
            raise ValueError("Invalid value for parameter `module_id`. This parameter couldn't be cast to type `str`")
             
        if not isinstance(theme_id, str) and theme_id != None:
            raise ValueError("Invalid value for parameter `theme_id`. This parameter couldn't be cast to type `str`")
             
        if not isinstance(file_path, str) and file_path != None:
            raise ValueError("Invalid value for parameter `file_path`. This parameter couldn't be cast to type `str`")
                 
        if (not isinstance(accepted_extensions, list) or not isinstance(accepted_extensions[0], str)) and accepted_extensions != None:
            raise ValueError("Invalid value for parameter `accepted_extensions`. This parameter couldn't be cast to type `List[str]`")
                 


        if kwargs.get('async_req'):
            return self.get_theme_resource_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_theme_resource_with_http_info(module_id, theme_id, **passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_theme_resource_with_http_info(self, module_id, theme_id, **kwargs):  # noqa: E501
        """Return the theme requested resource  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_theme_resource_with_http_info(module_id, theme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_id: Module identifier (required)
        :param str theme_id: Theme identifier (required)
        :param str file_path: Resource path
        :param list[str] accepted_extensions: List of supported file extensions
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module_id', 'theme_id', 'file_path', 'accepted_extensions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_theme_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module_id' is set
        if ('module_id' not in params or
                params['module_id'] is None):
            raise ValueError("Missing the required parameter `module_id` when calling `get_theme_resource`")  # noqa: E501
        # verify the required parameter 'theme_id' is set
        if ('theme_id' not in params or
                params['theme_id'] is None):
            raise ValueError("Missing the required parameter `theme_id` when calling `get_theme_resource`")  # noqa: E501

        if 'module_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['module_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `module_id` when calling `get_theme_resource`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        if 'theme_id' in params and not re.search(r'([a-zA-Z0-9-]+$)', params['theme_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `theme_id` when calling `get_theme_resource`, must conform to the pattern `/([a-zA-Z0-9-]+$)/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'module_id' in params:
            path_params['moduleId'] = params['module_id']  # noqa: E501
        if 'theme_id' in params:
            path_params['themeId'] = params['theme_id']  # noqa: E501

        query_params = []
        if 'file_path' in params:
            query_params.append(('filePath', params['file_path']))  # noqa: E501
        if 'accepted_extensions' in params:
            query_params.append(('acceptedExtensions', params['accepted_extensions']))  # noqa: E501
            collection_formats['acceptedExtensions'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/theme/{moduleId}/{themeId}/resource', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_user_config(
        self,
        **kwargs
    ):  # noqa: E501
        """Return the user-specific configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Request accepted language
        :return: UserFrontConfigDTO
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
            return self.get_user_config_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_config_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_user_config_with_http_info(self, **kwargs):  # noqa: E501
        """Return the user-specific configuration  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str accept_language: Request accepted language
        :return: UserFrontConfigDTO
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
                    " to method get_user_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/vuejs/user_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserFrontConfigDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
