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


class CsvHeader(object):
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
        'columns': 'list[str]',
        'real_csv_header_length': 'int'
    }

    attribute_map = {
        'columns': 'columns',
        'real_csv_header_length': 'realCsvHeaderLength'
    }
    def __init__(self,
        columns : 'List[str]' = None,
        real_csv_header_length : 'int' = None):  # noqa: E501
        """CsvHeader - a model defined in Swagger"""  # noqa: E501

        self._columns = None
        self._real_csv_header_length = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if real_csv_header_length is not None:
            self.real_csv_header_length = real_csv_header_length

    @property
    def columns(self):
        """Gets the columns of this CsvHeader.  # noqa: E501


        :return: The columns of this CsvHeader.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CsvHeader.


        :param columns: The columns of this CsvHeader.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def real_csv_header_length(self):
        """Gets the real_csv_header_length of this CsvHeader.  # noqa: E501


        :return: The real_csv_header_length of this CsvHeader.  # noqa: E501
        :rtype: int
        """
        return self._real_csv_header_length

    @real_csv_header_length.setter
    def real_csv_header_length(self, real_csv_header_length):
        """Sets the real_csv_header_length of this CsvHeader.


        :param real_csv_header_length: The real_csv_header_length of this CsvHeader.  # noqa: E501
        :type: int
        """

        self._real_csv_header_length = real_csv_header_length

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
        if issubclass(CsvHeader, dict):
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
        if issubclass(CsvHeader, dict):
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
        if not isinstance(other, CsvHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




