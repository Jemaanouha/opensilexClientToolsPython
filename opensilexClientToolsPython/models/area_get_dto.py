# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject
from opensilexClientToolsPython.models.event_get_dto import EventGetDTO



class AreaGetDTO(object):
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
        'is_structural_area': 'bool',
        'name': 'str',
        'description': 'str',
        'author': 'str',
        'geometry': 'GeoJsonObject',
        'event': 'EventGetDTO'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'is_structural_area': 'is_structural_area',
        'name': 'name',
        'description': 'description',
        'author': 'author',
        'geometry': 'geometry',
        'event': 'event'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, is_structural_area : 'bool' = None, name : 'str' = None, description : 'str' = None, author : 'str' = None, geometry : 'GeoJsonObject' = None, event : 'EventGetDTO' = None):  # noqa: E501
        """AreaGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._is_structural_area = None
        self._name = None
        self._description = None
        self._author = None
        self._geometry = None
        self._event = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if is_structural_area is not None:
            self.is_structural_area = is_structural_area
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if author is not None:
            self.author = author
        if geometry is not None:
            self.geometry = geometry
        if event is not None:
            self.event = event

    @property
    def uri(self):
        """Gets the uri of this AreaGetDTO.  # noqa: E501


        :return: The uri of this AreaGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AreaGetDTO.


        :param uri: The uri of this AreaGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this AreaGetDTO.  # noqa: E501


        :return: The rdf_type of this AreaGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this AreaGetDTO.


        :param rdf_type: The rdf_type of this AreaGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def is_structural_area(self):
        """Gets the is_structural_area of this AreaGetDTO.  # noqa: E501


        :return: The is_structural_area of this AreaGetDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_structural_area

    @is_structural_area.setter
    def is_structural_area(self, is_structural_area):
        """Sets the is_structural_area of this AreaGetDTO.


        :param is_structural_area: The is_structural_area of this AreaGetDTO.  # noqa: E501
        :type: bool
        """

        self._is_structural_area = is_structural_area

    @property
    def name(self):
        """Gets the name of this AreaGetDTO.  # noqa: E501


        :return: The name of this AreaGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AreaGetDTO.


        :param name: The name of this AreaGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AreaGetDTO.  # noqa: E501


        :return: The description of this AreaGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AreaGetDTO.


        :param description: The description of this AreaGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def author(self):
        """Gets the author of this AreaGetDTO.  # noqa: E501


        :return: The author of this AreaGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this AreaGetDTO.


        :param author: The author of this AreaGetDTO.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def geometry(self):
        """Gets the geometry of this AreaGetDTO.  # noqa: E501


        :return: The geometry of this AreaGetDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this AreaGetDTO.


        :param geometry: The geometry of this AreaGetDTO.  # noqa: E501
        :type: GeoJsonObject
        """

        self._geometry = geometry

    @property
    def event(self):
        """Gets the event of this AreaGetDTO.  # noqa: E501


        :return: The event of this AreaGetDTO.  # noqa: E501
        :rtype: EventGetDTO
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this AreaGetDTO.


        :param event: The event of this AreaGetDTO.  # noqa: E501
        :type: EventGetDTO
        """

        self._event = event

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
        if issubclass(AreaGetDTO, dict):
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
        if not isinstance(other, AreaGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

