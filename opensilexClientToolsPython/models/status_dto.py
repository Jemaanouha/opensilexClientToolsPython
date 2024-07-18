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


class StatusDTO(object):
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
        'message': 'str',
        'translation_key': 'str',
        'translation_values': 'dict(str, str)',
        'level': 'str'
    }

    attribute_map = {
        'message': 'message',
        'translation_key': 'translationKey',
        'translation_values': 'translationValues',
        'level': 'level'
    }
    def __init__(self,
        message : 'str' = None,
        translation_key : 'str' = None,
        translation_values : 'Dict[str, str]' = None,
        level : 'str' = None):  # noqa: E501
        """StatusDTO - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._translation_key = None
        self._translation_values = None
        self._level = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if translation_key is not None:
            self.translation_key = translation_key
        if translation_values is not None:
            self.translation_values = translation_values
        if level is not None:
            self.level = level

    @property
    def message(self):
        """Gets the message of this StatusDTO.  # noqa: E501


        :return: The message of this StatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StatusDTO.


        :param message: The message of this StatusDTO.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def translation_key(self):
        """Gets the translation_key of this StatusDTO.  # noqa: E501


        :return: The translation_key of this StatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """Sets the translation_key of this StatusDTO.


        :param translation_key: The translation_key of this StatusDTO.  # noqa: E501
        :type: str
        """

        self._translation_key = translation_key

    @property
    def translation_values(self):
        """Gets the translation_values of this StatusDTO.  # noqa: E501


        :return: The translation_values of this StatusDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._translation_values

    @translation_values.setter
    def translation_values(self, translation_values):
        """Sets the translation_values of this StatusDTO.


        :param translation_values: The translation_values of this StatusDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._translation_values = translation_values

    @property
    def level(self):
        """Gets the level of this StatusDTO.  # noqa: E501


        :return: The level of this StatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this StatusDTO.


        :param level: The level of this StatusDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "WARNING", "INFO", "DEBUG"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

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
        if issubclass(StatusDTO, dict):
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
        if issubclass(StatusDTO, dict):
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
        if not isinstance(other, StatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




