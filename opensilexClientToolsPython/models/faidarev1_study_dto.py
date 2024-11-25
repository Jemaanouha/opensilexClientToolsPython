# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class Faidarev1StudyDTO(object):
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
        'active': 'str',
        'additional_info': 'dict(str, str)',
        'documentation_url': 'str',
        'end_date': 'str',
        'location_db_id': 'str',
        'location_name': 'str',
        'last_update': 'Faidarev1LastUpdateDTO',
        'name': 'str',
        'program_db_id': 'str',
        'program_name': 'str',
        'start_date': 'str',
        'study_type': 'str',
        'study_db_id': 'str',
        'study_name': 'str',
        'trial_db_id': 'str',
        'trial_name': 'str',
        'trial_db_ids': 'list[str]',
        'contacts': 'list[Faidarev1ContactDTO]',
        'data_links': 'list[Faidarev1DataLinkDTO]',
        'study_description': 'str',
        'seasons': 'list[str]',
        'observation_variable_db_ids': 'list[str]',
        'germplasm_db_ids': 'list[str]'
    }

    attribute_map = {
        'active': 'active',
        'additional_info': 'additionalInfo',
        'documentation_url': 'documentationURL',
        'end_date': 'endDate',
        'location_db_id': 'locationDbId',
        'location_name': 'locationName',
        'last_update': 'lastUpdate',
        'name': 'name',
        'program_db_id': 'programDbId',
        'program_name': 'programName',
        'start_date': 'startDate',
        'study_type': 'studyType',
        'study_db_id': 'studyDbId',
        'study_name': 'studyName',
        'trial_db_id': 'trialDbId',
        'trial_name': 'trialName',
        'trial_db_ids': 'trialDbIds',
        'contacts': 'contacts',
        'data_links': 'dataLinks',
        'study_description': 'studyDescription',
        'seasons': 'seasons',
        'observation_variable_db_ids': 'observationVariableDbIds',
        'germplasm_db_ids': 'germplasmDbIds'
    }
    def __init__(self,
        active : 'str' = None,
        additional_info : 'Dict[str, str]' = None,
        documentation_url : 'str' = None,
        end_date : 'str' = None,
        location_db_id : 'str' = None,
        location_name : 'str' = None,
        last_update : 'Faidarev1LastUpdateDTO' = None,
        name : 'str' = None,
        program_db_id : 'str' = None,
        program_name : 'str' = None,
        start_date : 'str' = None,
        study_type : 'str' = None,
        study_db_id : 'str' = None,
        study_name : 'str' = None,
        trial_db_id : 'str' = None,
        trial_name : 'str' = None,
        trial_db_ids : 'List[str]' = None,
        contacts : 'List[Faidarev1ContactDTO]' = None,
        data_links : 'List[Faidarev1DataLinkDTO]' = None,
        study_description : 'str' = None,
        seasons : 'List[str]' = None,
        observation_variable_db_ids : 'List[str]' = None,
        germplasm_db_ids : 'List[str]' = None):  # noqa: E501
        """Faidarev1StudyDTO - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._additional_info = None
        self._documentation_url = None
        self._end_date = None
        self._location_db_id = None
        self._location_name = None
        self._last_update = None
        self._name = None
        self._program_db_id = None
        self._program_name = None
        self._start_date = None
        self._study_type = None
        self._study_db_id = None
        self._study_name = None
        self._trial_db_id = None
        self._trial_name = None
        self._trial_db_ids = None
        self._contacts = None
        self._data_links = None
        self._study_description = None
        self._seasons = None
        self._observation_variable_db_ids = None
        self._germplasm_db_ids = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if additional_info is not None:
            self.additional_info = additional_info
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if end_date is not None:
            self.end_date = end_date
        if location_db_id is not None:
            self.location_db_id = location_db_id
        if location_name is not None:
            self.location_name = location_name
        if last_update is not None:
            self.last_update = last_update
        if name is not None:
            self.name = name
        if program_db_id is not None:
            self.program_db_id = program_db_id
        if program_name is not None:
            self.program_name = program_name
        if start_date is not None:
            self.start_date = start_date
        if study_type is not None:
            self.study_type = study_type
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if study_name is not None:
            self.study_name = study_name
        if trial_db_id is not None:
            self.trial_db_id = trial_db_id
        if trial_name is not None:
            self.trial_name = trial_name
        if trial_db_ids is not None:
            self.trial_db_ids = trial_db_ids
        if contacts is not None:
            self.contacts = contacts
        if data_links is not None:
            self.data_links = data_links
        if study_description is not None:
            self.study_description = study_description
        if seasons is not None:
            self.seasons = seasons
        if observation_variable_db_ids is not None:
            self.observation_variable_db_ids = observation_variable_db_ids
        if germplasm_db_ids is not None:
            self.germplasm_db_ids = germplasm_db_ids

    @property
    def active(self):
        """Gets the active of this Faidarev1StudyDTO.  # noqa: E501


        :return: The active of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Faidarev1StudyDTO.


        :param active: The active of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def additional_info(self):
        """Gets the additional_info of this Faidarev1StudyDTO.  # noqa: E501


        :return: The additional_info of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Faidarev1StudyDTO.


        :param additional_info: The additional_info of this Faidarev1StudyDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_info = additional_info

    @property
    def documentation_url(self):
        """Gets the documentation_url of this Faidarev1StudyDTO.  # noqa: E501


        :return: The documentation_url of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this Faidarev1StudyDTO.


        :param documentation_url: The documentation_url of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def end_date(self):
        """Gets the end_date of this Faidarev1StudyDTO.  # noqa: E501


        :return: The end_date of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Faidarev1StudyDTO.


        :param end_date: The end_date of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def location_db_id(self):
        """Gets the location_db_id of this Faidarev1StudyDTO.  # noqa: E501


        :return: The location_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_db_id

    @location_db_id.setter
    def location_db_id(self, location_db_id):
        """Sets the location_db_id of this Faidarev1StudyDTO.


        :param location_db_id: The location_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._location_db_id = location_db_id

    @property
    def location_name(self):
        """Gets the location_name of this Faidarev1StudyDTO.  # noqa: E501


        :return: The location_name of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this Faidarev1StudyDTO.


        :param location_name: The location_name of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def last_update(self):
        """Gets the last_update of this Faidarev1StudyDTO.  # noqa: E501


        :return: The last_update of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: Faidarev1LastUpdateDTO
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this Faidarev1StudyDTO.


        :param last_update: The last_update of this Faidarev1StudyDTO.  # noqa: E501
        :type: Faidarev1LastUpdateDTO
        """

        self._last_update = last_update

    @property
    def name(self):
        """Gets the name of this Faidarev1StudyDTO.  # noqa: E501


        :return: The name of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Faidarev1StudyDTO.


        :param name: The name of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def program_db_id(self):
        """Gets the program_db_id of this Faidarev1StudyDTO.  # noqa: E501


        :return: The program_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_db_id

    @program_db_id.setter
    def program_db_id(self, program_db_id):
        """Sets the program_db_id of this Faidarev1StudyDTO.


        :param program_db_id: The program_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._program_db_id = program_db_id

    @property
    def program_name(self):
        """Gets the program_name of this Faidarev1StudyDTO.  # noqa: E501


        :return: The program_name of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this Faidarev1StudyDTO.


        :param program_name: The program_name of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

    @property
    def start_date(self):
        """Gets the start_date of this Faidarev1StudyDTO.  # noqa: E501


        :return: The start_date of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Faidarev1StudyDTO.


        :param start_date: The start_date of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def study_type(self):
        """Gets the study_type of this Faidarev1StudyDTO.  # noqa: E501


        :return: The study_type of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_type

    @study_type.setter
    def study_type(self, study_type):
        """Sets the study_type of this Faidarev1StudyDTO.


        :param study_type: The study_type of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._study_type = study_type

    @property
    def study_db_id(self):
        """Gets the study_db_id of this Faidarev1StudyDTO.  # noqa: E501


        :return: The study_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this Faidarev1StudyDTO.


        :param study_db_id: The study_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def study_name(self):
        """Gets the study_name of this Faidarev1StudyDTO.  # noqa: E501


        :return: The study_name of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_name

    @study_name.setter
    def study_name(self, study_name):
        """Sets the study_name of this Faidarev1StudyDTO.


        :param study_name: The study_name of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._study_name = study_name

    @property
    def trial_db_id(self):
        """Gets the trial_db_id of this Faidarev1StudyDTO.  # noqa: E501


        :return: The trial_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_db_id

    @trial_db_id.setter
    def trial_db_id(self, trial_db_id):
        """Sets the trial_db_id of this Faidarev1StudyDTO.


        :param trial_db_id: The trial_db_id of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._trial_db_id = trial_db_id

    @property
    def trial_name(self):
        """Gets the trial_name of this Faidarev1StudyDTO.  # noqa: E501


        :return: The trial_name of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_name

    @trial_name.setter
    def trial_name(self, trial_name):
        """Sets the trial_name of this Faidarev1StudyDTO.


        :param trial_name: The trial_name of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._trial_name = trial_name

    @property
    def trial_db_ids(self):
        """Gets the trial_db_ids of this Faidarev1StudyDTO.  # noqa: E501


        :return: The trial_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._trial_db_ids

    @trial_db_ids.setter
    def trial_db_ids(self, trial_db_ids):
        """Sets the trial_db_ids of this Faidarev1StudyDTO.


        :param trial_db_ids: The trial_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[str]
        """

        self._trial_db_ids = trial_db_ids

    @property
    def contacts(self):
        """Gets the contacts of this Faidarev1StudyDTO.  # noqa: E501


        :return: The contacts of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[Faidarev1ContactDTO]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Faidarev1StudyDTO.


        :param contacts: The contacts of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[Faidarev1ContactDTO]
        """

        self._contacts = contacts

    @property
    def data_links(self):
        """Gets the data_links of this Faidarev1StudyDTO.  # noqa: E501


        :return: The data_links of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[Faidarev1DataLinkDTO]
        """
        return self._data_links

    @data_links.setter
    def data_links(self, data_links):
        """Sets the data_links of this Faidarev1StudyDTO.


        :param data_links: The data_links of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[Faidarev1DataLinkDTO]
        """

        self._data_links = data_links

    @property
    def study_description(self):
        """Gets the study_description of this Faidarev1StudyDTO.  # noqa: E501


        :return: The study_description of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_description

    @study_description.setter
    def study_description(self, study_description):
        """Sets the study_description of this Faidarev1StudyDTO.


        :param study_description: The study_description of this Faidarev1StudyDTO.  # noqa: E501
        :type: str
        """

        self._study_description = study_description

    @property
    def seasons(self):
        """Gets the seasons of this Faidarev1StudyDTO.  # noqa: E501


        :return: The seasons of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._seasons

    @seasons.setter
    def seasons(self, seasons):
        """Sets the seasons of this Faidarev1StudyDTO.


        :param seasons: The seasons of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[str]
        """

        self._seasons = seasons

    @property
    def observation_variable_db_ids(self):
        """Gets the observation_variable_db_ids of this Faidarev1StudyDTO.  # noqa: E501


        :return: The observation_variable_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._observation_variable_db_ids

    @observation_variable_db_ids.setter
    def observation_variable_db_ids(self, observation_variable_db_ids):
        """Sets the observation_variable_db_ids of this Faidarev1StudyDTO.


        :param observation_variable_db_ids: The observation_variable_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[str]
        """

        self._observation_variable_db_ids = observation_variable_db_ids

    @property
    def germplasm_db_ids(self):
        """Gets the germplasm_db_ids of this Faidarev1StudyDTO.  # noqa: E501


        :return: The germplasm_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._germplasm_db_ids

    @germplasm_db_ids.setter
    def germplasm_db_ids(self, germplasm_db_ids):
        """Sets the germplasm_db_ids of this Faidarev1StudyDTO.


        :param germplasm_db_ids: The germplasm_db_ids of this Faidarev1StudyDTO.  # noqa: E501
        :type: list[str]
        """

        self._germplasm_db_ids = germplasm_db_ids

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
        if issubclass(Faidarev1StudyDTO, dict):
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
        if issubclass(Faidarev1StudyDTO, dict):
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
        if not isinstance(other, Faidarev1StudyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.faidarev1_last_update_dto import Faidarev1LastUpdateDTO
from opensilexClientToolsPython.models.faidarev1_contact_dto import Faidarev1ContactDTO
from opensilexClientToolsPython.models.faidarev1_data_link_dto import Faidarev1DataLinkDTO


