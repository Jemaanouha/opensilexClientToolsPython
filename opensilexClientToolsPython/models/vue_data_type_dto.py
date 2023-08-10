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




class VueDataTypeDTO(object):
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
        'short_uri': 'str',
        'input_component': 'str',
        'view_component': 'str',
        'label_key': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'short_uri': 'short_uri',
        'input_component': 'input_component',
        'view_component': 'view_component',
        'label_key': 'label_key'
    }
    def __init__(self,
        uri : 'str' = None,
        short_uri : 'str' = None,
        input_component : 'str' = None,
        view_component : 'str' = None,
        label_key : 'str' = None):  # noqa: E501
        """VueDataTypeDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._short_uri = None
        self._input_component = None
        self._view_component = None
        self._label_key = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if short_uri is not None:
            self.short_uri = short_uri
        if input_component is not None:
            self.input_component = input_component
        if view_component is not None:
            self.view_component = view_component
        if label_key is not None:
            self.label_key = label_key

    @property
    def uri(self):
        """Gets the uri of this VueDataTypeDTO.  # noqa: E501


        :return: The uri of this VueDataTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VueDataTypeDTO.


        :param uri: The uri of this VueDataTypeDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def short_uri(self):
        """Gets the short_uri of this VueDataTypeDTO.  # noqa: E501


        :return: The short_uri of this VueDataTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._short_uri

    @short_uri.setter
    def short_uri(self, short_uri):
        """Sets the short_uri of this VueDataTypeDTO.


        :param short_uri: The short_uri of this VueDataTypeDTO.  # noqa: E501
        :type: str
        """

        self._short_uri = short_uri

    @property
    def input_component(self):
        """Gets the input_component of this VueDataTypeDTO.  # noqa: E501


        :return: The input_component of this VueDataTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._input_component

    @input_component.setter
    def input_component(self, input_component):
        """Sets the input_component of this VueDataTypeDTO.


        :param input_component: The input_component of this VueDataTypeDTO.  # noqa: E501
        :type: str
        """

        self._input_component = input_component

    @property
    def view_component(self):
        """Gets the view_component of this VueDataTypeDTO.  # noqa: E501


        :return: The view_component of this VueDataTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._view_component

    @view_component.setter
    def view_component(self, view_component):
        """Sets the view_component of this VueDataTypeDTO.


        :param view_component: The view_component of this VueDataTypeDTO.  # noqa: E501
        :type: str
        """

        self._view_component = view_component

    @property
    def label_key(self):
        """Gets the label_key of this VueDataTypeDTO.  # noqa: E501


        :return: The label_key of this VueDataTypeDTO.  # noqa: E501
        :rtype: str
        """
        return self._label_key

    @label_key.setter
    def label_key(self, label_key):
        """Sets the label_key of this VueDataTypeDTO.


        :param label_key: The label_key of this VueDataTypeDTO.  # noqa: E501
        :type: str
        """

        self._label_key = label_key

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
        if issubclass(VueDataTypeDTO, dict):
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
        if not isinstance(other, VueDataTypeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

