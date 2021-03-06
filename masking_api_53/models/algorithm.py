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


class Algorithm(object):
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
        'algorithm_name': 'str',
        'algorithm_type': 'str',
        'created_by': 'str',
        'description': 'str',
        'algorithm_extension': 'object'
    }

    attribute_map = {
        'algorithm_name': 'algorithmName',
        'algorithm_type': 'algorithmType',
        'created_by': 'createdBy',
        'description': 'description',
        'algorithm_extension': 'algorithmExtension'
    }

    def __init__(self, algorithm_name=None, algorithm_type=None, created_by=None, description=None, algorithm_extension=None):  # noqa: E501
        """Algorithm - a model defined in Swagger"""  # noqa: E501

        self._algorithm_name = None
        self._algorithm_type = None
        self._created_by = None
        self._description = None
        self._algorithm_extension = None
        self.discriminator = None

        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if algorithm_extension is not None:
            self.algorithm_extension = algorithm_extension

    @property
    def algorithm_name(self):
        """Gets the algorithm_name of this Algorithm.  # noqa: E501

        Equivalent to the algorithm name saved by the user through the GUI. For out of the box algorithms, this will be a similar name as that in the GUI, but presented in a more user-friendly format.  # noqa: E501

        :return: The algorithm_name of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        """Sets the algorithm_name of this Algorithm.

        Equivalent to the algorithm name saved by the user through the GUI. For out of the box algorithms, this will be a similar name as that in the GUI, but presented in a more user-friendly format.  # noqa: E501

        :param algorithm_name: The algorithm_name of this Algorithm.  # noqa: E501
        :type: str
        """
        if algorithm_name is None:
            raise ValueError("Invalid value for `algorithm_name`, must not be `None`")  # noqa: E501
        if algorithm_name is not None and len(algorithm_name) > 100:
            raise ValueError("Invalid value for `algorithm_name`, length must be less than or equal to `100`")  # noqa: E501

        self._algorithm_name = algorithm_name

    @property
    def algorithm_type(self):
        """Gets the algorithm_type of this Algorithm.  # noqa: E501

        The type of algorithm  # noqa: E501

        :return: The algorithm_type of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        """Sets the algorithm_type of this Algorithm.

        The type of algorithm  # noqa: E501

        :param algorithm_type: The algorithm_type of this Algorithm.  # noqa: E501
        :type: str
        """
        if algorithm_type is None:
            raise ValueError("Invalid value for `algorithm_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BINARY_LOOKUP", "CLEANSING", "CUSTOM_ALGORITHM", "DATE", "LOOKUP", "MAPPING", "MINMAX", "MISC", "REDACTION", "SEGMENT", "TOKENIZATION"]  # noqa: E501
        if algorithm_type not in allowed_values:
            raise ValueError(
                "Invalid value for `algorithm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm_type, allowed_values)
            )

        self._algorithm_type = algorithm_type

    @property
    def created_by(self):
        """Gets the created_by of this Algorithm.  # noqa: E501

        The name of the user that created the algorithm  # noqa: E501

        :return: The created_by of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Algorithm.

        The name of the user that created the algorithm  # noqa: E501

        :param created_by: The created_by of this Algorithm.  # noqa: E501
        :type: str
        """
        if created_by is not None and len(created_by) > 255:
            raise ValueError("Invalid value for `created_by`, length must be less than or equal to `255`")  # noqa: E501

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this Algorithm.  # noqa: E501

        The description of the algorithm  # noqa: E501

        :return: The description of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Algorithm.

        The description of the algorithm  # noqa: E501

        :param description: The description of this Algorithm.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def algorithm_extension(self):
        """Gets the algorithm_extension of this Algorithm.  # noqa: E501


        :return: The algorithm_extension of this Algorithm.  # noqa: E501
        :rtype: object
        """
        return self._algorithm_extension

    @algorithm_extension.setter
    def algorithm_extension(self, algorithm_extension):
        """Sets the algorithm_extension of this Algorithm.


        :param algorithm_extension: The algorithm_extension of this Algorithm.  # noqa: E501
        :type: object
        """

        self._algorithm_extension = algorithm_extension

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
        if issubclass(Algorithm, dict):
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
        if not isinstance(other, Algorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
