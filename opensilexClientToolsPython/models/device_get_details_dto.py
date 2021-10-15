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


class DeviceGetDetailsDTO(object):
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
        'rdf_type_name': 'str',
        'name': 'str',
        'brand': 'str',
        'constructor_model': 'str',
        'serial_number': 'str',
        'person_in_charge': 'str',
        'start_up': 'date',
        'removal': 'date',
        'relations': 'list[RDFObjectRelationDTO]',
        'description': 'str',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'uri': 'uri',
        'rdf_type': 'rdf_type',
        'rdf_type_name': 'rdf_type_name',
        'name': 'name',
        'brand': 'brand',
        'constructor_model': 'constructor_model',
        'serial_number': 'serial_number',
        'person_in_charge': 'person_in_charge',
        'start_up': 'start_up',
        'removal': 'removal',
        'relations': 'relations',
        'description': 'description',
        'metadata': 'metadata'
    }

    def __init__(self, uri=None, rdf_type=None, rdf_type_name=None, name=None, brand=None, constructor_model=None, serial_number=None, person_in_charge=None, start_up=None, removal=None, relations=None, description=None, metadata=None):  # noqa: E501
        """DeviceGetDetailsDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._rdf_type = None
        self._rdf_type_name = None
        self._name = None
        self._brand = None
        self._constructor_model = None
        self._serial_number = None
        self._person_in_charge = None
        self._start_up = None
        self._removal = None
        self._relations = None
        self._description = None
        self._metadata = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if rdf_type is not None:
            self.rdf_type = rdf_type
        if rdf_type_name is not None:
            self.rdf_type_name = rdf_type_name
        self.name = name
        if brand is not None:
            self.brand = brand
        if constructor_model is not None:
            self.constructor_model = constructor_model
        if serial_number is not None:
            self.serial_number = serial_number
        if person_in_charge is not None:
            self.person_in_charge = person_in_charge
        if start_up is not None:
            self.start_up = start_up
        if removal is not None:
            self.removal = removal
        if relations is not None:
            self.relations = relations
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata

    @property
    def uri(self):
        """Gets the uri of this DeviceGetDetailsDTO.  # noqa: E501


        :return: The uri of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DeviceGetDetailsDTO.


        :param uri: The uri of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def rdf_type(self):
        """Gets the rdf_type of this DeviceGetDetailsDTO.  # noqa: E501

        rdfType URI  # noqa: E501

        :return: The rdf_type of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type

    @rdf_type.setter
    def rdf_type(self, rdf_type):
        """Sets the rdf_type of this DeviceGetDetailsDTO.

        rdfType URI  # noqa: E501

        :param rdf_type: The rdf_type of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type = rdf_type

    @property
    def rdf_type_name(self):
        """Gets the rdf_type_name of this DeviceGetDetailsDTO.  # noqa: E501


        :return: The rdf_type_name of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._rdf_type_name

    @rdf_type_name.setter
    def rdf_type_name(self, rdf_type_name):
        """Sets the rdf_type_name of this DeviceGetDetailsDTO.


        :param rdf_type_name: The rdf_type_name of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._rdf_type_name = rdf_type_name

    @property
    def name(self):
        """Gets the name of this DeviceGetDetailsDTO.  # noqa: E501

        Device name  # noqa: E501

        :return: The name of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceGetDetailsDTO.

        Device name  # noqa: E501

        :param name: The name of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def brand(self):
        """Gets the brand of this DeviceGetDetailsDTO.  # noqa: E501

        Device brand  # noqa: E501

        :return: The brand of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this DeviceGetDetailsDTO.

        Device brand  # noqa: E501

        :param brand: The brand of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def constructor_model(self):
        """Gets the constructor_model of this DeviceGetDetailsDTO.  # noqa: E501

        Device model  # noqa: E501

        :return: The constructor_model of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._constructor_model

    @constructor_model.setter
    def constructor_model(self, constructor_model):
        """Sets the constructor_model of this DeviceGetDetailsDTO.

        Device model  # noqa: E501

        :param constructor_model: The constructor_model of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._constructor_model = constructor_model

    @property
    def serial_number(self):
        """Gets the serial_number of this DeviceGetDetailsDTO.  # noqa: E501

        Device serial number  # noqa: E501

        :return: The serial_number of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this DeviceGetDetailsDTO.

        Device serial number  # noqa: E501

        :param serial_number: The serial_number of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def person_in_charge(self):
        """Gets the person_in_charge of this DeviceGetDetailsDTO.  # noqa: E501

        Person in charge  # noqa: E501

        :return: The person_in_charge of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._person_in_charge

    @person_in_charge.setter
    def person_in_charge(self, person_in_charge):
        """Sets the person_in_charge of this DeviceGetDetailsDTO.

        Person in charge  # noqa: E501

        :param person_in_charge: The person_in_charge of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._person_in_charge = person_in_charge

    @property
    def start_up(self):
        """Gets the start_up of this DeviceGetDetailsDTO.  # noqa: E501

        Device date of start-up  # noqa: E501

        :return: The start_up of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: date
        """
        return self._start_up

    @start_up.setter
    def start_up(self, start_up):
        """Sets the start_up of this DeviceGetDetailsDTO.

        Device date of start-up  # noqa: E501

        :param start_up: The start_up of this DeviceGetDetailsDTO.  # noqa: E501
        :type: date
        """

        self._start_up = start_up

    @property
    def removal(self):
        """Gets the removal of this DeviceGetDetailsDTO.  # noqa: E501

        Device date of removal  # noqa: E501

        :return: The removal of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: date
        """
        return self._removal

    @removal.setter
    def removal(self, removal):
        """Sets the removal of this DeviceGetDetailsDTO.

        Device date of removal  # noqa: E501

        :param removal: The removal of this DeviceGetDetailsDTO.  # noqa: E501
        :type: date
        """

        self._removal = removal

    @property
    def relations(self):
        """Gets the relations of this DeviceGetDetailsDTO.  # noqa: E501


        :return: The relations of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: list[RDFObjectRelationDTO]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this DeviceGetDetailsDTO.


        :param relations: The relations of this DeviceGetDetailsDTO.  # noqa: E501
        :type: list[RDFObjectRelationDTO]
        """

        self._relations = relations

    @property
    def description(self):
        """Gets the description of this DeviceGetDetailsDTO.  # noqa: E501

        comment  # noqa: E501

        :return: The description of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceGetDetailsDTO.

        comment  # noqa: E501

        :param description: The description of this DeviceGetDetailsDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this DeviceGetDetailsDTO.  # noqa: E501


        :return: The metadata of this DeviceGetDetailsDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeviceGetDetailsDTO.


        :param metadata: The metadata of this DeviceGetDetailsDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

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
        if issubclass(DeviceGetDetailsDTO, dict):
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
        if not isinstance(other, DeviceGetDetailsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
