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




class ApiGitCommitDTO(object):
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
        'commit_id': 'str',
        'commit_message': 'str'
    }

    attribute_map = {
        'commit_id': 'commit_id',
        'commit_message': 'commit_message'
    }
    def __init__(self,
        commit_id : 'str' = None,
        commit_message : 'str' = None):  # noqa: E501
        """ApiGitCommitDTO - a model defined in Swagger"""  # noqa: E501

        self._commit_id = None
        self._commit_message = None
        self.discriminator = None

        if commit_id is not None:
            self.commit_id = commit_id
        if commit_message is not None:
            self.commit_message = commit_message

    @property
    def commit_id(self):
        """Gets the commit_id of this ApiGitCommitDTO.  # noqa: E501


        :return: The commit_id of this ApiGitCommitDTO.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ApiGitCommitDTO.


        :param commit_id: The commit_id of this ApiGitCommitDTO.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def commit_message(self):
        """Gets the commit_message of this ApiGitCommitDTO.  # noqa: E501


        :return: The commit_message of this ApiGitCommitDTO.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this ApiGitCommitDTO.


        :param commit_message: The commit_message of this ApiGitCommitDTO.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

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
        if issubclass(ApiGitCommitDTO, dict):
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
        if not isinstance(other, ApiGitCommitDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

