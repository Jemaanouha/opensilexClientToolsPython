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




class GermplasmGetSingleDTO(object):
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
        'synonyms': 'list[str]',
        'code': 'str',
        'production_year': 'int',
        'description': 'str',
        'species': 'str',
        'species_name': 'str',
        'variety': 'str',
        'variety_name': 'str',
        'accession': 'str',
        'accession_name': 'str',
        'institute': 'str',
        'website': 'str',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'synonyms': 'synonyms',
        'code': 'code',
        'production_year': 'production_year',
        'description': 'description',
        'species': 'species',
        'species_name': 'species_name',
        'variety': 'variety',
        'variety_name': 'variety_name',
        'accession': 'accession',
        'accession_name': 'accession_name',
        'institute': 'institute',
        'website': 'website',
        'metadata': 'metadata'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, rdf_type_name : 'str' = None, name : 'str' = None, synonyms : List['str'] = None, code : 'str' = None, production_year : 'int' = None, description : 'str' = None, species : 'str' = None, species_name : 'str' = None, variety : 'str' = None, variety_name : 'str' = None, accession : 'str' = None, accession_name : 'str' = None, institute : 'str' = None, website : 'str' = None, metadata : Dict[str, 'str'] = None):  # noqa: E501
        """GermplasmGetSingleDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._synonyms = None
        self._code = None
        self._production_year = None
        self._description = None
        self._species = None
        self._species_name = None
        self._variety = None
        self._variety_name = None
        self._accession = None
        self._accession_name = None
        self._institute = None
        self._website = None
        self._metadata = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if name is not None:
            self.name = name
        if synonyms is not None:
            self.synonyms = synonyms
        if code is not None:
            self.code = code
        if production_year is not None:
            self.production_year = production_year
        if description is not None:
            self.description = description
        if species is not None:
            self.species = species
        if species_name is not None:
            self.species_name = species_name
        if variety is not None:
            self.variety = variety
        if variety_name is not None:
            self.variety_name = variety_name
        if accession is not None:
            self.accession = accession
        if accession_name is not None:
            self.accession_name = accession_name
        if institute is not None:
            self.institute = institute
        if website is not None:
            self.website = website
        if metadata is not None:
            self.metadata = metadata

    @property
    def uri(self):
        """Gets the uri of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The uri of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this GermplasmGetSingleDTO.


        :param uri: The uri of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The rdf_type of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this GermplasmGetSingleDTO.


        :param rdf_type: The rdf_type of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The rdf_type_name of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this GermplasmGetSingleDTO.


        :param rdf_type_name: The rdf_type_name of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The name of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GermplasmGetSingleDTO.


        :param name: The name of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def synonyms(self):
        """Gets the synonyms of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The synonyms of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this GermplasmGetSingleDTO.


        :param synonyms: The synonyms of this GermplasmGetSingleDTO.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def code(self):
        """Gets the code of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The code of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GermplasmGetSingleDTO.


        :param code: The code of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def production_year(self):
        """Gets the production_year of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The production_year of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: int
        """
        return self._production_year

    @production_year.setter
    def production_year(self, production_year):
        """Sets the production_year of this GermplasmGetSingleDTO.


        :param production_year: The production_year of this GermplasmGetSingleDTO.  # noqa: E501
        :type: int
        """

        self._production_year = production_year

    @property
    def description(self):
        """Gets the description of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The description of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GermplasmGetSingleDTO.


        :param description: The description of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def species(self):
        """Gets the species of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The species of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this GermplasmGetSingleDTO.


        :param species: The species of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._species = species

    @property
    def species_name(self):
        """Gets the species_name of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The species_name of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._species_name

    @species_name.setter
    def species_name(self, species_name):
        """Sets the species_name of this GermplasmGetSingleDTO.


        :param species_name: The species_name of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._species_name = species_name

    @property
    def variety(self):
        """Gets the variety of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The variety of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this GermplasmGetSingleDTO.


        :param variety: The variety of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._variety = variety

    @property
    def variety_name(self):
        """Gets the variety_name of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The variety_name of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._variety_name

    @variety_name.setter
    def variety_name(self, variety_name):
        """Sets the variety_name of this GermplasmGetSingleDTO.


        :param variety_name: The variety_name of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._variety_name = variety_name

    @property
    def accession(self):
        """Gets the accession of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The accession of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this GermplasmGetSingleDTO.


        :param accession: The accession of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def accession_name(self):
        """Gets the accession_name of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The accession_name of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._accession_name

    @accession_name.setter
    def accession_name(self, accession_name):
        """Sets the accession_name of this GermplasmGetSingleDTO.


        :param accession_name: The accession_name of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._accession_name = accession_name

    @property
    def institute(self):
        """Gets the institute of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The institute of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._institute

    @institute.setter
    def institute(self, institute):
        """Sets the institute of this GermplasmGetSingleDTO.


        :param institute: The institute of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._institute = institute

    @property
    def website(self):
        """Gets the website of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The website of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GermplasmGetSingleDTO.


        :param website: The website of this GermplasmGetSingleDTO.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def metadata(self):
        """Gets the metadata of this GermplasmGetSingleDTO.  # noqa: E501


        :return: The metadata of this GermplasmGetSingleDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GermplasmGetSingleDTO.


        :param metadata: The metadata of this GermplasmGetSingleDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

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
        if issubclass(GermplasmGetSingleDTO, dict):
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
        if not isinstance(other, GermplasmGetSingleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

