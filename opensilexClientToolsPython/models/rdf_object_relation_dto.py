# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class RDFObjectRelationDTO(object):
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
        '_property': 'str',
        'value': 'str',
        'inverse': 'bool'
    }

    attribute_map = {
        '_property': 'property',
        'value': 'value',
        'inverse': 'inverse'
    }
    def __init__(self, _property : 'str' = None, value : 'str' = None, inverse : 'bool' = None):  # noqa: E501
        """RDFObjectRelationDTO - a model defined in Swagger"""  # noqa: E501

        self.__property = None
        self._value = None
        self._inverse = None
        self.discriminator = None

        if _property is not None:
            self._property = _property
        if value is not None:
            self.value = value
        if inverse is not None:
            self.inverse = inverse

    @property
    def _property(self):
        """Gets the _property of this RDFObjectRelationDTO.  # noqa: E501


        :return: The _property of this RDFObjectRelationDTO.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this RDFObjectRelationDTO.


        :param _property: The _property of this RDFObjectRelationDTO.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def value(self):
        """Gets the value of this RDFObjectRelationDTO.  # noqa: E501


        :return: The value of this RDFObjectRelationDTO.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RDFObjectRelationDTO.


        :param value: The value of this RDFObjectRelationDTO.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def inverse(self):
        """Gets the inverse of this RDFObjectRelationDTO.  # noqa: E501


        :return: The inverse of this RDFObjectRelationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._inverse

    @inverse.setter
    def inverse(self, inverse):
        """Sets the inverse of this RDFObjectRelationDTO.


        :param inverse: The inverse of this RDFObjectRelationDTO.  # noqa: E501
        :type: bool
        """

        self._inverse = inverse

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
        if issubclass(RDFObjectRelationDTO, dict):
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
        if not isinstance(other, RDFObjectRelationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

