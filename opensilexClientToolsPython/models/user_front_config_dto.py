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


class UserFrontConfigDTO(object):
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
        'menu': 'list[MenuItemDTO]',
        'user_is_anonymous': 'bool'
    }

    attribute_map = {
        'menu': 'menu',
        'user_is_anonymous': 'userIsAnonymous'
    }
    def __init__(self,
        menu : 'List[MenuItemDTO]',
        user_is_anonymous : 'bool'):  # noqa: E501
        """UserFrontConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._menu = None
        self._user_is_anonymous = None
        self.discriminator = None

        self.menu = menu
        self.user_is_anonymous = user_is_anonymous

    @property
    def menu(self):
        """Gets the menu of this UserFrontConfigDTO.  # noqa: E501

        Application menu with routes  # noqa: E501

        :return: The menu of this UserFrontConfigDTO.  # noqa: E501
        :rtype: list[MenuItemDTO]
        """
        return self._menu

    @menu.setter
    def menu(self, menu):
        """Sets the menu of this UserFrontConfigDTO.

        Application menu with routes  # noqa: E501

        :param menu: The menu of this UserFrontConfigDTO.  # noqa: E501
        :type: list[MenuItemDTO]
        """
        if menu is None:
            raise ValueError("Invalid value for `menu`, must not be `None`")  # noqa: E501

        self._menu = menu

    @property
    def user_is_anonymous(self):
        """Gets the user_is_anonymous of this UserFrontConfigDTO.  # noqa: E501

        User is anonymous  # noqa: E501

        :return: The user_is_anonymous of this UserFrontConfigDTO.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_anonymous

    @user_is_anonymous.setter
    def user_is_anonymous(self, user_is_anonymous):
        """Sets the user_is_anonymous of this UserFrontConfigDTO.

        User is anonymous  # noqa: E501

        :param user_is_anonymous: The user_is_anonymous of this UserFrontConfigDTO.  # noqa: E501
        :type: bool
        """
        if user_is_anonymous is None:
            raise ValueError("Invalid value for `user_is_anonymous`, must not be `None`")  # noqa: E501

        self._user_is_anonymous = user_is_anonymous

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
        if issubclass(UserFrontConfigDTO, dict):
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
        if not isinstance(other, UserFrontConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.menu_item_dto import MenuItemDTO


