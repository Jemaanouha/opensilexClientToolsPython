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


class Trait(object):
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
        'alternative_abbreviations': 'list[str]',
        'attribute': 'str',
        'description': 'str',
        'entity': 'str',
        'main_abbreviation': 'str',
        'name': 'str',
        'ontology_reference': 'OntologyReference',
        'status': 'str',
        'synonyms': 'list[str]',
        'trait_db_id': 'str',
        'trait_name': 'str',
        'xref': 'str',
        '_class': 'str'
    }

    attribute_map = {
        'alternative_abbreviations': 'alternativeAbbreviations',
        'attribute': 'attribute',
        'description': 'description',
        'entity': 'entity',
        'main_abbreviation': 'mainAbbreviation',
        'name': 'name',
        'ontology_reference': 'ontologyReference',
        'status': 'status',
        'synonyms': 'synonyms',
        'trait_db_id': 'traitDbId',
        'trait_name': 'traitName',
        'xref': 'xref',
        '_class': 'class'
    }

    def __init__(self, alternative_abbreviations=None, attribute=None, description=None, entity=None, main_abbreviation=None, name=None, ontology_reference=None, status=None, synonyms=None, trait_db_id=None, trait_name=None, xref=None, _class=None):  # noqa: E501
        """Trait - a model defined in Swagger"""  # noqa: E501

        self._alternative_abbreviations = None
        self._attribute = None
        self._description = None
        self._entity = None
        self._main_abbreviation = None
        self._name = None
        self._ontology_reference = None
        self._status = None
        self._synonyms = None
        self._trait_db_id = None
        self._trait_name = None
        self._xref = None
        self.__class = None
        self.discriminator = None

        if alternative_abbreviations is not None:
            self.alternative_abbreviations = alternative_abbreviations
        if attribute is not None:
            self.attribute = attribute
        if description is not None:
            self.description = description
        if entity is not None:
            self.entity = entity
        if main_abbreviation is not None:
            self.main_abbreviation = main_abbreviation
        if name is not None:
            self.name = name
        if ontology_reference is not None:
            self.ontology_reference = ontology_reference
        if status is not None:
            self.status = status
        if synonyms is not None:
            self.synonyms = synonyms
        if trait_db_id is not None:
            self.trait_db_id = trait_db_id
        if trait_name is not None:
            self.trait_name = trait_name
        if xref is not None:
            self.xref = xref
        if _class is not None:
            self._class = _class

    @property
    def alternative_abbreviations(self):
        """Gets the alternative_abbreviations of this Trait.  # noqa: E501


        :return: The alternative_abbreviations of this Trait.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternative_abbreviations

    @alternative_abbreviations.setter
    def alternative_abbreviations(self, alternative_abbreviations):
        """Sets the alternative_abbreviations of this Trait.


        :param alternative_abbreviations: The alternative_abbreviations of this Trait.  # noqa: E501
        :type: list[str]
        """

        self._alternative_abbreviations = alternative_abbreviations

    @property
    def attribute(self):
        """Gets the attribute of this Trait.  # noqa: E501


        :return: The attribute of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Trait.


        :param attribute: The attribute of this Trait.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def description(self):
        """Gets the description of this Trait.  # noqa: E501


        :return: The description of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Trait.


        :param description: The description of this Trait.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity(self):
        """Gets the entity of this Trait.  # noqa: E501


        :return: The entity of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Trait.


        :param entity: The entity of this Trait.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def main_abbreviation(self):
        """Gets the main_abbreviation of this Trait.  # noqa: E501


        :return: The main_abbreviation of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._main_abbreviation

    @main_abbreviation.setter
    def main_abbreviation(self, main_abbreviation):
        """Sets the main_abbreviation of this Trait.


        :param main_abbreviation: The main_abbreviation of this Trait.  # noqa: E501
        :type: str
        """

        self._main_abbreviation = main_abbreviation

    @property
    def name(self):
        """Gets the name of this Trait.  # noqa: E501


        :return: The name of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Trait.


        :param name: The name of this Trait.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ontology_reference(self):
        """Gets the ontology_reference of this Trait.  # noqa: E501


        :return: The ontology_reference of this Trait.  # noqa: E501
        :rtype: OntologyReference
        """
        return self._ontology_reference

    @ontology_reference.setter
    def ontology_reference(self, ontology_reference):
        """Sets the ontology_reference of this Trait.


        :param ontology_reference: The ontology_reference of this Trait.  # noqa: E501
        :type: OntologyReference
        """

        self._ontology_reference = ontology_reference

    @property
    def status(self):
        """Gets the status of this Trait.  # noqa: E501


        :return: The status of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Trait.


        :param status: The status of this Trait.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def synonyms(self):
        """Gets the synonyms of this Trait.  # noqa: E501


        :return: The synonyms of this Trait.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this Trait.


        :param synonyms: The synonyms of this Trait.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def trait_db_id(self):
        """Gets the trait_db_id of this Trait.  # noqa: E501


        :return: The trait_db_id of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._trait_db_id

    @trait_db_id.setter
    def trait_db_id(self, trait_db_id):
        """Sets the trait_db_id of this Trait.


        :param trait_db_id: The trait_db_id of this Trait.  # noqa: E501
        :type: str
        """

        self._trait_db_id = trait_db_id

    @property
    def trait_name(self):
        """Gets the trait_name of this Trait.  # noqa: E501


        :return: The trait_name of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._trait_name

    @trait_name.setter
    def trait_name(self, trait_name):
        """Sets the trait_name of this Trait.


        :param trait_name: The trait_name of this Trait.  # noqa: E501
        :type: str
        """

        self._trait_name = trait_name

    @property
    def xref(self):
        """Gets the xref of this Trait.  # noqa: E501


        :return: The xref of this Trait.  # noqa: E501
        :rtype: str
        """
        return self._xref

    @xref.setter
    def xref(self, xref):
        """Sets the xref of this Trait.


        :param xref: The xref of this Trait.  # noqa: E501
        :type: str
        """

        self._xref = xref

    @property
    def _class(self):
        """Gets the _class of this Trait.  # noqa: E501


        :return: The _class of this Trait.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Trait.


        :param _class: The _class of this Trait.  # noqa: E501
        :type: str
        """

        self.__class = _class

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
        if issubclass(Trait, dict):
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
        if not isinstance(other, Trait):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
