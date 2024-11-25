# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class GraphConfigDTO(object):
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
        'variable': 'str',
        'data_location_informations': 'str'
    }

    attribute_map = {
        'variable': 'variable',
        'data_location_informations': 'dataLocationInformations'
    }
    def __init__(self,
        variable : 'str' = None,
        data_location_informations : 'str' = None):  # noqa: E501
        """GraphConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._variable = None
        self._data_location_informations = None
        self.discriminator = None

        if variable is not None:
            self.variable = variable
        if data_location_informations is not None:
            self.data_location_informations = data_location_informations

    @property
    def variable(self):
        """Gets the variable of this GraphConfigDTO.  # noqa: E501


        :return: The variable of this GraphConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this GraphConfigDTO.


        :param variable: The variable of this GraphConfigDTO.  # noqa: E501
        :type: str
        """

        self._variable = variable

    @property
    def data_location_informations(self):
        """Gets the data_location_informations of this GraphConfigDTO.  # noqa: E501


        :return: The data_location_informations of this GraphConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._data_location_informations

    @data_location_informations.setter
    def data_location_informations(self, data_location_informations):
        """Sets the data_location_informations of this GraphConfigDTO.


        :param data_location_informations: The data_location_informations of this GraphConfigDTO.  # noqa: E501
        :type: str
        """

        self._data_location_informations = data_location_informations

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
        if issubclass(GraphConfigDTO, dict):
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
        if issubclass(GraphConfigDTO, dict):
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
        if not isinstance(other, GraphConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




