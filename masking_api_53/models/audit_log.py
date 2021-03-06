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


class AuditLog(object):
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
        'audit_id': 'int',
        'user_name': 'str',
        'activity_description': 'str',
        'activity_time': 'datetime',
        'action_type': 'str',
        'target': 'str',
        'status': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'audit_id': 'auditId',
        'user_name': 'userName',
        'activity_description': 'activityDescription',
        'activity_time': 'activityTime',
        'action_type': 'actionType',
        'target': 'target',
        'status': 'status',
        'ip_address': 'ipAddress'
    }

    def __init__(self, audit_id=None, user_name=None, activity_description=None, activity_time=None, action_type=None, target=None, status=None, ip_address=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501

        self._audit_id = None
        self._user_name = None
        self._activity_description = None
        self._activity_time = None
        self._action_type = None
        self._target = None
        self._status = None
        self._ip_address = None
        self.discriminator = None

        if audit_id is not None:
            self.audit_id = audit_id
        if user_name is not None:
            self.user_name = user_name
        if activity_description is not None:
            self.activity_description = activity_description
        if activity_time is not None:
            self.activity_time = activity_time
        if action_type is not None:
            self.action_type = action_type
        if target is not None:
            self.target = target
        if status is not None:
            self.status = status
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def audit_id(self):
        """Gets the audit_id of this AuditLog.  # noqa: E501

        The ID of the Audit Log. This field will be generated by the Masking Engine.  # noqa: E501

        :return: The audit_id of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this AuditLog.

        The ID of the Audit Log. This field will be generated by the Masking Engine.  # noqa: E501

        :param audit_id: The audit_id of this AuditLog.  # noqa: E501
        :type: int
        """

        self._audit_id = audit_id

    @property
    def user_name(self):
        """Gets the user_name of this AuditLog.  # noqa: E501

        The name for the user that took the action for this entry.  # noqa: E501

        :return: The user_name of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuditLog.

        The name for the user that took the action for this entry.  # noqa: E501

        :param user_name: The user_name of this AuditLog.  # noqa: E501
        :type: str
        """
        if user_name is not None and len(user_name) > 1000:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `1000`")  # noqa: E501

        self._user_name = user_name

    @property
    def activity_description(self):
        """Gets the activity_description of this AuditLog.  # noqa: E501

        A description of the action that occurred for this Audit Log entry. This will usually include the user friendly names of the involved objects.  # noqa: E501

        :return: The activity_description of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._activity_description

    @activity_description.setter
    def activity_description(self, activity_description):
        """Sets the activity_description of this AuditLog.

        A description of the action that occurred for this Audit Log entry. This will usually include the user friendly names of the involved objects.  # noqa: E501

        :param activity_description: The activity_description of this AuditLog.  # noqa: E501
        :type: str
        """
        if activity_description is not None and len(activity_description) > 1000:
            raise ValueError("Invalid value for `activity_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._activity_description = activity_description

    @property
    def activity_time(self):
        """Gets the activity_time of this AuditLog.  # noqa: E501

        The date and time that the action for this Audit Log entry occurred.  # noqa: E501

        :return: The activity_time of this AuditLog.  # noqa: E501
        :rtype: datetime
        """
        return self._activity_time

    @activity_time.setter
    def activity_time(self, activity_time):
        """Sets the activity_time of this AuditLog.

        The date and time that the action for this Audit Log entry occurred.  # noqa: E501

        :param activity_time: The activity_time of this AuditLog.  # noqa: E501
        :type: datetime
        """

        self._activity_time = activity_time

    @property
    def action_type(self):
        """Gets the action_type of this AuditLog.  # noqa: E501

        The type of action that occurred for this Audit Log entry.  # noqa: E501

        :return: The action_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this AuditLog.

        The type of action that occurred for this Audit Log entry.  # noqa: E501

        :param action_type: The action_type of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANCEL", "CREATE", "DELETE", "EDIT", "EXPORT", "GET", "GET_ALL", "IMPORT", "LOCK", "LOGIN", "LOGOUT", "RUN", "TEST", "UNLOCK"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def target(self):
        """Gets the target of this AuditLog.  # noqa: E501

        The type object or operation that the action occurred on for this Audit Log entry.  # noqa: E501

        :return: The target of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AuditLog.

        The type object or operation that the action occurred on for this Audit Log entry.  # noqa: E501

        :param target: The target of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALGORITHM", "ANALYTIC", "APPLICATION", "APPLICATION_LOG", "APPLICATION_SETTING", "ASYNC_TASK", "AUDIT_LOG", "COLUMN_METADATA", "DATABASE_CONNECTOR", "DATABASE_RULESET", "DEBUG_BREAKPOINT", "DOMAIN", "ENCRYPTION_KEY", "ENVIRONMENT", "EXECUTION", "EXECUTION_EVENT", "FILE_CONNECTOR", "FILE_DOWNLOAD", "FILE_FIELD_METADATA", "FILE_FORMAT", "FILE_METADATA", "FILE_RULESET", "FILE_UPLOAD", "INSTALLATION", "LDAP", "MAINFRAME_DATASET_CONNECTOR", "MAINFRAME_DATASET_FIELD_METADATA", "MAINFRAME_DATASET_FORMAT", "MAINFRAME_DATASET_METADATA", "MAINFRAME_DATASET_RULESET", "MASKING_JOB", "NON_CONFORMING_DATA_SAMPLE", "PROFILE_EXPRESSION", "PROFILE_JOB", "PROFILE_SET", "REIDENTIFICATION_JOB", "ROLE", "SSH_KEY", "SSO", "SYNCABLE_OBJECT", "SYSTEM_INFORMATION", "TABLE_METADATA", "TOKENIZATION_JOB", "UNIFIED_AUTH", "USER"]  # noqa: E501
        if target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                .format(target, allowed_values)
            )

        self._target = target

    @property
    def status(self):
        """Gets the status of this AuditLog.  # noqa: E501

        The status of the action that occurred for this Audit Log entry. This can change over time as ATTEMPTED actions are completed.  # noqa: E501

        :return: The status of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuditLog.

        The status of the action that occurred for this Audit Log entry. This can change over time as ATTEMPTED actions are completed.  # noqa: E501

        :param status: The status of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["ATTEMPTED", "FAILED", "SUCCEEDED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def ip_address(self):
        """Gets the ip_address of this AuditLog.  # noqa: E501

        The IP address of the user who performed the action for this Audit Log entry.  # noqa: E501

        :return: The ip_address of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this AuditLog.

        The IP address of the user who performed the action for this Audit Log entry.  # noqa: E501

        :param ip_address: The ip_address of this AuditLog.  # noqa: E501
        :type: str
        """
        if ip_address is not None and len(ip_address) > 45:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `45`")  # noqa: E501

        self._ip_address = ip_address

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
