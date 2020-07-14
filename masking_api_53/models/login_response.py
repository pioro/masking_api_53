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


class LoginResponse(object):
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
        'authorization': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization'
    }

    def __init__(self, authorization=None):  # noqa: E501
        """LoginResponse - a model defined in Swagger"""  # noqa: E501

        self._authorization = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization

    @property
    def authorization(self):
        """Gets the authorization of this LoginResponse.  # noqa: E501

        The Authorization token to be provided in the headers of subsequent endpoint calls. Note that the timeout for the Authorization token is controlled by the 'API_AUTHORIZATION_TIMEOUT' property.  # noqa: E501

        :return: The authorization of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this LoginResponse.

        The Authorization token to be provided in the headers of subsequent endpoint calls. Note that the timeout for the Authorization token is controlled by the 'API_AUTHORIZATION_TIMEOUT' property.  # noqa: E501

        :param authorization: The authorization of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._authorization = authorization

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
        if issubclass(LoginResponse, dict):
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
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
