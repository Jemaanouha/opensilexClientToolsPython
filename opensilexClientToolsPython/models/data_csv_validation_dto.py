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


class DataCSVValidationDTO(object):
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
        'errors': 'CSVValidationModel',
        'data_errors': 'DataCSVValidationModel',
        'size_max': 'int',
        'validation_token': 'str',
        'nb_lines_imported': 'int'
    }

    attribute_map = {
        'errors': 'errors',
        'data_errors': 'dataErrors',
        'size_max': 'sizeMax',
        'validation_token': 'validation_token',
        'nb_lines_imported': 'nb_lines_imported'
    }
    def __init__(self,
        errors : 'CSVValidationModel' = None,
        data_errors : 'DataCSVValidationModel' = None,
        size_max : 'int' = None,
        validation_token : 'str' = None,
        nb_lines_imported : 'int' = None):  # noqa: E501
        """DataCSVValidationDTO - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._data_errors = None
        self._size_max = None
        self._validation_token = None
        self._nb_lines_imported = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if data_errors is not None:
            self.data_errors = data_errors
        if size_max is not None:
            self.size_max = size_max
        if validation_token is not None:
            self.validation_token = validation_token
        if nb_lines_imported is not None:
            self.nb_lines_imported = nb_lines_imported

    @property
    def errors(self):
        """Gets the errors of this DataCSVValidationDTO.  # noqa: E501


        :return: The errors of this DataCSVValidationDTO.  # noqa: E501
        :rtype: CSVValidationModel
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DataCSVValidationDTO.


        :param errors: The errors of this DataCSVValidationDTO.  # noqa: E501
        :type: CSVValidationModel
        """

        self._errors = errors

    @property
    def data_errors(self):
        """Gets the data_errors of this DataCSVValidationDTO.  # noqa: E501


        :return: The data_errors of this DataCSVValidationDTO.  # noqa: E501
        :rtype: DataCSVValidationModel
        """
        return self._data_errors

    @data_errors.setter
    def data_errors(self, data_errors):
        """Sets the data_errors of this DataCSVValidationDTO.


        :param data_errors: The data_errors of this DataCSVValidationDTO.  # noqa: E501
        :type: DataCSVValidationModel
        """

        self._data_errors = data_errors

    @property
    def size_max(self):
        """Gets the size_max of this DataCSVValidationDTO.  # noqa: E501


        :return: The size_max of this DataCSVValidationDTO.  # noqa: E501
        :rtype: int
        """
        return self._size_max

    @size_max.setter
    def size_max(self, size_max):
        """Sets the size_max of this DataCSVValidationDTO.


        :param size_max: The size_max of this DataCSVValidationDTO.  # noqa: E501
        :type: int
        """

        self._size_max = size_max

    @property
    def validation_token(self):
        """Gets the validation_token of this DataCSVValidationDTO.  # noqa: E501


        :return: The validation_token of this DataCSVValidationDTO.  # noqa: E501
        :rtype: str
        """
        return self._validation_token

    @validation_token.setter
    def validation_token(self, validation_token):
        """Sets the validation_token of this DataCSVValidationDTO.


        :param validation_token: The validation_token of this DataCSVValidationDTO.  # noqa: E501
        :type: str
        """

        self._validation_token = validation_token

    @property
    def nb_lines_imported(self):
        """Gets the nb_lines_imported of this DataCSVValidationDTO.  # noqa: E501


        :return: The nb_lines_imported of this DataCSVValidationDTO.  # noqa: E501
        :rtype: int
        """
        return self._nb_lines_imported

    @nb_lines_imported.setter
    def nb_lines_imported(self, nb_lines_imported):
        """Sets the nb_lines_imported of this DataCSVValidationDTO.


        :param nb_lines_imported: The nb_lines_imported of this DataCSVValidationDTO.  # noqa: E501
        :type: int
        """

        self._nb_lines_imported = nb_lines_imported

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
        if issubclass(DataCSVValidationDTO, dict):
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
        if issubclass(DataCSVValidationDTO, dict):
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
        if not isinstance(other, DataCSVValidationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel
from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel


