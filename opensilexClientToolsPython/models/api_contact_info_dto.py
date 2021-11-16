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


class ApiContactInfoDTO(object):
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
        'name': 'str',
        'email': 'str',
        'homepage': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'homepage': 'homepage'
    }

    def __init__(self, name=None, email=None, homepage=None):  # noqa: E501
        """ApiContactInfoDTO - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._email = None
        self._homepage = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if homepage is not None:
            self.homepage = homepage

    @property
    def name(self):
        """Gets the name of this ApiContactInfoDTO.  # noqa: E501

        Opensilex Team  # noqa: E501

        :return: The name of this ApiContactInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiContactInfoDTO.

        Opensilex Team  # noqa: E501

        :param name: The name of this ApiContactInfoDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this ApiContactInfoDTO.  # noqa: E501

        opensilex@gmail.com  # noqa: E501

        :return: The email of this ApiContactInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApiContactInfoDTO.

        opensilex@gmail.com  # noqa: E501

        :param email: The email of this ApiContactInfoDTO.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def homepage(self):
        """Gets the homepage of this ApiContactInfoDTO.  # noqa: E501


        :return: The homepage of this ApiContactInfoDTO.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this ApiContactInfoDTO.


        :param homepage: The homepage of this ApiContactInfoDTO.  # noqa: E501
        :type: str
        """

        self._homepage = homepage

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
        if issubclass(ApiContactInfoDTO, dict):
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
        if not isinstance(other, ApiContactInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
