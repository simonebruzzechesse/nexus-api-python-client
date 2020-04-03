# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.20.1-01
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nexus_api_python_client.configuration import Configuration


class IqConnectionXo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'enabled': 'bool',
        'show_link': 'bool',
        'url': 'str',
        'authentication_type': 'str',
        'username': 'str',
        'password': 'str',
        'use_trust_store_for_url': 'bool',
        'timeout_seconds': 'int',
        'properties': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'show_link': 'showLink',
        'url': 'url',
        'authentication_type': 'authenticationType',
        'username': 'username',
        'password': 'password',
        'use_trust_store_for_url': 'useTrustStoreForUrl',
        'timeout_seconds': 'timeoutSeconds',
        'properties': 'properties'
    }

    def __init__(self, enabled=None, show_link=None, url=None, authentication_type=None, username=None, password=None, use_trust_store_for_url=None, timeout_seconds=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """IqConnectionXo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._show_link = None
        self._url = None
        self._authentication_type = None
        self._username = None
        self._password = None
        self._use_trust_store_for_url = None
        self._timeout_seconds = None
        self._properties = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if show_link is not None:
            self.show_link = show_link
        if url is not None:
            self.url = url
        self.authentication_type = authentication_type
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if use_trust_store_for_url is not None:
            self.use_trust_store_for_url = use_trust_store_for_url
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if properties is not None:
            self.properties = properties

    @property
    def enabled(self):
        """Gets the enabled of this IqConnectionXo.  # noqa: E501

        Whether to use IQ Server  # noqa: E501

        :return: The enabled of this IqConnectionXo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IqConnectionXo.

        Whether to use IQ Server  # noqa: E501

        :param enabled: The enabled of this IqConnectionXo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def show_link(self):
        """Gets the show_link of this IqConnectionXo.  # noqa: E501

        Show IQ Server link in Browse menu when server is enabled  # noqa: E501

        :return: The show_link of this IqConnectionXo.  # noqa: E501
        :rtype: bool
        """
        return self._show_link

    @show_link.setter
    def show_link(self, show_link):
        """Sets the show_link of this IqConnectionXo.

        Show IQ Server link in Browse menu when server is enabled  # noqa: E501

        :param show_link: The show_link of this IqConnectionXo.  # noqa: E501
        :type: bool
        """

        self._show_link = show_link

    @property
    def url(self):
        """Gets the url of this IqConnectionXo.  # noqa: E501

        The address of your IQ Server  # noqa: E501

        :return: The url of this IqConnectionXo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IqConnectionXo.

        The address of your IQ Server  # noqa: E501

        :param url: The url of this IqConnectionXo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def authentication_type(self):
        """Gets the authentication_type of this IqConnectionXo.  # noqa: E501

        Authentication method  # noqa: E501

        :return: The authentication_type of this IqConnectionXo.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this IqConnectionXo.

        Authentication method  # noqa: E501

        :param authentication_type: The authentication_type of this IqConnectionXo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and authentication_type is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501
        allowed_values = ["USER", "PKI"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and authentication_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `authentication_type` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_type, allowed_values)
            )

        self._authentication_type = authentication_type

    @property
    def username(self):
        """Gets the username of this IqConnectionXo.  # noqa: E501

        User with access to IQ Server  # noqa: E501

        :return: The username of this IqConnectionXo.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this IqConnectionXo.

        User with access to IQ Server  # noqa: E501

        :param username: The username of this IqConnectionXo.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this IqConnectionXo.  # noqa: E501

        Credentials for the IQ Server User  # noqa: E501

        :return: The password of this IqConnectionXo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this IqConnectionXo.

        Credentials for the IQ Server User  # noqa: E501

        :param password: The password of this IqConnectionXo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def use_trust_store_for_url(self):
        """Gets the use_trust_store_for_url of this IqConnectionXo.  # noqa: E501

        Use certificates stored in the Nexus truststore to connect to IQ Server  # noqa: E501

        :return: The use_trust_store_for_url of this IqConnectionXo.  # noqa: E501
        :rtype: bool
        """
        return self._use_trust_store_for_url

    @use_trust_store_for_url.setter
    def use_trust_store_for_url(self, use_trust_store_for_url):
        """Sets the use_trust_store_for_url of this IqConnectionXo.

        Use certificates stored in the Nexus truststore to connect to IQ Server  # noqa: E501

        :param use_trust_store_for_url: The use_trust_store_for_url of this IqConnectionXo.  # noqa: E501
        :type: bool
        """

        self._use_trust_store_for_url = use_trust_store_for_url

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this IqConnectionXo.  # noqa: E501

        Seconds to wait for activity before stopping and retrying the connection. Leave blank to use the globally defined HTTP timeout.  # noqa: E501

        :return: The timeout_seconds of this IqConnectionXo.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this IqConnectionXo.

        Seconds to wait for activity before stopping and retrying the connection. Leave blank to use the globally defined HTTP timeout.  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this IqConnectionXo.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                timeout_seconds is not None and timeout_seconds > 3600):  # noqa: E501
            raise ValueError("Invalid value for `timeout_seconds`, must be a value less than or equal to `3600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timeout_seconds is not None and timeout_seconds < 1):  # noqa: E501
            raise ValueError("Invalid value for `timeout_seconds`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout_seconds = timeout_seconds

    @property
    def properties(self):
        """Gets the properties of this IqConnectionXo.  # noqa: E501

        Additional properties to configure for IQ Server  # noqa: E501

        :return: The properties of this IqConnectionXo.  # noqa: E501
        :rtype: str
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this IqConnectionXo.

        Additional properties to configure for IQ Server  # noqa: E501

        :param properties: The properties of this IqConnectionXo.  # noqa: E501
        :type: str
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IqConnectionXo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IqConnectionXo):
            return True

        return self.to_dict() != other.to_dict()
