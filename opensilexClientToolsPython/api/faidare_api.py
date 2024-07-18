# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0-rdg
    
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


class FaidareApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        
    def get_calls1(
        self,
        page : 'int' = None,
        page_size : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Check the available faidare calls  # noqa: E501

        Check the available faidare calls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_calls1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1CallListResponse
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

        
        
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_calls1_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_calls1_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_calls1_with_http_info(self, **kwargs):  # noqa: E501
        """Check the available faidare calls  # noqa: E501

        Check the available faidare calls  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_calls1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1CallListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_calls1" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_calls1`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_calls1`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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
            '/faidare/v1/calls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1CallListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_germplasms_by_search(
        self,
        germplasm_db_id : 'str' = None,
        germplasm_pui : 'str' = None,
        germplasm_name : 'str' = None,
        page : 'int' = None,
        page_size : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Submit a search request for germplasm  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_germplasms_by_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str germplasm_db_id: Search by germplasmDbId
        :param str germplasm_pui: Search by germplasmPUI
        :param str germplasm_name: Search by germplasmName
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1GermplasmListResponse
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

        
        
        if not isinstance(germplasm_db_id, str) and germplasm_db_id != None:
            raise ValueError("Invalid value for parameter `germplasm_db_id`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(germplasm_pui, str) and germplasm_pui != None:
            raise ValueError("Invalid value for parameter `germplasm_pui`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(germplasm_name, str) and germplasm_name != None:
            raise ValueError("Invalid value for parameter `germplasm_name`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_germplasms_by_search_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_germplasms_by_search_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_germplasms_by_search_with_http_info(self, **kwargs):  # noqa: E501
        """Submit a search request for germplasm  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_germplasms_by_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str germplasm_db_id: Search by germplasmDbId
        :param str germplasm_pui: Search by germplasmPUI
        :param str germplasm_name: Search by germplasmName
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1GermplasmListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['germplasm_db_id', 'germplasm_pui', 'germplasm_name', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_germplasms_by_search" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_germplasms_by_search`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_germplasms_by_search`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'germplasm_db_id' in params:
            query_params.append(('germplasmDbId', params['germplasm_db_id']))  # noqa: E501
        if 'germplasm_pui' in params:
            query_params.append(('germplasmPUI', params['germplasm_pui']))  # noqa: E501
        if 'germplasm_name' in params:
            query_params.append(('germplasmName', params['germplasm_name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/faidare/v1/germplasm', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1GermplasmListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_locations_list(
        self,
        location_db_id : 'str' = None,
        page : 'int' = None,
        page_size : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of locations available in the system  # noqa: E501

        retrieve locations information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locations_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str location_db_id: Search by Location
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1LocationListResponse
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

        
        
        if not isinstance(location_db_id, str) and location_db_id != None:
            raise ValueError("Invalid value for parameter `location_db_id`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_locations_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_locations_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_locations_list_with_http_info(self, **kwargs):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of locations available in the system  # noqa: E501

        retrieve locations information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locations_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str location_db_id: Search by Location
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1LocationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_db_id', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_locations_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_locations_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_locations_list`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'location_db_id' in params:
            query_params.append(('locationDbId', params['location_db_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/faidare/v1/locations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1LocationListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_studies_list(
        self,
        study_db_id : 'str' = None,
        page : 'int' = None,
        page_size : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Retrieve studies information  # noqa: E501

        Retrieve studies information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_studies_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str study_db_id: Search by studyDbId
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1StudyListResponse
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

        
        
        if not isinstance(study_db_id, str) and study_db_id != None:
            raise ValueError("Invalid value for parameter `study_db_id`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_studies_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_studies_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_studies_list_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve studies information  # noqa: E501

        Retrieve studies information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_studies_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str study_db_id: Search by studyDbId
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: Faidarev1StudyListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['study_db_id', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_studies_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_studies_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_studies_list`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'study_db_id' in params:
            query_params.append(('studyDbId', params['study_db_id']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/faidare/v1/studies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1StudyListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_trials_list(
        self,
        page_size : 'int' = None,
        page : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of trials available in the system  # noqa: E501

        retrieve trials information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trials_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param int page_size: pageSize
        :param int page: page
        :param str accept_language: Request accepted language
        :return: Faidarev1TrialListResponse
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

        
        
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_trials_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_trials_list_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_trials_list_with_http_info(self, **kwargs):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of trials available in the system  # noqa: E501

        retrieve trials information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_trials_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param int page_size: pageSize
        :param int page: page
        :param str accept_language: Request accepted language
        :return: Faidarev1TrialListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trials_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_trials_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_trials_list`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/faidare/v1/trials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1TrialListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        
    def get_variables_list1(
        self,
        observation_variable_db_id : 'str' = None,
        page_size : 'int' = None,
        page : 'int' = None,
        **kwargs
    ):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of observationVariables available in the system  # noqa: E501

        retrieve variables information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_variables_list1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str observation_variable_db_id: observationVariableDbId
        :param int page_size: pageSize
        :param int page: page
        :param str accept_language: Request accepted language
        :return: Faidarev1ObservationVariableListResponse
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

        
        
        if not isinstance(observation_variable_db_id, str) and observation_variable_db_id != None:
            raise ValueError("Invalid value for parameter `observation_variable_db_id`. This parameter couldn't be cast to type `str`")
                 
        if not isinstance(page_size, int) and page_size != None:
            raise ValueError("Invalid value for parameter `page_size`. This parameter couldn't be cast to type `int`")
                 
        if not isinstance(page, int) and page != None:
            raise ValueError("Invalid value for parameter `page`. This parameter couldn't be cast to type `int`")
                 


        if kwargs.get('async_req'):
            return self.get_variables_list1_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_variables_list1_with_http_info(**passed_arguments, **kwargs)  # noqa: E501
            return data

    def get_variables_list1_with_http_info(self, **kwargs):  # noqa: E501
        """Faidarev1CallDTO to retrieve a list of observationVariables available in the system  # noqa: E501

        retrieve variables information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_variables_list1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str observation_variable_db_id: observationVariableDbId
        :param int page_size: pageSize
        :param int page: page
        :param str accept_language: Request accepted language
        :return: Faidarev1ObservationVariableListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['observation_variable_db_id', 'page_size', 'page', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_variables_list1" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_variables_list1`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_variables_list1`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'observation_variable_db_id' in params:
            query_params.append(('observationVariableDbId', params['observation_variable_db_id']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/faidare/v1/variables', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Faidarev1ObservationVariableListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
