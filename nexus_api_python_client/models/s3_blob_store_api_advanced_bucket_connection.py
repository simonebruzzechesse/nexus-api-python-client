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


class S3BlobStoreApiAdvancedBucketConnection(object):
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
        'endpoint': 'str',
        'signer_type': 'str',
        'force_path_style': 'bool'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'signer_type': 'signerType',
        'force_path_style': 'forcePathStyle'
    }

    def __init__(self, endpoint=None, signer_type=None, force_path_style=None, local_vars_configuration=None):  # noqa: E501
        """S3BlobStoreApiAdvancedBucketConnection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._endpoint = None
        self._signer_type = None
        self._force_path_style = None
        self.discriminator = None

        if endpoint is not None:
            self.endpoint = endpoint
        if signer_type is not None:
            self.signer_type = signer_type
        if force_path_style is not None:
            self.force_path_style = force_path_style

    @property
    def endpoint(self):
        """Gets the endpoint of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501

        A custom endpoint URL for third party object stores using the S3 API.  # noqa: E501

        :return: The endpoint of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this S3BlobStoreApiAdvancedBucketConnection.

        A custom endpoint URL for third party object stores using the S3 API.  # noqa: E501

        :param endpoint: The endpoint of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def signer_type(self):
        """Gets the signer_type of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501

        An API signature version which may be required for third party object stores using the S3 API.  # noqa: E501

        :return: The signer_type of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :rtype: str
        """
        return self._signer_type

    @signer_type.setter
    def signer_type(self, signer_type):
        """Sets the signer_type of this S3BlobStoreApiAdvancedBucketConnection.

        An API signature version which may be required for third party object stores using the S3 API.  # noqa: E501

        :param signer_type: The signer_type of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :type: str
        """

        self._signer_type = signer_type

    @property
    def force_path_style(self):
        """Gets the force_path_style of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501

        Setting this flag will result in path-style access being used for all requests.  # noqa: E501

        :return: The force_path_style of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :rtype: bool
        """
        return self._force_path_style

    @force_path_style.setter
    def force_path_style(self, force_path_style):
        """Sets the force_path_style of this S3BlobStoreApiAdvancedBucketConnection.

        Setting this flag will result in path-style access being used for all requests.  # noqa: E501

        :param force_path_style: The force_path_style of this S3BlobStoreApiAdvancedBucketConnection.  # noqa: E501
        :type: bool
        """

        self._force_path_style = force_path_style

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
        if not isinstance(other, S3BlobStoreApiAdvancedBucketConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, S3BlobStoreApiAdvancedBucketConnection):
            return True

        return self.to_dict() != other.to_dict()
