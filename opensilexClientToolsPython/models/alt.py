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


class Alt(object):
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
        'default': 'RDFNode',
        'default_language': 'str',
        'default_boolean': 'bool',
        'default_byte': 'str',
        'default_short': 'int',
        'default_int': 'int',
        'default_long': 'int',
        'default_char': 'str',
        'default_float': 'float',
        'default_double': 'float',
        'default_string': 'str',
        'default_alt': 'Alt',
        'default_bag': 'Bag',
        'default_seq': 'Seq',
        'default_resource': 'Resource',
        'default_literal': 'Literal',
        'alt': 'bool',
        'seq': 'bool',
        'bag': 'bool',
        'id': 'AnonId',
        'name_space': 'str',
        'stmt_term': 'Statement',
        'uri': 'str',
        'local_name': 'str',
        'resource': 'bool',
        'model': 'Model',
        'literal': 'bool',
        'anon': 'bool',
        'uriresource': 'bool',
        'stmt_resource': 'bool'
    }

    attribute_map = {
        'default': 'default',
        'default_language': 'defaultLanguage',
        'default_boolean': 'defaultBoolean',
        'default_byte': 'defaultByte',
        'default_short': 'defaultShort',
        'default_int': 'defaultInt',
        'default_long': 'defaultLong',
        'default_char': 'defaultChar',
        'default_float': 'defaultFloat',
        'default_double': 'defaultDouble',
        'default_string': 'defaultString',
        'default_alt': 'defaultAlt',
        'default_bag': 'defaultBag',
        'default_seq': 'defaultSeq',
        'default_resource': 'defaultResource',
        'default_literal': 'defaultLiteral',
        'alt': 'alt',
        'seq': 'seq',
        'bag': 'bag',
        'id': 'id',
        'name_space': 'nameSpace',
        'stmt_term': 'stmtTerm',
        'uri': 'uri',
        'local_name': 'localName',
        'resource': 'resource',
        'model': 'model',
        'literal': 'literal',
        'anon': 'anon',
        'uriresource': 'uriresource',
        'stmt_resource': 'stmtResource'
    }
    def __init__(self,
        default : 'RDFNode' = None,
        default_language : 'str' = None,
        default_boolean : 'bool' = None,
        default_byte : 'str' = None,
        default_short : 'int' = None,
        default_int : 'int' = None,
        default_long : 'int' = None,
        default_char : 'str' = None,
        default_float : 'float' = None,
        default_double : 'float' = None,
        default_string : 'str' = None,
        default_alt : 'Alt' = None,
        default_bag : 'Bag' = None,
        default_seq : 'Seq' = None,
        default_resource : 'Resource' = None,
        default_literal : 'Literal' = None,
        alt : 'bool' = None,
        seq : 'bool' = None,
        bag : 'bool' = None,
        id : 'AnonId' = None,
        name_space : 'str' = None,
        stmt_term : 'Statement' = None,
        uri : 'str' = None,
        local_name : 'str' = None,
        resource : 'bool' = None,
        model : 'Model' = None,
        literal : 'bool' = None,
        anon : 'bool' = None,
        uriresource : 'bool' = None,
        stmt_resource : 'bool' = None):  # noqa: E501
        """Alt - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._default_language = None
        self._default_boolean = None
        self._default_byte = None
        self._default_short = None
        self._default_int = None
        self._default_long = None
        self._default_char = None
        self._default_float = None
        self._default_double = None
        self._default_string = None
        self._default_alt = None
        self._default_bag = None
        self._default_seq = None
        self._default_resource = None
        self._default_literal = None
        self._alt = None
        self._seq = None
        self._bag = None
        self._id = None
        self._name_space = None
        self._stmt_term = None
        self._uri = None
        self._local_name = None
        self._resource = None
        self._model = None
        self._literal = None
        self._anon = None
        self._uriresource = None
        self._stmt_resource = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if default_language is not None:
            self.default_language = default_language
        if default_boolean is not None:
            self.default_boolean = default_boolean
        if default_byte is not None:
            self.default_byte = default_byte
        if default_short is not None:
            self.default_short = default_short
        if default_int is not None:
            self.default_int = default_int
        if default_long is not None:
            self.default_long = default_long
        if default_char is not None:
            self.default_char = default_char
        if default_float is not None:
            self.default_float = default_float
        if default_double is not None:
            self.default_double = default_double
        if default_string is not None:
            self.default_string = default_string
        if default_alt is not None:
            self.default_alt = default_alt
        if default_bag is not None:
            self.default_bag = default_bag
        if default_seq is not None:
            self.default_seq = default_seq
        if default_resource is not None:
            self.default_resource = default_resource
        if default_literal is not None:
            self.default_literal = default_literal
        if alt is not None:
            self.alt = alt
        if seq is not None:
            self.seq = seq
        if bag is not None:
            self.bag = bag
        if id is not None:
            self.id = id
        if name_space is not None:
            self.name_space = name_space
        if stmt_term is not None:
            self.stmt_term = stmt_term
        if uri is not None:
            self.uri = uri
        if local_name is not None:
            self.local_name = local_name
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
    def default(self):
        """Gets the default of this Alt.  # noqa: E501


        :return: The default of this Alt.  # noqa: E501
        :rtype: RDFNode
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Alt.


        :param default: The default of this Alt.  # noqa: E501
        :type: RDFNode
        """

        self._default = default

    @property
    def default_language(self):
        """Gets the default_language of this Alt.  # noqa: E501


        :return: The default_language of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """Sets the default_language of this Alt.


        :param default_language: The default_language of this Alt.  # noqa: E501
        :type: str
        """

        self._default_language = default_language

    @property
    def default_boolean(self):
        """Gets the default_boolean of this Alt.  # noqa: E501


        :return: The default_boolean of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._default_boolean

    @default_boolean.setter
    def default_boolean(self, default_boolean):
        """Sets the default_boolean of this Alt.


        :param default_boolean: The default_boolean of this Alt.  # noqa: E501
        :type: bool
        """

        self._default_boolean = default_boolean

    @property
    def default_byte(self):
        """Gets the default_byte of this Alt.  # noqa: E501


        :return: The default_byte of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._default_byte

    @default_byte.setter
    def default_byte(self, default_byte):
        """Sets the default_byte of this Alt.


        :param default_byte: The default_byte of this Alt.  # noqa: E501
        :type: str
        """
        if default_byte is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', default_byte):  # noqa: E501
            raise ValueError(r"Invalid value for `default_byte`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._default_byte = default_byte

    @property
    def default_short(self):
        """Gets the default_short of this Alt.  # noqa: E501


        :return: The default_short of this Alt.  # noqa: E501
        :rtype: int
        """
        return self._default_short

    @default_short.setter
    def default_short(self, default_short):
        """Sets the default_short of this Alt.


        :param default_short: The default_short of this Alt.  # noqa: E501
        :type: int
        """

        self._default_short = default_short

    @property
    def default_int(self):
        """Gets the default_int of this Alt.  # noqa: E501


        :return: The default_int of this Alt.  # noqa: E501
        :rtype: int
        """
        return self._default_int

    @default_int.setter
    def default_int(self, default_int):
        """Sets the default_int of this Alt.


        :param default_int: The default_int of this Alt.  # noqa: E501
        :type: int
        """

        self._default_int = default_int

    @property
    def default_long(self):
        """Gets the default_long of this Alt.  # noqa: E501


        :return: The default_long of this Alt.  # noqa: E501
        :rtype: int
        """
        return self._default_long

    @default_long.setter
    def default_long(self, default_long):
        """Sets the default_long of this Alt.


        :param default_long: The default_long of this Alt.  # noqa: E501
        :type: int
        """

        self._default_long = default_long

    @property
    def default_char(self):
        """Gets the default_char of this Alt.  # noqa: E501


        :return: The default_char of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._default_char

    @default_char.setter
    def default_char(self, default_char):
        """Sets the default_char of this Alt.


        :param default_char: The default_char of this Alt.  # noqa: E501
        :type: str
        """

        self._default_char = default_char

    @property
    def default_float(self):
        """Gets the default_float of this Alt.  # noqa: E501


        :return: The default_float of this Alt.  # noqa: E501
        :rtype: float
        """
        return self._default_float

    @default_float.setter
    def default_float(self, default_float):
        """Sets the default_float of this Alt.


        :param default_float: The default_float of this Alt.  # noqa: E501
        :type: float
        """

        self._default_float = default_float

    @property
    def default_double(self):
        """Gets the default_double of this Alt.  # noqa: E501


        :return: The default_double of this Alt.  # noqa: E501
        :rtype: float
        """
        return self._default_double

    @default_double.setter
    def default_double(self, default_double):
        """Sets the default_double of this Alt.


        :param default_double: The default_double of this Alt.  # noqa: E501
        :type: float
        """

        self._default_double = default_double

    @property
    def default_string(self):
        """Gets the default_string of this Alt.  # noqa: E501


        :return: The default_string of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._default_string

    @default_string.setter
    def default_string(self, default_string):
        """Sets the default_string of this Alt.


        :param default_string: The default_string of this Alt.  # noqa: E501
        :type: str
        """

        self._default_string = default_string

    @property
    def default_alt(self):
        """Gets the default_alt of this Alt.  # noqa: E501


        :return: The default_alt of this Alt.  # noqa: E501
        :rtype: Alt
        """
        return self._default_alt

    @default_alt.setter
    def default_alt(self, default_alt):
        """Sets the default_alt of this Alt.


        :param default_alt: The default_alt of this Alt.  # noqa: E501
        :type: Alt
        """

        self._default_alt = default_alt

    @property
    def default_bag(self):
        """Gets the default_bag of this Alt.  # noqa: E501


        :return: The default_bag of this Alt.  # noqa: E501
        :rtype: Bag
        """
        return self._default_bag

    @default_bag.setter
    def default_bag(self, default_bag):
        """Sets the default_bag of this Alt.


        :param default_bag: The default_bag of this Alt.  # noqa: E501
        :type: Bag
        """

        self._default_bag = default_bag

    @property
    def default_seq(self):
        """Gets the default_seq of this Alt.  # noqa: E501


        :return: The default_seq of this Alt.  # noqa: E501
        :rtype: Seq
        """
        return self._default_seq

    @default_seq.setter
    def default_seq(self, default_seq):
        """Sets the default_seq of this Alt.


        :param default_seq: The default_seq of this Alt.  # noqa: E501
        :type: Seq
        """

        self._default_seq = default_seq

    @property
    def default_resource(self):
        """Gets the default_resource of this Alt.  # noqa: E501


        :return: The default_resource of this Alt.  # noqa: E501
        :rtype: Resource
        """
        return self._default_resource

    @default_resource.setter
    def default_resource(self, default_resource):
        """Sets the default_resource of this Alt.


        :param default_resource: The default_resource of this Alt.  # noqa: E501
        :type: Resource
        """

        self._default_resource = default_resource

    @property
    def default_literal(self):
        """Gets the default_literal of this Alt.  # noqa: E501


        :return: The default_literal of this Alt.  # noqa: E501
        :rtype: Literal
        """
        return self._default_literal

    @default_literal.setter
    def default_literal(self, default_literal):
        """Sets the default_literal of this Alt.


        :param default_literal: The default_literal of this Alt.  # noqa: E501
        :type: Literal
        """

        self._default_literal = default_literal

    @property
    def alt(self):
        """Gets the alt of this Alt.  # noqa: E501


        :return: The alt of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._alt

    @alt.setter
    def alt(self, alt):
        """Sets the alt of this Alt.


        :param alt: The alt of this Alt.  # noqa: E501
        :type: bool
        """

        self._alt = alt

    @property
    def seq(self):
        """Gets the seq of this Alt.  # noqa: E501


        :return: The seq of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._seq

    @seq.setter
    def seq(self, seq):
        """Sets the seq of this Alt.


        :param seq: The seq of this Alt.  # noqa: E501
        :type: bool
        """

        self._seq = seq

    @property
    def bag(self):
        """Gets the bag of this Alt.  # noqa: E501


        :return: The bag of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._bag

    @bag.setter
    def bag(self, bag):
        """Sets the bag of this Alt.


        :param bag: The bag of this Alt.  # noqa: E501
        :type: bool
        """

        self._bag = bag

    @property
    def id(self):
        """Gets the id of this Alt.  # noqa: E501


        :return: The id of this Alt.  # noqa: E501
        :rtype: AnonId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alt.


        :param id: The id of this Alt.  # noqa: E501
        :type: AnonId
        """

        self._id = id

    @property
    def name_space(self):
        """Gets the name_space of this Alt.  # noqa: E501


        :return: The name_space of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this Alt.


        :param name_space: The name_space of this Alt.  # noqa: E501
        :type: str
        """

        self._name_space = name_space

    @property
    def stmt_term(self):
        """Gets the stmt_term of this Alt.  # noqa: E501


        :return: The stmt_term of this Alt.  # noqa: E501
        :rtype: Statement
        """
        return self._stmt_term

    @stmt_term.setter
    def stmt_term(self, stmt_term):
        """Sets the stmt_term of this Alt.


        :param stmt_term: The stmt_term of this Alt.  # noqa: E501
        :type: Statement
        """

        self._stmt_term = stmt_term

    @property
    def uri(self):
        """Gets the uri of this Alt.  # noqa: E501


        :return: The uri of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Alt.


        :param uri: The uri of this Alt.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def local_name(self):
        """Gets the local_name of this Alt.  # noqa: E501


        :return: The local_name of this Alt.  # noqa: E501
        :rtype: str
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        """Sets the local_name of this Alt.


        :param local_name: The local_name of this Alt.  # noqa: E501
        :type: str
        """

        self._local_name = local_name

    @property
    def resource(self):
        """Gets the resource of this Alt.  # noqa: E501


        :return: The resource of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Alt.


        :param resource: The resource of this Alt.  # noqa: E501
        :type: bool
        """

        self._resource = resource

    @property
    def model(self):
        """Gets the model of this Alt.  # noqa: E501


        :return: The model of this Alt.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Alt.


        :param model: The model of this Alt.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def literal(self):
        """Gets the literal of this Alt.  # noqa: E501


        :return: The literal of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._literal

    @literal.setter
    def literal(self, literal):
        """Sets the literal of this Alt.


        :param literal: The literal of this Alt.  # noqa: E501
        :type: bool
        """

        self._literal = literal

    @property
    def anon(self):
        """Gets the anon of this Alt.  # noqa: E501


        :return: The anon of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._anon

    @anon.setter
    def anon(self, anon):
        """Sets the anon of this Alt.


        :param anon: The anon of this Alt.  # noqa: E501
        :type: bool
        """

        self._anon = anon

    @property
    def uriresource(self):
        """Gets the uriresource of this Alt.  # noqa: E501


        :return: The uriresource of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._uriresource

    @uriresource.setter
    def uriresource(self, uriresource):
        """Sets the uriresource of this Alt.


        :param uriresource: The uriresource of this Alt.  # noqa: E501
        :type: bool
        """

        self._uriresource = uriresource

    @property
    def stmt_resource(self):
        """Gets the stmt_resource of this Alt.  # noqa: E501


        :return: The stmt_resource of this Alt.  # noqa: E501
        :rtype: bool
        """
        return self._stmt_resource

    @stmt_resource.setter
    def stmt_resource(self, stmt_resource):
        """Sets the stmt_resource of this Alt.


        :param stmt_resource: The stmt_resource of this Alt.  # noqa: E501
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
        if issubclass(Alt, dict):
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
        if not isinstance(other, Alt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.rdf_node import RDFNode
from opensilexClientToolsPython.models.bag import Bag
from opensilexClientToolsPython.models.seq import Seq
from opensilexClientToolsPython.models.resource import Resource
from opensilexClientToolsPython.models.literal import Literal
from opensilexClientToolsPython.models.anon_id import AnonId
from opensilexClientToolsPython.models.statement import Statement
from opensilexClientToolsPython.models.model import Model


