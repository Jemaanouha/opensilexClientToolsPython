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

from opensilexClientToolsPython.models.named_resource_dto_factor_level_model import NamedResourceDTOFactorLevelModel
from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO
from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject



class ScientificObjectDetailDTO(object):
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
        'parent': 'str',
        'parent_name': 'str',
        'factor_level': 'list[NamedResourceDTOFactorLevelModel]',
        'relations': 'list[RDFObjectRelationDTO]',
        'geometry': 'GeoJsonObject'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'parent': 'parent',
        'parent_name': 'parent_name',
        'factor_level': 'factor_level',
        'relations': 'relations',
        'geometry': 'geometry'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, rdf_type_name : 'str' = None, name : 'str' = None, parent : 'str' = None, parent_name : 'str' = None, factor_level : List['NamedResourceDTOFactorLevelModel'] = None, relations : List['RDFObjectRelationDTO'] = None, geometry : 'GeoJsonObject' = None):  # noqa: E501
        """ScientificObjectDetailDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._parent = None
        self._parent_name = None
        self._factor_level = None
        self._relations = None
        self._geometry = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if parent_name is not None:
            self.parent_name = parent_name
        if factor_level is not None:
            self.factor_level = factor_level
        if relations is not None:
            self.relations = relations
        if geometry is not None:
            self.geometry = geometry

    @property
    def uri(self):
        """Gets the uri of this ScientificObjectDetailDTO.  # noqa: E501


        :return: The uri of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ScientificObjectDetailDTO.


        :param uri: The uri of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this ScientificObjectDetailDTO.  # noqa: E501

        Scientific object type  # noqa: E501

        :return: The rdf_type of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this ScientificObjectDetailDTO.

        Scientific object type  # noqa: E501

        :param rdf_type: The rdf_type of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this ScientificObjectDetailDTO.  # noqa: E501

        Scientific object type  # noqa: E501

        :return: The rdf_type_name of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this ScientificObjectDetailDTO.

        Scientific object type  # noqa: E501

        :param rdf_type_name: The rdf_type_name of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this ScientificObjectDetailDTO.  # noqa: E501


        :return: The name of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScientificObjectDetailDTO.


        :param name: The name of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ScientificObjectDetailDTO.  # noqa: E501

        Scientific object parent URI  # noqa: E501

        :return: The parent of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ScientificObjectDetailDTO.

        Scientific object parent URI  # noqa: E501

        :param parent: The parent of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def parent_name(self):
        """Gets the parent_name of this ScientificObjectDetailDTO.  # noqa: E501

        Scientific object parent name  # noqa: E501

        :return: The parent_name of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this ScientificObjectDetailDTO.

        Scientific object parent name  # noqa: E501

        :param parent_name: The parent_name of this ScientificObjectDetailDTO.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

    @property
    def factor_level(self):
        """Gets the factor_level of this ScientificObjectDetailDTO.  # noqa: E501

        Scientific object factor levels  # noqa: E501

        :return: The factor_level of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: list[NamedResourceDTOFactorLevelModel]
        """
        return self._factor_level

    @factor_level.setter
    def factor_level(self, factor_level):
        """Sets the factor_level of this ScientificObjectDetailDTO.

        Scientific object factor levels  # noqa: E501

        :param factor_level: The factor_level of this ScientificObjectDetailDTO.  # noqa: E501
        :type: list[NamedResourceDTOFactorLevelModel]
        """

        self._factor_level = factor_level

    @property
    def relations(self):
        """Gets the relations of this ScientificObjectDetailDTO.  # noqa: E501


        :return: The relations of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this ScientificObjectDetailDTO.


        :param relations: The relations of this ScientificObjectDetailDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def geometry(self):
        """Gets the geometry of this ScientificObjectDetailDTO.  # noqa: E501


        :return: The geometry of this ScientificObjectDetailDTO.  # noqa: E501
        :rtype: GeoJsonObject
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this ScientificObjectDetailDTO.


        :param geometry: The geometry of this ScientificObjectDetailDTO.  # noqa: E501
        :type: GeoJsonObject
        """

        self._geometry = geometry

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
        if issubclass(ScientificObjectDetailDTO, dict):
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
        if not isinstance(other, ScientificObjectDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

