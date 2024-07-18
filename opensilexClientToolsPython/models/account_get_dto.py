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


class AccountGetDTO(object):
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
        'email': 'str',
        'admin': 'bool',
        'language': 'str',
        'enable': 'bool',
        'favorites': 'list[str]',
        'linked_person': 'str',
        'person_first_name': 'str',
        'person_last_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'email': 'email',
        'admin': 'admin',
        'language': 'language',
        'enable': 'enable',
        'favorites': 'favorites',
        'linked_person': 'linked_person',
        'person_first_name': 'person_first_name',
        'person_last_name': 'person_last_name'
    }
    def __init__(self,
        uri : 'str' = None,
        email : 'str' = None,
        admin : 'bool' = None,
        language : 'str' = None,
        enable : 'bool' = None,
        favorites : 'List[str]' = None,
        linked_person : 'str' = None,
        person_first_name : 'str' = None,
        person_last_name : 'str' = None):  # noqa: E501
        """AccountGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._email = None
        self._admin = None
        self._language = None
        self._enable = None
        self._favorites = None
        self._linked_person = None
        self._person_first_name = None
        self._person_last_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if email is not None:
            self.email = email
        if admin is not None:
            self.admin = admin
        if language is not None:
            self.language = language
        if enable is not None:
            self.enable = enable
        if favorites is not None:
            self.favorites = favorites
        if linked_person is not None:
            self.linked_person = linked_person
        if person_first_name is not None:
            self.person_first_name = person_first_name
        if person_last_name is not None:
            self.person_last_name = person_last_name

    @property
    def uri(self):
        """Gets the uri of this AccountGetDTO.  # noqa: E501

        Account URI  # noqa: E501

        :return: The uri of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AccountGetDTO.

        Account URI  # noqa: E501

        :param uri: The uri of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def email(self):
        """Gets the email of this AccountGetDTO.  # noqa: E501

        Account email  # noqa: E501

        :return: The email of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountGetDTO.

        Account email  # noqa: E501

        :param email: The email of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def admin(self):
        """Gets the admin of this AccountGetDTO.  # noqa: E501

        Account admin flag  # noqa: E501

        :return: The admin of this AccountGetDTO.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this AccountGetDTO.

        Account admin flag  # noqa: E501

        :param admin: The admin of this AccountGetDTO.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def language(self):
        """Gets the language of this AccountGetDTO.  # noqa: E501

        Account language  # noqa: E501

        :return: The language of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AccountGetDTO.

        Account language  # noqa: E501

        :param language: The language of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def enable(self):
        """Gets the enable of this AccountGetDTO.  # noqa: E501

        Account is enable  # noqa: E501

        :return: The enable of this AccountGetDTO.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AccountGetDTO.

        Account is enable  # noqa: E501

        :param enable: The enable of this AccountGetDTO.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def favorites(self):
        """Gets the favorites of this AccountGetDTO.  # noqa: E501

        Favorites URI  # noqa: E501

        :return: The favorites of this AccountGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this AccountGetDTO.

        Favorites URI  # noqa: E501

        :param favorites: The favorites of this AccountGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._favorites = favorites

    @property
    def linked_person(self):
        """Gets the linked_person of this AccountGetDTO.  # noqa: E501

        URI of the Person linked to this account  # noqa: E501

        :return: The linked_person of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._linked_person

    @linked_person.setter
    def linked_person(self, linked_person):
        """Sets the linked_person of this AccountGetDTO.

        URI of the Person linked to this account  # noqa: E501

        :param linked_person: The linked_person of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._linked_person = linked_person

    @property
    def person_first_name(self):
        """Gets the person_first_name of this AccountGetDTO.  # noqa: E501

        first name of the linked person  # noqa: E501

        :return: The person_first_name of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._person_first_name

    @person_first_name.setter
    def person_first_name(self, person_first_name):
        """Sets the person_first_name of this AccountGetDTO.

        first name of the linked person  # noqa: E501

        :param person_first_name: The person_first_name of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._person_first_name = person_first_name

    @property
    def person_last_name(self):
        """Gets the person_last_name of this AccountGetDTO.  # noqa: E501

        last name of the linked person  # noqa: E501

        :return: The person_last_name of this AccountGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._person_last_name

    @person_last_name.setter
    def person_last_name(self, person_last_name):
        """Sets the person_last_name of this AccountGetDTO.

        last name of the linked person  # noqa: E501

        :param person_last_name: The person_last_name of this AccountGetDTO.  # noqa: E501
        :type: str
        """

        self._person_last_name = person_last_name

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
        if issubclass(AccountGetDTO, dict):
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
        if issubclass(AccountGetDTO, dict):
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
        if not isinstance(other, AccountGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




