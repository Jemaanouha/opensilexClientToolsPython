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

from opensilexClientToolsPython.models.observation_unit_xref import ObservationUnitXref
from opensilexClientToolsPython.models.observation_summary import ObservationSummary
from opensilexClientToolsPython.models.observation_treatment import ObservationTreatment



class ObservationUnitDTO(object):
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
        'block_number': 'str',
        'entry_number': 'str',
        'entry_type': 'str',
        'germplasm_db_id': 'str',
        'germplasm_name': 'str',
        'observation_level': 'str',
        'observation_levels': 'str',
        'observation_unit_db_id': 'str',
        'observation_unit_xref': 'list[ObservationUnitXref]',
        'observations': 'list[ObservationSummary]',
        'plant_number': 'str',
        'plot_number': 'str',
        'position_coordinate_x': 'str',
        'position_coordinate_x_type': 'str',
        'position_coordinate_y': 'str',
        'position_coordinate_y_type': 'str',
        'program_name': 'str',
        'replicate': 'str',
        'study_db_id': 'str',
        'study_location': 'str',
        'study_location_db_id': 'str',
        'study_name': 'str',
        'treatments': 'list[ObservationTreatment]'
    }

    attribute_map = {
        'block_number': 'blockNumber',
        'entry_number': 'entryNumber',
        'entry_type': 'entryType',
        'germplasm_db_id': 'germplasmDbId',
        'germplasm_name': 'germplasmName',
        'observation_level': 'observationLevel',
        'observation_levels': 'observationLevels',
        'observation_unit_db_id': 'observationUnitDbId',
        'observation_unit_xref': 'observationUnitXref',
        'observations': 'observations',
        'plant_number': 'plantNumber',
        'plot_number': 'plotNumber',
        'position_coordinate_x': 'positionCoordinateX',
        'position_coordinate_x_type': 'positionCoordinateXType',
        'position_coordinate_y': 'positionCoordinateY',
        'position_coordinate_y_type': 'positionCoordinateYType',
        'program_name': 'programName',
        'replicate': 'replicate',
        'study_db_id': 'studyDbId',
        'study_location': 'studyLocation',
        'study_location_db_id': 'studyLocationDbId',
        'study_name': 'studyName',
        'treatments': 'treatments'
    }
    def __init__(self, block_number : 'str' = None, entry_number : 'str' = None, entry_type : 'str' = None, germplasm_db_id : 'str' = None, germplasm_name : 'str' = None, observation_level : 'str' = None, observation_levels : 'str' = None, observation_unit_db_id : 'str' = None, observation_unit_xref : List['ObservationUnitXref'] = None, observations : List['ObservationSummary'] = None, plant_number : 'str' = None, plot_number : 'str' = None, position_coordinate_x : 'str' = None, position_coordinate_x_type : 'str' = None, position_coordinate_y : 'str' = None, position_coordinate_y_type : 'str' = None, program_name : 'str' = None, replicate : 'str' = None, study_db_id : 'str' = None, study_location : 'str' = None, study_location_db_id : 'str' = None, study_name : 'str' = None, treatments : List['ObservationTreatment'] = None):  # noqa: E501
        """ObservationUnitDTO - a model defined in Swagger"""  # noqa: E501

        self._block_number = None
        self._entry_number = None
        self._entry_type = None
        self._germplasm_db_id = None
        self._germplasm_name = None
        self._observation_level = None
        self._observation_levels = None
        self._observation_unit_db_id = None
        self._observation_unit_xref = None
        self._observations = None
        self._plant_number = None
        self._plot_number = None
        self._position_coordinate_x = None
        self._position_coordinate_x_type = None
        self._position_coordinate_y = None
        self._position_coordinate_y_type = None
        self._program_name = None
        self._replicate = None
        self._study_db_id = None
        self._study_location = None
        self._study_location_db_id = None
        self._study_name = None
        self._treatments = None
        self.discriminator = None

        if block_number is not None:
            self.block_number = block_number
        if entry_number is not None:
            self.entry_number = entry_number
        if entry_type is not None:
            self.entry_type = entry_type
        if germplasm_db_id is not None:
            self.germplasm_db_id = germplasm_db_id
        if germplasm_name is not None:
            self.germplasm_name = germplasm_name
        if observation_level is not None:
            self.observation_level = observation_level
        if observation_levels is not None:
            self.observation_levels = observation_levels
        if observation_unit_db_id is not None:
            self.observation_unit_db_id = observation_unit_db_id
        if observation_unit_xref is not None:
            self.observation_unit_xref = observation_unit_xref
        if observations is not None:
            self.observations = observations
        if plant_number is not None:
            self.plant_number = plant_number
        if plot_number is not None:
            self.plot_number = plot_number
        if position_coordinate_x is not None:
            self.position_coordinate_x = position_coordinate_x
        if position_coordinate_x_type is not None:
            self.position_coordinate_x_type = position_coordinate_x_type
        if position_coordinate_y is not None:
            self.position_coordinate_y = position_coordinate_y
        if position_coordinate_y_type is not None:
            self.position_coordinate_y_type = position_coordinate_y_type
        if program_name is not None:
            self.program_name = program_name
        if replicate is not None:
            self.replicate = replicate
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if study_location is not None:
            self.study_location = study_location
        if study_location_db_id is not None:
            self.study_location_db_id = study_location_db_id
        if study_name is not None:
            self.study_name = study_name
        if treatments is not None:
            self.treatments = treatments

    @property
    def block_number(self):
        """Gets the block_number of this ObservationUnitDTO.  # noqa: E501


        :return: The block_number of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number):
        """Sets the block_number of this ObservationUnitDTO.


        :param block_number: The block_number of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._block_number = block_number

    @property
    def entry_number(self):
        """Gets the entry_number of this ObservationUnitDTO.  # noqa: E501


        :return: The entry_number of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._entry_number

    @entry_number.setter
    def entry_number(self, entry_number):
        """Sets the entry_number of this ObservationUnitDTO.


        :param entry_number: The entry_number of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._entry_number = entry_number

    @property
    def entry_type(self):
        """Gets the entry_type of this ObservationUnitDTO.  # noqa: E501


        :return: The entry_type of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this ObservationUnitDTO.


        :param entry_type: The entry_type of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._entry_type = entry_type

    @property
    def germplasm_db_id(self):
        """Gets the germplasm_db_id of this ObservationUnitDTO.  # noqa: E501


        :return: The germplasm_db_id of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id):
        """Sets the germplasm_db_id of this ObservationUnitDTO.


        :param germplasm_db_id: The germplasm_db_id of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self):
        """Gets the germplasm_name of this ObservationUnitDTO.  # noqa: E501


        :return: The germplasm_name of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name):
        """Sets the germplasm_name of this ObservationUnitDTO.


        :param germplasm_name: The germplasm_name of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_name = germplasm_name

    @property
    def observation_level(self):
        """Gets the observation_level of this ObservationUnitDTO.  # noqa: E501


        :return: The observation_level of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_level

    @observation_level.setter
    def observation_level(self, observation_level):
        """Sets the observation_level of this ObservationUnitDTO.


        :param observation_level: The observation_level of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._observation_level = observation_level

    @property
    def observation_levels(self):
        """Gets the observation_levels of this ObservationUnitDTO.  # noqa: E501


        :return: The observation_levels of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_levels

    @observation_levels.setter
    def observation_levels(self, observation_levels):
        """Sets the observation_levels of this ObservationUnitDTO.


        :param observation_levels: The observation_levels of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._observation_levels = observation_levels

    @property
    def observation_unit_db_id(self):
        """Gets the observation_unit_db_id of this ObservationUnitDTO.  # noqa: E501


        :return: The observation_unit_db_id of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id):
        """Sets the observation_unit_db_id of this ObservationUnitDTO.


        :param observation_unit_db_id: The observation_unit_db_id of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def observation_unit_xref(self):
        """Gets the observation_unit_xref of this ObservationUnitDTO.  # noqa: E501


        :return: The observation_unit_xref of this ObservationUnitDTO.  # noqa: E501
        :rtype: list[ObservationUnitXref]
        """
        return self._observation_unit_xref

    @observation_unit_xref.setter
    def observation_unit_xref(self, observation_unit_xref):
        """Sets the observation_unit_xref of this ObservationUnitDTO.


        :param observation_unit_xref: The observation_unit_xref of this ObservationUnitDTO.  # noqa: E501
        :type: list[ObservationUnitXref]
        """

        self._observation_unit_xref = observation_unit_xref

    @property
    def observations(self):
        """Gets the observations of this ObservationUnitDTO.  # noqa: E501


        :return: The observations of this ObservationUnitDTO.  # noqa: E501
        :rtype: list[ObservationSummary]
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        """Sets the observations of this ObservationUnitDTO.


        :param observations: The observations of this ObservationUnitDTO.  # noqa: E501
        :type: list[ObservationSummary]
        """

        self._observations = observations

    @property
    def plant_number(self):
        """Gets the plant_number of this ObservationUnitDTO.  # noqa: E501


        :return: The plant_number of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._plant_number

    @plant_number.setter
    def plant_number(self, plant_number):
        """Sets the plant_number of this ObservationUnitDTO.


        :param plant_number: The plant_number of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._plant_number = plant_number

    @property
    def plot_number(self):
        """Gets the plot_number of this ObservationUnitDTO.  # noqa: E501


        :return: The plot_number of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._plot_number

    @plot_number.setter
    def plot_number(self, plot_number):
        """Sets the plot_number of this ObservationUnitDTO.


        :param plot_number: The plot_number of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._plot_number = plot_number

    @property
    def position_coordinate_x(self):
        """Gets the position_coordinate_x of this ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_x of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_x

    @position_coordinate_x.setter
    def position_coordinate_x(self, position_coordinate_x):
        """Sets the position_coordinate_x of this ObservationUnitDTO.


        :param position_coordinate_x: The position_coordinate_x of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_x = position_coordinate_x

    @property
    def position_coordinate_x_type(self):
        """Gets the position_coordinate_x_type of this ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_x_type of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_x_type

    @position_coordinate_x_type.setter
    def position_coordinate_x_type(self, position_coordinate_x_type):
        """Sets the position_coordinate_x_type of this ObservationUnitDTO.


        :param position_coordinate_x_type: The position_coordinate_x_type of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_x_type = position_coordinate_x_type

    @property
    def position_coordinate_y(self):
        """Gets the position_coordinate_y of this ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_y of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_y

    @position_coordinate_y.setter
    def position_coordinate_y(self, position_coordinate_y):
        """Sets the position_coordinate_y of this ObservationUnitDTO.


        :param position_coordinate_y: The position_coordinate_y of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_y = position_coordinate_y

    @property
    def position_coordinate_y_type(self):
        """Gets the position_coordinate_y_type of this ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_y_type of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_y_type

    @position_coordinate_y_type.setter
    def position_coordinate_y_type(self, position_coordinate_y_type):
        """Sets the position_coordinate_y_type of this ObservationUnitDTO.


        :param position_coordinate_y_type: The position_coordinate_y_type of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_y_type = position_coordinate_y_type

    @property
    def program_name(self):
        """Gets the program_name of this ObservationUnitDTO.  # noqa: E501


        :return: The program_name of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this ObservationUnitDTO.


        :param program_name: The program_name of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

    @property
    def replicate(self):
        """Gets the replicate of this ObservationUnitDTO.  # noqa: E501


        :return: The replicate of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._replicate

    @replicate.setter
    def replicate(self, replicate):
        """Sets the replicate of this ObservationUnitDTO.


        :param replicate: The replicate of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._replicate = replicate

    @property
    def study_db_id(self):
        """Gets the study_db_id of this ObservationUnitDTO.  # noqa: E501


        :return: The study_db_id of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this ObservationUnitDTO.


        :param study_db_id: The study_db_id of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def study_location(self):
        """Gets the study_location of this ObservationUnitDTO.  # noqa: E501


        :return: The study_location of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_location

    @study_location.setter
    def study_location(self, study_location):
        """Sets the study_location of this ObservationUnitDTO.


        :param study_location: The study_location of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_location = study_location

    @property
    def study_location_db_id(self):
        """Gets the study_location_db_id of this ObservationUnitDTO.  # noqa: E501


        :return: The study_location_db_id of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_location_db_id

    @study_location_db_id.setter
    def study_location_db_id(self, study_location_db_id):
        """Sets the study_location_db_id of this ObservationUnitDTO.


        :param study_location_db_id: The study_location_db_id of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_location_db_id = study_location_db_id

    @property
    def study_name(self):
        """Gets the study_name of this ObservationUnitDTO.  # noqa: E501


        :return: The study_name of this ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_name

    @study_name.setter
    def study_name(self, study_name):
        """Sets the study_name of this ObservationUnitDTO.


        :param study_name: The study_name of this ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_name = study_name

    @property
    def treatments(self):
        """Gets the treatments of this ObservationUnitDTO.  # noqa: E501


        :return: The treatments of this ObservationUnitDTO.  # noqa: E501
        :rtype: list[ObservationTreatment]
        """
        return self._treatments

    @treatments.setter
    def treatments(self, treatments):
        """Sets the treatments of this ObservationUnitDTO.


        :param treatments: The treatments of this ObservationUnitDTO.  # noqa: E501
        :type: list[ObservationTreatment]
        """

        self._treatments = treatments

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
        if issubclass(ObservationUnitDTO, dict):
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
        if not isinstance(other, ObservationUnitDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

