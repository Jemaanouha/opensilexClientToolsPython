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


class EventGetDTO(object):
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
        'publisher': 'UserGetDTO',
        'rdf_type': 'str',
        'rdf_type_name': 'str',
        'start': 'str',
        'end': 'str',
        'is_instant': 'bool',
        'description': 'str',
        'targets': 'list[str]',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime'
    }

    attribute_map = {
        'uri': 'uri',
        'publisher': 'publisher',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'start': 'start',
        'end': 'end',
        'is_instant': 'is_instant',
        'description': 'description',
        'targets': 'targets',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date'
    }
    def __init__(self,
        uri : 'str' = None,
        publisher : 'UserGetDTO' = None,
        rdf_type : 'str' = None,
        rdf_type_name : 'str' = None,
        start : 'str' = None,
        end : 'str' = None,
        is_instant : 'bool' = None,
        description : 'str' = None,
        targets : 'List[str]' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None):  # noqa: E501
        """EventGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._publisher = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._start = None
        self._end = None
        self._is_instant = None
        self._description = None
        self._targets = None
        self._publication_date = None
        self._last_updated_date = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if publisher is not None:
            self.publisher = publisher
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if is_instant is not None:
            self.is_instant = is_instant
        if description is not None:
            self.description = description
        if targets is not None:
            self.targets = targets
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date

    @property
    def uri(self):
        """Gets the uri of this EventGetDTO.  # noqa: E501

        Event URI  # noqa: E501

        :return: The uri of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this EventGetDTO.

        Event URI  # noqa: E501

        :param uri: The uri of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def publisher(self):
        """Gets the publisher of this EventGetDTO.  # noqa: E501


        :return: The publisher of this EventGetDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this EventGetDTO.


        :param publisher: The publisher of this EventGetDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def rdf_type(self):
        """Gets the rdf_type of this EventGetDTO.  # noqa: E501

        Event type URI  # noqa: E501

        :return: The rdf_type of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this EventGetDTO.

        Event type URI  # noqa: E501

        :param rdf_type: The rdf_type of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this EventGetDTO.  # noqa: E501

        Event type name  # noqa: E501

        :return: The rdf_type_name of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this EventGetDTO.

        Event type name  # noqa: E501

        :param rdf_type_name: The rdf_type_name of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def start(self):
        """Gets the start of this EventGetDTO.  # noqa: E501

        Beginning of the event  # noqa: E501

        :return: The start of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventGetDTO.

        Beginning of the event  # noqa: E501

        :param start: The start of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this EventGetDTO.  # noqa: E501

        End of the event  # noqa: E501

        :return: The end of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EventGetDTO.

        End of the event  # noqa: E501

        :param end: The end of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def is_instant(self):
        """Gets the is_instant of this EventGetDTO.  # noqa: E501

        Indicate if the event is instant  # noqa: E501

        :return: The is_instant of this EventGetDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_instant

    @is_instant.setter
    def is_instant(self, is_instant):
        """Sets the is_instant of this EventGetDTO.

        Indicate if the event is instant  # noqa: E501

        :param is_instant: The is_instant of this EventGetDTO.  # noqa: E501
        :type: bool
        """

        self._is_instant = is_instant

    @property
    def description(self):
        """Gets the description of this EventGetDTO.  # noqa: E501

        Description of the event  # noqa: E501

        :return: The description of this EventGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventGetDTO.

        Description of the event  # noqa: E501

        :param description: The description of this EventGetDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def targets(self):
        """Gets the targets of this EventGetDTO.  # noqa: E501

        URI(s) of items concerned by this event  # noqa: E501

        :return: The targets of this EventGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this EventGetDTO.

        URI(s) of items concerned by this event  # noqa: E501

        :param targets: The targets of this EventGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def publication_date(self):
        """Gets the publication_date of this EventGetDTO.  # noqa: E501


        :return: The publication_date of this EventGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this EventGetDTO.


        :param publication_date: The publication_date of this EventGetDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this EventGetDTO.  # noqa: E501


        :return: The last_updated_date of this EventGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this EventGetDTO.


        :param last_updated_date: The last_updated_date of this EventGetDTO.  # noqa: E501
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
        if issubclass(EventGetDTO, dict):
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
        if not isinstance(other, EventGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.user_get_dto import UserGetDTO


