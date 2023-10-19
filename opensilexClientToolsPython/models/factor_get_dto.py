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


class FactorGetDTO(object):
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
        'category': 'str',
        'description': 'str',
        'experiment': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'experiment': 'experiment'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        category : 'str' = None,
        description : 'str' = None,
        experiment : 'str' = None):  # noqa: E501
        """FactorGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._category = None
        self._description = None
        self._experiment = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if experiment is not None:
            self.experiment = experiment

    @property
    def uri(self):
        """Gets the uri of this FactorGetDTO.  # noqa: E501


        :return: The uri of this FactorGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FactorGetDTO.


        :param uri: The uri of this FactorGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this FactorGetDTO.  # noqa: E501


        :return: The name of this FactorGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FactorGetDTO.


        :param name: The name of this FactorGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this FactorGetDTO.  # noqa: E501


        :return: The category of this FactorGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FactorGetDTO.


        :param category: The category of this FactorGetDTO.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this FactorGetDTO.  # noqa: E501


        :return: The description of this FactorGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FactorGetDTO.


        :param description: The description of this FactorGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def experiment(self):
        """Gets the experiment of this FactorGetDTO.  # noqa: E501


        :return: The experiment of this FactorGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this FactorGetDTO.


        :param experiment: The experiment of this FactorGetDTO.  # noqa: E501
        :type: str
        """

        self._experiment = experiment

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
        if issubclass(FactorGetDTO, dict):
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
        if not isinstance(other, FactorGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




