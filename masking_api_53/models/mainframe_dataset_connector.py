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


class MainframeDatasetConnector(object):
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
        'mainframe_dataset_connector_id': 'int',
        'connector_name': 'str',
        'environment_id': 'int',
        'connection_info': 'ConnectionInfo'
    }

    attribute_map = {
        'mainframe_dataset_connector_id': 'mainframe-datasetConnectorId',
        'connector_name': 'connectorName',
        'environment_id': 'environmentId',
        'connection_info': 'connectionInfo'
    }

    def __init__(self, mainframe_dataset_connector_id=None, connector_name=None, environment_id=None, connection_info=None):  # noqa: E501
        """MainframeDatasetConnector - a model defined in Swagger"""  # noqa: E501

        self._mainframe_dataset_connector_id = None
        self._connector_name = None
        self._environment_id = None
        self._connection_info = None
        self.discriminator = None

        if mainframe_dataset_connector_id is not None:
            self.mainframe_dataset_connector_id = mainframe_dataset_connector_id
        self.connector_name = connector_name
        self.environment_id = environment_id
        self.connection_info = connection_info

    @property
    def mainframe_dataset_connector_id(self):
        """Gets the mainframe_dataset_connector_id of this MainframeDatasetConnector.  # noqa: E501

        The ID number of the Mainframe Dataset connector. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The mainframe_dataset_connector_id of this MainframeDatasetConnector.  # noqa: E501
        :rtype: int
        """
        return self._mainframe_dataset_connector_id

    @mainframe_dataset_connector_id.setter
    def mainframe_dataset_connector_id(self, mainframe_dataset_connector_id):
        """Sets the mainframe_dataset_connector_id of this MainframeDatasetConnector.

        The ID number of the Mainframe Dataset connector. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param mainframe_dataset_connector_id: The mainframe_dataset_connector_id of this MainframeDatasetConnector.  # noqa: E501
        :type: int
        """

        self._mainframe_dataset_connector_id = mainframe_dataset_connector_id

    @property
    def connector_name(self):
        """Gets the connector_name of this MainframeDatasetConnector.  # noqa: E501

        The name of the Mainframe Dataset connector.  # noqa: E501

        :return: The connector_name of this MainframeDatasetConnector.  # noqa: E501
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this MainframeDatasetConnector.

        The name of the Mainframe Dataset connector.  # noqa: E501

        :param connector_name: The connector_name of this MainframeDatasetConnector.  # noqa: E501
        :type: str
        """
        if connector_name is None:
            raise ValueError("Invalid value for `connector_name`, must not be `None`")  # noqa: E501
        if connector_name is not None and len(connector_name) > 45:
            raise ValueError("Invalid value for `connector_name`, length must be less than or equal to `45`")  # noqa: E501

        self._connector_name = connector_name

    @property
    def environment_id(self):
        """Gets the environment_id of this MainframeDatasetConnector.  # noqa: E501

        The ID number of the environment that the Mainframe Dataset connector is in. Once the Mainframe Dataset connector is created, this field cannot be changed.  # noqa: E501

        :return: The environment_id of this MainframeDatasetConnector.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this MainframeDatasetConnector.

        The ID number of the environment that the Mainframe Dataset connector is in. Once the Mainframe Dataset connector is created, this field cannot be changed.  # noqa: E501

        :param environment_id: The environment_id of this MainframeDatasetConnector.  # noqa: E501
        :type: int
        """
        if environment_id is None:
            raise ValueError("Invalid value for `environment_id`, must not be `None`")  # noqa: E501

        self._environment_id = environment_id

    @property
    def connection_info(self):
        """Gets the connection_info of this MainframeDatasetConnector.  # noqa: E501

        This field object contains the information needed to connect to the underlying files.  # noqa: E501

        :return: The connection_info of this MainframeDatasetConnector.  # noqa: E501
        :rtype: ConnectionInfo
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        """Sets the connection_info of this MainframeDatasetConnector.

        This field object contains the information needed to connect to the underlying files.  # noqa: E501

        :param connection_info: The connection_info of this MainframeDatasetConnector.  # noqa: E501
        :type: ConnectionInfo
        """
        if connection_info is None:
            raise ValueError("Invalid value for `connection_info`, must not be `None`")  # noqa: E501

        self._connection_info = connection_info

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
        if issubclass(MainframeDatasetConnector, dict):
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
        if not isinstance(other, MainframeDatasetConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
