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


class Literal(object):
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
        'string': 'str',
        'boolean': 'bool',
        'byte': 'str',
        'short': 'int',
        'char': 'str',
        '_int': 'int',
        'long': 'int',
        '_float': 'float',
        'double': 'float',
        'value': 'object',
        'language': 'str',
        'datatype': 'RDFDatatype',
        'datatype_uri': 'str',
        'lexical_form': 'str',
        'well_formed_xml': 'bool',
        'resource': 'bool',
        'model': 'Model',
        'literal': 'bool',
        'anon': 'bool',
        'uriresource': 'bool',
        'stmt_resource': 'bool'
    }

    attribute_map = {
        'string': 'string',
        'boolean': 'boolean',
        'byte': 'byte',
        'short': 'short',
        'char': 'char',
        '_int': 'int',
        'long': 'long',
        '_float': 'float',
        'double': 'double',
        'value': 'value',
        'language': 'language',
        'datatype': 'datatype',
        'datatype_uri': 'datatypeURI',
        'lexical_form': 'lexicalForm',
        'well_formed_xml': 'wellFormedXML',
        'resource': 'resource',
        'model': 'model',
        'literal': 'literal',
        'anon': 'anon',
        'uriresource': 'uriresource',
        'stmt_resource': 'stmtResource'
    }
    def __init__(self,
        string : 'str' = None,
        boolean : 'bool' = None,
        byte : 'str' = None,
        short : 'int' = None,
        char : 'str' = None,
        _int : 'int' = None,
        long : 'int' = None,
        _float : 'float' = None,
        double : 'float' = None,
        value : 'object' = None,
        language : 'str' = None,
        datatype : 'RDFDatatype' = None,
        datatype_uri : 'str' = None,
        lexical_form : 'str' = None,
        well_formed_xml : 'bool' = None,
        resource : 'bool' = None,
        model : 'Model' = None,
        literal : 'bool' = None,
        anon : 'bool' = None,
        uriresource : 'bool' = None,
        stmt_resource : 'bool' = None):  # noqa: E501
        """Literal - a model defined in Swagger"""  # noqa: E501

        self._string = None
        self._boolean = None
        self._byte = None
        self._short = None
        self._char = None
        self.__int = None
        self._long = None
        self.__float = None
        self._double = None
        self._value = None
        self._language = None
        self._datatype = None
        self._datatype_uri = None
        self._lexical_form = None
        self._well_formed_xml = None
        self._resource = None
        self._model = None
        self._literal = None
        self._anon = None
        self._uriresource = None
        self._stmt_resource = None
        self.discriminator = None

        if string is not None:
            self.string = string
        if boolean is not None:
            self.boolean = boolean
        if byte is not None:
            self.byte = byte
        if short is not None:
            self.short = short
        if char is not None:
            self.char = char
        if _int is not None:
            self._int = _int
        if long is not None:
            self.long = long
        if _float is not None:
            self._float = _float
        if double is not None:
            self.double = double
        if value is not None:
            self.value = value
        if language is not None:
            self.language = language
        if datatype is not None:
            self.datatype = datatype
        if datatype_uri is not None:
            self.datatype_uri = datatype_uri
        if lexical_form is not None:
            self.lexical_form = lexical_form
        if well_formed_xml is not None:
            self.well_formed_xml = well_formed_xml
        if resource is not None:
            self.resource = resource
        if model is not None:
            self.model = model
        if literal is not None:
            self.literal = literal
        if anon is not None:
            self.anon = anon
        if uriresource is not None:
            self.uriresource = uriresource
        if stmt_resource is not None:
            self.stmt_resource = stmt_resource

    @property
    def string(self):
        """Gets the string of this Literal.  # noqa: E501


        :return: The string of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this Literal.


        :param string: The string of this Literal.  # noqa: E501
        :type: str
        """

        self._string = string

    @property
    def boolean(self):
        """Gets the boolean of this Literal.  # noqa: E501


        :return: The boolean of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """Sets the boolean of this Literal.


        :param boolean: The boolean of this Literal.  # noqa: E501
        :type: bool
        """

        self._boolean = boolean

    @property
    def byte(self):
        """Gets the byte of this Literal.  # noqa: E501


        :return: The byte of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._byte

    @byte.setter
    def byte(self, byte):
        """Sets the byte of this Literal.


        :param byte: The byte of this Literal.  # noqa: E501
        :type: str
        """
        if byte is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', byte):  # noqa: E501
            raise ValueError(r"Invalid value for `byte`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._byte = byte

    @property
    def short(self):
        """Gets the short of this Literal.  # noqa: E501


        :return: The short of this Literal.  # noqa: E501
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this Literal.


        :param short: The short of this Literal.  # noqa: E501
        :type: int
        """

        self._short = short

    @property
    def char(self):
        """Gets the char of this Literal.  # noqa: E501


        :return: The char of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._char

    @char.setter
    def char(self, char):
        """Sets the char of this Literal.


        :param char: The char of this Literal.  # noqa: E501
        :type: str
        """

        self._char = char

    @property
    def _int(self):
        """Gets the _int of this Literal.  # noqa: E501


        :return: The _int of this Literal.  # noqa: E501
        :rtype: int
        """
        return self.__int

    @_int.setter
    def _int(self, _int):
        """Sets the _int of this Literal.


        :param _int: The _int of this Literal.  # noqa: E501
        :type: int
        """

        self.__int = _int

    @property
    def long(self):
        """Gets the long of this Literal.  # noqa: E501


        :return: The long of this Literal.  # noqa: E501
        :rtype: int
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this Literal.


        :param long: The long of this Literal.  # noqa: E501
        :type: int
        """

        self._long = long

    @property
    def _float(self):
        """Gets the _float of this Literal.  # noqa: E501


        :return: The _float of this Literal.  # noqa: E501
        :rtype: float
        """
        return self.__float

    @_float.setter
    def _float(self, _float):
        """Sets the _float of this Literal.


        :param _float: The _float of this Literal.  # noqa: E501
        :type: float
        """

        self.__float = _float

    @property
    def double(self):
        """Gets the double of this Literal.  # noqa: E501


        :return: The double of this Literal.  # noqa: E501
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this Literal.


        :param double: The double of this Literal.  # noqa: E501
        :type: float
        """

        self._double = double

    @property
    def value(self):
        """Gets the value of this Literal.  # noqa: E501


        :return: The value of this Literal.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Literal.


        :param value: The value of this Literal.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def language(self):
        """Gets the language of this Literal.  # noqa: E501


        :return: The language of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Literal.


        :param language: The language of this Literal.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def datatype(self):
        """Gets the datatype of this Literal.  # noqa: E501


        :return: The datatype of this Literal.  # noqa: E501
        :rtype: RDFDatatype
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this Literal.


        :param datatype: The datatype of this Literal.  # noqa: E501
        :type: RDFDatatype
        """

        self._datatype = datatype

    @property
    def datatype_uri(self):
        """Gets the datatype_uri of this Literal.  # noqa: E501


        :return: The datatype_uri of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._datatype_uri

    @datatype_uri.setter
    def datatype_uri(self, datatype_uri):
        """Sets the datatype_uri of this Literal.


        :param datatype_uri: The datatype_uri of this Literal.  # noqa: E501
        :type: str
        """

        self._datatype_uri = datatype_uri

    @property
    def lexical_form(self):
        """Gets the lexical_form of this Literal.  # noqa: E501


        :return: The lexical_form of this Literal.  # noqa: E501
        :rtype: str
        """
        return self._lexical_form

    @lexical_form.setter
    def lexical_form(self, lexical_form):
        """Sets the lexical_form of this Literal.


        :param lexical_form: The lexical_form of this Literal.  # noqa: E501
        :type: str
        """

        self._lexical_form = lexical_form

    @property
    def well_formed_xml(self):
        """Gets the well_formed_xml of this Literal.  # noqa: E501


        :return: The well_formed_xml of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._well_formed_xml

    @well_formed_xml.setter
    def well_formed_xml(self, well_formed_xml):
        """Sets the well_formed_xml of this Literal.


        :param well_formed_xml: The well_formed_xml of this Literal.  # noqa: E501
        :type: bool
        """

        self._well_formed_xml = well_formed_xml

    @property
    def resource(self):
        """Gets the resource of this Literal.  # noqa: E501


        :return: The resource of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Literal.


        :param resource: The resource of this Literal.  # noqa: E501
        :type: bool
        """

        self._resource = resource

    @property
    def model(self):
        """Gets the model of this Literal.  # noqa: E501


        :return: The model of this Literal.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Literal.


        :param model: The model of this Literal.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def literal(self):
        """Gets the literal of this Literal.  # noqa: E501


        :return: The literal of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this Literal.


        :param literal: The literal of this Literal.  # noqa: E501
        :type: bool
        """

        self._literal = literal

    @property
    def anon(self):
        """Gets the anon of this Literal.  # noqa: E501


        :return: The anon of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this Literal.


        :param anon: The anon of this Literal.  # noqa: E501
        :type: bool
        """

        self._anon = anon

    @property
    def uriresource(self):
        """Gets the uriresource of this Literal.  # noqa: E501


        :return: The uriresource of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._uriresource

    @uriresource.setter
    def uriresource(self, uriresource):
        """Sets the uriresource of this Literal.


        :param uriresource: The uriresource of this Literal.  # noqa: E501
        :type: bool
        """

        self._uriresource = uriresource

    @property
    def stmt_resource(self):
        """Gets the stmt_resource of this Literal.  # noqa: E501


        :return: The stmt_resource of this Literal.  # noqa: E501
        :rtype: bool
        """
        return self._stmt_resource

    @stmt_resource.setter
    def stmt_resource(self, stmt_resource):
        """Sets the stmt_resource of this Literal.


        :param stmt_resource: The stmt_resource of this Literal.  # noqa: E501
        :type: bool
        """

        self._stmt_resource = stmt_resource

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
        if issubclass(Literal, dict):
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
        if not isinstance(other, Literal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_datatype import RDFDatatype
from opensilexClientToolsPython.models.model import Model


