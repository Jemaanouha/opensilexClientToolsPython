# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class SiteAddressDTO(object):
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
        'country_name': 'str',
        'locality': 'str',
        'postal_code': 'str',
        'region': 'str',
        'street_address': 'str',
        'readable_address': 'str'
    }

    attribute_map = {
        'country_name': 'countryName',
        'locality': 'locality',
        'postal_code': 'postalCode',
        'region': 'region',
        'street_address': 'streetAddress',
        'readable_address': 'readableAddress'
    }
    def __init__(self, country_name : 'str' = None, locality : 'str' = None, postal_code : 'str' = None, region : 'str' = None, street_address : 'str' = None, readable_address : 'str' = None):  # noqa: E501
        """SiteAddressDTO - a model defined in Swagger"""  # noqa: E501

        self._country_name = None
        self._locality = None
        self._postal_code = None
        self._region = None
        self._street_address = None
        self._readable_address = None
        self.discriminator = None

        if country_name is not None:
            self.country_name = country_name
        if locality is not None:
            self.locality = locality
        if postal_code is not None:
            self.postal_code = postal_code
        if region is not None:
            self.region = region
        if street_address is not None:
            self.street_address = street_address
        if readable_address is not None:
            self.readable_address = readable_address

    @property
    def country_name(self):
        """Gets the country_name of this SiteAddressDTO.  # noqa: E501


        :return: The country_name of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this SiteAddressDTO.


        :param country_name: The country_name of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def locality(self):
        """Gets the locality of this SiteAddressDTO.  # noqa: E501


        :return: The locality of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this SiteAddressDTO.


        :param locality: The locality of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def postal_code(self):
        """Gets the postal_code of this SiteAddressDTO.  # noqa: E501


        :return: The postal_code of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SiteAddressDTO.


        :param postal_code: The postal_code of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def region(self):
        """Gets the region of this SiteAddressDTO.  # noqa: E501


        :return: The region of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SiteAddressDTO.


        :param region: The region of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def street_address(self):
        """Gets the street_address of this SiteAddressDTO.  # noqa: E501


        :return: The street_address of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this SiteAddressDTO.


        :param street_address: The street_address of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def readable_address(self):
        """Gets the readable_address of this SiteAddressDTO.  # noqa: E501


        :return: The readable_address of this SiteAddressDTO.  # noqa: E501
        :rtype: str
        """
        return self._readable_address

    @readable_address.setter
    def readable_address(self, readable_address):
        """Sets the readable_address of this SiteAddressDTO.


        :param readable_address: The readable_address of this SiteAddressDTO.  # noqa: E501
        :type: str
        """

        self._readable_address = readable_address

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
        if issubclass(SiteAddressDTO, dict):
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
        if not isinstance(other, SiteAddressDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

