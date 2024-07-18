# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class Faidarev1CallDTO(object):
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
        'call': 'str',
        'data_types': 'list[str]',
        'methods': 'list[str]',
        'versions': 'list[str]'
    }

    attribute_map = {
        'call': 'call',
        'data_types': 'dataTypes',
        'methods': 'methods',
        'versions': 'versions'
    }
    def __init__(self,
        call : 'str' = None,
        data_types : 'List[str]' = None,
        methods : 'List[str]' = None,
        versions : 'List[str]' = None):  # noqa: E501
        """Faidarev1CallDTO - a model defined in Swagger"""  # noqa: E501

        self._call = None
        self._data_types = None
        self._methods = None
        self._versions = None
        self.discriminator = None

        if call is not None:
            self.call = call
        if data_types is not None:
            self.data_types = data_types
        if methods is not None:
            self.methods = methods
        if versions is not None:
            self.versions = versions

    @property
    def call(self):
        """Gets the call of this Faidarev1CallDTO.  # noqa: E501


        :return: The call of this Faidarev1CallDTO.  # noqa: E501
        :rtype: str
        """
        return self._call

    @call.setter
    def call(self, call):
        """Sets the call of this Faidarev1CallDTO.


        :param call: The call of this Faidarev1CallDTO.  # noqa: E501
        :type: str
        """

        self._call = call

    @property
    def data_types(self):
        """Gets the data_types of this Faidarev1CallDTO.  # noqa: E501


        :return: The data_types of this Faidarev1CallDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_types

    @data_types.setter
    def data_types(self, data_types):
        """Sets the data_types of this Faidarev1CallDTO.


        :param data_types: The data_types of this Faidarev1CallDTO.  # noqa: E501
        :type: list[str]
        """

        self._data_types = data_types

    @property
    def methods(self):
        """Gets the methods of this Faidarev1CallDTO.  # noqa: E501


        :return: The methods of this Faidarev1CallDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this Faidarev1CallDTO.


        :param methods: The methods of this Faidarev1CallDTO.  # noqa: E501
        :type: list[str]
        """

        self._methods = methods

    @property
    def versions(self):
        """Gets the versions of this Faidarev1CallDTO.  # noqa: E501


        :return: The versions of this Faidarev1CallDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Faidarev1CallDTO.


        :param versions: The versions of this Faidarev1CallDTO.  # noqa: E501
        :type: list[str]
        """

        self._versions = versions

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
        if issubclass(Faidarev1CallDTO, dict):
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
        if issubclass(Faidarev1CallDTO, dict):
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
        if not isinstance(other, Faidarev1CallDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




