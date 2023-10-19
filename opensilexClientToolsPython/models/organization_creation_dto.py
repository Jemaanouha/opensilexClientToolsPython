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


class OrganizationCreationDTO(object):
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
        'rdf_type': 'str',
        'rdf_type_name': 'str',
        'name': 'str',
        'parents': 'list[str]',
        'groups': 'list[str]',
        'facilities': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'parents': 'parents',
        'groups': 'groups',
        'facilities': 'facilities'
    }
    def __init__(self,
        uri : 'str' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        name : 'str' = None,
        parents : 'List[str]' = None,
        groups : 'List[str]' = None,
        facilities : 'List[str]' = None):  # noqa: E501
        """OrganizationCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._parents = None
        self._groups = None
        self._facilities = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        if parents is not None:
            self.parents = parents
        if groups is not None:
            self.groups = groups
        if facilities is not None:
            self.facilities = facilities

    @property
    def uri(self):
        """Gets the uri of this OrganizationCreationDTO.  # noqa: E501


        :return: The uri of this OrganizationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this OrganizationCreationDTO.


        :param uri: The uri of this OrganizationCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this OrganizationCreationDTO.  # noqa: E501


        :return: The rdf_type of this OrganizationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this OrganizationCreationDTO.


        :param rdf_type: The rdf_type of this OrganizationCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this OrganizationCreationDTO.  # noqa: E501


        :return: The rdf_type_name of this OrganizationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this OrganizationCreationDTO.


        :param rdf_type_name: The rdf_type_name of this OrganizationCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this OrganizationCreationDTO.  # noqa: E501


        :return: The name of this OrganizationCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationCreationDTO.


        :param name: The name of this OrganizationCreationDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parents(self):
        """Gets the parents of this OrganizationCreationDTO.  # noqa: E501


        :return: The parents of this OrganizationCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this OrganizationCreationDTO.


        :param parents: The parents of this OrganizationCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._parents = parents

    @property
    def groups(self):
        """Gets the groups of this OrganizationCreationDTO.  # noqa: E501


        :return: The groups of this OrganizationCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OrganizationCreationDTO.


        :param groups: The groups of this OrganizationCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def facilities(self):
        """Gets the facilities of this OrganizationCreationDTO.  # noqa: E501


        :return: The facilities of this OrganizationCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this OrganizationCreationDTO.


        :param facilities: The facilities of this OrganizationCreationDTO.  # noqa: E501
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
        if issubclass(OrganizationCreationDTO, dict):
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
        if not isinstance(other, OrganizationCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




