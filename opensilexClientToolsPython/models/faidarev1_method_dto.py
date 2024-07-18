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


class Faidarev1MethodDTO(object):
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
        'description': 'str',
        'formula': 'str',
        'method_db_id': 'str',
        'name': 'str',
        'reference': 'str',
        '_class': 'str'
    }

    attribute_map = {
        'description': 'description',
        'formula': 'formula',
        'method_db_id': 'methodDbId',
        'name': 'name',
        'reference': 'reference',
        '_class': 'class'
    }
    def __init__(self,
        description : 'str' = None,
        formula : 'str' = None,
        method_db_id : 'str' = None,
        name : 'str' = None,
        reference : 'str' = None,
        _class : 'str' = None):  # noqa: E501
        """Faidarev1MethodDTO - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._formula = None
        self._method_db_id = None
        self._name = None
        self._reference = None
        self.__class = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if formula is not None:
            self.formula = formula
        if method_db_id is not None:
            self.method_db_id = method_db_id
        if name is not None:
            self.name = name
        if reference is not None:
            self.reference = reference
        if _class is not None:
            self._class = _class

    @property
    def description(self):
        """Gets the description of this Faidarev1MethodDTO.  # noqa: E501


        :return: The description of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Faidarev1MethodDTO.


        :param description: The description of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """Gets the formula of this Faidarev1MethodDTO.  # noqa: E501


        :return: The formula of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this Faidarev1MethodDTO.


        :param formula: The formula of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self._formula = formula

    @property
    def method_db_id(self):
        """Gets the method_db_id of this Faidarev1MethodDTO.  # noqa: E501


        :return: The method_db_id of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self._method_db_id

    @method_db_id.setter
    def method_db_id(self, method_db_id):
        """Sets the method_db_id of this Faidarev1MethodDTO.


        :param method_db_id: The method_db_id of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self._method_db_id = method_db_id

    @property
    def name(self):
        """Gets the name of this Faidarev1MethodDTO.  # noqa: E501


        :return: The name of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Faidarev1MethodDTO.


        :param name: The name of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reference(self):
        """Gets the reference of this Faidarev1MethodDTO.  # noqa: E501


        :return: The reference of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Faidarev1MethodDTO.


        :param reference: The reference of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def _class(self):
        """Gets the _class of this Faidarev1MethodDTO.  # noqa: E501


        :return: The _class of this Faidarev1MethodDTO.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Faidarev1MethodDTO.


        :param _class: The _class of this Faidarev1MethodDTO.  # noqa: E501
        :type: str
        """

        self.__class = _class

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
        if issubclass(Faidarev1MethodDTO, dict):
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
        if issubclass(Faidarev1MethodDTO, dict):
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
        if not isinstance(other, Faidarev1MethodDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




