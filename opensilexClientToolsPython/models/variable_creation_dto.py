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


class VariableCreationDTO(object):
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
        'alternative_name': 'str',
        'description': 'str',
        'entity': 'str',
        'entity_of_interest': 'str',
        'characteristic': 'str',
        'trait': 'str',
        'trait_name': 'str',
        'method': 'str',
        'unit': 'str',
        'species': 'list[str]',
        'datatype': 'str',
        'time_interval': 'str',
        'sampling_interval': 'str',
        'exact_match': 'list[str]',
        'close_match': 'list[str]',
        'broad_match': 'list[str]',
        'narrow_match': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'alternative_name': 'alternative_name',
        'description': 'description',
        'entity': 'entity',
        'entity_of_interest': 'entity_of_interest',
        'characteristic': 'characteristic',
        'trait': 'trait',
        'trait_name': 'trait_name',
        'method': 'method',
        'unit': 'unit',
        'species': 'species',
        'datatype': 'datatype',
        'time_interval': 'time_interval',
        'sampling_interval': 'sampling_interval',
        'exact_match': 'exact_match',
        'close_match': 'close_match',
        'broad_match': 'broad_match',
        'narrow_match': 'narrow_match'
    }
    def __init__(self,
        name : 'str',
        entity : 'str',
        characteristic : 'str',
        method : 'str',
        unit : 'str',
        datatype : 'str',
        uri : 'str' = None,
        alternative_name : 'str' = None,
        description : 'str' = None,
        entity_of_interest : 'str' = None,
        trait : 'str' = None,
        trait_name : 'str' = None,
        species : 'List[str]' = None,
        time_interval : 'str' = None,
        sampling_interval : 'str' = None,
        exact_match : 'List[str]' = None,
        close_match : 'List[str]' = None,
        broad_match : 'List[str]' = None,
        narrow_match : 'List[str]' = None):  # noqa: E501
        """VariableCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._alternative_name = None
        self._description = None
        self._entity = None
        self._entity_of_interest = None
        self._characteristic = None
        self._trait = None
        self._trait_name = None
        self._method = None
        self._unit = None
        self._species = None
        self._datatype = None
        self._time_interval = None
        self._sampling_interval = None
        self._exact_match = None
        self._close_match = None
        self._broad_match = None
        self._narrow_match = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        self.name = name
        if alternative_name is not None:
            self.alternative_name = alternative_name
        if description is not None:
            self.description = description
        self.entity = entity
        if entity_of_interest is not None:
            self.entity_of_interest = entity_of_interest
        self.characteristic = characteristic
        if trait is not None:
            self.trait = trait
        if trait_name is not None:
            self.trait_name = trait_name
        self.method = method
        self.unit = unit
        if species is not None:
            self.species = species
        self.datatype = datatype
        if time_interval is not None:
            self.time_interval = time_interval
        if sampling_interval is not None:
            self.sampling_interval = sampling_interval
        if exact_match is not None:
            self.exact_match = exact_match
        if close_match is not None:
            self.close_match = close_match
        if broad_match is not None:
            self.broad_match = broad_match
        if narrow_match is not None:
            self.narrow_match = narrow_match

    @property
    def uri(self):
        """Gets the uri of this VariableCreationDTO.  # noqa: E501


        :return: The uri of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VariableCreationDTO.


        :param uri: The uri of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VariableCreationDTO.  # noqa: E501


        :return: The name of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableCreationDTO.


        :param name: The name of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def alternative_name(self):
        """Gets the alternative_name of this VariableCreationDTO.  # noqa: E501


        :return: The alternative_name of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._alternative_name

    @alternative_name.setter
    def alternative_name(self, alternative_name):
        """Sets the alternative_name of this VariableCreationDTO.


        :param alternative_name: The alternative_name of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._alternative_name = alternative_name

    @property
    def description(self):
        """Gets the description of this VariableCreationDTO.  # noqa: E501


        :return: The description of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableCreationDTO.


        :param description: The description of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity(self):
        """Gets the entity of this VariableCreationDTO.  # noqa: E501


        :return: The entity of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this VariableCreationDTO.


        :param entity: The entity of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def entity_of_interest(self):
        """Gets the entity_of_interest of this VariableCreationDTO.  # noqa: E501


        :return: The entity_of_interest of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._entity_of_interest

    @entity_of_interest.setter
    def entity_of_interest(self, entity_of_interest):
        """Sets the entity_of_interest of this VariableCreationDTO.


        :param entity_of_interest: The entity_of_interest of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._entity_of_interest = entity_of_interest

    @property
    def characteristic(self):
        """Gets the characteristic of this VariableCreationDTO.  # noqa: E501


        :return: The characteristic of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._characteristic

    @characteristic.setter
    def characteristic(self, characteristic):
        """Sets the characteristic of this VariableCreationDTO.


        :param characteristic: The characteristic of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if characteristic is None:
            raise ValueError("Invalid value for `characteristic`, must not be `None`")  # noqa: E501

        self._characteristic = characteristic

    @property
    def trait(self):
        """Gets the trait of this VariableCreationDTO.  # noqa: E501


        :return: The trait of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """Sets the trait of this VariableCreationDTO.


        :param trait: The trait of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._trait = trait

    @property
    def trait_name(self):
        """Gets the trait_name of this VariableCreationDTO.  # noqa: E501


        :return: The trait_name of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._trait_name

    @trait_name.setter
    def trait_name(self, trait_name):
        """Sets the trait_name of this VariableCreationDTO.


        :param trait_name: The trait_name of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._trait_name = trait_name

    @property
    def method(self):
        """Gets the method of this VariableCreationDTO.  # noqa: E501


        :return: The method of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this VariableCreationDTO.


        :param method: The method of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def unit(self):
        """Gets the unit of this VariableCreationDTO.  # noqa: E501


        :return: The unit of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this VariableCreationDTO.


        :param unit: The unit of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def species(self):
        """Gets the species of this VariableCreationDTO.  # noqa: E501


        :return: The species of this VariableCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this VariableCreationDTO.


        :param species: The species of this VariableCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._species = species

    @property
    def datatype(self):
        """Gets the datatype of this VariableCreationDTO.  # noqa: E501


        :return: The datatype of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this VariableCreationDTO.


        :param datatype: The datatype of this VariableCreationDTO.  # noqa: E501
        :type: str
        """
        if datatype is None:
            raise ValueError("Invalid value for `datatype`, must not be `None`")  # noqa: E501

        self._datatype = datatype

    @property
    def time_interval(self):
        """Gets the time_interval of this VariableCreationDTO.  # noqa: E501


        :return: The time_interval of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this VariableCreationDTO.


        :param time_interval: The time_interval of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._time_interval = time_interval

    @property
    def sampling_interval(self):
        """Gets the sampling_interval of this VariableCreationDTO.  # noqa: E501


        :return: The sampling_interval of this VariableCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, sampling_interval):
        """Sets the sampling_interval of this VariableCreationDTO.


        :param sampling_interval: The sampling_interval of this VariableCreationDTO.  # noqa: E501
        :type: str
        """

        self._sampling_interval = sampling_interval

    @property
    def exact_match(self):
        """Gets the exact_match of this VariableCreationDTO.  # noqa: E501


        :return: The exact_match of this VariableCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this VariableCreationDTO.


        :param exact_match: The exact_match of this VariableCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._exact_match = exact_match

    @property
    def close_match(self):
        """Gets the close_match of this VariableCreationDTO.  # noqa: E501


        :return: The close_match of this VariableCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._close_match

    @close_match.setter
    def close_match(self, close_match):
        """Sets the close_match of this VariableCreationDTO.


        :param close_match: The close_match of this VariableCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._close_match = close_match

    @property
    def broad_match(self):
        """Gets the broad_match of this VariableCreationDTO.  # noqa: E501


        :return: The broad_match of this VariableCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._broad_match

    @broad_match.setter
    def broad_match(self, broad_match):
        """Sets the broad_match of this VariableCreationDTO.


        :param broad_match: The broad_match of this VariableCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._broad_match = broad_match

    @property
    def narrow_match(self):
        """Gets the narrow_match of this VariableCreationDTO.  # noqa: E501


        :return: The narrow_match of this VariableCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._narrow_match

    @narrow_match.setter
    def narrow_match(self, narrow_match):
        """Sets the narrow_match of this VariableCreationDTO.


        :param narrow_match: The narrow_match of this VariableCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._narrow_match = narrow_match

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
        if issubclass(VariableCreationDTO, dict):
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
        if issubclass(VariableCreationDTO, dict):
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
        if not isinstance(other, VariableCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




