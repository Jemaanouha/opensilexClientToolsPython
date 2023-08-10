# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict

from opensilexClientToolsPython.models.season import Season



class ObservationDTO(object):
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
        'germplasm_db_id': 'str',
        'germplasm_name': 'str',
        'observation_db_id': 'str',
        'observation_level': 'str',
        'observation_time_stamp': 'str',
        'observation_unit_db_id': 'str',
        'observation_unit_name': 'str',
        'observation_variable_db_id': 'str',
        'observation_variable_name': 'str',
        'operator': 'str',
        'season': 'Season',
        'study_db_id': 'str',
        'uploaded_by': 'str',
        'value': 'str'
    }

    attribute_map = {
        'germplasm_db_id': 'germplasmDbId',
        'germplasm_name': 'germplasmName',
        'observation_db_id': 'observationDbId',
        'observation_level': 'observationLevel',
        'observation_time_stamp': 'observationTimeStamp',
        'observation_unit_db_id': 'observationUnitDbId',
        'observation_unit_name': 'observationUnitName',
        'observation_variable_db_id': 'observationVariableDbId',
        'observation_variable_name': 'observationVariableName',
        'operator': 'operator',
        'season': 'season',
        'study_db_id': 'studyDbId',
        'uploaded_by': 'uploadedBy',
        'value': 'value'
    }
    def __init__(self,
        germplasm_db_id : 'str' = None,
        germplasm_name : 'str' = None,
        observation_db_id : 'str' = None,
        observation_level : 'str' = None,
        observation_time_stamp : 'str' = None,
        observation_unit_db_id : 'str' = None,
        observation_unit_name : 'str' = None,
        observation_variable_db_id : 'str' = None,
        observation_variable_name : 'str' = None,
        operator : 'str' = None,
        season : 'Season' = None,
        study_db_id : 'str' = None,
        uploaded_by : 'str' = None,
        value : 'str' = None):  # noqa: E501
        """ObservationDTO - a model defined in Swagger"""  # noqa: E501

        self._germplasm_db_id = None
        self._germplasm_name = None
        self._observation_db_id = None
        self._observation_level = None
        self._observation_time_stamp = None
        self._observation_unit_db_id = None
        self._observation_unit_name = None
        self._observation_variable_db_id = None
        self._observation_variable_name = None
        self._operator = None
        self._season = None
        self._study_db_id = None
        self._uploaded_by = None
        self._value = None
        self.discriminator = None

        if germplasm_db_id is not None:
            self.germplasm_db_id = germplasm_db_id
        if germplasm_name is not None:
            self.germplasm_name = germplasm_name
        if observation_db_id is not None:
            self.observation_db_id = observation_db_id
        if observation_level is not None:
            self.observation_level = observation_level
        if observation_time_stamp is not None:
            self.observation_time_stamp = observation_time_stamp
        if observation_unit_db_id is not None:
            self.observation_unit_db_id = observation_unit_db_id
        if observation_unit_name is not None:
            self.observation_unit_name = observation_unit_name
        if observation_variable_db_id is not None:
            self.observation_variable_db_id = observation_variable_db_id
        if observation_variable_name is not None:
            self.observation_variable_name = observation_variable_name
        if operator is not None:
            self.operator = operator
        if season is not None:
            self.season = season
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if uploaded_by is not None:
            self.uploaded_by = uploaded_by
        if value is not None:
            self.value = value

    @property
    def germplasm_db_id(self):
        """Gets the germplasm_db_id of this ObservationDTO.  # noqa: E501


        :return: The germplasm_db_id of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id):
        """Sets the germplasm_db_id of this ObservationDTO.


        :param germplasm_db_id: The germplasm_db_id of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self):
        """Gets the germplasm_name of this ObservationDTO.  # noqa: E501


        :return: The germplasm_name of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name):
        """Sets the germplasm_name of this ObservationDTO.


        :param germplasm_name: The germplasm_name of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_name = germplasm_name

    @property
    def observation_db_id(self):
        """Gets the observation_db_id of this ObservationDTO.  # noqa: E501


        :return: The observation_db_id of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_db_id

    @observation_db_id.setter
    def observation_db_id(self, observation_db_id):
        """Sets the observation_db_id of this ObservationDTO.


        :param observation_db_id: The observation_db_id of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_db_id = observation_db_id

    @property
    def observation_level(self):
        """Gets the observation_level of this ObservationDTO.  # noqa: E501


        :return: The observation_level of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_level

    @observation_level.setter
    def observation_level(self, observation_level):
        """Sets the observation_level of this ObservationDTO.


        :param observation_level: The observation_level of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_level = observation_level

    @property
    def observation_time_stamp(self):
        """Gets the observation_time_stamp of this ObservationDTO.  # noqa: E501


        :return: The observation_time_stamp of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_time_stamp

    @observation_time_stamp.setter
    def observation_time_stamp(self, observation_time_stamp):
        """Sets the observation_time_stamp of this ObservationDTO.


        :param observation_time_stamp: The observation_time_stamp of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_time_stamp = observation_time_stamp

    @property
    def observation_unit_db_id(self):
        """Gets the observation_unit_db_id of this ObservationDTO.  # noqa: E501


        :return: The observation_unit_db_id of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id):
        """Sets the observation_unit_db_id of this ObservationDTO.


        :param observation_unit_db_id: The observation_unit_db_id of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def observation_unit_name(self):
        """Gets the observation_unit_name of this ObservationDTO.  # noqa: E501


        :return: The observation_unit_name of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_unit_name

    @observation_unit_name.setter
    def observation_unit_name(self, observation_unit_name):
        """Sets the observation_unit_name of this ObservationDTO.


        :param observation_unit_name: The observation_unit_name of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_unit_name = observation_unit_name

    @property
    def observation_variable_db_id(self):
        """Gets the observation_variable_db_id of this ObservationDTO.  # noqa: E501


        :return: The observation_variable_db_id of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_db_id

    @observation_variable_db_id.setter
    def observation_variable_db_id(self, observation_variable_db_id):
        """Sets the observation_variable_db_id of this ObservationDTO.


        :param observation_variable_db_id: The observation_variable_db_id of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_variable_db_id = observation_variable_db_id

    @property
    def observation_variable_name(self):
        """Gets the observation_variable_name of this ObservationDTO.  # noqa: E501


        :return: The observation_variable_name of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_variable_name

    @observation_variable_name.setter
    def observation_variable_name(self, observation_variable_name):
        """Sets the observation_variable_name of this ObservationDTO.


        :param observation_variable_name: The observation_variable_name of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._observation_variable_name = observation_variable_name

    @property
    def operator(self):
        """Gets the operator of this ObservationDTO.  # noqa: E501


        :return: The operator of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ObservationDTO.


        :param operator: The operator of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def season(self):
        """Gets the season of this ObservationDTO.  # noqa: E501


        :return: The season of this ObservationDTO.  # noqa: E501
        :rtype: Season
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this ObservationDTO.


        :param season: The season of this ObservationDTO.  # noqa: E501
        :type: Season
        """

        self._season = season

    @property
    def study_db_id(self):
        """Gets the study_db_id of this ObservationDTO.  # noqa: E501


        :return: The study_db_id of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this ObservationDTO.


        :param study_db_id: The study_db_id of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def uploaded_by(self):
        """Gets the uploaded_by of this ObservationDTO.  # noqa: E501


        :return: The uploaded_by of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        """Sets the uploaded_by of this ObservationDTO.


        :param uploaded_by: The uploaded_by of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._uploaded_by = uploaded_by

    @property
    def value(self):
        """Gets the value of this ObservationDTO.  # noqa: E501


        :return: The value of this ObservationDTO.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ObservationDTO.


        :param value: The value of this ObservationDTO.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(ObservationDTO, dict):
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
        if not isinstance(other, ObservationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

