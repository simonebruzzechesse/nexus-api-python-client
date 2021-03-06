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


class ReadOnlyState(object):
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
        'system_initiated': 'bool',
        'summary_reason': 'str',
        'frozen': 'bool'
    }

    attribute_map = {
        'system_initiated': 'systemInitiated',
        'summary_reason': 'summaryReason',
        'frozen': 'frozen'
    }

    def __init__(self, system_initiated=None, summary_reason=None, frozen=None, local_vars_configuration=None):  # noqa: E501
        """ReadOnlyState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_initiated = None
        self._summary_reason = None
        self._frozen = None
        self.discriminator = None

        if system_initiated is not None:
            self.system_initiated = system_initiated
        if summary_reason is not None:
            self.summary_reason = summary_reason
        if frozen is not None:
            self.frozen = frozen

    @property
    def system_initiated(self):
        """Gets the system_initiated of this ReadOnlyState.  # noqa: E501


        :return: The system_initiated of this ReadOnlyState.  # noqa: E501
        :rtype: bool
        """
        return self._system_initiated

    @system_initiated.setter
    def system_initiated(self, system_initiated):
        """Sets the system_initiated of this ReadOnlyState.


        :param system_initiated: The system_initiated of this ReadOnlyState.  # noqa: E501
        :type: bool
        """

        self._system_initiated = system_initiated

    @property
    def summary_reason(self):
        """Gets the summary_reason of this ReadOnlyState.  # noqa: E501


        :return: The summary_reason of this ReadOnlyState.  # noqa: E501
        :rtype: str
        """
        return self._summary_reason

    @summary_reason.setter
    def summary_reason(self, summary_reason):
        """Sets the summary_reason of this ReadOnlyState.


        :param summary_reason: The summary_reason of this ReadOnlyState.  # noqa: E501
        :type: str
        """

        self._summary_reason = summary_reason

    @property
    def frozen(self):
        """Gets the frozen of this ReadOnlyState.  # noqa: E501


        :return: The frozen of this ReadOnlyState.  # noqa: E501
        :rtype: bool
        """
        return self._frozen

    @frozen.setter
    def frozen(self, frozen):
        """Sets the frozen of this ReadOnlyState.


        :param frozen: The frozen of this ReadOnlyState.  # noqa: E501
        :type: bool
        """

        self._frozen = frozen

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
        if not isinstance(other, ReadOnlyState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadOnlyState):
            return True

        return self.to_dict() != other.to_dict()
