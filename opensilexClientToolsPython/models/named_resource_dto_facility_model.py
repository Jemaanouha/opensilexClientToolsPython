# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class NamedResourceDTOFacilityModel(object):
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
        'name': 'str',
        'rdf_type': 'str',
        'rdf_type_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name'
    }
    def __init__(self,
        uri : 'str' = None,
        name : 'str' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None):  # noqa: E501
        """NamedResourceDTOFacilityModel - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._rdf_type = None
        self._rdf_type_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name

    @property
    def uri(self):
        """Gets the uri of this NamedResourceDTOFacilityModel.  # noqa: E501


        :return: The uri of this NamedResourceDTOFacilityModel.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this NamedResourceDTOFacilityModel.


        :param uri: The uri of this NamedResourceDTOFacilityModel.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this NamedResourceDTOFacilityModel.  # noqa: E501


        :return: The name of this NamedResourceDTOFacilityModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NamedResourceDTOFacilityModel.


        :param name: The name of this NamedResourceDTOFacilityModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rdf_type(self):
        """Gets the rdf_type of this NamedResourceDTOFacilityModel.  # noqa: E501


        :return: The rdf_type of this NamedResourceDTOFacilityModel.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this NamedResourceDTOFacilityModel.


        :param rdf_type: The rdf_type of this NamedResourceDTOFacilityModel.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this NamedResourceDTOFacilityModel.  # noqa: E501


        :return: The rdf_type_name of this NamedResourceDTOFacilityModel.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this NamedResourceDTOFacilityModel.


        :param rdf_type_name: The rdf_type_name of this NamedResourceDTOFacilityModel.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

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
        if issubclass(NamedResourceDTOFacilityModel, dict):
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
        if not isinstance(other, NamedResourceDTOFacilityModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

