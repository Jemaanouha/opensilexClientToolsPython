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


class DataUpdateDTO(object):
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
        'uri': 'str',
        '_date': 'str',
        'timezone': 'str',
        'target': 'str',
        'variable': 'str',
        'value': 'object',
        'confidence': 'float',
        'provenance': 'DataProvenanceModel',
        'metadata': 'dict(str, object)',
        'raw_data': 'list[object]'
    }

    attribute_map = {
        'uri': 'uri',
        '_date': 'date',
        'timezone': 'timezone',
        'target': 'target',
        'variable': 'variable',
        'value': 'value',
        'confidence': 'confidence',
        'provenance': 'provenance',
        'metadata': 'metadata',
        'raw_data': 'raw_data'
    }
    def __init__(self,
        uri : 'str',
        _date : 'str',
        variable : 'str',
        value : 'object',
        provenance : 'DataProvenanceModel',
        timezone : 'str' = None,
        target : 'str' = None,
        confidence : 'float' = None,
        metadata : 'Dict[str, object]' = None,
        raw_data : 'List[object]' = None):  # noqa: E501
        """DataUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self.__date = None
        self._timezone = None
        self._target = None
        self._variable = None
        self._value = None
        self._confidence = None
        self._provenance = None
        self._metadata = None
        self._raw_data = None
        self.discriminator = None

        self.uri = uri
        self._date = _date
        if timezone is not None:
            self.timezone = timezone
        if target is not None:
            self.target = target
        self.variable = variable
        self.value = value
        if confidence is not None:
            self.confidence = confidence
        self.provenance = provenance
        if metadata is not None:
            self.metadata = metadata
        if raw_data is not None:
            self.raw_data = raw_data

    @property
    def uri(self):
        """Gets the uri of this DataUpdateDTO.  # noqa: E501

        URI of the data being updated  # noqa: E501

        :return: The uri of this DataUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DataUpdateDTO.

        URI of the data being updated  # noqa: E501

        :param uri: The uri of this DataUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def _date(self):
        """Gets the _date of this DataUpdateDTO.  # noqa: E501

        date or datetime  # noqa: E501

        :return: The _date of this DataUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DataUpdateDTO.

        date or datetime  # noqa: E501

        :param _date: The _date of this DataUpdateDTO.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def timezone(self):
        """Gets the timezone of this DataUpdateDTO.  # noqa: E501

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :return: The timezone of this DataUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DataUpdateDTO.

        to specify if the offset is not in the date and if the timezone is different from the default one  # noqa: E501

        :param timezone: The timezone of this DataUpdateDTO.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def target(self):
        """Gets the target of this DataUpdateDTO.  # noqa: E501

        target URI on which the data have been collected (e.g. a scientific object)  # noqa: E501

        :return: The target of this DataUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this DataUpdateDTO.

        target URI on which the data have been collected (e.g. a scientific object)  # noqa: E501

        :param target: The target of this DataUpdateDTO.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def variable(self):
        """Gets the variable of this DataUpdateDTO.  # noqa: E501

        variable URI  # noqa: E501

        :return: The variable of this DataUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this DataUpdateDTO.

        variable URI  # noqa: E501

        :param variable: The variable of this DataUpdateDTO.  # noqa: E501
        :type: str
        """
        if variable is None:
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501

        self._variable = variable

    @property
    def value(self):
        """Gets the value of this DataUpdateDTO.  # noqa: E501

        can be decimal, integer, boolean, string or date  # noqa: E501

        :return: The value of this DataUpdateDTO.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DataUpdateDTO.

        can be decimal, integer, boolean, string or date  # noqa: E501

        :param value: The value of this DataUpdateDTO.  # noqa: E501
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def confidence(self):
        """Gets the confidence of this DataUpdateDTO.  # noqa: E501

        confidence index  # noqa: E501

        :return: The confidence of this DataUpdateDTO.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this DataUpdateDTO.

        confidence index  # noqa: E501

        :param confidence: The confidence of this DataUpdateDTO.  # noqa: E501
        :type: float
        """
        if confidence is not None and confidence > 1:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def provenance(self):
        """Gets the provenance of this DataUpdateDTO.  # noqa: E501


        :return: The provenance of this DataUpdateDTO.  # noqa: E501
        :rtype: DataProvenanceModel
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this DataUpdateDTO.


        :param provenance: The provenance of this DataUpdateDTO.  # noqa: E501
        :type: DataProvenanceModel
        """
        if provenance is None:
            raise ValueError("Invalid value for `provenance`, must not be `None`")  # noqa: E501

        self._provenance = provenance

    @property
    def metadata(self):
        """Gets the metadata of this DataUpdateDTO.  # noqa: E501

        key-value system to store additional information that can be used to query data  # noqa: E501

        :return: The metadata of this DataUpdateDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DataUpdateDTO.

        key-value system to store additional information that can be used to query data  # noqa: E501

        :param metadata: The metadata of this DataUpdateDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

    @property
    def raw_data(self):
        """Gets the raw_data of this DataUpdateDTO.  # noqa: E501

        list of repetition values  # noqa: E501

        :return: The raw_data of this DataUpdateDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this DataUpdateDTO.

        list of repetition values  # noqa: E501

        :param raw_data: The raw_data of this DataUpdateDTO.  # noqa: E501
        :type: list[object]
        """

        self._raw_data = raw_data

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
        if issubclass(DataUpdateDTO, dict):
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
        if issubclass(DataUpdateDTO, dict):
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
        if not isinstance(other, DataUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.data_provenance_model import DataProvenanceModel


