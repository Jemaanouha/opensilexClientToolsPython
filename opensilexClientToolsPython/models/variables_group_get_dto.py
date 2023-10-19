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


class VariablesGroupGetDTO(object):
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
        'description': 'str',
        'variables': 'list[NamedResourceDTOVariableModel]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'description': 'description',
        'variables': 'variables'
    }
    def __init__(self,
        name : 'str',
        uri : 'str' = None,
        description : 'str' = None,
        variables : 'List[NamedResourceDTOVariableModel]' = None):  # noqa: E501
        """VariablesGroupGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._description = None
        self._variables = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        self.name = name
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables

    @property
    def uri(self):
        """Gets the uri of this VariablesGroupGetDTO.  # noqa: E501


        :return: The uri of this VariablesGroupGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VariablesGroupGetDTO.


        :param uri: The uri of this VariablesGroupGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this VariablesGroupGetDTO.  # noqa: E501


        :return: The name of this VariablesGroupGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariablesGroupGetDTO.


        :param name: The name of this VariablesGroupGetDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VariablesGroupGetDTO.  # noqa: E501


        :return: The description of this VariablesGroupGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariablesGroupGetDTO.


        :param description: The description of this VariablesGroupGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def variables(self):
        """Gets the variables of this VariablesGroupGetDTO.  # noqa: E501


        :return: The variables of this VariablesGroupGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOVariableModel]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this VariablesGroupGetDTO.


        :param variables: The variables of this VariablesGroupGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOVariableModel]
        """

        self._variables = variables

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
        if issubclass(VariablesGroupGetDTO, dict):
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
        if not isinstance(other, VariablesGroupGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.named_resource_dto_variable_model import NamedResourceDTOVariableModel


