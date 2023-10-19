# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class ExperimentCreationDTO(object):
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
        'name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'description': 'str',
        'objective': 'str',
        'organisations': 'list[str]',
        'facilities': 'list[str]',
        'projects': 'list[str]',
        'scientific_supervisors': 'list[str]',
        'technical_supervisors': 'list[str]',
        'groups': 'list[str]',
        'factors': 'list[str]',
        'is_public': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'description': 'description',
        'objective': 'objective',
        'organisations': 'organisations',
        'facilities': 'facilities',
        'projects': 'projects',
        'scientific_supervisors': 'scientific_supervisors',
        'technical_supervisors': 'technical_supervisors',
        'groups': 'groups',
        'factors': 'factors',
        'is_public': 'is_public'
    }
    def __init__(self,
        name : 'str',
        start_date : 'str',
        objective : 'str',
        uri : 'str' = None,
        end_date : 'str' = None,
        description : 'str' = None,
        organisations : 'List[str]' = None,
        facilities : 'List[str]' = None,
        projects : 'List[str]' = None,
        scientific_supervisors : 'List[str]' = None,
        technical_supervisors : 'List[str]' = None,
        groups : 'List[str]' = None,
        factors : 'List[str]' = None,
        is_public : 'bool' = None):  # noqa: E501
        """ExperimentCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._start_date = None
        self._end_date = None
        self._description = None
        self._objective = None
        self._organisations = None
        self._facilities = None
        self._projects = None
        self._scientific_supervisors = None
        self._technical_supervisors = None
        self._groups = None
        self._factors = None
        self._is_public = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        self.name = name
        self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if description is not None:
            self.description = description
        self.objective = objective
        if organisations is not None:
            self.organisations = organisations
        if facilities is not None:
            self.facilities = facilities
        if projects is not None:
            self.projects = projects
        if scientific_supervisors is not None:
            self.scientific_supervisors = scientific_supervisors
        if technical_supervisors is not None:
            self.technical_supervisors = technical_supervisors
        if groups is not None:
            self.groups = groups
        if factors is not None:
            self.factors = factors
        if is_public is not None:
            self.is_public = is_public

    @property
    def uri(self):
        """Gets the uri of this ExperimentCreationDTO.  # noqa: E501


        :return: The uri of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ExperimentCreationDTO.


        :param uri: The uri of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ExperimentCreationDTO.  # noqa: E501


        :return: The name of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExperimentCreationDTO.


        :param name: The name of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this ExperimentCreationDTO.  # noqa: E501


        :return: The start_date of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ExperimentCreationDTO.


        :param start_date: The start_date of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ExperimentCreationDTO.  # noqa: E501


        :return: The end_date of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ExperimentCreationDTO.


        :param end_date: The end_date of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def description(self):
        """Gets the description of this ExperimentCreationDTO.  # noqa: E501


        :return: The description of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExperimentCreationDTO.


        :param description: The description of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def objective(self):
        """Gets the objective of this ExperimentCreationDTO.  # noqa: E501


        :return: The objective of this ExperimentCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this ExperimentCreationDTO.


        :param objective: The objective of this ExperimentCreationDTO.  # noqa: E501
        :type: str
        """
        if objective is None:
            raise ValueError("Invalid value for `objective`, must not be `None`")  # noqa: E501

        self._objective = objective

    @property
    def organisations(self):
        """Gets the organisations of this ExperimentCreationDTO.  # noqa: E501


        :return: The organisations of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._organisations

    @organisations.setter
    def organisations(self, organisations):
        """Sets the organisations of this ExperimentCreationDTO.


        :param organisations: The organisations of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._organisations = organisations

    @property
    def facilities(self):
        """Gets the facilities of this ExperimentCreationDTO.  # noqa: E501


        :return: The facilities of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this ExperimentCreationDTO.


        :param facilities: The facilities of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._facilities = facilities

    @property
    def projects(self):
        """Gets the projects of this ExperimentCreationDTO.  # noqa: E501


        :return: The projects of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ExperimentCreationDTO.


        :param projects: The projects of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._projects = projects

    @property
    def scientific_supervisors(self):
        """Gets the scientific_supervisors of this ExperimentCreationDTO.  # noqa: E501


        :return: The scientific_supervisors of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._scientific_supervisors

    @scientific_supervisors.setter
    def scientific_supervisors(self, scientific_supervisors):
        """Sets the scientific_supervisors of this ExperimentCreationDTO.


        :param scientific_supervisors: The scientific_supervisors of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._scientific_supervisors = scientific_supervisors

    @property
    def technical_supervisors(self):
        """Gets the technical_supervisors of this ExperimentCreationDTO.  # noqa: E501


        :return: The technical_supervisors of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._technical_supervisors

    @technical_supervisors.setter
    def technical_supervisors(self, technical_supervisors):
        """Sets the technical_supervisors of this ExperimentCreationDTO.


        :param technical_supervisors: The technical_supervisors of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._technical_supervisors = technical_supervisors

    @property
    def groups(self):
        """Gets the groups of this ExperimentCreationDTO.  # noqa: E501


        :return: The groups of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ExperimentCreationDTO.


        :param groups: The groups of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def factors(self):
        """Gets the factors of this ExperimentCreationDTO.  # noqa: E501


        :return: The factors of this ExperimentCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._factors

    @factors.setter
    def factors(self, factors):
        """Sets the factors of this ExperimentCreationDTO.


        :param factors: The factors of this ExperimentCreationDTO.  # noqa: E501
        :type: list[str]
        """

        self._factors = factors

    @property
    def is_public(self):
        """Gets the is_public of this ExperimentCreationDTO.  # noqa: E501


        :return: The is_public of this ExperimentCreationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ExperimentCreationDTO.


        :param is_public: The is_public of this ExperimentCreationDTO.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

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
        if issubclass(ExperimentCreationDTO, dict):
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
        if not isinstance(other, ExperimentCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




