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


class CSVValidationModel(object):
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
        'missing_headers': 'list[str]',
        'empty_headers': 'list[int]',
        'invalid_header_ur_is': 'dict(str, str)',
        'datatype_errors': 'dict(str, list[CSVDatatypeError])',
        'uri_not_found_errors': 'dict(str, list[CSVURINotFoundError])',
        'invalid_uri_errors': 'dict(str, list[CSVCell])',
        'missing_required_value_errors': 'dict(str, list[CSVCell])',
        'invalid_value_errors': 'dict(str, list[CSVCell])',
        'already_existing_uri_errors': 'dict(str, CSVCell)',
        'duplicate_uri_errors': 'dict(str, CSVDuplicateURIError)'
    }

    attribute_map = {
        'missing_headers': 'missingHeaders',
        'empty_headers': 'emptyHeaders',
        'invalid_header_ur_is': 'invalidHeaderURIs',
        'datatype_errors': 'datatypeErrors',
        'uri_not_found_errors': 'uriNotFoundErrors',
        'invalid_uri_errors': 'invalidURIErrors',
        'missing_required_value_errors': 'missingRequiredValueErrors',
        'invalid_value_errors': 'invalidValueErrors',
        'already_existing_uri_errors': 'alreadyExistingURIErrors',
        'duplicate_uri_errors': 'duplicateURIErrors'
    }

    def __init__(self, missing_headers=None, empty_headers=None, invalid_header_ur_is=None, datatype_errors=None, uri_not_found_errors=None, invalid_uri_errors=None, missing_required_value_errors=None, invalid_value_errors=None, already_existing_uri_errors=None, duplicate_uri_errors=None):  # noqa: E501
        """CSVValidationModel - a model defined in Swagger"""  # noqa: E501

        self._missing_headers = None
        self._empty_headers = None
        self._invalid_header_ur_is = None
        self._datatype_errors = None
        self._uri_not_found_errors = None
        self._invalid_uri_errors = None
        self._missing_required_value_errors = None
        self._invalid_value_errors = None
        self._already_existing_uri_errors = None
        self._duplicate_uri_errors = None
        self.discriminator = None

        if missing_headers is not None:
            self.missing_headers = missing_headers
        if empty_headers is not None:
            self.empty_headers = empty_headers
        if invalid_header_ur_is is not None:
            self.invalid_header_ur_is = invalid_header_ur_is
        if datatype_errors is not None:
            self.datatype_errors = datatype_errors
        if uri_not_found_errors is not None:
            self.uri_not_found_errors = uri_not_found_errors
        if invalid_uri_errors is not None:
            self.invalid_uri_errors = invalid_uri_errors
        if missing_required_value_errors is not None:
            self.missing_required_value_errors = missing_required_value_errors
        if invalid_value_errors is not None:
            self.invalid_value_errors = invalid_value_errors
        if already_existing_uri_errors is not None:
            self.already_existing_uri_errors = already_existing_uri_errors
        if duplicate_uri_errors is not None:
            self.duplicate_uri_errors = duplicate_uri_errors

    @property
    def missing_headers(self):
        """Gets the missing_headers of this CSVValidationModel.  # noqa: E501


        :return: The missing_headers of this CSVValidationModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_headers

    @missing_headers.setter
    def missing_headers(self, missing_headers):
        """Sets the missing_headers of this CSVValidationModel.


        :param missing_headers: The missing_headers of this CSVValidationModel.  # noqa: E501
        :type: list[str]
        """

        self._missing_headers = missing_headers

    @property
    def empty_headers(self):
        """Gets the empty_headers of this CSVValidationModel.  # noqa: E501


        :return: The empty_headers of this CSVValidationModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._empty_headers

    @empty_headers.setter
    def empty_headers(self, empty_headers):
        """Sets the empty_headers of this CSVValidationModel.


        :param empty_headers: The empty_headers of this CSVValidationModel.  # noqa: E501
        :type: list[int]
        """

        self._empty_headers = empty_headers

    @property
    def invalid_header_ur_is(self):
        """Gets the invalid_header_ur_is of this CSVValidationModel.  # noqa: E501


        :return: The invalid_header_ur_is of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._invalid_header_ur_is

    @invalid_header_ur_is.setter
    def invalid_header_ur_is(self, invalid_header_ur_is):
        """Sets the invalid_header_ur_is of this CSVValidationModel.


        :param invalid_header_ur_is: The invalid_header_ur_is of this CSVValidationModel.  # noqa: E501
        :type: dict(str, str)
        """

        self._invalid_header_ur_is = invalid_header_ur_is

    @property
    def datatype_errors(self):
        """Gets the datatype_errors of this CSVValidationModel.  # noqa: E501


        :return: The datatype_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVDatatypeError])
        """
        return self._datatype_errors

    @datatype_errors.setter
    def datatype_errors(self, datatype_errors):
        """Sets the datatype_errors of this CSVValidationModel.


        :param datatype_errors: The datatype_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVDatatypeError])
        """

        self._datatype_errors = datatype_errors

    @property
    def uri_not_found_errors(self):
        """Gets the uri_not_found_errors of this CSVValidationModel.  # noqa: E501


        :return: The uri_not_found_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVURINotFoundError])
        """
        return self._uri_not_found_errors

    @uri_not_found_errors.setter
    def uri_not_found_errors(self, uri_not_found_errors):
        """Sets the uri_not_found_errors of this CSVValidationModel.


        :param uri_not_found_errors: The uri_not_found_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVURINotFoundError])
        """

        self._uri_not_found_errors = uri_not_found_errors

    @property
    def invalid_uri_errors(self):
        """Gets the invalid_uri_errors of this CSVValidationModel.  # noqa: E501


        :return: The invalid_uri_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_uri_errors

    @invalid_uri_errors.setter
    def invalid_uri_errors(self, invalid_uri_errors):
        """Sets the invalid_uri_errors of this CSVValidationModel.


        :param invalid_uri_errors: The invalid_uri_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_uri_errors = invalid_uri_errors

    @property
    def missing_required_value_errors(self):
        """Gets the missing_required_value_errors of this CSVValidationModel.  # noqa: E501


        :return: The missing_required_value_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._missing_required_value_errors

    @missing_required_value_errors.setter
    def missing_required_value_errors(self, missing_required_value_errors):
        """Sets the missing_required_value_errors of this CSVValidationModel.


        :param missing_required_value_errors: The missing_required_value_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._missing_required_value_errors = missing_required_value_errors

    @property
    def invalid_value_errors(self):
        """Gets the invalid_value_errors of this CSVValidationModel.  # noqa: E501


        :return: The invalid_value_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, list[CSVCell])
        """
        return self._invalid_value_errors

    @invalid_value_errors.setter
    def invalid_value_errors(self, invalid_value_errors):
        """Sets the invalid_value_errors of this CSVValidationModel.


        :param invalid_value_errors: The invalid_value_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, list[CSVCell])
        """

        self._invalid_value_errors = invalid_value_errors

    @property
    def already_existing_uri_errors(self):
        """Gets the already_existing_uri_errors of this CSVValidationModel.  # noqa: E501


        :return: The already_existing_uri_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, CSVCell)
        """
        return self._already_existing_uri_errors

    @already_existing_uri_errors.setter
    def already_existing_uri_errors(self, already_existing_uri_errors):
        """Sets the already_existing_uri_errors of this CSVValidationModel.


        :param already_existing_uri_errors: The already_existing_uri_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, CSVCell)
        """

        self._already_existing_uri_errors = already_existing_uri_errors

    @property
    def duplicate_uri_errors(self):
        """Gets the duplicate_uri_errors of this CSVValidationModel.  # noqa: E501


        :return: The duplicate_uri_errors of this CSVValidationModel.  # noqa: E501
        :rtype: dict(str, CSVDuplicateURIError)
        """
        return self._duplicate_uri_errors

    @duplicate_uri_errors.setter
    def duplicate_uri_errors(self, duplicate_uri_errors):
        """Sets the duplicate_uri_errors of this CSVValidationModel.


        :param duplicate_uri_errors: The duplicate_uri_errors of this CSVValidationModel.  # noqa: E501
        :type: dict(str, CSVDuplicateURIError)
        """

        self._duplicate_uri_errors = duplicate_uri_errors

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
        if issubclass(CSVValidationModel, dict):
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
        if not isinstance(other, CSVValidationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
