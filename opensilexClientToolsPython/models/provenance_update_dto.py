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


class ProvenanceUpdateDTO(object):
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
        'description': 'str',
        'prov_activity': 'list[ActivityCreationDTO]',
        'prov_agent': 'list[AgentModel]'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'description': 'description',
        'prov_activity': 'prov_activity',
        'prov_agent': 'prov_agent'
    }
    def __init__(self,
        uri : 'str',
        name : 'str',
        description : 'str' = None,
        prov_activity : 'List[ActivityCreationDTO]' = None,
        prov_agent : 'List[AgentModel]' = None):  # noqa: E501
        """ProvenanceUpdateDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._name = None
        self._description = None
        self._prov_activity = None
        self._prov_agent = None
        self.discriminator = None

        self.uri = uri
        self.name = name
        if description is not None:
            self.description = description
        if prov_activity is not None:
            self.prov_activity = prov_activity
        if prov_agent is not None:
            self.prov_agent = prov_agent

    @property
    def uri(self):
        """Gets the uri of this ProvenanceUpdateDTO.  # noqa: E501

        uri of the provenance being updated  # noqa: E501

        :return: The uri of this ProvenanceUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ProvenanceUpdateDTO.

        uri of the provenance being updated  # noqa: E501

        :param uri: The uri of this ProvenanceUpdateDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this ProvenanceUpdateDTO.  # noqa: E501

        provenance uri manually entered  # noqa: E501

        :return: The name of this ProvenanceUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvenanceUpdateDTO.

        provenance uri manually entered  # noqa: E501

        :param name: The name of this ProvenanceUpdateDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProvenanceUpdateDTO.  # noqa: E501

        provenance description  # noqa: E501

        :return: The description of this ProvenanceUpdateDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProvenanceUpdateDTO.

        provenance description  # noqa: E501

        :param description: The description of this ProvenanceUpdateDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def prov_activity(self):
        """Gets the prov_activity of this ProvenanceUpdateDTO.  # noqa: E501


        :return: The prov_activity of this ProvenanceUpdateDTO.  # noqa: E501
        :rtype: list[ActivityCreationDTO]
        """
        return self._prov_activity

    @prov_activity.setter
    def prov_activity(self, prov_activity):
        """Sets the prov_activity of this ProvenanceUpdateDTO.


        :param prov_activity: The prov_activity of this ProvenanceUpdateDTO.  # noqa: E501
        :type: list[ActivityCreationDTO]
        """

        self._prov_activity = prov_activity

    @property
    def prov_agent(self):
        """Gets the prov_agent of this ProvenanceUpdateDTO.  # noqa: E501


        :return: The prov_agent of this ProvenanceUpdateDTO.  # noqa: E501
        :rtype: list[AgentModel]
        """
        return self._prov_agent

    @prov_agent.setter
    def prov_agent(self, prov_agent):
        """Sets the prov_agent of this ProvenanceUpdateDTO.


        :param prov_agent: The prov_agent of this ProvenanceUpdateDTO.  # noqa: E501
        :type: list[AgentModel]
        """

        self._prov_agent = prov_agent

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
        if issubclass(ProvenanceUpdateDTO, dict):
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
        if not isinstance(other, ProvenanceUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.activity_creation_dto import ActivityCreationDTO
from opensilexClientToolsPython.models.agent_model import AgentModel


