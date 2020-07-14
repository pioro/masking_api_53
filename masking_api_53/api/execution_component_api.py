# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from masking_api_53.api_client import ApiClient


class ExecutionComponentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_execution_components(self, **kwargs):  # noqa: E501
        """Get all execution components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_execution_components(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to get all components for
        :param int page_number: The page number for which to get executions. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: ExecutionComponentList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_execution_components_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_execution_components_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_execution_components_with_http_info(self, **kwargs):  # noqa: E501
        """Get all execution components  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_execution_components_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int execution_id: The ID of the execution to get all components for
        :param int page_number: The page number for which to get executions. This will default to the first page if excluded
        :param int page_size: The maximum number of objects to return. This will default to the DEFAULT_API_PAGE_SIZE property if not provided
        :return: ExecutionComponentList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['execution_id', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_execution_components" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'execution_id' in params:
            query_params.append(('execution_id', params['execution_id']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page_number', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/execution-components', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExecutionComponentList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
