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




class Level(object):
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
        'level_int': 'int',
        'level_str': 'str'
    }

    attribute_map = {
        'level_int': 'levelInt',
        'level_str': 'levelStr'
    }
    def __init__(self, level_int : 'int' = None, level_str : 'str' = None):  # noqa: E501
        """Level - a model defined in Swagger"""  # noqa: E501

        self._level_int = None
        self._level_str = None
        self.discriminator = None

        if level_int is not None:
            self.level_int = level_int
        if level_str is not None:
            self.level_str = level_str

    @property
    def level_int(self):
        """Gets the level_int of this Level.  # noqa: E501


        :return: The level_int of this Level.  # noqa: E501
        :rtype: int
        """
        return self._level_int

    @level_int.setter
    def level_int(self, level_int):
        """Sets the level_int of this Level.


        :param level_int: The level_int of this Level.  # noqa: E501
        :type: int
        """

        self._level_int = level_int

    @property
    def level_str(self):
        """Gets the level_str of this Level.  # noqa: E501


        :return: The level_str of this Level.  # noqa: E501
        :rtype: str
        """
        return self._level_str

    @level_str.setter
    def level_str(self, level_str):
        """Sets the level_str of this Level.


        :param level_str: The level_str of this Level.  # noqa: E501
        :type: str
        """

        self._level_str = level_str

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
        if issubclass(Level, dict):
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
        if not isinstance(other, Level):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

