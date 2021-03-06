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


class DatabaseConnector(object):
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
        'database_connector_id': 'int',
        'connector_name': 'str',
        'database_type': 'str',
        'environment_id': 'int',
        'custom_driver_name': 'str',
        'database_name': 'str',
        'host': 'str',
        'instance_name': 'str',
        'jdbc': 'str',
        'password': 'str',
        'port': 'int',
        'schema_name': 'str',
        'sid': 'str',
        'username': 'str',
        'kerberos_auth': 'bool',
        'service_principal': 'str'
    }

    attribute_map = {
        'database_connector_id': 'databaseConnectorId',
        'connector_name': 'connectorName',
        'database_type': 'databaseType',
        'environment_id': 'environmentId',
        'custom_driver_name': 'customDriverName',
        'database_name': 'databaseName',
        'host': 'host',
        'instance_name': 'instanceName',
        'jdbc': 'jdbc',
        'password': 'password',
        'port': 'port',
        'schema_name': 'schemaName',
        'sid': 'sid',
        'username': 'username',
        'kerberos_auth': 'kerberosAuth',
        'service_principal': 'servicePrincipal'
    }

    def __init__(self, database_connector_id=None, connector_name=None, database_type=None, environment_id=None, custom_driver_name=None, database_name=None, host=None, instance_name=None, jdbc=None, password=None, port=None, schema_name=None, sid=None, username=None, kerberos_auth=False, service_principal=None):  # noqa: E501
        """DatabaseConnector - a model defined in Swagger"""  # noqa: E501

        self._database_connector_id = None
        self._connector_name = None
        self._database_type = None
        self._environment_id = None
        self._custom_driver_name = None
        self._database_name = None
        self._host = None
        self._instance_name = None
        self._jdbc = None
        self._password = None
        self._port = None
        self._schema_name = None
        self._sid = None
        self._username = None
        self._kerberos_auth = None
        self._service_principal = None
        self.discriminator = None

        if database_connector_id is not None:
            self.database_connector_id = database_connector_id
        self.connector_name = connector_name
        self.database_type = database_type
        self.environment_id = environment_id
        if custom_driver_name is not None:
            self.custom_driver_name = custom_driver_name
        if database_name is not None:
            self.database_name = database_name
        if host is not None:
            self.host = host
        if instance_name is not None:
            self.instance_name = instance_name
        if jdbc is not None:
            self.jdbc = jdbc
        if password is not None:
            self.password = password
        if port is not None:
            self.port = port
        if schema_name is not None:
            self.schema_name = schema_name
        if sid is not None:
            self.sid = sid
        if username is not None:
            self.username = username
        if kerberos_auth is not None:
            self.kerberos_auth = kerberos_auth
        if service_principal is not None:
            self.service_principal = service_principal

    @property
    def database_connector_id(self):
        """Gets the database_connector_id of this DatabaseConnector.  # noqa: E501

        The ID number of the connector. This field is auto-generated by the Masking Engine.  # noqa: E501

        :return: The database_connector_id of this DatabaseConnector.  # noqa: E501
        :rtype: int
        """
        return self._database_connector_id

    @database_connector_id.setter
    def database_connector_id(self, database_connector_id):
        """Sets the database_connector_id of this DatabaseConnector.

        The ID number of the connector. This field is auto-generated by the Masking Engine.  # noqa: E501

        :param database_connector_id: The database_connector_id of this DatabaseConnector.  # noqa: E501
        :type: int
        """

        self._database_connector_id = database_connector_id

    @property
    def connector_name(self):
        """Gets the connector_name of this DatabaseConnector.  # noqa: E501

        The name of the connector.  # noqa: E501

        :return: The connector_name of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this DatabaseConnector.

        The name of the connector.  # noqa: E501

        :param connector_name: The connector_name of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if connector_name is None:
            raise ValueError("Invalid value for `connector_name`, must not be `None`")  # noqa: E501
        if connector_name is not None and len(connector_name) > 255:
            raise ValueError("Invalid value for `connector_name`, length must be less than or equal to `255`")  # noqa: E501

        self._connector_name = connector_name

    @property
    def database_type(self):
        """Gets the database_type of this DatabaseConnector.  # noqa: E501

        The type of database the connector will connect to.  # noqa: E501

        :return: The database_type of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """Sets the database_type of this DatabaseConnector.

        The type of database the connector will connect to.  # noqa: E501

        :param database_type: The database_type of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if database_type is None:
            raise ValueError("Invalid value for `database_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AURORA_POSTGRES", "DB2", "DB2_ISERIES", "DB2_MAINFRAME", "GENERIC", "MSSQL", "MYSQL", "ORACLE", "POSTGRES", "RDS_POSTGRES", "SYBASE"]  # noqa: E501
        if database_type not in allowed_values:
            raise ValueError(
                "Invalid value for `database_type` ({0}), must be one of {1}"  # noqa: E501
                .format(database_type, allowed_values)
            )

        self._database_type = database_type

    @property
    def environment_id(self):
        """Gets the environment_id of this DatabaseConnector.  # noqa: E501

        The ID of the environment under which to create the connector. Once the connector is created, this value cannot be changed.  # noqa: E501

        :return: The environment_id of this DatabaseConnector.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this DatabaseConnector.

        The ID of the environment under which to create the connector. Once the connector is created, this value cannot be changed.  # noqa: E501

        :param environment_id: The environment_id of this DatabaseConnector.  # noqa: E501
        :type: int
        """
        if environment_id is None:
            raise ValueError("Invalid value for `environment_id`, must not be `None`")  # noqa: E501

        self._environment_id = environment_id

    @property
    def custom_driver_name(self):
        """Gets the custom_driver_name of this DatabaseConnector.  # noqa: E501

        The name of the custom driver to use. Only used for database type 'GENERIC'.  # noqa: E501

        :return: The custom_driver_name of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._custom_driver_name

    @custom_driver_name.setter
    def custom_driver_name(self, custom_driver_name):
        """Sets the custom_driver_name of this DatabaseConnector.

        The name of the custom driver to use. Only used for database type 'GENERIC'.  # noqa: E501

        :param custom_driver_name: The custom_driver_name of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if custom_driver_name is not None and len(custom_driver_name) > 255:
            raise ValueError("Invalid value for `custom_driver_name`, length must be less than or equal to `255`")  # noqa: E501

        self._custom_driver_name = custom_driver_name

    @property
    def database_name(self):
        """Gets the database_name of this DatabaseConnector.  # noqa: E501

        The name of the database to connect to. This field is not valid for database types 'ORACLE' and 'GENERIC'.  # noqa: E501

        :return: The database_name of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DatabaseConnector.

        The name of the database to connect to. This field is not valid for database types 'ORACLE' and 'GENERIC'.  # noqa: E501

        :param database_name: The database_name of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if database_name is not None and len(database_name) > 255:
            raise ValueError("Invalid value for `database_name`, length must be less than or equal to `255`")  # noqa: E501

        self._database_name = database_name

    @property
    def host(self):
        """Gets the host of this DatabaseConnector.  # noqa: E501

        The host name or IP address where the database is located.  # noqa: E501

        :return: The host of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DatabaseConnector.

        The host name or IP address where the database is located.  # noqa: E501

        :param host: The host of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if host is not None and len(host) > 500:
            raise ValueError("Invalid value for `host`, length must be less than or equal to `500`")  # noqa: E501

        self._host = host

    @property
    def instance_name(self):
        """Gets the instance_name of this DatabaseConnector.  # noqa: E501

        The name of the database instance. Only used for database type 'MSSQL'.  # noqa: E501

        :return: The instance_name of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this DatabaseConnector.

        The name of the database instance. Only used for database type 'MSSQL'.  # noqa: E501

        :param instance_name: The instance_name of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if instance_name is not None and len(instance_name) > 50:
            raise ValueError("Invalid value for `instance_name`, length must be less than or equal to `50`")  # noqa: E501

        self._instance_name = instance_name

    @property
    def jdbc(self):
        """Gets the jdbc of this DatabaseConnector.  # noqa: E501

        The jdbc connection string. This can be used as an alternative to specifying a 'host', 'databaseName', 'SID', and 'port'. This value is only applicable when using database types 'ORACLE', 'MSSQL', 'SYBASE', and 'GENERIC'.  # noqa: E501

        :return: The jdbc of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._jdbc

    @jdbc.setter
    def jdbc(self, jdbc):
        """Sets the jdbc of this DatabaseConnector.

        The jdbc connection string. This can be used as an alternative to specifying a 'host', 'databaseName', 'SID', and 'port'. This value is only applicable when using database types 'ORACLE', 'MSSQL', 'SYBASE', and 'GENERIC'.  # noqa: E501

        :param jdbc: The jdbc of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if jdbc is not None and len(jdbc) > 1000:
            raise ValueError("Invalid value for `jdbc`, length must be less than or equal to `1000`")  # noqa: E501

        self._jdbc = jdbc

    @property
    def password(self):
        """Gets the password of this DatabaseConnector.  # noqa: E501

        The password required to access the database. NOTE: For updates, this field does not have to be set. If no password is provided on an update, then the current password will persist.  # noqa: E501

        :return: The password of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DatabaseConnector.

        The password required to access the database. NOTE: For updates, this field does not have to be set. If no password is provided on an update, then the current password will persist.  # noqa: E501

        :param password: The password of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if password is not None and len(password) > 250:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `250`")  # noqa: E501

        self._password = password

    @property
    def port(self):
        """Gets the port of this DatabaseConnector.  # noqa: E501

        The port to use for connecting to the database. This field is not valid for the database type 'GENERIC'.  # noqa: E501

        :return: The port of this DatabaseConnector.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DatabaseConnector.

        The port to use for connecting to the database. This field is not valid for the database type 'GENERIC'.  # noqa: E501

        :param port: The port of this DatabaseConnector.  # noqa: E501
        :type: int
        """
        if port is not None and port > 65535:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if port is not None and port < 0:  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def schema_name(self):
        """Gets the schema_name of this DatabaseConnector.  # noqa: E501

        The schema name on the database. Note that this field should be uppercase for database type 'ORACLE'. Also note that this field is not relevant for database type 'MYSQL'.  # noqa: E501

        :return: The schema_name of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DatabaseConnector.

        The schema name on the database. Note that this field should be uppercase for database type 'ORACLE'. Also note that this field is not relevant for database type 'MYSQL'.  # noqa: E501

        :param schema_name: The schema_name of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if schema_name is not None and len(schema_name) > 255:
            raise ValueError("Invalid value for `schema_name`, length must be less than or equal to `255`")  # noqa: E501

        self._schema_name = schema_name

    @property
    def sid(self):
        """Gets the sid of this DatabaseConnector.  # noqa: E501

        The SID of the Oracle Instance to connect to. This field is only valid for database type 'ORACLE'.  # noqa: E501

        :return: The sid of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this DatabaseConnector.

        The SID of the Oracle Instance to connect to. This field is only valid for database type 'ORACLE'.  # noqa: E501

        :param sid: The sid of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if sid is not None and len(sid) > 255:
            raise ValueError("Invalid value for `sid`, length must be less than or equal to `255`")  # noqa: E501

        self._sid = sid

    @property
    def username(self):
        """Gets the username of this DatabaseConnector.  # noqa: E501

        The username required to access the database. Note that this field should be uppercase for database type 'ORACLE'.  # noqa: E501

        :return: The username of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DatabaseConnector.

        The username required to access the database. Note that this field should be uppercase for database type 'ORACLE'.  # noqa: E501

        :param username: The username of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 255:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501

        self._username = username

    @property
    def kerberos_auth(self):
        """Gets the kerberos_auth of this DatabaseConnector.  # noqa: E501

        Whether to use kerberos to authenticate database connections. When kerberosAuth is enabled, the username field is treated as the kerberos principal. Kerberos must be enabled on the appliance  # noqa: E501

        :return: The kerberos_auth of this DatabaseConnector.  # noqa: E501
        :rtype: bool
        """
        return self._kerberos_auth

    @kerberos_auth.setter
    def kerberos_auth(self, kerberos_auth):
        """Sets the kerberos_auth of this DatabaseConnector.

        Whether to use kerberos to authenticate database connections. When kerberosAuth is enabled, the username field is treated as the kerberos principal. Kerberos must be enabled on the appliance  # noqa: E501

        :param kerberos_auth: The kerberos_auth of this DatabaseConnector.  # noqa: E501
        :type: bool
        """

        self._kerberos_auth = kerberos_auth

    @property
    def service_principal(self):
        """Gets the service_principal of this DatabaseConnector.  # noqa: E501

        The service principal used to access the database. This property is exclusive to Sybase connectors using Kerberos.  # noqa: E501

        :return: The service_principal of this DatabaseConnector.  # noqa: E501
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        """Sets the service_principal of this DatabaseConnector.

        The service principal used to access the database. This property is exclusive to Sybase connectors using Kerberos.  # noqa: E501

        :param service_principal: The service_principal of this DatabaseConnector.  # noqa: E501
        :type: str
        """
        if service_principal is not None and len(service_principal) > 256:
            raise ValueError("Invalid value for `service_principal`, length must be less than or equal to `256`")  # noqa: E501

        self._service_principal = service_principal

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
        if issubclass(DatabaseConnector, dict):
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
        if not isinstance(other, DatabaseConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
