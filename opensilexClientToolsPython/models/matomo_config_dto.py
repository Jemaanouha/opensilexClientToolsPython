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

from typing import List, Dict


class MatomoConfigDTO(object):
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
        'server_url': 'str',
        'site_id': 'int'
    }

    attribute_map = {
        'server_url': 'serverUrl',
        'site_id': 'siteId'
    }
    def __init__(self,
        server_url : 'str' = None,
        site_id : 'int' = None):  # noqa: E501
        """MatomoConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._server_url = None
        self._site_id = None
        self.discriminator = None

        if server_url is not None:
            self.server_url = server_url
        if site_id is not None:
            self.site_id = site_id

    @property
    def server_url(self):
        """Gets the server_url of this MatomoConfigDTO.  # noqa: E501


        :return: The server_url of this MatomoConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this MatomoConfigDTO.


        :param server_url: The server_url of this MatomoConfigDTO.  # noqa: E501
        :type: str
        """

        self._server_url = server_url

    @property
    def site_id(self):
        """Gets the site_id of this MatomoConfigDTO.  # noqa: E501


        :return: The site_id of this MatomoConfigDTO.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this MatomoConfigDTO.


        :param site_id: The site_id of this MatomoConfigDTO.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

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
        if issubclass(MatomoConfigDTO, dict):
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
        if not isinstance(other, MatomoConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




