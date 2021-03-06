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


class ComponentXO(object):
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
        'repository': 'str',
        'format': 'str',
        'group': 'str',
        'name': 'str',
        'version': 'str',
        'assets': 'list[AssetXO]'
    }

    attribute_map = {
        'id': 'id',
        'repository': 'repository',
        'format': 'format',
        'group': 'group',
        'name': 'name',
        'version': 'version',
        'assets': 'assets'
    }

    def __init__(self, id=None, repository=None, format=None, group=None, name=None, version=None, assets=None, local_vars_configuration=None):  # noqa: E501
        """ComponentXO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._repository = None
        self._format = None
        self._group = None
        self._name = None
        self._version = None
        self._assets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository is not None:
            self.repository = repository
        if format is not None:
            self.format = format
        if group is not None:
            self.group = group
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if assets is not None:
            self.assets = assets

    @property
    def id(self):
        """Gets the id of this ComponentXO.  # noqa: E501


        :return: The id of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentXO.


        :param id: The id of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def repository(self):
        """Gets the repository of this ComponentXO.  # noqa: E501


        :return: The repository of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ComponentXO.


        :param repository: The repository of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def format(self):
        """Gets the format of this ComponentXO.  # noqa: E501


        :return: The format of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ComponentXO.


        :param format: The format of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def group(self):
        """Gets the group of this ComponentXO.  # noqa: E501


        :return: The group of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ComponentXO.


        :param group: The group of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def name(self):
        """Gets the name of this ComponentXO.  # noqa: E501


        :return: The name of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentXO.


        :param name: The name of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this ComponentXO.  # noqa: E501


        :return: The version of this ComponentXO.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComponentXO.


        :param version: The version of this ComponentXO.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def assets(self):
        """Gets the assets of this ComponentXO.  # noqa: E501


        :return: The assets of this ComponentXO.  # noqa: E501
        :rtype: list[AssetXO]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ComponentXO.


        :param assets: The assets of this ComponentXO.  # noqa: E501
        :type: list[AssetXO]
        """

        self._assets = assets

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
        if not isinstance(other, ComponentXO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentXO):
            return True

        return self.to_dict() != other.to_dict()
