# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class VariableCopyResponseDTO(object):
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
        'variable_uris': 'list[str]',
        'entity_uris': 'list[str]',
        'characteristic_uris': 'list[str]',
        'method_uris': 'list[str]',
        'unit_uris': 'list[str]',
        'interest_entity_uris': 'list[str]'
    }

    attribute_map = {
        'variable_uris': 'variableUris',
        'entity_uris': 'entityUris',
        'characteristic_uris': 'characteristicUris',
        'method_uris': 'methodUris',
        'unit_uris': 'unitUris',
        'interest_entity_uris': 'interestEntityUris'
    }
    def __init__(self,
        variable_uris : 'List[str]' = None,
        entity_uris : 'List[str]' = None,
        characteristic_uris : 'List[str]' = None,
        method_uris : 'List[str]' = None,
        unit_uris : 'List[str]' = None,
        interest_entity_uris : 'List[str]' = None):  # noqa: E501
        """VariableCopyResponseDTO - a model defined in Swagger"""  # noqa: E501

        self._variable_uris = None
        self._entity_uris = None
        self._characteristic_uris = None
        self._method_uris = None
        self._unit_uris = None
        self._interest_entity_uris = None
        self.discriminator = None

        if variable_uris is not None:
            self.variable_uris = variable_uris
        if entity_uris is not None:
            self.entity_uris = entity_uris
        if characteristic_uris is not None:
            self.characteristic_uris = characteristic_uris
        if method_uris is not None:
            self.method_uris = method_uris
        if unit_uris is not None:
            self.unit_uris = unit_uris
        if interest_entity_uris is not None:
            self.interest_entity_uris = interest_entity_uris

    @property
    def variable_uris(self):
        """Gets the variable_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The variable_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._variable_uris

    @variable_uris.setter
    def variable_uris(self, variable_uris):
        """Sets the variable_uris of this VariableCopyResponseDTO.


        :param variable_uris: The variable_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._variable_uris = variable_uris

    @property
    def entity_uris(self):
        """Gets the entity_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The entity_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_uris

    @entity_uris.setter
    def entity_uris(self, entity_uris):
        """Sets the entity_uris of this VariableCopyResponseDTO.


        :param entity_uris: The entity_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._entity_uris = entity_uris

    @property
    def characteristic_uris(self):
        """Gets the characteristic_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The characteristic_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._characteristic_uris

    @characteristic_uris.setter
    def characteristic_uris(self, characteristic_uris):
        """Sets the characteristic_uris of this VariableCopyResponseDTO.


        :param characteristic_uris: The characteristic_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._characteristic_uris = characteristic_uris

    @property
    def method_uris(self):
        """Gets the method_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The method_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._method_uris

    @method_uris.setter
    def method_uris(self, method_uris):
        """Sets the method_uris of this VariableCopyResponseDTO.


        :param method_uris: The method_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._method_uris = method_uris

    @property
    def unit_uris(self):
        """Gets the unit_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The unit_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._unit_uris

    @unit_uris.setter
    def unit_uris(self, unit_uris):
        """Sets the unit_uris of this VariableCopyResponseDTO.


        :param unit_uris: The unit_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._unit_uris = unit_uris

    @property
    def interest_entity_uris(self):
        """Gets the interest_entity_uris of this VariableCopyResponseDTO.  # noqa: E501


        :return: The interest_entity_uris of this VariableCopyResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._interest_entity_uris

    @interest_entity_uris.setter
    def interest_entity_uris(self, interest_entity_uris):
        """Sets the interest_entity_uris of this VariableCopyResponseDTO.


        :param interest_entity_uris: The interest_entity_uris of this VariableCopyResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._interest_entity_uris = interest_entity_uris

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
        if issubclass(VariableCopyResponseDTO, dict):
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
        if not isinstance(other, VariableCopyResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




