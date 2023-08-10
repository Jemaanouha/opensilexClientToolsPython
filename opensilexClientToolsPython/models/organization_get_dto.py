# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel
from opensilexClientToolsPython.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel
from opensilexClientToolsPython.models.named_resource_dto_group_model import NamedResourceDTOGroupModel
from opensilexClientToolsPython.models.named_resource_dto_facility_model import NamedResourceDTOFacilityModel
from opensilexClientToolsPython.models.named_resource_dto_site_model import NamedResourceDTOSiteModel
from opensilexClientToolsPython.models.named_resource_dto_experiment_model import NamedResourceDTOExperimentModel



class OrganizationGetDTO(object):
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
        'name': 'str',
        'parents': 'list[NamedResourceDTOOrganizationModel]',
        'children': 'list[NamedResourceDTOOrganizationModel]',
        'groups': 'list[NamedResourceDTOGroupModel]',
        'facilities': 'list[NamedResourceDTOFacilityModel]',
        'sites': 'list[NamedResourceDTOSiteModel]',
        'experiments': 'list[NamedResourceDTOExperimentModel]'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'parents': 'parents',
        'children': 'children',
        'groups': 'groups',
        'facilities': 'facilities',
        'sites': 'sites',
        'experiments': 'experiments'
    }
    def __init__(self,
        uri : 'str' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        name : 'str' = None,
        parents : 'List[NamedResourceDTOOrganizationModel]' = None,
        children : 'List[NamedResourceDTOOrganizationModel]' = None,
        groups : 'List[NamedResourceDTOGroupModel]' = None,
        facilities : 'List[NamedResourceDTOFacilityModel]' = None,
        sites : 'List[NamedResourceDTOSiteModel]' = None,
        experiments : 'List[NamedResourceDTOExperimentModel]' = None):  # noqa: E501
        """OrganizationGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._parents = None
        self._children = None
        self._groups = None
        self._facilities = None
        self._sites = None
        self._experiments = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        if parents is not None:
            self.parents = parents
        if children is not None:
            self.children = children
        if groups is not None:
            self.groups = groups
        if facilities is not None:
            self.facilities = facilities
        if sites is not None:
            self.sites = sites
        if experiments is not None:
            self.experiments = experiments

    @property
    def uri(self):
        """Gets the uri of this OrganizationGetDTO.  # noqa: E501


        :return: The uri of this OrganizationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this OrganizationGetDTO.


        :param uri: The uri of this OrganizationGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this OrganizationGetDTO.  # noqa: E501


        :return: The rdf_type of this OrganizationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this OrganizationGetDTO.


        :param rdf_type: The rdf_type of this OrganizationGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this OrganizationGetDTO.  # noqa: E501


        :return: The rdf_type_name of this OrganizationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this OrganizationGetDTO.


        :param rdf_type_name: The rdf_type_name of this OrganizationGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this OrganizationGetDTO.  # noqa: E501


        :return: The name of this OrganizationGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationGetDTO.


        :param name: The name of this OrganizationGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parents(self):
        """Gets the parents of this OrganizationGetDTO.  # noqa: E501


        :return: The parents of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOOrganizationModel]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this OrganizationGetDTO.


        :param parents: The parents of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOOrganizationModel]
        """

        self._parents = parents

    @property
    def children(self):
        """Gets the children of this OrganizationGetDTO.  # noqa: E501


        :return: The children of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOOrganizationModel]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this OrganizationGetDTO.


        :param children: The children of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOOrganizationModel]
        """

        self._children = children

    @property
    def groups(self):
        """Gets the groups of this OrganizationGetDTO.  # noqa: E501


        :return: The groups of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOGroupModel]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this OrganizationGetDTO.


        :param groups: The groups of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOGroupModel]
        """

        self._groups = groups

    @property
    def facilities(self):
        """Gets the facilities of this OrganizationGetDTO.  # noqa: E501


        :return: The facilities of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOFacilityModel]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this OrganizationGetDTO.


        :param facilities: The facilities of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOFacilityModel]
        """

        self._facilities = facilities

    @property
    def sites(self):
        """Gets the sites of this OrganizationGetDTO.  # noqa: E501


        :return: The sites of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOSiteModel]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this OrganizationGetDTO.


        :param sites: The sites of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOSiteModel]
        """

        self._sites = sites

    @property
    def experiments(self):
        """Gets the experiments of this OrganizationGetDTO.  # noqa: E501


        :return: The experiments of this OrganizationGetDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOExperimentModel]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this OrganizationGetDTO.


        :param experiments: The experiments of this OrganizationGetDTO.  # noqa: E501
        :type: list[NamedResourceDTOExperimentModel]
        """

        self._experiments = experiments

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
        if issubclass(OrganizationGetDTO, dict):
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
        if not isinstance(other, OrganizationGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

