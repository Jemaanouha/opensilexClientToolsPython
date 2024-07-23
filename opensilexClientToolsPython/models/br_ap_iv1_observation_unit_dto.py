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


class BrAPIv1ObservationUnitDTO(object):
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
        'location_db_id': 'str',
        'location_name': 'str',
        'observation_level': 'str',
        'observation_unit_db_id': 'str',
        'observation_unit_xref': 'list[BrAPIv1ObservationUnitXrefDTO]',
        'observations': 'list[BrAPIv1ObservationSummaryDTO]',
        'pedigree': 'str',
        'plant_number': 'str',
        'plot_number': 'str',
        'position_coordinate_x': 'str',
        'position_coordinate_x_type': 'str',
        'position_coordinate_y': 'str',
        'position_coordinate_y_type': 'str',
        'program_db_id': 'str',
        'program_name': 'str',
        'replicate': 'str',
        'study_db_id': 'str',
        'study_name': 'str',
        'treatments': 'list[BrAPIv1ObservationUnitTreatmentDTO]',
        'trial_db_id': 'str',
        'trial_name': 'str'
    }

    attribute_map = {
        'block_number': 'blockNumber',
        'entry_number': 'entryNumber',
        'entry_type': 'entryType',
        'germplasm_db_id': 'germplasmDbId',
        'germplasm_name': 'germplasmName',
        'location_db_id': 'locationDbId',
        'location_name': 'locationName',
        'observation_level': 'observationLevel',
        'observation_unit_db_id': 'observationUnitDbId',
        'observation_unit_xref': 'observationUnitXref',
        'observations': 'observations',
        'pedigree': 'pedigree',
        'plant_number': 'plantNumber',
        'plot_number': 'plotNumber',
        'position_coordinate_x': 'positionCoordinateX',
        'position_coordinate_x_type': 'positionCoordinateXType',
        'position_coordinate_y': 'positionCoordinateY',
        'position_coordinate_y_type': 'positionCoordinateYType',
        'program_db_id': 'programDbId',
        'program_name': 'programName',
        'replicate': 'replicate',
        'study_db_id': 'studyDbId',
        'study_name': 'studyName',
        'treatments': 'treatments',
        'trial_db_id': 'trialDbId',
        'trial_name': 'trialName'
    }
    def __init__(self,
        block_number : 'str' = None,
        entry_number : 'str' = None,
        entry_type : 'str' = None,
        germplasm_db_id : 'str' = None,
        germplasm_name : 'str' = None,
        location_db_id : 'str' = None,
        location_name : 'str' = None,
        observation_level : 'str' = None,
        observation_unit_db_id : 'str' = None,
        observation_unit_xref : 'List[BrAPIv1ObservationUnitXrefDTO]' = None,
        observations : 'List[BrAPIv1ObservationSummaryDTO]' = None,
        pedigree : 'str' = None,
        plant_number : 'str' = None,
        plot_number : 'str' = None,
        position_coordinate_x : 'str' = None,
        position_coordinate_x_type : 'str' = None,
        position_coordinate_y : 'str' = None,
        position_coordinate_y_type : 'str' = None,
        program_db_id : 'str' = None,
        program_name : 'str' = None,
        replicate : 'str' = None,
        study_db_id : 'str' = None,
        study_name : 'str' = None,
        treatments : 'List[BrAPIv1ObservationUnitTreatmentDTO]' = None,
        trial_db_id : 'str' = None,
        trial_name : 'str' = None):  # noqa: E501
        """BrAPIv1ObservationUnitDTO - a model defined in Swagger"""  # noqa: E501

        self._block_number = None
        self._entry_number = None
        self._entry_type = None
        self._germplasm_db_id = None
        self._germplasm_name = None
        self._location_db_id = None
        self._location_name = None
        self._observation_level = None
        self._observation_unit_db_id = None
        self._observation_unit_xref = None
        self._observations = None
        self._pedigree = None
        self._plant_number = None
        self._plot_number = None
        self._position_coordinate_x = None
        self._position_coordinate_x_type = None
        self._position_coordinate_y = None
        self._position_coordinate_y_type = None
        self._program_db_id = None
        self._program_name = None
        self._replicate = None
        self._study_db_id = None
        self._study_name = None
        self._treatments = None
        self._trial_db_id = None
        self._trial_name = None
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
        if location_db_id is not None:
            self.location_db_id = location_db_id
        if location_name is not None:
            self.location_name = location_name
        if observation_level is not None:
            self.observation_level = observation_level
        if observation_unit_db_id is not None:
            self.observation_unit_db_id = observation_unit_db_id
        if observation_unit_xref is not None:
            self.observation_unit_xref = observation_unit_xref
        if observations is not None:
            self.observations = observations
        if pedigree is not None:
            self.pedigree = pedigree
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
        if program_db_id is not None:
            self.program_db_id = program_db_id
        if program_name is not None:
            self.program_name = program_name
        if replicate is not None:
            self.replicate = replicate
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if study_name is not None:
            self.study_name = study_name
        if treatments is not None:
            self.treatments = treatments
        if trial_db_id is not None:
            self.trial_db_id = trial_db_id
        if trial_name is not None:
            self.trial_name = trial_name

    @property
    def block_number(self):
        """Gets the block_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The block_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number):
        """Sets the block_number of this BrAPIv1ObservationUnitDTO.


        :param block_number: The block_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._block_number = block_number

    @property
    def entry_number(self):
        """Gets the entry_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The entry_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._entry_number

    @entry_number.setter
    def entry_number(self, entry_number):
        """Sets the entry_number of this BrAPIv1ObservationUnitDTO.


        :param entry_number: The entry_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._entry_number = entry_number

    @property
    def entry_type(self):
        """Gets the entry_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The entry_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this BrAPIv1ObservationUnitDTO.


        :param entry_type: The entry_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._entry_type = entry_type

    @property
    def germplasm_db_id(self):
        """Gets the germplasm_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The germplasm_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_db_id

    @germplasm_db_id.setter
    def germplasm_db_id(self, germplasm_db_id):
        """Sets the germplasm_db_id of this BrAPIv1ObservationUnitDTO.


        :param germplasm_db_id: The germplasm_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_db_id = germplasm_db_id

    @property
    def germplasm_name(self):
        """Gets the germplasm_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The germplasm_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._germplasm_name

    @germplasm_name.setter
    def germplasm_name(self, germplasm_name):
        """Sets the germplasm_name of this BrAPIv1ObservationUnitDTO.


        :param germplasm_name: The germplasm_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._germplasm_name = germplasm_name

    @property
    def location_db_id(self):
        """Gets the location_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The location_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_db_id

    @location_db_id.setter
    def location_db_id(self, location_db_id):
        """Sets the location_db_id of this BrAPIv1ObservationUnitDTO.


        :param location_db_id: The location_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._location_db_id = location_db_id

    @property
    def location_name(self):
        """Gets the location_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The location_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this BrAPIv1ObservationUnitDTO.


        :param location_name: The location_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def observation_level(self):
        """Gets the observation_level of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The observation_level of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_level

    @observation_level.setter
    def observation_level(self, observation_level):
        """Sets the observation_level of this BrAPIv1ObservationUnitDTO.


        :param observation_level: The observation_level of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._observation_level = observation_level

    @property
    def observation_unit_db_id(self):
        """Gets the observation_unit_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The observation_unit_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._observation_unit_db_id

    @observation_unit_db_id.setter
    def observation_unit_db_id(self, observation_unit_db_id):
        """Sets the observation_unit_db_id of this BrAPIv1ObservationUnitDTO.


        :param observation_unit_db_id: The observation_unit_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._observation_unit_db_id = observation_unit_db_id

    @property
    def observation_unit_xref(self):
        """Gets the observation_unit_xref of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The observation_unit_xref of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: list[BrAPIv1ObservationUnitXrefDTO]
        """
        return self._observation_unit_xref

    @observation_unit_xref.setter
    def observation_unit_xref(self, observation_unit_xref):
        """Sets the observation_unit_xref of this BrAPIv1ObservationUnitDTO.


        :param observation_unit_xref: The observation_unit_xref of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: list[BrAPIv1ObservationUnitXrefDTO]
        """

        self._observation_unit_xref = observation_unit_xref

    @property
    def observations(self):
        """Gets the observations of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The observations of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: list[BrAPIv1ObservationSummaryDTO]
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        """Sets the observations of this BrAPIv1ObservationUnitDTO.


        :param observations: The observations of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: list[BrAPIv1ObservationSummaryDTO]
        """

        self._observations = observations

    @property
    def pedigree(self):
        """Gets the pedigree of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The pedigree of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._pedigree

    @pedigree.setter
    def pedigree(self, pedigree):
        """Sets the pedigree of this BrAPIv1ObservationUnitDTO.


        :param pedigree: The pedigree of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._pedigree = pedigree

    @property
    def plant_number(self):
        """Gets the plant_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The plant_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._plant_number

    @plant_number.setter
    def plant_number(self, plant_number):
        """Sets the plant_number of this BrAPIv1ObservationUnitDTO.


        :param plant_number: The plant_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._plant_number = plant_number

    @property
    def plot_number(self):
        """Gets the plot_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The plot_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._plot_number

    @plot_number.setter
    def plot_number(self, plot_number):
        """Sets the plot_number of this BrAPIv1ObservationUnitDTO.


        :param plot_number: The plot_number of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._plot_number = plot_number

    @property
    def position_coordinate_x(self):
        """Gets the position_coordinate_x of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_x of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_x

    @position_coordinate_x.setter
    def position_coordinate_x(self, position_coordinate_x):
        """Sets the position_coordinate_x of this BrAPIv1ObservationUnitDTO.


        :param position_coordinate_x: The position_coordinate_x of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_x = position_coordinate_x

    @property
    def position_coordinate_x_type(self):
        """Gets the position_coordinate_x_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_x_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_x_type

    @position_coordinate_x_type.setter
    def position_coordinate_x_type(self, position_coordinate_x_type):
        """Sets the position_coordinate_x_type of this BrAPIv1ObservationUnitDTO.


        :param position_coordinate_x_type: The position_coordinate_x_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_x_type = position_coordinate_x_type

    @property
    def position_coordinate_y(self):
        """Gets the position_coordinate_y of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_y of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_y

    @position_coordinate_y.setter
    def position_coordinate_y(self, position_coordinate_y):
        """Sets the position_coordinate_y of this BrAPIv1ObservationUnitDTO.


        :param position_coordinate_y: The position_coordinate_y of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_y = position_coordinate_y

    @property
    def position_coordinate_y_type(self):
        """Gets the position_coordinate_y_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The position_coordinate_y_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._position_coordinate_y_type

    @position_coordinate_y_type.setter
    def position_coordinate_y_type(self, position_coordinate_y_type):
        """Sets the position_coordinate_y_type of this BrAPIv1ObservationUnitDTO.


        :param position_coordinate_y_type: The position_coordinate_y_type of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._position_coordinate_y_type = position_coordinate_y_type

    @property
    def program_db_id(self):
        """Gets the program_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The program_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_db_id

    @program_db_id.setter
    def program_db_id(self, program_db_id):
        """Sets the program_db_id of this BrAPIv1ObservationUnitDTO.


        :param program_db_id: The program_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._program_db_id = program_db_id

    @property
    def program_name(self):
        """Gets the program_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The program_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this BrAPIv1ObservationUnitDTO.


        :param program_name: The program_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

    @property
    def replicate(self):
        """Gets the replicate of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The replicate of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._replicate

    @replicate.setter
    def replicate(self, replicate):
        """Sets the replicate of this BrAPIv1ObservationUnitDTO.


        :param replicate: The replicate of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._replicate = replicate

    @property
    def study_db_id(self):
        """Gets the study_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The study_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this BrAPIv1ObservationUnitDTO.


        :param study_db_id: The study_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def study_name(self):
        """Gets the study_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The study_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_name

    @study_name.setter
    def study_name(self, study_name):
        """Sets the study_name of this BrAPIv1ObservationUnitDTO.


        :param study_name: The study_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._study_name = study_name

    @property
    def treatments(self):
        """Gets the treatments of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The treatments of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: list[BrAPIv1ObservationUnitTreatmentDTO]
        """
        return self._treatments

    @treatments.setter
    def treatments(self, treatments):
        """Sets the treatments of this BrAPIv1ObservationUnitDTO.


        :param treatments: The treatments of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: list[BrAPIv1ObservationUnitTreatmentDTO]
        """

        self._treatments = treatments

    @property
    def trial_db_id(self):
        """Gets the trial_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The trial_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_db_id

    @trial_db_id.setter
    def trial_db_id(self, trial_db_id):
        """Sets the trial_db_id of this BrAPIv1ObservationUnitDTO.


        :param trial_db_id: The trial_db_id of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._trial_db_id = trial_db_id

    @property
    def trial_name(self):
        """Gets the trial_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501


        :return: The trial_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_name

    @trial_name.setter
    def trial_name(self, trial_name):
        """Sets the trial_name of this BrAPIv1ObservationUnitDTO.


        :param trial_name: The trial_name of this BrAPIv1ObservationUnitDTO.  # noqa: E501
        :type: str
        """

        self._trial_name = trial_name

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
        if issubclass(BrAPIv1ObservationUnitDTO, dict):
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
        if issubclass(BrAPIv1ObservationUnitDTO, dict):
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
        if not isinstance(other, BrAPIv1ObservationUnitDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.br_ap_iv1_observation_unit_xref_dto import BrAPIv1ObservationUnitXrefDTO
from opensilexClientToolsPython.models.br_ap_iv1_observation_summary_dto import BrAPIv1ObservationSummaryDTO
from opensilexClientToolsPython.models.br_ap_iv1_observation_unit_treatment_dto import BrAPIv1ObservationUnitTreatmentDTO


