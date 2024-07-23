# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.2-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class SharedResourceInstanceDTO(object):
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
        'api_url': 'str',
        'label': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'api_url': 'apiUrl',
        'label': 'label'
    }
    def __init__(self,
        uri : 'str' = None,
        api_url : 'str' = None,
        label : 'str' = None):  # noqa: E501
        """SharedResourceInstanceDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._api_url = None
        self._label = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if api_url is not None:
            self.api_url = api_url
        if label is not None:
            self.label = label

    @property
    def uri(self):
        """Gets the uri of this SharedResourceInstanceDTO.  # noqa: E501


        :return: The uri of this SharedResourceInstanceDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this SharedResourceInstanceDTO.


        :param uri: The uri of this SharedResourceInstanceDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def api_url(self):
        """Gets the api_url of this SharedResourceInstanceDTO.  # noqa: E501


        :return: The api_url of this SharedResourceInstanceDTO.  # noqa: E501
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        """Sets the api_url of this SharedResourceInstanceDTO.


        :param api_url: The api_url of this SharedResourceInstanceDTO.  # noqa: E501
        :type: str
        """

        self._api_url = api_url

    @property
    def label(self):
        """Gets the label of this SharedResourceInstanceDTO.  # noqa: E501


        :return: The label of this SharedResourceInstanceDTO.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SharedResourceInstanceDTO.


        :param label: The label of this SharedResourceInstanceDTO.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if issubclass(SharedResourceInstanceDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_api_formated_dict(self):
        """Returns a dict of properties as named in the API rather than in the model itself"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_api_formated_dict() if hasattr(x, "to_api_formated_dict") else x,
                    value
                ))
            elif hasattr(value, "to_api_formated_dict"):
                result[self.attribute_map[attr]] = value.to_api_formated_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_api_formated_dict())
                    if hasattr(item[1], "to_api_formated_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map[attr]] = value
        if issubclass(SharedResourceInstanceDTO, dict):
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
        if not isinstance(other, SharedResourceInstanceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




