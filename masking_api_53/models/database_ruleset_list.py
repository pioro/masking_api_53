# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DatabaseRulesetList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_info': 'PageInfo',
        'response_list': 'list[DatabaseRuleset]'
    }

    attribute_map = {
        'page_info': '_pageInfo',
        'response_list': 'responseList'
    }

    def __init__(self, page_info=None, response_list=None):  # noqa: E501
        """DatabaseRulesetList - a model defined in Swagger"""  # noqa: E501

        self._page_info = None
        self._response_list = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if response_list is not None:
            self.response_list = response_list

    @property
    def page_info(self):
        """Gets the page_info of this DatabaseRulesetList.  # noqa: E501


        :return: The page_info of this DatabaseRulesetList.  # noqa: E501
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this DatabaseRulesetList.


        :param page_info: The page_info of this DatabaseRulesetList.  # noqa: E501
        :type: PageInfo
        """

        self._page_info = page_info

    @property
    def response_list(self):
        """Gets the response_list of this DatabaseRulesetList.  # noqa: E501


        :return: The response_list of this DatabaseRulesetList.  # noqa: E501
        :rtype: list[DatabaseRuleset]
        """
        return self._response_list

    @response_list.setter
    def response_list(self, response_list):
        """Sets the response_list of this DatabaseRulesetList.


        :param response_list: The response_list of this DatabaseRulesetList.  # noqa: E501
        :type: list[DatabaseRuleset]
        """

        self._response_list = response_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DatabaseRulesetList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatabaseRulesetList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
