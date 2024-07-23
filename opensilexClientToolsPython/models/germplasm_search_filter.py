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


class GermplasmSearchFilter(object):
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
        'included_uris': 'list[str]',
        'rdf_types': 'list[str]',
        'page': 'int',
        'lang': 'str',
        'uri': 'str',
        'name': 'str',
        'code': 'str',
        'species': 'str',
        'variety': 'str',
        'accession': 'str',
        'institute': 'str',
        'experiment': 'str',
        'metadata': 'str',
        'uris': 'list[str]',
        'group': 'str',
        'parent_germplasms': 'list[str]',
        'parent_m_germplasms': 'list[str]',
        'parent_f_germplasms': 'list[str]',
        'order_by': 'list[OrderBy]',
        'page_size': 'int',
        'rdf_type': 'str',
        'production_year': 'int'
    }

    attribute_map = {
        'included_uris': 'includedUris',
        'rdf_types': 'rdfTypes',
        'page': 'page',
        'lang': 'lang',
        'uri': 'uri',
        'name': 'name',
        'code': 'code',
        'species': 'species',
        'variety': 'variety',
        'accession': 'accession',
        'institute': 'institute',
        'experiment': 'experiment',
        'metadata': 'metadata',
        'uris': 'uris',
        'group': 'group',
        'parent_germplasms': 'parentGermplasms',
        'parent_m_germplasms': 'parentMGermplasms',
        'parent_f_germplasms': 'parentFGermplasms',
        'order_by': 'order_by',
        'page_size': 'page_size',
        'rdf_type': 'rdf_type',
        'production_year': 'production_year'
    }
    def __init__(self,
        included_uris : 'List[str]' = None,
        rdf_types : 'List[str]' = None,
        page : 'int' = None,
        lang : 'str' = None,
        uri : 'str' = None,
        name : 'str' = None,
        code : 'str' = None,
        species : 'str' = None,
        variety : 'str' = None,
        accession : 'str' = None,
        institute : 'str' = None,
        experiment : 'str' = None,
        metadata : 'str' = None,
        uris : 'List[str]' = None,
        group : 'str' = None,
        parent_germplasms : 'List[str]' = None,
        parent_m_germplasms : 'List[str]' = None,
        parent_f_germplasms : 'List[str]' = None,
        order_by : 'List[OrderBy]' = None,
        page_size : 'int' = None,
        rdf_type : 'str' = None,
        production_year : 'int' = None):  # noqa: E501
        """GermplasmSearchFilter - a model defined in Swagger"""  # noqa: E501

        self._included_uris = None
        self._rdf_types = None
        self._page = None
        self._lang = None
        self._uri = None
        self._name = None
        self._code = None
        self._species = None
        self._variety = None
        self._accession = None
        self._institute = None
        self._experiment = None
        self._metadata = None
        self._uris = None
        self._group = None
        self._parent_germplasms = None
        self._parent_m_germplasms = None
        self._parent_f_germplasms = None
        self._order_by = None
        self._page_size = None
        self._rdf_type = None
        self._production_year = None
        self.discriminator = None

        if included_uris is not None:
            self.included_uris = included_uris
        if rdf_types is not None:
            self.rdf_types = rdf_types
        if page is not None:
            self.page = page
        if lang is not None:
            self.lang = lang
        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if species is not None:
            self.species = species
        if variety is not None:
            self.variety = variety
        if accession is not None:
            self.accession = accession
        if institute is not None:
            self.institute = institute
        if experiment is not None:
            self.experiment = experiment
        if metadata is not None:
            self.metadata = metadata
        if uris is not None:
            self.uris = uris
        if group is not None:
            self.group = group
        if parent_germplasms is not None:
            self.parent_germplasms = parent_germplasms
        if parent_m_germplasms is not None:
            self.parent_m_germplasms = parent_m_germplasms
        if parent_f_germplasms is not None:
            self.parent_f_germplasms = parent_f_germplasms
        if order_by is not None:
            self.order_by = order_by
        if page_size is not None:
            self.page_size = page_size
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if production_year is not None:
            self.production_year = production_year

    @property
    def included_uris(self):
        """Gets the included_uris of this GermplasmSearchFilter.  # noqa: E501


        :return: The included_uris of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_uris

    @included_uris.setter
    def included_uris(self, included_uris):
        """Sets the included_uris of this GermplasmSearchFilter.


        :param included_uris: The included_uris of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._included_uris = included_uris

    @property
    def rdf_types(self):
        """Gets the rdf_types of this GermplasmSearchFilter.  # noqa: E501


        :return: The rdf_types of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._rdf_types

    @rdf_types.setter
    def rdf_types(self, rdf_types):
        """Sets the rdf_types of this GermplasmSearchFilter.


        :param rdf_types: The rdf_types of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._rdf_types = rdf_types

    @property
    def page(self):
        """Gets the page of this GermplasmSearchFilter.  # noqa: E501

        Page number  # noqa: E501

        :return: The page of this GermplasmSearchFilter.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this GermplasmSearchFilter.

        Page number  # noqa: E501

        :param page: The page of this GermplasmSearchFilter.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def lang(self):
        """Gets the lang of this GermplasmSearchFilter.  # noqa: E501


        :return: The lang of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this GermplasmSearchFilter.


        :param lang: The lang of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._lang = lang

    @property
    def uri(self):
        """Gets the uri of this GermplasmSearchFilter.  # noqa: E501

        Regex pattern for filtering list by uri  # noqa: E501

        :return: The uri of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GermplasmSearchFilter.

        Regex pattern for filtering list by uri  # noqa: E501

        :param uri: The uri of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this GermplasmSearchFilter.  # noqa: E501

        Regex pattern for filtering list by name and synonyms  # noqa: E501

        :return: The name of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GermplasmSearchFilter.

        Regex pattern for filtering list by name and synonyms  # noqa: E501

        :param name: The name of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this GermplasmSearchFilter.  # noqa: E501

        Regex pattern for filtering list by code  # noqa: E501

        :return: The code of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GermplasmSearchFilter.

        Regex pattern for filtering list by code  # noqa: E501

        :param code: The code of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def species(self):
        """Gets the species of this GermplasmSearchFilter.  # noqa: E501

        Search by species  # noqa: E501

        :return: The species of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this GermplasmSearchFilter.

        Search by species  # noqa: E501

        :param species: The species of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._species = species

    @property
    def variety(self):
        """Gets the variety of this GermplasmSearchFilter.  # noqa: E501

        Search by variety  # noqa: E501

        :return: The variety of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this GermplasmSearchFilter.

        Search by variety  # noqa: E501

        :param variety: The variety of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._variety = variety

    @property
    def accession(self):
        """Gets the accession of this GermplasmSearchFilter.  # noqa: E501

        Search by accession  # noqa: E501

        :return: The accession of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this GermplasmSearchFilter.

        Search by accession  # noqa: E501

        :param accession: The accession of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def institute(self):
        """Gets the institute of this GermplasmSearchFilter.  # noqa: E501

        Search by institute  # noqa: E501

        :return: The institute of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._institute

    @institute.setter
    def institute(self, institute):
        """Sets the institute of this GermplasmSearchFilter.

        Search by institute  # noqa: E501

        :param institute: The institute of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._institute = institute

    @property
    def experiment(self):
        """Gets the experiment of this GermplasmSearchFilter.  # noqa: E501

        Search by experiment  # noqa: E501

        :return: The experiment of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this GermplasmSearchFilter.

        Search by experiment  # noqa: E501

        :param experiment: The experiment of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._experiment = experiment

    @property
    def metadata(self):
        """Gets the metadata of this GermplasmSearchFilter.  # noqa: E501

        Search by metadata  # noqa: E501

        :return: The metadata of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GermplasmSearchFilter.

        Search by metadata  # noqa: E501

        :param metadata: The metadata of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def uris(self):
        """Gets the uris of this GermplasmSearchFilter.  # noqa: E501

        List of germplasm URI  # noqa: E501

        :return: The uris of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this GermplasmSearchFilter.

        List of germplasm URI  # noqa: E501

        :param uris: The uris of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._uris = uris

    @property
    def group(self):
        """Gets the group of this GermplasmSearchFilter.  # noqa: E501

        Search by germplasm group  # noqa: E501

        :return: The group of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GermplasmSearchFilter.

        Search by germplasm group  # noqa: E501

        :param group: The group of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def parent_germplasms(self):
        """Gets the parent_germplasms of this GermplasmSearchFilter.  # noqa: E501


        :return: The parent_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_germplasms

    @parent_germplasms.setter
    def parent_germplasms(self, parent_germplasms):
        """Sets the parent_germplasms of this GermplasmSearchFilter.


        :param parent_germplasms: The parent_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._parent_germplasms = parent_germplasms

    @property
    def parent_m_germplasms(self):
        """Gets the parent_m_germplasms of this GermplasmSearchFilter.  # noqa: E501


        :return: The parent_m_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_m_germplasms

    @parent_m_germplasms.setter
    def parent_m_germplasms(self, parent_m_germplasms):
        """Sets the parent_m_germplasms of this GermplasmSearchFilter.


        :param parent_m_germplasms: The parent_m_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._parent_m_germplasms = parent_m_germplasms

    @property
    def parent_f_germplasms(self):
        """Gets the parent_f_germplasms of this GermplasmSearchFilter.  # noqa: E501


        :return: The parent_f_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_f_germplasms

    @parent_f_germplasms.setter
    def parent_f_germplasms(self, parent_f_germplasms):
        """Sets the parent_f_germplasms of this GermplasmSearchFilter.


        :param parent_f_germplasms: The parent_f_germplasms of this GermplasmSearchFilter.  # noqa: E501
        :type: list[str]
        """

        self._parent_f_germplasms = parent_f_germplasms

    @property
    def order_by(self):
        """Gets the order_by of this GermplasmSearchFilter.  # noqa: E501

        List of fields to sort as an array of fieldName=asc|desc  # noqa: E501

        :return: The order_by of this GermplasmSearchFilter.  # noqa: E501
        :rtype: list[OrderBy]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this GermplasmSearchFilter.

        List of fields to sort as an array of fieldName=asc|desc  # noqa: E501

        :param order_by: The order_by of this GermplasmSearchFilter.  # noqa: E501
        :type: list[OrderBy]
        """

        self._order_by = order_by

    @property
    def page_size(self):
        """Gets the page_size of this GermplasmSearchFilter.  # noqa: E501

        Page size  # noqa: E501

        :return: The page_size of this GermplasmSearchFilter.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GermplasmSearchFilter.

        Page size  # noqa: E501

        :param page_size: The page_size of this GermplasmSearchFilter.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def rdf_type(self):
        """Gets the rdf_type of this GermplasmSearchFilter.  # noqa: E501

        Search by type  # noqa: E501

        :return: The rdf_type of this GermplasmSearchFilter.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this GermplasmSearchFilter.

        Search by type  # noqa: E501

        :param rdf_type: The rdf_type of this GermplasmSearchFilter.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def production_year(self):
        """Gets the production_year of this GermplasmSearchFilter.  # noqa: E501

        Search by production year  # noqa: E501

        :return: The production_year of this GermplasmSearchFilter.  # noqa: E501
        :rtype: int
        """
        return self._production_year

    @production_year.setter
    def production_year(self, production_year):
        """Sets the production_year of this GermplasmSearchFilter.

        Search by production year  # noqa: E501

        :param production_year: The production_year of this GermplasmSearchFilter.  # noqa: E501
        :type: int
        """

        self._production_year = production_year

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
        if issubclass(GermplasmSearchFilter, dict):
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
        if issubclass(GermplasmSearchFilter, dict):
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
        if not isinstance(other, GermplasmSearchFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.order_by import OrderBy


