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


class ExperimentGetListDTO(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'description': 'str',
        'objective': 'str',
        'species': 'list[str]',
        'is_public': 'bool',
        'facilities': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
        'objective': 'objective',
        'species': 'species',
        'is_public': 'is_public',
        'facilities': 'facilities'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        start_date : 'str' = None,
        end_date : 'str' = None,
        description : 'str' = None,
        objective : 'str' = None,
        species : 'List[str]' = None,
        is_public : 'bool' = None,
        facilities : 'List[str]' = None):  # noqa: E501
        """ExperimentGetListDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._objective = None
        self._species = None
        self._is_public = None
        self._facilities = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        if objective is not None:
            self.objective = objective
        if species is not None:
            self.species = species
        if is_public is not None:
            self.is_public = is_public
        if facilities is not None:
            self.facilities = facilities

    @property
    def uri(self):
        """Gets the uri of this ExperimentGetListDTO.  # noqa: E501


        :return: The uri of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ExperimentGetListDTO.


        :param uri: The uri of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ExperimentGetListDTO.  # noqa: E501


        :return: The name of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentGetListDTO.


        :param name: The name of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this ExperimentGetListDTO.  # noqa: E501


        :return: The start_date of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExperimentGetListDTO.


        :param start_date: The start_date of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ExperimentGetListDTO.  # noqa: E501


        :return: The end_date of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ExperimentGetListDTO.


        :param end_date: The end_date of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this ExperimentGetListDTO.  # noqa: E501


        :return: The description of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExperimentGetListDTO.


        :param description: The description of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def objective(self):
        """Gets the objective of this ExperimentGetListDTO.  # noqa: E501


        :return: The objective of this ExperimentGetListDTO.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this ExperimentGetListDTO.


        :param objective: The objective of this ExperimentGetListDTO.  # noqa: E501
        :type: str
        """

        self._objective = objective

    @property
    def species(self):
        """Gets the species of this ExperimentGetListDTO.  # noqa: E501


        :return: The species of this ExperimentGetListDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this ExperimentGetListDTO.


        :param species: The species of this ExperimentGetListDTO.  # noqa: E501
        :type: list[str]
        """

        self._species = species

    @property
    def is_public(self):
        """Gets the is_public of this ExperimentGetListDTO.  # noqa: E501


        :return: The is_public of this ExperimentGetListDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ExperimentGetListDTO.


        :param is_public: The is_public of this ExperimentGetListDTO.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def facilities(self):
        """Gets the facilities of this ExperimentGetListDTO.  # noqa: E501


        :return: The facilities of this ExperimentGetListDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this ExperimentGetListDTO.


        :param facilities: The facilities of this ExperimentGetListDTO.  # noqa: E501
        :type: list[str]
        """

        self._facilities = facilities

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
        if issubclass(ExperimentGetListDTO, dict):
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
        if issubclass(ExperimentGetListDTO, dict):
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
        if not isinstance(other, ExperimentGetListDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




