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


class DataVariableSeriesGetDTO(object):
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
        'variable': 'VariableDetailsDTO',
        'provenances': 'list[DataSimpleProvenanceGetDTO]',
        'devices': 'list[DeviceGetDTO]',
        'data_series': 'list[DataSerieGetDTO]',
        'calculated_series': 'list[DataSerieGetDTO]',
        'last_data_stored': 'DataComputedGetDTO'
    }

    attribute_map = {
        'variable': 'variable',
        'provenances': 'provenances',
        'devices': 'devices',
        'data_series': 'data_series',
        'calculated_series': 'calculated_series',
        'last_data_stored': 'last_data_stored'
    }
    def __init__(self,
        variable : 'VariableDetailsDTO' = None,
        provenances : 'List[DataSimpleProvenanceGetDTO]' = None,
        devices : 'List[DeviceGetDTO]' = None,
        data_series : 'List[DataSerieGetDTO]' = None,
        calculated_series : 'List[DataSerieGetDTO]' = None,
        last_data_stored : 'DataComputedGetDTO' = None):  # noqa: E501
        """DataVariableSeriesGetDTO - a model defined in Swagger"""  # noqa: E501

        self._variable = None
        self._provenances = None
        self._devices = None
        self._data_series = None
        self._calculated_series = None
        self._last_data_stored = None
        self.discriminator = None

        if variable is not None:
            self.variable = variable
        if provenances is not None:
            self.provenances = provenances
        if devices is not None:
            self.devices = devices
        if data_series is not None:
            self.data_series = data_series
        if calculated_series is not None:
            self.calculated_series = calculated_series
        if last_data_stored is not None:
            self.last_data_stored = last_data_stored

    @property
    def variable(self):
        """Gets the variable of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The variable of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: VariableDetailsDTO
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this DataVariableSeriesGetDTO.


        :param variable: The variable of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: VariableDetailsDTO
        """

        self._variable = variable

    @property
    def provenances(self):
        """Gets the provenances of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The provenances of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: list[DataSimpleProvenanceGetDTO]
        """
        return self._provenances

    @provenances.setter
    def provenances(self, provenances):
        """Sets the provenances of this DataVariableSeriesGetDTO.


        :param provenances: The provenances of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: list[DataSimpleProvenanceGetDTO]
        """

        self._provenances = provenances

    @property
    def devices(self):
        """Gets the devices of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The devices of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: list[DeviceGetDTO]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DataVariableSeriesGetDTO.


        :param devices: The devices of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: list[DeviceGetDTO]
        """

        self._devices = devices

    @property
    def data_series(self):
        """Gets the data_series of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The data_series of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: list[DataSerieGetDTO]
        """
        return self._data_series

    @data_series.setter
    def data_series(self, data_series):
        """Sets the data_series of this DataVariableSeriesGetDTO.


        :param data_series: The data_series of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: list[DataSerieGetDTO]
        """

        self._data_series = data_series

    @property
    def calculated_series(self):
        """Gets the calculated_series of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The calculated_series of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: list[DataSerieGetDTO]
        """
        return self._calculated_series

    @calculated_series.setter
    def calculated_series(self, calculated_series):
        """Sets the calculated_series of this DataVariableSeriesGetDTO.


        :param calculated_series: The calculated_series of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: list[DataSerieGetDTO]
        """

        self._calculated_series = calculated_series

    @property
    def last_data_stored(self):
        """Gets the last_data_stored of this DataVariableSeriesGetDTO.  # noqa: E501


        :return: The last_data_stored of this DataVariableSeriesGetDTO.  # noqa: E501
        :rtype: DataComputedGetDTO
        """
        return self._last_data_stored

    @last_data_stored.setter
    def last_data_stored(self, last_data_stored):
        """Sets the last_data_stored of this DataVariableSeriesGetDTO.


        :param last_data_stored: The last_data_stored of this DataVariableSeriesGetDTO.  # noqa: E501
        :type: DataComputedGetDTO
        """

        self._last_data_stored = last_data_stored

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
        if issubclass(DataVariableSeriesGetDTO, dict):
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
        if not isinstance(other, DataVariableSeriesGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.data_simple_provenance_get_dto import DataSimpleProvenanceGetDTO
from opensilexClientToolsPython.models.device_get_dto import DeviceGetDTO
from opensilexClientToolsPython.models.data_serie_get_dto import DataSerieGetDTO
from opensilexClientToolsPython.models.data_serie_get_dto import DataSerieGetDTO
from opensilexClientToolsPython.models.data_computed_get_dto import DataComputedGetDTO


