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


class AnalyticsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_analytic(self, analytic_id, **kwargs):  # noqa: E501
        """Cancel analytic by ID [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_analytic(analytic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int analytic_id: The ID of the analytic to cancel (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_analytic_with_http_info(analytic_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_analytic_with_http_info(analytic_id, **kwargs)  # noqa: E501
            return data

    def cancel_analytic_with_http_info(self, analytic_id, **kwargs):  # noqa: E501
        """Cancel analytic by ID [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_analytic_with_http_info(analytic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int analytic_id: The ID of the analytic to cancel (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analytic_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_analytic" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analytic_id' is set
        if ('analytic_id' not in params or
                params['analytic_id'] is None):
            raise ValueError("Missing the required parameter `analytic_id` when calling `cancel_analytic`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'analytic_id' in params:
            path_params['analyticId'] = params['analytic_id']  # noqa: E501

        query_params = []

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
            '/analytics/{analyticId}/cancel', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Analytics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_analytic(self, analytic_type, **kwargs):  # noqa: E501
        """Run analytic job on the application [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_analytic(analytic_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str analytic_type: The type of the analytic to run (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_analytic_with_http_info(analytic_type, **kwargs)  # noqa: E501
        else:
            (data) = self.create_analytic_with_http_info(analytic_type, **kwargs)  # noqa: E501
            return data

    def create_analytic_with_http_info(self, analytic_type, **kwargs):  # noqa: E501
        """Run analytic job on the application [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_analytic_with_http_info(analytic_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str analytic_type: The type of the analytic to run (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analytic_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_analytic" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analytic_type' is set
        if ('analytic_type' not in params or
                params['analytic_type'] is None):
            raise ValueError("Missing the required parameter `analytic_type` when calling `create_analytic`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'analytic_type' in params:
            form_params.append(('analyticType', params['analytic_type']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/analytics', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Analytics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_analytics(self, **kwargs):  # noqa: E501
        """Get all analytics which are currently running [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_analytics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Analytics]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_analytics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_analytics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_analytics_with_http_info(self, **kwargs):  # noqa: E501
        """Get all analytics which are currently running [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_analytics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Analytics]
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
                    " to method get_all_analytics" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/analytics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Analytics]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_analytic(self, analytic_id, **kwargs):  # noqa: E501
        """Get analytic by ID [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_analytic(analytic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int analytic_id: The ID number of the analytics job. This field is auto-generated by the Masking Engine. (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_analytic_with_http_info(analytic_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_analytic_with_http_info(analytic_id, **kwargs)  # noqa: E501
            return data

    def get_analytic_with_http_info(self, analytic_id, **kwargs):  # noqa: E501
        """Get analytic by ID [INCUBATING]  # noqa: E501

        Incubating endpoints are subject to changes that may or may not maintain backwards-compatibility.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_analytic_with_http_info(analytic_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int analytic_id: The ID number of the analytics job. This field is auto-generated by the Masking Engine. (required)
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['analytic_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_analytic" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'analytic_id' is set
        if ('analytic_id' not in params or
                params['analytic_id'] is None):
            raise ValueError("Missing the required parameter `analytic_id` when calling `get_analytic`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'analytic_id' in params:
            path_params['analyticId'] = params['analytic_id']  # noqa: E501

        query_params = []

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
            '/analytics/{analyticId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Analytics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
