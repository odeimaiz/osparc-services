# coding: utf-8

"""
    simcore-service-webserver API

    simcore-service-webserver rest API definition  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: support@simcore.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class HealthCheck(object):
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
        'status': 'str',
        'version': 'str',
        'api_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'version': 'version',
        'api_version': 'api_version'
    }

    def __init__(self, name=None, status=None, version=None, api_version=None):  # noqa: E501
        """HealthCheck - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._status = None
        self._version = None
        self._api_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if api_version is not None:
            self.api_version = api_version

    @property
    def name(self):
        """Gets the name of this HealthCheck.  # noqa: E501


        :return: The name of this HealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthCheck.


        :param name: The name of this HealthCheck.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this HealthCheck.  # noqa: E501


        :return: The status of this HealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HealthCheck.


        :param status: The status of this HealthCheck.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this HealthCheck.  # noqa: E501


        :return: The version of this HealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this HealthCheck.


        :param version: The version of this HealthCheck.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def api_version(self):
        """Gets the api_version of this HealthCheck.  # noqa: E501


        :return: The api_version of this HealthCheck.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this HealthCheck.


        :param api_version: The api_version of this HealthCheck.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

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
        if not isinstance(other, HealthCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
