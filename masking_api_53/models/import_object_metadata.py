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


class ImportObjectMetadata(object):
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
        'object_identifier': 'object',
        'imported_object_identifier': 'object',
        'object_type': 'str',
        'import_status': 'str',
        'failure_message': 'str'
    }

    attribute_map = {
        'object_identifier': 'objectIdentifier',
        'imported_object_identifier': 'importedObjectIdentifier',
        'object_type': 'objectType',
        'import_status': 'importStatus',
        'failure_message': 'failureMessage'
    }

    def __init__(self, object_identifier=None, imported_object_identifier=None, object_type=None, import_status=None, failure_message=None):  # noqa: E501
        """ImportObjectMetadata - a model defined in Swagger"""  # noqa: E501

        self._object_identifier = None
        self._imported_object_identifier = None
        self._object_type = None
        self._import_status = None
        self._failure_message = None
        self.discriminator = None

        self.object_identifier = object_identifier
        if imported_object_identifier is not None:
            self.imported_object_identifier = imported_object_identifier
        self.object_type = object_type
        if import_status is not None:
            self.import_status = import_status
        if failure_message is not None:
            self.failure_message = failure_message

    @property
    def object_identifier(self):
        """Gets the object_identifier of this ImportObjectMetadata.  # noqa: E501

        Identifier of the imported object on the engine where it was exported from.  # noqa: E501

        :return: The object_identifier of this ImportObjectMetadata.  # noqa: E501
        :rtype: object
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier):
        """Sets the object_identifier of this ImportObjectMetadata.

        Identifier of the imported object on the engine where it was exported from.  # noqa: E501

        :param object_identifier: The object_identifier of this ImportObjectMetadata.  # noqa: E501
        :type: object
        """
        if object_identifier is None:
            raise ValueError("Invalid value for `object_identifier`, must not be `None`")  # noqa: E501

        self._object_identifier = object_identifier

    @property
    def imported_object_identifier(self):
        """Gets the imported_object_identifier of this ImportObjectMetadata.  # noqa: E501

        Identifier of the imported object on this engine.  # noqa: E501

        :return: The imported_object_identifier of this ImportObjectMetadata.  # noqa: E501
        :rtype: object
        """
        return self._imported_object_identifier

    @imported_object_identifier.setter
    def imported_object_identifier(self, imported_object_identifier):
        """Sets the imported_object_identifier of this ImportObjectMetadata.

        Identifier of the imported object on this engine.  # noqa: E501

        :param imported_object_identifier: The imported_object_identifier of this ImportObjectMetadata.  # noqa: E501
        :type: object
        """

        self._imported_object_identifier = imported_object_identifier

    @property
    def object_type(self):
        """Gets the object_type of this ImportObjectMetadata.  # noqa: E501

        Type of object to export  # noqa: E501

        :return: The object_type of this ImportObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ImportObjectMetadata.

        Type of object to export  # noqa: E501

        :param object_type: The object_type of this ImportObjectMetadata.  # noqa: E501
        :type: str
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ALGORITHM_REFERENCE", "APPLICATION_SETTINGS", "BINARYLOOKUP", "CLEANSING", "DATABASE_CONNECTOR", "DATABASE_RULESET", "DATE_SHIFT", "DOMAIN", "DOMAIN_REFERENCE", "FILE_CONNECTOR", "FILE_FORMAT", "FILE_RULESET", "GLOBAL_OBJECT", "KEY", "LOOKUP", "MAPPLET", "MASKING_JOB", "MIN_MAX", "PROFILE_EXPRESSION", "PROFILE_EXPRESSION_REFERENCE", "PROFILE_JOB", "PROFILE_SET", "PROFILE_SET_REFERENCE", "REDACTION", "SEGMENT", "SOURCE_DATABASE_CONNECTOR", "SOURCE_FILE_CONNECTOR", "TOKENIZATION"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"  # noqa: E501
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def import_status(self):
        """Gets the import_status of this ImportObjectMetadata.  # noqa: E501


        :return: The import_status of this ImportObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """Sets the import_status of this ImportObjectMetadata.


        :param import_status: The import_status of this ImportObjectMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "SKIPPED"]  # noqa: E501
        if import_status not in allowed_values:
            raise ValueError(
                "Invalid value for `import_status` ({0}), must be one of {1}"  # noqa: E501
                .format(import_status, allowed_values)
            )

        self._import_status = import_status

    @property
    def failure_message(self):
        """Gets the failure_message of this ImportObjectMetadata.  # noqa: E501


        :return: The failure_message of this ImportObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this ImportObjectMetadata.


        :param failure_message: The failure_message of this ImportObjectMetadata.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

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
        if issubclass(ImportObjectMetadata, dict):
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
        if not isinstance(other, ImportObjectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
