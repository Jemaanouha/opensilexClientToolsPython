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

from typing import List, Dict


class BrAPIv1SuperStudyDTO(object):
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
        'common_crop_name': 'str',
        'documentation_url': 'str',
        'end_date': 'str',
        'location_db_id': 'str',
        'location_name': 'str',
        'program_db_id': 'str',
        'program_name': 'str',
        'start_date': 'str',
        'study_db_id': 'str',
        'study_name': 'str',
        'study_type_db_id': 'str',
        'study_type_name': 'str',
        'trial_db_id': 'str',
        'trial_name': 'str'
    }

    attribute_map = {
        'active': 'active',
        'additional_info': 'additionalInfo',
        'common_crop_name': 'commonCropName',
        'documentation_url': 'documentationURL',
        'end_date': 'endDate',
        'location_db_id': 'locationDbId',
        'location_name': 'locationName',
        'program_db_id': 'programDbId',
        'program_name': 'programName',
        'start_date': 'startDate',
        'study_db_id': 'studyDbId',
        'study_name': 'studyName',
        'study_type_db_id': 'studyTypeDbId',
        'study_type_name': 'studyTypeName',
        'trial_db_id': 'trialDbId',
        'trial_name': 'trialName'
    }
    def __init__(self,
        active : 'str' = None,
        additional_info : 'Dict[str, str]' = None,
        common_crop_name : 'str' = None,
        documentation_url : 'str' = None,
        end_date : 'str' = None,
        location_db_id : 'str' = None,
        location_name : 'str' = None,
        program_db_id : 'str' = None,
        program_name : 'str' = None,
        start_date : 'str' = None,
        study_db_id : 'str' = None,
        study_name : 'str' = None,
        study_type_db_id : 'str' = None,
        study_type_name : 'str' = None,
        trial_db_id : 'str' = None,
        trial_name : 'str' = None):  # noqa: E501
        """BrAPIv1SuperStudyDTO - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._additional_info = None
        self._common_crop_name = None
        self._documentation_url = None
        self._end_date = None
        self._location_db_id = None
        self._location_name = None
        self._program_db_id = None
        self._program_name = None
        self._start_date = None
        self._study_db_id = None
        self._study_name = None
        self._study_type_db_id = None
        self._study_type_name = None
        self._trial_db_id = None
        self._trial_name = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if additional_info is not None:
            self.additional_info = additional_info
        if common_crop_name is not None:
            self.common_crop_name = common_crop_name
        if documentation_url is not None:
            self.documentation_url = documentation_url
        if end_date is not None:
            self.end_date = end_date
        if location_db_id is not None:
            self.location_db_id = location_db_id
        if location_name is not None:
            self.location_name = location_name
        if program_db_id is not None:
            self.program_db_id = program_db_id
        if program_name is not None:
            self.program_name = program_name
        if start_date is not None:
            self.start_date = start_date
        if study_db_id is not None:
            self.study_db_id = study_db_id
        if study_name is not None:
            self.study_name = study_name
        if study_type_db_id is not None:
            self.study_type_db_id = study_type_db_id
        if study_type_name is not None:
            self.study_type_name = study_type_name
        if trial_db_id is not None:
            self.trial_db_id = trial_db_id
        if trial_name is not None:
            self.trial_name = trial_name

    @property
    def active(self):
        """Gets the active of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The active of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BrAPIv1SuperStudyDTO.


        :param active: The active of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def additional_info(self):
        """Gets the additional_info of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The additional_info of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BrAPIv1SuperStudyDTO.


        :param additional_info: The additional_info of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_info = additional_info

    @property
    def common_crop_name(self):
        """Gets the common_crop_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The common_crop_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._common_crop_name

    @common_crop_name.setter
    def common_crop_name(self, common_crop_name):
        """Sets the common_crop_name of this BrAPIv1SuperStudyDTO.


        :param common_crop_name: The common_crop_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._common_crop_name = common_crop_name

    @property
    def documentation_url(self):
        """Gets the documentation_url of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The documentation_url of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this BrAPIv1SuperStudyDTO.


        :param documentation_url: The documentation_url of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._documentation_url = documentation_url

    @property
    def end_date(self):
        """Gets the end_date of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The end_date of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BrAPIv1SuperStudyDTO.


        :param end_date: The end_date of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def location_db_id(self):
        """Gets the location_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The location_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_db_id

    @location_db_id.setter
    def location_db_id(self, location_db_id):
        """Sets the location_db_id of this BrAPIv1SuperStudyDTO.


        :param location_db_id: The location_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._location_db_id = location_db_id

    @property
    def location_name(self):
        """Gets the location_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The location_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this BrAPIv1SuperStudyDTO.


        :param location_name: The location_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def program_db_id(self):
        """Gets the program_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The program_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_db_id

    @program_db_id.setter
    def program_db_id(self, program_db_id):
        """Sets the program_db_id of this BrAPIv1SuperStudyDTO.


        :param program_db_id: The program_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._program_db_id = program_db_id

    @property
    def program_name(self):
        """Gets the program_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The program_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._program_name

    @program_name.setter
    def program_name(self, program_name):
        """Sets the program_name of this BrAPIv1SuperStudyDTO.


        :param program_name: The program_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._program_name = program_name

    @property
    def start_date(self):
        """Gets the start_date of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The start_date of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BrAPIv1SuperStudyDTO.


        :param start_date: The start_date of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def study_db_id(self):
        """Gets the study_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The study_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_db_id

    @study_db_id.setter
    def study_db_id(self, study_db_id):
        """Sets the study_db_id of this BrAPIv1SuperStudyDTO.


        :param study_db_id: The study_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._study_db_id = study_db_id

    @property
    def study_name(self):
        """Gets the study_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The study_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_name

    @study_name.setter
    def study_name(self, study_name):
        """Sets the study_name of this BrAPIv1SuperStudyDTO.


        :param study_name: The study_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._study_name = study_name

    @property
    def study_type_db_id(self):
        """Gets the study_type_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The study_type_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_type_db_id

    @study_type_db_id.setter
    def study_type_db_id(self, study_type_db_id):
        """Sets the study_type_db_id of this BrAPIv1SuperStudyDTO.


        :param study_type_db_id: The study_type_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._study_type_db_id = study_type_db_id

    @property
    def study_type_name(self):
        """Gets the study_type_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The study_type_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._study_type_name

    @study_type_name.setter
    def study_type_name(self, study_type_name):
        """Sets the study_type_name of this BrAPIv1SuperStudyDTO.


        :param study_type_name: The study_type_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._study_type_name = study_type_name

    @property
    def trial_db_id(self):
        """Gets the trial_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The trial_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_db_id

    @trial_db_id.setter
    def trial_db_id(self, trial_db_id):
        """Sets the trial_db_id of this BrAPIv1SuperStudyDTO.


        :param trial_db_id: The trial_db_id of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :type: str
        """

        self._trial_db_id = trial_db_id

    @property
    def trial_name(self):
        """Gets the trial_name of this BrAPIv1SuperStudyDTO.  # noqa: E501


        :return: The trial_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
        :rtype: str
        """
        return self._trial_name

    @trial_name.setter
    def trial_name(self, trial_name):
        """Sets the trial_name of this BrAPIv1SuperStudyDTO.


        :param trial_name: The trial_name of this BrAPIv1SuperStudyDTO.  # noqa: E501
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
        if issubclass(BrAPIv1SuperStudyDTO, dict):
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
        if not isinstance(other, BrAPIv1SuperStudyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




