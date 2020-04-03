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


class ApiPrivilegeRepositoryAdminRequest(object):
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
        'name': 'str',
        'description': 'str',
        'actions': 'list[str]',
        'format': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'actions': 'actions',
        'format': 'format',
        'repository': 'repository'
    }

    def __init__(self, name=None, description=None, actions=None, format=None, repository=None, local_vars_configuration=None):  # noqa: E501
        """ApiPrivilegeRepositoryAdminRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._actions = None
        self._format = None
        self._repository = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if actions is not None:
            self.actions = actions
        if format is not None:
            self.format = format
        if repository is not None:
            self.repository = repository

    @property
    def name(self):
        """Gets the name of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :return: The name of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPrivilegeRepositoryAdminRequest.

        The name of the privilege.  This value cannot be changed.  # noqa: E501

        :param name: The name of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-]{1}[a-zA-Z0-9_\-\.]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501


        :return: The description of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiPrivilegeRepositoryAdminRequest.


        :param description: The description of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def actions(self):
        """Gets the actions of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501

        A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as 'run' for script privileges.  # noqa: E501

        :return: The actions of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ApiPrivilegeRepositoryAdminRequest.

        A collection of actions to associate with the privilege, using BREAD syntax (browse,read,edit,add,delete,all) as well as 'run' for script privileges.  # noqa: E501

        :param actions: The actions of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["READ", "BROWSE", "EDIT", "ADD", "DELETE", "RUN", "ASSOCIATE", "DISASSOCIATE", "ALL"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(actions).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def format(self):
        """Gets the format of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501

        The repository format (i.e 'nuget', 'npm') this privilege will grant access to (or * for all).  # noqa: E501

        :return: The format of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ApiPrivilegeRepositoryAdminRequest.

        The repository format (i.e 'nuget', 'npm') this privilege will grant access to (or * for all).  # noqa: E501

        :param format: The format of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def repository(self):
        """Gets the repository of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501

        The name of the repository this privilege will grant access to (or * for all).  # noqa: E501

        :return: The repository of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ApiPrivilegeRepositoryAdminRequest.

        The name of the repository this privilege will grant access to (or * for all).  # noqa: E501

        :param repository: The repository of this ApiPrivilegeRepositoryAdminRequest.  # noqa: E501
        :type: str
        """

        self._repository = repository

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
        if not isinstance(other, ApiPrivilegeRepositoryAdminRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiPrivilegeRepositoryAdminRequest):
            return True

        return self.to_dict() != other.to_dict()
