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




class AgentModel(object):
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
        'rdf_type': 'str',
        'settings': 'dict(str, object)'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'settings': 'settings'
    }
    def __init__(self, uri : 'str' = None, rdf_type : 'str' = None, settings : Dict[str, 'object'] = None):  # noqa: E501
        """AgentModel - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._settings = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if settings is not None:
            self.settings = settings

    @property
    def uri(self):
        """Gets the uri of this AgentModel.  # noqa: E501

        agent uri  # noqa: E501

        :return: The uri of this AgentModel.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AgentModel.

        agent uri  # noqa: E501

        :param uri: The uri of this AgentModel.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this AgentModel.  # noqa: E501

        activity type defined in the ontology  # noqa: E501

        :return: The rdf_type of this AgentModel.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this AgentModel.

        activity type defined in the ontology  # noqa: E501

        :param rdf_type: The rdf_type of this AgentModel.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def settings(self):
        """Gets the settings of this AgentModel.  # noqa: E501

        a key value system to store agent parameters  # noqa: E501

        :return: The settings of this AgentModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AgentModel.

        a key value system to store agent parameters  # noqa: E501

        :param settings: The settings of this AgentModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._settings = settings

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
        if issubclass(AgentModel, dict):
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
        if not isinstance(other, AgentModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

