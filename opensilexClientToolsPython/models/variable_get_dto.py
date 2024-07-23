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


class VariableGetDTO(object):
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
        'entity': 'EntityGetDTO',
        'entity_of_interest': 'NamedResourceDTO',
        'characteristic': 'CharacteristicGetDTO',
        'method': 'MethodGetDTO',
        'unit': 'UnitGetDTO',
        'on_local': 'bool',
        'shared_resource_instance': 'SharedResourceInstanceDTO',
        'alternative_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'entity': 'entity',
        'entity_of_interest': 'entity_of_interest',
        'characteristic': 'characteristic',
        'method': 'method',
        'unit': 'unit',
        'on_local': 'onLocal',
        'shared_resource_instance': 'sharedResourceInstance',
        'alternative_name': 'alternative_name'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        entity : 'EntityGetDTO' = None,
        entity_of_interest : 'NamedResourceDTO' = None,
        characteristic : 'CharacteristicGetDTO' = None,
        method : 'MethodGetDTO' = None,
        unit : 'UnitGetDTO' = None,
        on_local : 'bool' = None,
        shared_resource_instance : 'SharedResourceInstanceDTO' = None,
        alternative_name : 'str' = None):  # noqa: E501
        """VariableGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._entity = None
        self._entity_of_interest = None
        self._characteristic = None
        self._method = None
        self._unit = None
        self._on_local = None
        self._shared_resource_instance = None
        self._alternative_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if entity is not None:
            self.entity = entity
        if entity_of_interest is not None:
            self.entity_of_interest = entity_of_interest
        if characteristic is not None:
            self.characteristic = characteristic
        if method is not None:
            self.method = method
        if unit is not None:
            self.unit = unit
        if on_local is not None:
            self.on_local = on_local
        if shared_resource_instance is not None:
            self.shared_resource_instance = shared_resource_instance
        if alternative_name is not None:
            self.alternative_name = alternative_name

    @property
    def uri(self):
        """Gets the uri of this VariableGetDTO.  # noqa: E501


        :return: The uri of this VariableGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VariableGetDTO.


        :param uri: The uri of this VariableGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VariableGetDTO.  # noqa: E501


        :return: The name of this VariableGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableGetDTO.


        :param name: The name of this VariableGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def entity(self):
        """Gets the entity of this VariableGetDTO.  # noqa: E501


        :return: The entity of this VariableGetDTO.  # noqa: E501
        :rtype: EntityGetDTO
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this VariableGetDTO.


        :param entity: The entity of this VariableGetDTO.  # noqa: E501
        :type: EntityGetDTO
        """

        self._entity = entity

    @property
    def entity_of_interest(self):
        """Gets the entity_of_interest of this VariableGetDTO.  # noqa: E501


        :return: The entity_of_interest of this VariableGetDTO.  # noqa: E501
        :rtype: NamedResourceDTO
        """
        return self._entity_of_interest

    @entity_of_interest.setter
    def entity_of_interest(self, entity_of_interest):
        """Sets the entity_of_interest of this VariableGetDTO.


        :param entity_of_interest: The entity_of_interest of this VariableGetDTO.  # noqa: E501
        :type: NamedResourceDTO
        """

        self._entity_of_interest = entity_of_interest

    @property
    def characteristic(self):
        """Gets the characteristic of this VariableGetDTO.  # noqa: E501


        :return: The characteristic of this VariableGetDTO.  # noqa: E501
        :rtype: CharacteristicGetDTO
        """
        return self._characteristic

    @characteristic.setter
    def characteristic(self, characteristic):
        """Sets the characteristic of this VariableGetDTO.


        :param characteristic: The characteristic of this VariableGetDTO.  # noqa: E501
        :type: CharacteristicGetDTO
        """

        self._characteristic = characteristic

    @property
    def method(self):
        """Gets the method of this VariableGetDTO.  # noqa: E501


        :return: The method of this VariableGetDTO.  # noqa: E501
        :rtype: MethodGetDTO
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this VariableGetDTO.


        :param method: The method of this VariableGetDTO.  # noqa: E501
        :type: MethodGetDTO
        """

        self._method = method

    @property
    def unit(self):
        """Gets the unit of this VariableGetDTO.  # noqa: E501


        :return: The unit of this VariableGetDTO.  # noqa: E501
        :rtype: UnitGetDTO
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this VariableGetDTO.


        :param unit: The unit of this VariableGetDTO.  # noqa: E501
        :type: UnitGetDTO
        """

        self._unit = unit

    @property
    def on_local(self):
        """Gets the on_local of this VariableGetDTO.  # noqa: E501


        :return: The on_local of this VariableGetDTO.  # noqa: E501
        :rtype: bool
        """
        return self._on_local

    @on_local.setter
    def on_local(self, on_local):
        """Sets the on_local of this VariableGetDTO.


        :param on_local: The on_local of this VariableGetDTO.  # noqa: E501
        :type: bool
        """

        self._on_local = on_local

    @property
    def shared_resource_instance(self):
        """Gets the shared_resource_instance of this VariableGetDTO.  # noqa: E501


        :return: The shared_resource_instance of this VariableGetDTO.  # noqa: E501
        :rtype: SharedResourceInstanceDTO
        """
        return self._shared_resource_instance

    @shared_resource_instance.setter
    def shared_resource_instance(self, shared_resource_instance):
        """Sets the shared_resource_instance of this VariableGetDTO.


        :param shared_resource_instance: The shared_resource_instance of this VariableGetDTO.  # noqa: E501
        :type: SharedResourceInstanceDTO
        """

        self._shared_resource_instance = shared_resource_instance

    @property
    def alternative_name(self):
        """Gets the alternative_name of this VariableGetDTO.  # noqa: E501


        :return: The alternative_name of this VariableGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._alternative_name

    @alternative_name.setter
    def alternative_name(self, alternative_name):
        """Sets the alternative_name of this VariableGetDTO.


        :param alternative_name: The alternative_name of this VariableGetDTO.  # noqa: E501
        :type: str
        """

        self._alternative_name = alternative_name

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
        if issubclass(VariableGetDTO, dict):
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
        if issubclass(VariableGetDTO, dict):
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
        if not isinstance(other, VariableGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.entity_get_dto import EntityGetDTO
from opensilexClientToolsPython.models.named_resource_dto import NamedResourceDTO
from opensilexClientToolsPython.models.characteristic_get_dto import CharacteristicGetDTO
from opensilexClientToolsPython.models.method_get_dto import MethodGetDTO
from opensilexClientToolsPython.models.unit_get_dto import UnitGetDTO
from opensilexClientToolsPython.models.shared_resource_instance_dto import SharedResourceInstanceDTO


