# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.2-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class GroupUserProfileDTO(object):
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
        'profile_uri': 'str',
        'profile_name': 'str',
        'user_uri': 'str',
        'user_name': 'str',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'profile_uri': 'profile_uri',
        'profile_name': 'profile_name',
        'user_uri': 'user_uri',
        'user_name': 'user_name',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date'
    }
    def __init__(self,
        user_uri : 'str',
        uri : 'str' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        profile_uri : 'str' = None,
        profile_name : 'str' = None,
        user_name : 'str' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None):  # noqa: E501
        """GroupUserProfileDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._profile_uri = None
        self._profile_name = None
        self._user_uri = None
        self._user_name = None
        self._publication_date = None
        self._last_updated_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if profile_uri is not None:
            self.profile_uri = profile_uri
        if profile_name is not None:
            self.profile_name = profile_name
        self.user_uri = user_uri
        if user_name is not None:
            self.user_name = user_name
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date

    @property
    def uri(self):
        """Gets the uri of this GroupUserProfileDTO.  # noqa: E501

        Group URI  # noqa: E501

        :return: The uri of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GroupUserProfileDTO.

        Group URI  # noqa: E501

        :param uri: The uri of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this GroupUserProfileDTO.  # noqa: E501


        :return: The rdf_type of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this GroupUserProfileDTO.


        :param rdf_type: The rdf_type of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this GroupUserProfileDTO.  # noqa: E501


        :return: The rdf_type_name of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this GroupUserProfileDTO.


        :param rdf_type_name: The rdf_type_name of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def profile_uri(self):
        """Gets the profile_uri of this GroupUserProfileDTO.  # noqa: E501

        User associated profile URI  # noqa: E501

        :return: The profile_uri of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._profile_uri

    @profile_uri.setter
    def profile_uri(self, profile_uri):
        """Sets the profile_uri of this GroupUserProfileDTO.

        User associated profile URI  # noqa: E501

        :param profile_uri: The profile_uri of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._profile_uri = profile_uri

    @property
    def profile_name(self):
        """Gets the profile_name of this GroupUserProfileDTO.  # noqa: E501

        User associated profile name  # noqa: E501

        :return: The profile_name of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this GroupUserProfileDTO.

        User associated profile name  # noqa: E501

        :param profile_name: The profile_name of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def user_uri(self):
        """Gets the user_uri of this GroupUserProfileDTO.  # noqa: E501

        User URI  # noqa: E501

        :return: The user_uri of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_uri

    @user_uri.setter
    def user_uri(self, user_uri):
        """Sets the user_uri of this GroupUserProfileDTO.

        User URI  # noqa: E501

        :param user_uri: The user_uri of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """
        if user_uri is None:
            raise ValueError("Invalid value for `user_uri`, must not be `None`")  # noqa: E501

        self._user_uri = user_uri

    @property
    def user_name(self):
        """Gets the user_name of this GroupUserProfileDTO.  # noqa: E501

        User name  # noqa: E501

        :return: The user_name of this GroupUserProfileDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GroupUserProfileDTO.

        User name  # noqa: E501

        :param user_name: The user_name of this GroupUserProfileDTO.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def publication_date(self):
        """Gets the publication_date of this GroupUserProfileDTO.  # noqa: E501


        :return: The publication_date of this GroupUserProfileDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this GroupUserProfileDTO.


        :param publication_date: The publication_date of this GroupUserProfileDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this GroupUserProfileDTO.  # noqa: E501


        :return: The last_updated_date of this GroupUserProfileDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this GroupUserProfileDTO.


        :param last_updated_date: The last_updated_date of this GroupUserProfileDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

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
        if issubclass(GroupUserProfileDTO, dict):
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
        if issubclass(GroupUserProfileDTO, dict):
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
        if not isinstance(other, GroupUserProfileDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




