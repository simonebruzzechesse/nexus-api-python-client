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


class Request(object):
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
        'system_information': 'bool',
        'thread_dump': 'bool',
        'metrics': 'bool',
        'configuration': 'bool',
        'security': 'bool',
        'log': 'bool',
        'task_log': 'bool',
        'audit_log': 'bool',
        'jmx': 'bool',
        'limit_file_sizes': 'bool',
        'limit_zip_size': 'bool'
    }

    attribute_map = {
        'system_information': 'systemInformation',
        'thread_dump': 'threadDump',
        'metrics': 'metrics',
        'configuration': 'configuration',
        'security': 'security',
        'log': 'log',
        'task_log': 'taskLog',
        'audit_log': 'auditLog',
        'jmx': 'jmx',
        'limit_file_sizes': 'limitFileSizes',
        'limit_zip_size': 'limitZipSize'
    }

    def __init__(self, system_information=None, thread_dump=None, metrics=None, configuration=None, security=None, log=None, task_log=None, audit_log=None, jmx=None, limit_file_sizes=None, limit_zip_size=None, local_vars_configuration=None):  # noqa: E501
        """Request - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_information = None
        self._thread_dump = None
        self._metrics = None
        self._configuration = None
        self._security = None
        self._log = None
        self._task_log = None
        self._audit_log = None
        self._jmx = None
        self._limit_file_sizes = None
        self._limit_zip_size = None
        self.discriminator = None

        if system_information is not None:
            self.system_information = system_information
        if thread_dump is not None:
            self.thread_dump = thread_dump
        if metrics is not None:
            self.metrics = metrics
        if configuration is not None:
            self.configuration = configuration
        if security is not None:
            self.security = security
        if log is not None:
            self.log = log
        if task_log is not None:
            self.task_log = task_log
        if audit_log is not None:
            self.audit_log = audit_log
        if jmx is not None:
            self.jmx = jmx
        if limit_file_sizes is not None:
            self.limit_file_sizes = limit_file_sizes
        if limit_zip_size is not None:
            self.limit_zip_size = limit_zip_size

    @property
    def system_information(self):
        """Gets the system_information of this Request.  # noqa: E501


        :return: The system_information of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._system_information

    @system_information.setter
    def system_information(self, system_information):
        """Sets the system_information of this Request.


        :param system_information: The system_information of this Request.  # noqa: E501
        :type: bool
        """

        self._system_information = system_information

    @property
    def thread_dump(self):
        """Gets the thread_dump of this Request.  # noqa: E501


        :return: The thread_dump of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._thread_dump

    @thread_dump.setter
    def thread_dump(self, thread_dump):
        """Sets the thread_dump of this Request.


        :param thread_dump: The thread_dump of this Request.  # noqa: E501
        :type: bool
        """

        self._thread_dump = thread_dump

    @property
    def metrics(self):
        """Gets the metrics of this Request.  # noqa: E501


        :return: The metrics of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Request.


        :param metrics: The metrics of this Request.  # noqa: E501
        :type: bool
        """

        self._metrics = metrics

    @property
    def configuration(self):
        """Gets the configuration of this Request.  # noqa: E501


        :return: The configuration of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this Request.


        :param configuration: The configuration of this Request.  # noqa: E501
        :type: bool
        """

        self._configuration = configuration

    @property
    def security(self):
        """Gets the security of this Request.  # noqa: E501


        :return: The security of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this Request.


        :param security: The security of this Request.  # noqa: E501
        :type: bool
        """

        self._security = security

    @property
    def log(self):
        """Gets the log of this Request.  # noqa: E501


        :return: The log of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Request.


        :param log: The log of this Request.  # noqa: E501
        :type: bool
        """

        self._log = log

    @property
    def task_log(self):
        """Gets the task_log of this Request.  # noqa: E501


        :return: The task_log of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._task_log

    @task_log.setter
    def task_log(self, task_log):
        """Sets the task_log of this Request.


        :param task_log: The task_log of this Request.  # noqa: E501
        :type: bool
        """

        self._task_log = task_log

    @property
    def audit_log(self):
        """Gets the audit_log of this Request.  # noqa: E501


        :return: The audit_log of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._audit_log

    @audit_log.setter
    def audit_log(self, audit_log):
        """Sets the audit_log of this Request.


        :param audit_log: The audit_log of this Request.  # noqa: E501
        :type: bool
        """

        self._audit_log = audit_log

    @property
    def jmx(self):
        """Gets the jmx of this Request.  # noqa: E501


        :return: The jmx of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._jmx

    @jmx.setter
    def jmx(self, jmx):
        """Sets the jmx of this Request.


        :param jmx: The jmx of this Request.  # noqa: E501
        :type: bool
        """

        self._jmx = jmx

    @property
    def limit_file_sizes(self):
        """Gets the limit_file_sizes of this Request.  # noqa: E501


        :return: The limit_file_sizes of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._limit_file_sizes

    @limit_file_sizes.setter
    def limit_file_sizes(self, limit_file_sizes):
        """Sets the limit_file_sizes of this Request.


        :param limit_file_sizes: The limit_file_sizes of this Request.  # noqa: E501
        :type: bool
        """

        self._limit_file_sizes = limit_file_sizes

    @property
    def limit_zip_size(self):
        """Gets the limit_zip_size of this Request.  # noqa: E501


        :return: The limit_zip_size of this Request.  # noqa: E501
        :rtype: bool
        """
        return self._limit_zip_size

    @limit_zip_size.setter
    def limit_zip_size(self, limit_zip_size):
        """Sets the limit_zip_size of this Request.


        :param limit_zip_size: The limit_zip_size of this Request.  # noqa: E501
        :type: bool
        """

        self._limit_zip_size = limit_zip_size

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
        if not isinstance(other, Request):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Request):
            return True

        return self.to_dict() != other.to_dict()