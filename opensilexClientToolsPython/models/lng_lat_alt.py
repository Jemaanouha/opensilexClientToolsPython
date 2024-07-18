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


class LngLatAlt(object):
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
        'longitude': 'float',
        'latitude': 'float',
        'altitude': 'float',
        'additional_elements': 'list[float]'
    }

    attribute_map = {
        'longitude': 'longitude',
        'latitude': 'latitude',
        'altitude': 'altitude',
        'additional_elements': 'additionalElements'
    }
    def __init__(self,
        longitude : 'float' = None,
        latitude : 'float' = None,
        altitude : 'float' = None,
        additional_elements : 'List[float]' = None):  # noqa: E501
        """LngLatAlt - a model defined in Swagger"""  # noqa: E501

        self._longitude = None
        self._latitude = None
        self._altitude = None
        self._additional_elements = None
        self.discriminator = None

        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if altitude is not None:
            self.altitude = altitude
        if additional_elements is not None:
            self.additional_elements = additional_elements

    @property
    def longitude(self):
        """Gets the longitude of this LngLatAlt.  # noqa: E501


        :return: The longitude of this LngLatAlt.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this LngLatAlt.


        :param longitude: The longitude of this LngLatAlt.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this LngLatAlt.  # noqa: E501


        :return: The latitude of this LngLatAlt.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this LngLatAlt.


        :param latitude: The latitude of this LngLatAlt.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def altitude(self):
        """Gets the altitude of this LngLatAlt.  # noqa: E501


        :return: The altitude of this LngLatAlt.  # noqa: E501
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this LngLatAlt.


        :param altitude: The altitude of this LngLatAlt.  # noqa: E501
        :type: float
        """

        self._altitude = altitude

    @property
    def additional_elements(self):
        """Gets the additional_elements of this LngLatAlt.  # noqa: E501


        :return: The additional_elements of this LngLatAlt.  # noqa: E501
        :rtype: list[float]
        """
        return self._additional_elements

    @additional_elements.setter
    def additional_elements(self, additional_elements):
        """Sets the additional_elements of this LngLatAlt.


        :param additional_elements: The additional_elements of this LngLatAlt.  # noqa: E501
        :type: list[float]
        """

        self._additional_elements = additional_elements

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
        if issubclass(LngLatAlt, dict):
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
        if issubclass(LngLatAlt, dict):
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
        if not isinstance(other, LngLatAlt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




