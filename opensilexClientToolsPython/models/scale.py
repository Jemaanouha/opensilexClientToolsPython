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

from opensilexClientToolsPython.models.ontology_reference import OntologyReference



class Scale(object):
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
        'data_type': 'str',
        'decimal_places': 'str',
        'name': 'str',
        'ontology_reference': 'OntologyReference',
        'scale_db_id': 'str',
        'scale_name': 'str',
        'valid_values': 'str',
        'xref': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'decimal_places': 'decimalPlaces',
        'name': 'name',
        'ontology_reference': 'ontologyReference',
        'scale_db_id': 'scaleDbId',
        'scale_name': 'scaleName',
        'valid_values': 'validValues',
        'xref': 'xref'
    }
    def __init__(self, data_type : 'str' = None, decimal_places : 'str' = None, name : 'str' = None, ontology_reference : 'OntologyReference' = None, scale_db_id : 'str' = None, scale_name : 'str' = None, valid_values : 'str' = None, xref : 'str' = None):  # noqa: E501
        """Scale - a model defined in Swagger"""  # noqa: E501

        self._data_type = None
        self._decimal_places = None
        self._name = None
        self._ontology_reference = None
        self._scale_db_id = None
        self._scale_name = None
        self._valid_values = None
        self._xref = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if name is not None:
            self.name = name
        if ontology_reference is not None:
            self.ontology_reference = ontology_reference
        if scale_db_id is not None:
            self.scale_db_id = scale_db_id
        if scale_name is not None:
            self.scale_name = scale_name
        if valid_values is not None:
            self.valid_values = valid_values
        if xref is not None:
            self.xref = xref

    @property
    def data_type(self):
        """Gets the data_type of this Scale.  # noqa: E501


        :return: The data_type of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Scale.


        :param data_type: The data_type of this Scale.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def decimal_places(self):
        """Gets the decimal_places of this Scale.  # noqa: E501


        :return: The decimal_places of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this Scale.


        :param decimal_places: The decimal_places of this Scale.  # noqa: E501
        :type: str
        """

        self._decimal_places = decimal_places

    @property
    def name(self):
        """Gets the name of this Scale.  # noqa: E501


        :return: The name of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scale.


        :param name: The name of this Scale.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ontology_reference(self):
        """Gets the ontology_reference of this Scale.  # noqa: E501


        :return: The ontology_reference of this Scale.  # noqa: E501
        :rtype: OntologyReference
        """
        return self._ontology_reference

    @ontology_reference.setter
    def ontology_reference(self, ontology_reference):
        """Sets the ontology_reference of this Scale.


        :param ontology_reference: The ontology_reference of this Scale.  # noqa: E501
        :type: OntologyReference
        """

        self._ontology_reference = ontology_reference

    @property
    def scale_db_id(self):
        """Gets the scale_db_id of this Scale.  # noqa: E501


        :return: The scale_db_id of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._scale_db_id

    @scale_db_id.setter
    def scale_db_id(self, scale_db_id):
        """Sets the scale_db_id of this Scale.


        :param scale_db_id: The scale_db_id of this Scale.  # noqa: E501
        :type: str
        """

        self._scale_db_id = scale_db_id

    @property
    def scale_name(self):
        """Gets the scale_name of this Scale.  # noqa: E501


        :return: The scale_name of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._scale_name

    @scale_name.setter
    def scale_name(self, scale_name):
        """Sets the scale_name of this Scale.


        :param scale_name: The scale_name of this Scale.  # noqa: E501
        :type: str
        """

        self._scale_name = scale_name

    @property
    def valid_values(self):
        """Gets the valid_values of this Scale.  # noqa: E501


        :return: The valid_values of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        """Sets the valid_values of this Scale.


        :param valid_values: The valid_values of this Scale.  # noqa: E501
        :type: str
        """

        self._valid_values = valid_values

    @property
    def xref(self):
        """Gets the xref of this Scale.  # noqa: E501


        :return: The xref of this Scale.  # noqa: E501
        :rtype: str
        """
        return self._xref

    @xref.setter
    def xref(self, xref):
        """Sets the xref of this Scale.


        :param xref: The xref of this Scale.  # noqa: E501
        :type: str
        """

        self._xref = xref

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
        if issubclass(Scale, dict):
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
        if not isinstance(other, Scale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

