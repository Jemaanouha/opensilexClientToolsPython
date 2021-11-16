# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MenuItemDTO(object):
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
        'id': 'str',
        'label': 'str',
        'children': 'list[MenuItemDTO]',
        'route': 'RouteDTO'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'children': 'children',
        'route': 'route'
    }

    def __init__(self, id=None, label=None, children=None, route=None):  # noqa: E501
        """MenuItemDTO - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._label = None
        self._children = None
        self._route = None
        self.discriminator = None

        self.id = id
        self.label = label
        self.children = children
        if route is not None:
            self.route = route

    @property
    def id(self):
        """Gets the id of this MenuItemDTO.  # noqa: E501

        Menu identifier  # noqa: E501

        :return: The id of this MenuItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MenuItemDTO.

        Menu identifier  # noqa: E501

        :param id: The id of this MenuItemDTO.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this MenuItemDTO.  # noqa: E501

        Menu label  # noqa: E501

        :return: The label of this MenuItemDTO.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MenuItemDTO.

        Menu label  # noqa: E501

        :param label: The label of this MenuItemDTO.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def children(self):
        """Gets the children of this MenuItemDTO.  # noqa: E501

        List of sub menu items  # noqa: E501

        :return: The children of this MenuItemDTO.  # noqa: E501
        :rtype: list[MenuItemDTO]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this MenuItemDTO.

        List of sub menu items  # noqa: E501

        :param children: The children of this MenuItemDTO.  # noqa: E501
        :type: list[MenuItemDTO]
        """
        if children is None:
            raise ValueError("Invalid value for `children`, must not be `None`")  # noqa: E501

        self._children = children

    @property
    def route(self):
        """Gets the route of this MenuItemDTO.  # noqa: E501

        Optional route definition  # noqa: E501

        :return: The route of this MenuItemDTO.  # noqa: E501
        :rtype: RouteDTO
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this MenuItemDTO.

        Optional route definition  # noqa: E501

        :param route: The route of this MenuItemDTO.  # noqa: E501
        :type: RouteDTO
        """

        self._route = route

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
        if issubclass(MenuItemDTO, dict):
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
        if not isinstance(other, MenuItemDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
