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

from openapi_client.configuration import Configuration


class DockerHostedRepositoryApiRequest(object):
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
        'online': 'bool',
        'storage': 'HostedStorageAttributes',
        'cleanup': 'CleanupPolicyAttributes',
        'docker': 'DockerAttributes'
    }

    attribute_map = {
        'name': 'name',
        'online': 'online',
        'storage': 'storage',
        'cleanup': 'cleanup',
        'docker': 'docker'
    }

    def __init__(self, name=None, online=None, storage=None, cleanup=None, docker=None, local_vars_configuration=None):  # noqa: E501
        """DockerHostedRepositoryApiRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._online = None
        self._storage = None
        self._cleanup = None
        self._docker = None
        self.discriminator = None

        self.name = name
        self.online = online
        self.storage = storage
        if cleanup is not None:
            self.cleanup = cleanup
        self.docker = docker

    @property
    def name(self):
        """Gets the name of this DockerHostedRepositoryApiRequest.  # noqa: E501

        A unique identifier for this repository  # noqa: E501

        :return: The name of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DockerHostedRepositoryApiRequest.

        A unique identifier for this repository  # noqa: E501

        :param name: The name of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def online(self):
        """Gets the online of this DockerHostedRepositoryApiRequest.  # noqa: E501

        Whether this repository accepts incoming requests  # noqa: E501

        :return: The online of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this DockerHostedRepositoryApiRequest.

        Whether this repository accepts incoming requests  # noqa: E501

        :param online: The online of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and online is None:  # noqa: E501
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

    @property
    def storage(self):
        """Gets the storage of this DockerHostedRepositoryApiRequest.  # noqa: E501


        :return: The storage of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :rtype: HostedStorageAttributes
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this DockerHostedRepositoryApiRequest.


        :param storage: The storage of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :type: HostedStorageAttributes
        """
        if self.local_vars_configuration.client_side_validation and storage is None:  # noqa: E501
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def cleanup(self):
        """Gets the cleanup of this DockerHostedRepositoryApiRequest.  # noqa: E501


        :return: The cleanup of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :rtype: CleanupPolicyAttributes
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this DockerHostedRepositoryApiRequest.


        :param cleanup: The cleanup of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :type: CleanupPolicyAttributes
        """

        self._cleanup = cleanup

    @property
    def docker(self):
        """Gets the docker of this DockerHostedRepositoryApiRequest.  # noqa: E501


        :return: The docker of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :rtype: DockerAttributes
        """
        return self._docker

    @docker.setter
    def docker(self, docker):
        """Sets the docker of this DockerHostedRepositoryApiRequest.


        :param docker: The docker of this DockerHostedRepositoryApiRequest.  # noqa: E501
        :type: DockerAttributes
        """
        if self.local_vars_configuration.client_side_validation and docker is None:  # noqa: E501
            raise ValueError("Invalid value for `docker`, must not be `None`")  # noqa: E501

        self._docker = docker

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
        if not isinstance(other, DockerHostedRepositoryApiRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerHostedRepositoryApiRequest):
            return True

        return self.to_dict() != other.to_dict()
