# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class CopyResourceDTO(object):
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
        'uris': 'list[str]',
        'shared_resource_instance': 'str'
    }

    attribute_map = {
        'uris': 'uris',
        'shared_resource_instance': 'sharedResourceInstance'
    }
    def __init__(self,
        uris : 'List[str]' = None,
        shared_resource_instance : 'str' = None):  # noqa: E501
        """CopyResourceDTO - a model defined in Swagger"""  # noqa: E501

        self._uris = None
        self._shared_resource_instance = None
        self.discriminator = None

        if uris is not None:
            self.uris = uris
        if shared_resource_instance is not None:
            self.shared_resource_instance = shared_resource_instance

    @property
    def uris(self):
        """Gets the uris of this CopyResourceDTO.  # noqa: E501


        :return: The uris of this CopyResourceDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this CopyResourceDTO.


        :param uris: The uris of this CopyResourceDTO.  # noqa: E501
        :type: list[str]
        """

        self._uris = uris

    @property
    def shared_resource_instance(self):
        """Gets the shared_resource_instance of this CopyResourceDTO.  # noqa: E501


        :return: The shared_resource_instance of this CopyResourceDTO.  # noqa: E501
        :rtype: str
        """
        return self._shared_resource_instance

    @shared_resource_instance.setter
    def shared_resource_instance(self, shared_resource_instance):
        """Sets the shared_resource_instance of this CopyResourceDTO.


        :param shared_resource_instance: The shared_resource_instance of this CopyResourceDTO.  # noqa: E501
        :type: str
        """

        self._shared_resource_instance = shared_resource_instance

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
        if issubclass(CopyResourceDTO, dict):
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
        if not isinstance(other, CopyResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




