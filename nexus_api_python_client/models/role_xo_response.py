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


class RoleXOResponse(object):
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
        'id': 'str',
        'source': 'str',
        'name': 'str',
        'description': 'str',
        'privileges': 'list[str]',
        'roles': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'name': 'name',
        'description': 'description',
        'privileges': 'privileges',
        'roles': 'roles'
    }

    def __init__(self, id=None, source=None, name=None, description=None, privileges=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """RoleXOResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._source = None
        self._name = None
        self._description = None
        self._privileges = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if privileges is not None:
            self.privileges = privileges
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        """Gets the id of this RoleXOResponse.  # noqa: E501

        The id of the role.  # noqa: E501

        :return: The id of this RoleXOResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleXOResponse.

        The id of the role.  # noqa: E501

        :param id: The id of this RoleXOResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source(self):
        """Gets the source of this RoleXOResponse.  # noqa: E501

        The user source which is the origin of this role.  # noqa: E501

        :return: The source of this RoleXOResponse.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RoleXOResponse.

        The user source which is the origin of this role.  # noqa: E501

        :param source: The source of this RoleXOResponse.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def name(self):
        """Gets the name of this RoleXOResponse.  # noqa: E501

        The name of the role.  # noqa: E501

        :return: The name of this RoleXOResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleXOResponse.

        The name of the role.  # noqa: E501

        :param name: The name of this RoleXOResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleXOResponse.  # noqa: E501

        The description of this role.  # noqa: E501

        :return: The description of this RoleXOResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleXOResponse.

        The description of this role.  # noqa: E501

        :param description: The description of this RoleXOResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def privileges(self):
        """Gets the privileges of this RoleXOResponse.  # noqa: E501

        The list of privileges assigned to this role.  # noqa: E501

        :return: The privileges of this RoleXOResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this RoleXOResponse.

        The list of privileges assigned to this role.  # noqa: E501

        :param privileges: The privileges of this RoleXOResponse.  # noqa: E501
        :type: list[str]
        """

        self._privileges = privileges

    @property
    def roles(self):
        """Gets the roles of this RoleXOResponse.  # noqa: E501

        The list of roles assigned to this role.  # noqa: E501

        :return: The roles of this RoleXOResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this RoleXOResponse.

        The list of roles assigned to this role.  # noqa: E501

        :param roles: The roles of this RoleXOResponse.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

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
        if not isinstance(other, RoleXOResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleXOResponse):
            return True

        return self.to_dict() != other.to_dict()
