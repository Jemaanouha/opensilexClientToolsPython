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


class Method(object):
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
        'description': 'str',
        'formula': 'str',
        'method_db_id': 'str',
        'method_name': 'str',
        'ontology_reference': 'OntologyReference',
        'reference': 'str',
        '_class': 'str'
    }

    attribute_map = {
        'description': 'description',
        'formula': 'formula',
        'method_db_id': 'methodDbId',
        'method_name': 'methodName',
        'ontology_reference': 'ontologyReference',
        'reference': 'reference',
        '_class': 'class'
    }
    def __init__(self,
        description : 'str' = None,
        formula : 'str' = None,
        method_db_id : 'str' = None,
        method_name : 'str' = None,
        ontology_reference : 'OntologyReference' = None,
        reference : 'str' = None,
        _class : 'str' = None):  # noqa: E501
        """Method - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._formula = None
        self._method_db_id = None
        self._method_name = None
        self._ontology_reference = None
        self._reference = None
        self.__class = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if formula is not None:
            self.formula = formula
        if method_db_id is not None:
            self.method_db_id = method_db_id
        if method_name is not None:
            self.method_name = method_name
        if ontology_reference is not None:
            self.ontology_reference = ontology_reference
        if reference is not None:
            self.reference = reference
        if _class is not None:
            self._class = _class

    @property
    def description(self):
        """Gets the description of this Method.  # noqa: E501


        :return: The description of this Method.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Method.


        :param description: The description of this Method.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def formula(self):
        """Gets the formula of this Method.  # noqa: E501


        :return: The formula of this Method.  # noqa: E501
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this Method.


        :param formula: The formula of this Method.  # noqa: E501
        :type: str
        """

        self._formula = formula

    @property
    def method_db_id(self):
        """Gets the method_db_id of this Method.  # noqa: E501


        :return: The method_db_id of this Method.  # noqa: E501
        :rtype: str
        """
        return self._method_db_id

    @method_db_id.setter
    def method_db_id(self, method_db_id):
        """Sets the method_db_id of this Method.


        :param method_db_id: The method_db_id of this Method.  # noqa: E501
        :type: str
        """

        self._method_db_id = method_db_id

    @property
    def method_name(self):
        """Gets the method_name of this Method.  # noqa: E501


        :return: The method_name of this Method.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this Method.


        :param method_name: The method_name of this Method.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def ontology_reference(self):
        """Gets the ontology_reference of this Method.  # noqa: E501


        :return: The ontology_reference of this Method.  # noqa: E501
        :rtype: OntologyReference
        """
        return self._ontology_reference

    @ontology_reference.setter
    def ontology_reference(self, ontology_reference):
        """Sets the ontology_reference of this Method.


        :param ontology_reference: The ontology_reference of this Method.  # noqa: E501
        :type: OntologyReference
        """

        self._ontology_reference = ontology_reference

    @property
    def reference(self):
        """Gets the reference of this Method.  # noqa: E501


        :return: The reference of this Method.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Method.


        :param reference: The reference of this Method.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def _class(self):
        """Gets the _class of this Method.  # noqa: E501


        :return: The _class of this Method.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Method.


        :param _class: The _class of this Method.  # noqa: E501
        :type: str
        """

        self.__class = _class

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
        if issubclass(Method, dict):
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
        if not isinstance(other, Method):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.ontology_reference import OntologyReference


