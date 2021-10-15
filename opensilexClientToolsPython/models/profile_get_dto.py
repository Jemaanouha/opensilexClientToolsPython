# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProfileGetDTO(object):
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
        'uri': 'str',
        'name': 'str',
        'credentials': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'credentials': 'credentials'
    }

    def __init__(self, uri=None, name=None, credentials=None):  # noqa: E501
        """ProfileGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._credentials = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if credentials is not None:
            self.credentials = credentials

    @property
    def uri(self):
        """Gets the uri of this ProfileGetDTO.  # noqa: E501

        User URI  # noqa: E501

        :return: The uri of this ProfileGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ProfileGetDTO.

        User URI  # noqa: E501

        :param uri: The uri of this ProfileGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ProfileGetDTO.  # noqa: E501

        Profile name  # noqa: E501

        :return: The name of this ProfileGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileGetDTO.

        Profile name  # noqa: E501

        :param name: The name of this ProfileGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def credentials(self):
        """Gets the credentials of this ProfileGetDTO.  # noqa: E501

        Profile credentials  # noqa: E501

        :return: The credentials of this ProfileGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ProfileGetDTO.

        Profile credentials  # noqa: E501

        :param credentials: The credentials of this ProfileGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._credentials = credentials

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
        if issubclass(ProfileGetDTO, dict):
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
        if not isinstance(other, ProfileGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
