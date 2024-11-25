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


class EventCreationDTO(object):
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
        'start': 'str',
        'end': 'str',
        'is_instant': 'bool',
        'description': 'str',
        'targets': 'list[str]',
        'relations': 'list[RDFObjectRelationDTO]',
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'start': 'start',
        'end': 'end',
        'is_instant': 'is_instant',
        'description': 'description',
        'targets': 'targets',
        'relations': 'relations',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date'
    }
    def __init__(self,
        is_instant : 'bool',
        targets : 'List[str]',
        uri : 'str' = None,
        rdf_type : 'str' = None,
        start : 'str' = None,
        end : 'str' = None,
        description : 'str' = None,
        relations : 'List[RDFObjectRelationDTO]' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None):  # noqa: E501
        """EventCreationDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._start = None
        self._end = None
        self._is_instant = None
        self._description = None
        self._targets = None
        self._relations = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        self.is_instant = is_instant
        if description is not None:
            self.description = description
        self.targets = targets
        if relations is not None:
            self.relations = relations
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date

    @property
    def uri(self):
        """Gets the uri of this EventCreationDTO.  # noqa: E501


        :return: The uri of this EventCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventCreationDTO.


        :param uri: The uri of this EventCreationDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this EventCreationDTO.  # noqa: E501

        Event type URI  # noqa: E501

        :return: The rdf_type of this EventCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this EventCreationDTO.

        Event type URI  # noqa: E501

        :param rdf_type: The rdf_type of this EventCreationDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def start(self):
        """Gets the start of this EventCreationDTO.  # noqa: E501


        :return: The start of this EventCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventCreationDTO.


        :param start: The start of this EventCreationDTO.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this EventCreationDTO.  # noqa: E501


        :return: The end of this EventCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EventCreationDTO.


        :param end: The end of this EventCreationDTO.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def is_instant(self):
        """Gets the is_instant of this EventCreationDTO.  # noqa: E501

        Indicate if the event is instant  # noqa: E501

        :return: The is_instant of this EventCreationDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_instant

    @is_instant.setter
    def is_instant(self, is_instant):
        """Sets the is_instant of this EventCreationDTO.

        Indicate if the event is instant  # noqa: E501

        :param is_instant: The is_instant of this EventCreationDTO.  # noqa: E501
        :type: bool
        """
        if is_instant is None:
            raise ValueError("Invalid value for `is_instant`, must not be `None`")  # noqa: E501

        self._is_instant = is_instant

    @property
    def description(self):
        """Gets the description of this EventCreationDTO.  # noqa: E501


        :return: The description of this EventCreationDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventCreationDTO.


        :param description: The description of this EventCreationDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def targets(self):
        """Gets the targets of this EventCreationDTO.  # noqa: E501

        URI(s) of items concerned by this event  # noqa: E501

        :return: The targets of this EventCreationDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this EventCreationDTO.

        URI(s) of items concerned by this event  # noqa: E501

        :param targets: The targets of this EventCreationDTO.  # noqa: E501
        :type: list[str]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def relations(self):
        """Gets the relations of this EventCreationDTO.  # noqa: E501


        :return: The relations of this EventCreationDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this EventCreationDTO.


        :param relations: The relations of this EventCreationDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def publisher(self):
        """Gets the publisher of this EventCreationDTO.  # noqa: E501


        :return: The publisher of this EventCreationDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this EventCreationDTO.


        :param publisher: The publisher of this EventCreationDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this EventCreationDTO.  # noqa: E501


        :return: The publication_date of this EventCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this EventCreationDTO.


        :param publication_date: The publication_date of this EventCreationDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this EventCreationDTO.  # noqa: E501


        :return: The last_updated_date of this EventCreationDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this EventCreationDTO.


        :param last_updated_date: The last_updated_date of this EventCreationDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

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
        if issubclass(EventCreationDTO, dict):
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
        if issubclass(EventCreationDTO, dict):
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
        if not isinstance(other, EventCreationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO
from opensilexClientToolsPython.models.user_get_dto import UserGetDTO


