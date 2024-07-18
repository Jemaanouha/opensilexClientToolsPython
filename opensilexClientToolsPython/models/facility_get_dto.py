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


class FacilityGetDTO(object):
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
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime',
        'rdf_type': 'str',
        'rdf_type_name': 'str',
        'name': 'str',
        'organizations': 'list[NamedResourceDTOOrganizationModel]',
        'sites': 'list[NamedResourceDTOSiteModel]',
        'address': 'FacilityAddressDTO',
        'variable_groups': 'list[NamedResourceDTOVariablesGroupModel]',
        'geometry': 'GeoJsonObject',
        'relations': 'list[RDFObjectRelationDTO]'
    }

    attribute_map = {
        'uri': 'uri',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'organizations': 'organizations',
        'sites': 'sites',
        'address': 'address',
        'variable_groups': 'variableGroups',
        'geometry': 'geometry',
        'relations': 'relations'
    }
    def __init__(self,
        organizations : 'List[NamedResourceDTOOrganizationModel]',
        uri : 'str' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        name : 'str' = None,
        sites : 'List[NamedResourceDTOSiteModel]' = None,
        address : 'FacilityAddressDTO' = None,
        variable_groups : 'List[NamedResourceDTOVariablesGroupModel]' = None,
        geometry : 'GeoJsonObject' = None,
        relations : 'List[RDFObjectRelationDTO]' = None):  # noqa: E501
        """FacilityGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._organizations = None
        self._sites = None
        self._address = None
        self._variable_groups = None
        self._geometry = None
        self._relations = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        self.organizations = organizations
        if sites is not None:
            self.sites = sites
        if address is not None:
            self.address = address
        if variable_groups is not None:
            self.variable_groups = variable_groups
        if geometry is not None:
            self.geometry = geometry
        if relations is not None:
            self.relations = relations

    @property
    def uri(self):
        """Gets the uri of this FacilityGetDTO.  # noqa: E501


        :return: The uri of this FacilityGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FacilityGetDTO.


        :param uri: The uri of this FacilityGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def publisher(self):
        """Gets the publisher of this FacilityGetDTO.  # noqa: E501


        :return: The publisher of this FacilityGetDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this FacilityGetDTO.


        :param publisher: The publisher of this FacilityGetDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this FacilityGetDTO.  # noqa: E501


        :return: The publication_date of this FacilityGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this FacilityGetDTO.


        :param publication_date: The publication_date of this FacilityGetDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this FacilityGetDTO.  # noqa: E501


        :return: The last_updated_date of this FacilityGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this FacilityGetDTO.


        :param last_updated_date: The last_updated_date of this FacilityGetDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def rdf_type(self):
        """Gets the rdf_type of this FacilityGetDTO.  # noqa: E501


        :return: The rdf_type of this FacilityGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this FacilityGetDTO.


        :param rdf_type: The rdf_type of this FacilityGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this FacilityGetDTO.  # noqa: E501


        :return: The rdf_type_name of this FacilityGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this FacilityGetDTO.


        :param rdf_type_name: The rdf_type_name of this FacilityGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this FacilityGetDTO.  # noqa: E501


        :return: The name of this FacilityGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FacilityGetDTO.


        :param name: The name of this FacilityGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organizations(self):
        """Gets the organizations of this FacilityGetDTO.  # noqa: E501


        :return: The organizations of this FacilityGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOOrganizationModel]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this FacilityGetDTO.


        :param organizations: The organizations of this FacilityGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOOrganizationModel]
        """
        if organizations is None:
            raise ValueError("Invalid value for `organizations`, must not be `None`")  # noqa: E501

        self._organizations = organizations

    @property
    def sites(self):
        """Gets the sites of this FacilityGetDTO.  # noqa: E501


        :return: The sites of this FacilityGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOSiteModel]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this FacilityGetDTO.


        :param sites: The sites of this FacilityGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOSiteModel]
        """

        self._sites = sites

    @property
    def address(self):
        """Gets the address of this FacilityGetDTO.  # noqa: E501


        :return: The address of this FacilityGetDTO.  # noqa: E501
        :rtype: FacilityAddressDTO
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this FacilityGetDTO.


        :param address: The address of this FacilityGetDTO.  # noqa: E501
        :type: FacilityAddressDTO
        """

        self._address = address

    @property
    def variable_groups(self):
        """Gets the variable_groups of this FacilityGetDTO.  # noqa: E501


        :return: The variable_groups of this FacilityGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOVariablesGroupModel]
        """
        return self._variable_groups

    @variable_groups.setter
    def variable_groups(self, variable_groups):
        """Sets the variable_groups of this FacilityGetDTO.


        :param variable_groups: The variable_groups of this FacilityGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOVariablesGroupModel]
        """

        self._variable_groups = variable_groups

    @property
    def geometry(self):
        """Gets the geometry of this FacilityGetDTO.  # noqa: E501


        :return: The geometry of this FacilityGetDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this FacilityGetDTO.


        :param geometry: The geometry of this FacilityGetDTO.  # noqa: E501
        :type: GeoJsonObject
        """

        self._geometry = geometry

    @property
    def relations(self):
        """Gets the relations of this FacilityGetDTO.  # noqa: E501


        :return: The relations of this FacilityGetDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this FacilityGetDTO.


        :param relations: The relations of this FacilityGetDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

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
        if issubclass(FacilityGetDTO, dict):
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
        if issubclass(FacilityGetDTO, dict):
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
        if not isinstance(other, FacilityGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.user_get_dto import UserGetDTO
from opensilexClientToolsPython.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel
from opensilexClientToolsPython.models.named_resource_dto_site_model import NamedResourceDTOSiteModel
from opensilexClientToolsPython.models.facility_address_dto import FacilityAddressDTO
from opensilexClientToolsPython.models.named_resource_dto_variables_group_model import NamedResourceDTOVariablesGroupModel
from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject
from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO


