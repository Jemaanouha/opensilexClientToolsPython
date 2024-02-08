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


class RDFPropertyGetDTO(object):
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
        'domain': 'str',
        'range': 'str',
        'parent': 'str',
        'name': 'str',
        'comment': 'str',
        'rdf_type': 'str',
        'name_translations': 'dict(str, str)',
        'comment_translations': 'dict(str, str)',
        'publisher': 'UserGetDTO',
        'publication_date': 'datetime',
        'last_updated_date': 'datetime',
        'domain_label': 'str',
        'range_label': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'domain': 'domain',
        'range': 'range',
        'parent': 'parent',
        'name': 'name',
        'comment': 'comment',
        'rdf_type': 'rdf_type',
        'name_translations': 'name_translations',
        'comment_translations': 'comment_translations',
        'publisher': 'publisher',
        'publication_date': 'publication_date',
        'last_updated_date': 'last_updated_date',
        'domain_label': 'domain_label',
        'range_label': 'range_label'
    }
    def __init__(self,
        uri : 'str',
        domain : 'str',
        range : 'str',
        rdf_type : 'str',
        name_translations : 'Dict[str, str]',
        comment_translations : 'Dict[str, str]',
        parent : 'str' = None,
        name : 'str' = None,
        comment : 'str' = None,
        publisher : 'UserGetDTO' = None,
        publication_date : 'datetime' = None,
        last_updated_date : 'datetime' = None,
        domain_label : 'str' = None,
        range_label : 'str' = None):  # noqa: E501
        """RDFPropertyGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._domain = None
        self._range = None
        self._parent = None
        self._name = None
        self._comment = None
        self._rdf_type = None
        self._name_translations = None
        self._comment_translations = None
        self._publisher = None
        self._publication_date = None
        self._last_updated_date = None
        self._domain_label = None
        self._range_label = None
        self.discriminator = None

        self.uri = uri
        self.domain = domain
        self.range = range
        if parent is not None:
            self.parent = parent
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        self.rdf_type = rdf_type
        self.name_translations = name_translations
        self.comment_translations = comment_translations
        if publisher is not None:
            self.publisher = publisher
        if publication_date is not None:
            self.publication_date = publication_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if domain_label is not None:
            self.domain_label = domain_label
        if range_label is not None:
            self.range_label = range_label

    @property
    def uri(self):
        """Gets the uri of this RDFPropertyGetDTO.  # noqa: E501

        URI of property  # noqa: E501

        :return: The uri of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this RDFPropertyGetDTO.

        URI of property  # noqa: E501

        :param uri: The uri of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def domain(self):
        """Gets the domain of this RDFPropertyGetDTO.  # noqa: E501

        Domain of the property : the rdf:type of any concept concerned by this property.  # noqa: E501

        :return: The domain of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RDFPropertyGetDTO.

        Domain of the property : the rdf:type of any concept concerned by this property.  # noqa: E501

        :param domain: The domain of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def range(self):
        """Gets the range of this RDFPropertyGetDTO.  # noqa: E501

        Range of the property : the rdf:type of any value(can be a literal type or a concept type) concerned by this property.  # noqa: E501

        :return: The range of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this RDFPropertyGetDTO.

        Range of the property : the rdf:type of any value(can be a literal type or a concept type) concerned by this property.  # noqa: E501

        :param range: The range of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """
        if range is None:
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def parent(self):
        """Gets the parent of this RDFPropertyGetDTO.  # noqa: E501

        Parent of the property.  # noqa: E501

        :return: The parent of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this RDFPropertyGetDTO.

        Parent of the property.  # noqa: E501

        :param parent: The parent of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def name(self):
        """Gets the name of this RDFPropertyGetDTO.  # noqa: E501

        Default property name according language  # noqa: E501

        :return: The name of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RDFPropertyGetDTO.

        Default property name according language  # noqa: E501

        :param name: The name of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this RDFPropertyGetDTO.  # noqa: E501

        Default property description according language  # noqa: E501

        :return: The comment of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this RDFPropertyGetDTO.

        Default property description according language  # noqa: E501

        :param comment: The comment of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def rdf_type(self):
        """Gets the rdf_type of this RDFPropertyGetDTO.  # noqa: E501

        The type of property  # noqa: E501

        :return: The rdf_type of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this RDFPropertyGetDTO.

        The type of property  # noqa: E501

        :param rdf_type: The rdf_type of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """
        if rdf_type is None:
            raise ValueError("Invalid value for `rdf_type`, must not be `None`")  # noqa: E501

        self._rdf_type = rdf_type

    @property
    def name_translations(self):
        """Gets the name_translations of this RDFPropertyGetDTO.  # noqa: E501

        Name by languages, at least one name/language is required. Use '' as language if no language is specified  # noqa: E501

        :return: The name_translations of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._name_translations

    @name_translations.setter
    def name_translations(self, name_translations):
        """Sets the name_translations of this RDFPropertyGetDTO.

        Name by languages, at least one name/language is required. Use '' as language if no language is specified  # noqa: E501

        :param name_translations: The name_translations of this RDFPropertyGetDTO.  # noqa: E501
        :type: dict(str, str)
        """
        if name_translations is None:
            raise ValueError("Invalid value for `name_translations`, must not be `None`")  # noqa: E501

        self._name_translations = name_translations

    @property
    def comment_translations(self):
        """Gets the comment_translations of this RDFPropertyGetDTO.  # noqa: E501

        Description by languages, at least one description/language is required. Use '' as language if no language is specified  # noqa: E501

        :return: The comment_translations of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._comment_translations

    @comment_translations.setter
    def comment_translations(self, comment_translations):
        """Sets the comment_translations of this RDFPropertyGetDTO.

        Description by languages, at least one description/language is required. Use '' as language if no language is specified  # noqa: E501

        :param comment_translations: The comment_translations of this RDFPropertyGetDTO.  # noqa: E501
        :type: dict(str, str)
        """
        if comment_translations is None:
            raise ValueError("Invalid value for `comment_translations`, must not be `None`")  # noqa: E501

        self._comment_translations = comment_translations

    @property
    def publisher(self):
        """Gets the publisher of this RDFPropertyGetDTO.  # noqa: E501


        :return: The publisher of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: UserGetDTO
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this RDFPropertyGetDTO.


        :param publisher: The publisher of this RDFPropertyGetDTO.  # noqa: E501
        :type: UserGetDTO
        """

        self._publisher = publisher

    @property
    def publication_date(self):
        """Gets the publication_date of this RDFPropertyGetDTO.  # noqa: E501


        :return: The publication_date of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this RDFPropertyGetDTO.


        :param publication_date: The publication_date of this RDFPropertyGetDTO.  # noqa: E501
        :type: datetime
        """

        self._publication_date = publication_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this RDFPropertyGetDTO.  # noqa: E501


        :return: The last_updated_date of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this RDFPropertyGetDTO.


        :param last_updated_date: The last_updated_date of this RDFPropertyGetDTO.  # noqa: E501
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def domain_label(self):
        """Gets the domain_label of this RDFPropertyGetDTO.  # noqa: E501


        :return: The domain_label of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._domain_label

    @domain_label.setter
    def domain_label(self, domain_label):
        """Sets the domain_label of this RDFPropertyGetDTO.


        :param domain_label: The domain_label of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """

        self._domain_label = domain_label

    @property
    def range_label(self):
        """Gets the range_label of this RDFPropertyGetDTO.  # noqa: E501


        :return: The range_label of this RDFPropertyGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._range_label

    @range_label.setter
    def range_label(self, range_label):
        """Sets the range_label of this RDFPropertyGetDTO.


        :param range_label: The range_label of this RDFPropertyGetDTO.  # noqa: E501
        :type: str
        """

        self._range_label = range_label

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
        if issubclass(RDFPropertyGetDTO, dict):
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
        if not isinstance(other, RDFPropertyGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.user_get_dto import UserGetDTO


