# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class SPARQLLabel(object):
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
        'default_value': 'str',
        'default_lang': 'str',
        'translations': 'dict(str, str)',
        'all_translations': 'dict(str, str)'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'default_lang': 'defaultLang',
        'translations': 'translations',
        'all_translations': 'allTranslations'
    }
    def __init__(self,
        default_value : 'str' = None,
        default_lang : 'str' = None,
        translations : 'Dict[str, str]' = None,
        all_translations : 'Dict[str, str]' = None):  # noqa: E501
        """SPARQLLabel - a model defined in Swagger"""  # noqa: E501

        self._default_value = None
        self._default_lang = None
        self._translations = None
        self._all_translations = None
        self.discriminator = None

        if default_value is not None:
            self.default_value = default_value
        if default_lang is not None:
            self.default_lang = default_lang
        if translations is not None:
            self.translations = translations
        if all_translations is not None:
            self.all_translations = all_translations

    @property
    def default_value(self):
        """Gets the default_value of this SPARQLLabel.  # noqa: E501


        :return: The default_value of this SPARQLLabel.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this SPARQLLabel.


        :param default_value: The default_value of this SPARQLLabel.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def default_lang(self):
        """Gets the default_lang of this SPARQLLabel.  # noqa: E501


        :return: The default_lang of this SPARQLLabel.  # noqa: E501
        :rtype: str
        """
        return self._default_lang

    @default_lang.setter
    def default_lang(self, default_lang):
        """Sets the default_lang of this SPARQLLabel.


        :param default_lang: The default_lang of this SPARQLLabel.  # noqa: E501
        :type: str
        """

        self._default_lang = default_lang

    @property
    def translations(self):
        """Gets the translations of this SPARQLLabel.  # noqa: E501


        :return: The translations of this SPARQLLabel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this SPARQLLabel.


        :param translations: The translations of this SPARQLLabel.  # noqa: E501
        :type: dict(str, str)
        """

        self._translations = translations

    @property
    def all_translations(self):
        """Gets the all_translations of this SPARQLLabel.  # noqa: E501


        :return: The all_translations of this SPARQLLabel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._all_translations

    @all_translations.setter
    def all_translations(self, all_translations):
        """Sets the all_translations of this SPARQLLabel.


        :param all_translations: The all_translations of this SPARQLLabel.  # noqa: E501
        :type: dict(str, str)
        """

        self._all_translations = all_translations

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
        if issubclass(SPARQLLabel, dict):
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
        if not isinstance(other, SPARQLLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

