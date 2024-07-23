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


class Faidarev1ObservationVariableDTO(object):
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
        'context_of_use': 'list[str]',
        'crop': 'str',
        'default_value': 'str',
        'documentation_url': 'str',
        'growth_stage': 'str',
        'institution': 'str',
        'language': 'str',
        'method': 'Faidarev1MethodDTO',
        'scale': 'Faidarev1ScaleDTO',
        'scientist': 'str',
        'status': 'str',
        'synonyms': 'list[str]',
        'trait': 'Faidarev1TraitDTO',
        'xref': 'str',
        'observation_variable_db_id': 'str',
        'name': 'str',
        '_date': 'str',
        'ontology_db_id': 'str',
        'ontology_name': 'str'
    }

    attribute_map = {
        'context_of_use': 'contextOfUse',
        'crop': 'crop',
        'default_value': 'defaultValue',
        'documentation_url': 'documentationURL',
        'growth_stage': 'growthStage',
        'institution': 'institution',
        'language': 'language',
        'method': 'method',
        'scale': 'scale',
        'scientist': 'scientist',
        'status': 'status',
        'synonyms': 'synonyms',
        'trait': 'trait',
        'xref': 'xref',
        'observation_variable_db_id': 'observationVariableDbId',
        'name': 'name',
        '_date': 'date',
        'ontology_db_id': 'ontologyDbId',
        'ontology_name': 'ontologyName'
    }
    def __init__(self,
        context_of_use : 'List[str]' = None,
        crop : 'str' = None,
        default_value : 'str' = None,
        documentation_url : 'str' = None,
        growth_stage : 'str' = None,
        institution : 'str' = None,
        language : 'str' = None,
        method : 'Faidarev1MethodDTO' = None,
        scale : 'Faidarev1ScaleDTO' = None,
        scientist : 'str' = None,
        status : 'str' = None,
        synonyms : 'List[str]' = None,
        trait : 'Faidarev1TraitDTO' = None,
        xref : 'str' = None,
        observation_variable_db_id : 'str' = None,
        name : 'str' = None,
        _date : 'str' = None,
        ontology_db_id : 'str' = None,
        ontology_name : 'str' = None):  # noqa: E501
        """Faidarev1ObservationVariableDTO - a model defined in Swagger"""  # noqa: E501

        self._context_of_use = None
        self._crop = None
        self._default_value = None
        self._documentation_url = None
        self._growth_stage = None
        self._institution = None
        self._language = None
        self._method = None
        self._scale = None
        self._scientist = None
        self._status = None
        self._synonyms = None
        self._trait = None
        self._xref = None
        self._observation_variable_db_id = None
        self._name = None
        self.__date = None
        self._ontology_db_id = None
        self._ontology_name = None
        self.discriminator = None

        if context_of_use is not None:
            self.context_of_use = context_of_use
        if crop is not None:
            self.crop = crop
        if default_value is not None:
            self.default_value = default_value
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if growth_stage is not None:
            self.growth_stage = growth_stage
        if institution is not None:
            self.institution = institution
        if language is not None:
            self.language = language
        if method is not None:
            self.method = method
        if scale is not None:
            self.scale = scale
        if scientist is not None:
            self.scientist = scientist
        if status is not None:
            self.status = status
        if synonyms is not None:
            self.synonyms = synonyms
        if trait is not None:
            self.trait = trait
        if xref is not None:
            self.xref = xref
        if observation_variable_db_id is not None:
            self.observation_variable_db_id = observation_variable_db_id
        if name is not None:
            self.name = name
        if _date is not None:
            self._date = _date
        if ontology_db_id is not None:
            self.ontology_db_id = ontology_db_id
        if ontology_name is not None:
            self.ontology_name = ontology_name

    @property
    def context_of_use(self):
        """Gets the context_of_use of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The context_of_use of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_of_use

    @context_of_use.setter
    def context_of_use(self, context_of_use):
        """Sets the context_of_use of this Faidarev1ObservationVariableDTO.


        :param context_of_use: The context_of_use of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: list[str]
        """

        self._context_of_use = context_of_use

    @property
    def crop(self):
        """Gets the crop of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The crop of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        """Sets the crop of this Faidarev1ObservationVariableDTO.


        :param crop: The crop of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._crop = crop

    @property
    def default_value(self):
        """Gets the default_value of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The default_value of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Faidarev1ObservationVariableDTO.


        :param default_value: The default_value of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def documentation_url(self):
        """Gets the documentation_url of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The documentation_url of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this Faidarev1ObservationVariableDTO.


        :param documentation_url: The documentation_url of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def growth_stage(self):
        """Gets the growth_stage of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The growth_stage of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._growth_stage

    @growth_stage.setter
    def growth_stage(self, growth_stage):
        """Sets the growth_stage of this Faidarev1ObservationVariableDTO.


        :param growth_stage: The growth_stage of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._growth_stage = growth_stage

    @property
    def institution(self):
        """Gets the institution of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The institution of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this Faidarev1ObservationVariableDTO.


        :param institution: The institution of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._institution = institution

    @property
    def language(self):
        """Gets the language of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The language of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Faidarev1ObservationVariableDTO.


        :param language: The language of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def method(self):
        """Gets the method of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The method of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: Faidarev1MethodDTO
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Faidarev1ObservationVariableDTO.


        :param method: The method of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: Faidarev1MethodDTO
        """

        self._method = method

    @property
    def scale(self):
        """Gets the scale of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The scale of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: Faidarev1ScaleDTO
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Faidarev1ObservationVariableDTO.


        :param scale: The scale of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: Faidarev1ScaleDTO
        """

        self._scale = scale

    @property
    def scientist(self):
        """Gets the scientist of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The scientist of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._scientist

    @scientist.setter
    def scientist(self, scientist):
        """Sets the scientist of this Faidarev1ObservationVariableDTO.


        :param scientist: The scientist of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._scientist = scientist

    @property
    def status(self):
        """Gets the status of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The status of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Faidarev1ObservationVariableDTO.


        :param status: The status of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def synonyms(self):
        """Gets the synonyms of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The synonyms of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this Faidarev1ObservationVariableDTO.


        :param synonyms: The synonyms of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def trait(self):
        """Gets the trait of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The trait of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: Faidarev1TraitDTO
        """
        return self._trait

    @trait.setter
    def trait(self, trait):
        """Sets the trait of this Faidarev1ObservationVariableDTO.


        :param trait: The trait of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: Faidarev1TraitDTO
        """

        self._trait = trait

    @property
    def xref(self):
        """Gets the xref of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The xref of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._xref

    @xref.setter
    def xref(self, xref):
        """Sets the xref of this Faidarev1ObservationVariableDTO.


        :param xref: The xref of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._xref = xref

    @property
    def observation_variable_db_id(self):
        """Gets the observation_variable_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The observation_variable_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_db_id

    @observation_variable_db_id.setter
    def observation_variable_db_id(self, observation_variable_db_id):
        """Sets the observation_variable_db_id of this Faidarev1ObservationVariableDTO.


        :param observation_variable_db_id: The observation_variable_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._observation_variable_db_id = observation_variable_db_id

    @property
    def name(self):
        """Gets the name of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The name of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Faidarev1ObservationVariableDTO.


        :param name: The name of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _date(self):
        """Gets the _date of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The _date of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Faidarev1ObservationVariableDTO.


        :param _date: The _date of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def ontology_db_id(self):
        """Gets the ontology_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The ontology_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._ontology_db_id

    @ontology_db_id.setter
    def ontology_db_id(self, ontology_db_id):
        """Sets the ontology_db_id of this Faidarev1ObservationVariableDTO.


        :param ontology_db_id: The ontology_db_id of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._ontology_db_id = ontology_db_id

    @property
    def ontology_name(self):
        """Gets the ontology_name of this Faidarev1ObservationVariableDTO.  # noqa: E501


        :return: The ontology_name of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :rtype: str
        """
        return self._ontology_name

    @ontology_name.setter
    def ontology_name(self, ontology_name):
        """Sets the ontology_name of this Faidarev1ObservationVariableDTO.


        :param ontology_name: The ontology_name of this Faidarev1ObservationVariableDTO.  # noqa: E501
        :type: str
        """

        self._ontology_name = ontology_name

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
        if issubclass(Faidarev1ObservationVariableDTO, dict):
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
        if issubclass(Faidarev1ObservationVariableDTO, dict):
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
        if not isinstance(other, Faidarev1ObservationVariableDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.faidarev1_method_dto import Faidarev1MethodDTO
from opensilexClientToolsPython.models.faidarev1_scale_dto import Faidarev1ScaleDTO
from opensilexClientToolsPython.models.faidarev1_trait_dto import Faidarev1TraitDTO


