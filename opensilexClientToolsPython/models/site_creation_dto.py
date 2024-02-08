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

from typing import List, Dict


class SiteCreationDTO(object):
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
        'name': 'str',
        'address': 'SiteAddressDTO',
        'organizations': 'list[str]',
        'facilities': 'list[str]',
        'groups': 'list[str]',
        'rdf_type_name': 'str',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'name': 'name',
        'address': 'address',
        'organizations': 'organizations',
        'facilities': 'facilities',
        'groups': 'groups',
        'rdf_type_name': 'rdf_type_name',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date'
    }
    def __init__(self,
        uri : 'str' = None,
        rdf_type : 'str' = None,
        name : 'str' = None,
        address : 'SiteAddressDTO' = None,
        organizations : 'List[str]' = None,
        facilities : 'List[str]' = None,
        groups : 'List[str]' = None,
        rdf_type_name : 'str' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None):  # noqa: E501
        """SiteCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._name = None
        self._address = None
        self._organizations = None
        self._facilities = None
        self._groups = None
        self._rdf_type_name = None
        self._publication_date = None
        self._last_updated_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if organizations is not None:
            self.organizations = organizations
        if facilities is not None:
            self.facilities = facilities
        if groups is not None:
            self.groups = groups
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date

    @property
    def uri(self):
        """Gets the uri of this SiteCreationDTO.  # noqa: E501


        :return: The uri of this SiteCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this SiteCreationDTO.


        :param uri: The uri of this SiteCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this SiteCreationDTO.  # noqa: E501


        :return: The rdf_type of this SiteCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this SiteCreationDTO.


        :param rdf_type: The rdf_type of this SiteCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def name(self):
        """Gets the name of this SiteCreationDTO.  # noqa: E501


        :return: The name of this SiteCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteCreationDTO.


        :param name: The name of this SiteCreationDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this SiteCreationDTO.  # noqa: E501


        :return: The address of this SiteCreationDTO.  # noqa: E501
        :rtype: SiteAddressDTO
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SiteCreationDTO.


        :param address: The address of this SiteCreationDTO.  # noqa: E501
        :type: SiteAddressDTO
        """

        self._address = address

    @property
    def organizations(self):
        """Gets the organizations of this SiteCreationDTO.  # noqa: E501


        :return: The organizations of this SiteCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this SiteCreationDTO.


        :param organizations: The organizations of this SiteCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._organizations = organizations

    @property
    def facilities(self):
        """Gets the facilities of this SiteCreationDTO.  # noqa: E501


        :return: The facilities of this SiteCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this SiteCreationDTO.


        :param facilities: The facilities of this SiteCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._facilities = facilities

    @property
    def groups(self):
        """Gets the groups of this SiteCreationDTO.  # noqa: E501


        :return: The groups of this SiteCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SiteCreationDTO.


        :param groups: The groups of this SiteCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this SiteCreationDTO.  # noqa: E501


        :return: The rdf_type_name of this SiteCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this SiteCreationDTO.


        :param rdf_type_name: The rdf_type_name of this SiteCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def publication_date(self):
        """Gets the publication_date of this SiteCreationDTO.  # noqa: E501


        :return: The publication_date of this SiteCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this SiteCreationDTO.


        :param publication_date: The publication_date of this SiteCreationDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this SiteCreationDTO.  # noqa: E501


        :return: The last_updated_date of this SiteCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this SiteCreationDTO.


        :param last_updated_date: The last_updated_date of this SiteCreationDTO.  # noqa: E501
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
        if issubclass(SiteCreationDTO, dict):
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
        if not isinstance(other, SiteCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.site_address_dto import SiteAddressDTO


