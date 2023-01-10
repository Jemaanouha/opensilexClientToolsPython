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

from opensilexClientToolsPython.models.point import Point



class PositionCreationDTO(object):
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
        'point': 'Point',
        'x': 'str',
        'y': 'str',
        'z': 'str',
        'text': 'str'
    }

    attribute_map = {
        'point': 'point',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'text': 'text'
    }
    def __init__(self, point : 'Point' = None, x : 'str' = None, y : 'str' = None, z : 'str' = None, text : 'str' = None):  # noqa: E501
        """PositionCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._point = None
        self._x = None
        self._y = None
        self._z = None
        self._text = None
        self.discriminator = None

        if point is not None:
            self.point = point
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if text is not None:
            self.text = text

    @property
    def point(self):
        """Gets the point of this PositionCreationDTO.  # noqa: E501


        :return: The point of this PositionCreationDTO.  # noqa: E501
        :rtype: Point
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PositionCreationDTO.


        :param point: The point of this PositionCreationDTO.  # noqa: E501
        :type: Point
        """

        self._point = point

    @property
    def x(self):
        """Gets the x of this PositionCreationDTO.  # noqa: E501


        :return: The x of this PositionCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this PositionCreationDTO.


        :param x: The x of this PositionCreationDTO.  # noqa: E501
        :type: str
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this PositionCreationDTO.  # noqa: E501


        :return: The y of this PositionCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this PositionCreationDTO.


        :param y: The y of this PositionCreationDTO.  # noqa: E501
        :type: str
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this PositionCreationDTO.  # noqa: E501


        :return: The z of this PositionCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this PositionCreationDTO.


        :param z: The z of this PositionCreationDTO.  # noqa: E501
        :type: str
        """

        self._z = z

    @property
    def text(self):
        """Gets the text of this PositionCreationDTO.  # noqa: E501


        :return: The text of this PositionCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PositionCreationDTO.


        :param text: The text of this PositionCreationDTO.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(PositionCreationDTO, dict):
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
        if not isinstance(other, PositionCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

