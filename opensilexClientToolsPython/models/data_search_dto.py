# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.0-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class DataSearchDTO(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'timezone': 'str',
        'experiments': 'list[str]',
        'targets': 'list[str]',
        'variables': 'list[str]',
        'devices': 'list[str]',
        'provenances': 'list[str]',
        'min_confidence': 'float',
        'max_confidence': 'float',
        'metadata': 'str',
        'mode': 'str',
        'with_raw_data': 'bool'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'timezone': 'timezone',
        'experiments': 'experiments',
        'targets': 'targets',
        'variables': 'variables',
        'devices': 'devices',
        'provenances': 'provenances',
        'min_confidence': 'min_confidence',
        'max_confidence': 'max_confidence',
        'metadata': 'metadata',
        'mode': 'mode',
        'with_raw_data': 'with_raw_data'
    }
    def __init__(self,
        start_date : 'str' = None,
        end_date : 'str' = None,
        timezone : 'str' = None,
        experiments : 'List[str]' = None,
        targets : 'List[str]' = None,
        variables : 'List[str]' = None,
        devices : 'List[str]' = None,
        provenances : 'List[str]' = None,
        min_confidence : 'float' = None,
        max_confidence : 'float' = None,
        metadata : 'str' = None,
        mode : 'str' = None,
        with_raw_data : 'bool' = None):  # noqa: E501
        """DataSearchDTO - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._timezone = None
        self._experiments = None
        self._targets = None
        self._variables = None
        self._devices = None
        self._provenances = None
        self._min_confidence = None
        self._max_confidence = None
        self._metadata = None
        self._mode = None
        self._with_raw_data = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if timezone is not None:
            self.timezone = timezone
        if experiments is not None:
            self.experiments = experiments
        if targets is not None:
            self.targets = targets
        if variables is not None:
            self.variables = variables
        if devices is not None:
            self.devices = devices
        if provenances is not None:
            self.provenances = provenances
        if min_confidence is not None:
            self.min_confidence = min_confidence
        if max_confidence is not None:
            self.max_confidence = max_confidence
        if metadata is not None:
            self.metadata = metadata
        if mode is not None:
            self.mode = mode
        if with_raw_data is not None:
            self.with_raw_data = with_raw_data

    @property
    def start_date(self):
        """Gets the start_date of this DataSearchDTO.  # noqa: E501

        start date  # noqa: E501

        :return: The start_date of this DataSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this DataSearchDTO.

        start date  # noqa: E501

        :param start_date: The start_date of this DataSearchDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this DataSearchDTO.  # noqa: E501

        end date  # noqa: E501

        :return: The end_date of this DataSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this DataSearchDTO.

        end date  # noqa: E501

        :param end_date: The end_date of this DataSearchDTO.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def timezone(self):
        """Gets the timezone of this DataSearchDTO.  # noqa: E501

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :return: The timezone of this DataSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DataSearchDTO.

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :param timezone: The timezone of this DataSearchDTO.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def experiments(self):
        """Gets the experiments of this DataSearchDTO.  # noqa: E501


        :return: The experiments of this DataSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this DataSearchDTO.


        :param experiments: The experiments of this DataSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._experiments = experiments

    @property
    def targets(self):
        """Gets the targets of this DataSearchDTO.  # noqa: E501


        :return: The targets of this DataSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this DataSearchDTO.


        :param targets: The targets of this DataSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def variables(self):
        """Gets the variables of this DataSearchDTO.  # noqa: E501


        :return: The variables of this DataSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this DataSearchDTO.


        :param variables: The variables of this DataSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._variables = variables

    @property
    def devices(self):
        """Gets the devices of this DataSearchDTO.  # noqa: E501


        :return: The devices of this DataSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DataSearchDTO.


        :param devices: The devices of this DataSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def provenances(self):
        """Gets the provenances of this DataSearchDTO.  # noqa: E501


        :return: The provenances of this DataSearchDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._provenances

    @provenances.setter
    def provenances(self, provenances):
        """Sets the provenances of this DataSearchDTO.


        :param provenances: The provenances of this DataSearchDTO.  # noqa: E501
        :type: list[str]
        """

        self._provenances = provenances

    @property
    def min_confidence(self):
        """Gets the min_confidence of this DataSearchDTO.  # noqa: E501

        confidence index  # noqa: E501

        :return: The min_confidence of this DataSearchDTO.  # noqa: E501
        :rtype: float
        """
        return self._min_confidence

    @min_confidence.setter
    def min_confidence(self, min_confidence):
        """Sets the min_confidence of this DataSearchDTO.

        confidence index  # noqa: E501

        :param min_confidence: The min_confidence of this DataSearchDTO.  # noqa: E501
        :type: float
        """
        if min_confidence is not None and min_confidence > 1:  # noqa: E501
            raise ValueError("Invalid value for `min_confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if min_confidence is not None and min_confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_confidence = min_confidence

    @property
    def max_confidence(self):
        """Gets the max_confidence of this DataSearchDTO.  # noqa: E501

        confidence index  # noqa: E501

        :return: The max_confidence of this DataSearchDTO.  # noqa: E501
        :rtype: float
        """
        return self._max_confidence

    @max_confidence.setter
    def max_confidence(self, max_confidence):
        """Sets the max_confidence of this DataSearchDTO.

        confidence index  # noqa: E501

        :param max_confidence: The max_confidence of this DataSearchDTO.  # noqa: E501
        :type: float
        """
        if max_confidence is not None and max_confidence > 1:  # noqa: E501
            raise ValueError("Invalid value for `max_confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if max_confidence is not None and max_confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_confidence = max_confidence

    @property
    def metadata(self):
        """Gets the metadata of this DataSearchDTO.  # noqa: E501

        key-value system to store additional information that can be used to query data  # noqa: E501

        :return: The metadata of this DataSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DataSearchDTO.

        key-value system to store additional information that can be used to query data  # noqa: E501

        :param metadata: The metadata of this DataSearchDTO.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def mode(self):
        """Gets the mode of this DataSearchDTO.  # noqa: E501

        format wide or long  # noqa: E501

        :return: The mode of this DataSearchDTO.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DataSearchDTO.

        format wide or long  # noqa: E501

        :param mode: The mode of this DataSearchDTO.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def with_raw_data(self):
        """Gets the with_raw_data of this DataSearchDTO.  # noqa: E501

        export also raw_data  # noqa: E501

        :return: The with_raw_data of this DataSearchDTO.  # noqa: E501
        :rtype: bool
        """
        return self._with_raw_data

    @with_raw_data.setter
    def with_raw_data(self, with_raw_data):
        """Sets the with_raw_data of this DataSearchDTO.

        export also raw_data  # noqa: E501

        :param with_raw_data: The with_raw_data of this DataSearchDTO.  # noqa: E501
        :type: bool
        """

        self._with_raw_data = with_raw_data

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
        if issubclass(DataSearchDTO, dict):
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
        if issubclass(DataSearchDTO, dict):
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
        if not isinstance(other, DataSearchDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




