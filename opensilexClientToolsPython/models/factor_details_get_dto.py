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


class FactorDetailsGetDTO(object):
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
        'levels': 'list[FactorLevelGetDTO]',
        'exact_match': 'list[str]',
        'close_match': 'list[str]',
        'broad_match': 'list[str]',
        'narrow_match': 'list[str]',
        'experiment': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'category': 'category',
        'description': 'description',
        'levels': 'levels',
        'exact_match': 'exact_match',
        'close_match': 'close_match',
        'broad_match': 'broad_match',
        'narrow_match': 'narrow_match',
        'experiment': 'experiment'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        category : 'str' = None,
        description : 'str' = None,
        levels : 'List[FactorLevelGetDTO]' = None,
        exact_match : 'List[str]' = None,
        close_match : 'List[str]' = None,
        broad_match : 'List[str]' = None,
        narrow_match : 'List[str]' = None,
        experiment : 'str' = None):  # noqa: E501
        """FactorDetailsGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._category = None
        self._description = None
        self._levels = None
        self._exact_match = None
        self._close_match = None
        self._broad_match = None
        self._narrow_match = None
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
        if levels is not None:
            self.levels = levels
        if exact_match is not None:
            self.exact_match = exact_match
        if close_match is not None:
            self.close_match = close_match
        if broad_match is not None:
            self.broad_match = broad_match
        if narrow_match is not None:
            self.narrow_match = narrow_match
        if experiment is not None:
            self.experiment = experiment

    @property
    def uri(self):
        """Gets the uri of this FactorDetailsGetDTO.  # noqa: E501


        :return: The uri of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FactorDetailsGetDTO.


        :param uri: The uri of this FactorDetailsGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this FactorDetailsGetDTO.  # noqa: E501


        :return: The name of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FactorDetailsGetDTO.


        :param name: The name of this FactorDetailsGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def category(self):
        """Gets the category of this FactorDetailsGetDTO.  # noqa: E501


        :return: The category of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FactorDetailsGetDTO.


        :param category: The category of this FactorDetailsGetDTO.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this FactorDetailsGetDTO.  # noqa: E501


        :return: The description of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FactorDetailsGetDTO.


        :param description: The description of this FactorDetailsGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def levels(self):
        """Gets the levels of this FactorDetailsGetDTO.  # noqa: E501


        :return: The levels of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: list[FactorLevelGetDTO]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this FactorDetailsGetDTO.


        :param levels: The levels of this FactorDetailsGetDTO.  # noqa: E501
        :type: list[FactorLevelGetDTO]
        """

        self._levels = levels

    @property
    def exact_match(self):
        """Gets the exact_match of this FactorDetailsGetDTO.  # noqa: E501


        :return: The exact_match of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this FactorDetailsGetDTO.


        :param exact_match: The exact_match of this FactorDetailsGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._exact_match = exact_match

    @property
    def close_match(self):
        """Gets the close_match of this FactorDetailsGetDTO.  # noqa: E501


        :return: The close_match of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._close_match

    @close_match.setter
    def close_match(self, close_match):
        """Sets the close_match of this FactorDetailsGetDTO.


        :param close_match: The close_match of this FactorDetailsGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._close_match = close_match

    @property
    def broad_match(self):
        """Gets the broad_match of this FactorDetailsGetDTO.  # noqa: E501


        :return: The broad_match of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._broad_match

    @broad_match.setter
    def broad_match(self, broad_match):
        """Sets the broad_match of this FactorDetailsGetDTO.


        :param broad_match: The broad_match of this FactorDetailsGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._broad_match = broad_match

    @property
    def narrow_match(self):
        """Gets the narrow_match of this FactorDetailsGetDTO.  # noqa: E501


        :return: The narrow_match of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._narrow_match

    @narrow_match.setter
    def narrow_match(self, narrow_match):
        """Sets the narrow_match of this FactorDetailsGetDTO.


        :param narrow_match: The narrow_match of this FactorDetailsGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._narrow_match = narrow_match

    @property
    def experiment(self):
        """Gets the experiment of this FactorDetailsGetDTO.  # noqa: E501


        :return: The experiment of this FactorDetailsGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this FactorDetailsGetDTO.


        :param experiment: The experiment of this FactorDetailsGetDTO.  # noqa: E501
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
        if issubclass(FactorDetailsGetDTO, dict):
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
        if not isinstance(other, FactorDetailsGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.factor_level_get_dto import FactorLevelGetDTO


