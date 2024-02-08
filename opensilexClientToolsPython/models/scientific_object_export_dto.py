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


class ScientificObjectExportDTO(object):
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
        'included_uris': 'list[str]',
        'page': 'int',
        'lang': 'str',
        'order_by': 'list[OrderBy]',
        'page_size': 'int',
        'uris': 'list[str]',
        'excluded_uris': 'list[str]',
        'experiment': 'str',
        'rdf_types': 'list[str]',
        'name': 'str',
        'parent': 'str',
        'germplasm': 'list[str]',
        'factor_levels': 'list[str]',
        'facility': 'str',
        'existence_date': 'str',
        'creation_date': 'str'
    }

    attribute_map = {
        'included_uris': 'includedUris',
        'page': 'page',
        'lang': 'lang',
        'order_by': 'order_by',
        'page_size': 'page_size',
        'uris': 'uris',
        'excluded_uris': 'excluded_uris',
        'experiment': 'experiment',
        'rdf_types': 'rdf_types',
        'name': 'name',
        'parent': 'parent',
        'germplasm': 'germplasm',
        'factor_levels': 'factor_levels',
        'facility': 'facility',
        'existence_date': 'existence_date',
        'creation_date': 'creation_date'
    }
    def __init__(self,
        included_uris : 'List[str]' = None,
        page : 'int' = None,
        lang : 'str' = None,
        order_by : 'List[OrderBy]' = None,
        page_size : 'int' = None,
        uris : 'List[str]' = None,
        excluded_uris : 'List[str]' = None,
        experiment : 'str' = None,
        rdf_types : 'List[str]' = None,
        name : 'str' = None,
        parent : 'str' = None,
        germplasm : 'List[str]' = None,
        factor_levels : 'List[str]' = None,
        facility : 'str' = None,
        existence_date : 'str' = None,
        creation_date : 'str' = None):  # noqa: E501
        """ScientificObjectExportDTO - a model defined in Swagger"""  # noqa: E501

        self._included_uris = None
        self._page = None
        self._lang = None
        self._order_by = None
        self._page_size = None
        self._uris = None
        self._excluded_uris = None
        self._experiment = None
        self._rdf_types = None
        self._name = None
        self._parent = None
        self._germplasm = None
        self._factor_levels = None
        self._facility = None
        self._existence_date = None
        self._creation_date = None
        self.discriminator = None

        if included_uris is not None:
            self.included_uris = included_uris
        if page is not None:
            self.page = page
        if lang is not None:
            self.lang = lang
        if order_by is not None:
            self.order_by = order_by
        if page_size is not None:
            self.page_size = page_size
        if uris is not None:
            self.uris = uris
        if excluded_uris is not None:
            self.excluded_uris = excluded_uris
        if experiment is not None:
            self.experiment = experiment
        if rdf_types is not None:
            self.rdf_types = rdf_types
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if germplasm is not None:
            self.germplasm = germplasm
        if factor_levels is not None:
            self.factor_levels = factor_levels
        if facility is not None:
            self.facility = facility
        if existence_date is not None:
            self.existence_date = existence_date
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def included_uris(self):
        """Gets the included_uris of this ScientificObjectExportDTO.  # noqa: E501


        :return: The included_uris of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_uris

    @included_uris.setter
    def included_uris(self, included_uris):
        """Sets the included_uris of this ScientificObjectExportDTO.


        :param included_uris: The included_uris of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._included_uris = included_uris

    @property
    def page(self):
        """Gets the page of this ScientificObjectExportDTO.  # noqa: E501

        Page number  # noqa: E501

        :return: The page of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ScientificObjectExportDTO.

        Page number  # noqa: E501

        :param page: The page of this ScientificObjectExportDTO.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def lang(self):
        """Gets the lang of this ScientificObjectExportDTO.  # noqa: E501


        :return: The lang of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this ScientificObjectExportDTO.


        :param lang: The lang of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._lang = lang

    @property
    def order_by(self):
        """Gets the order_by of this ScientificObjectExportDTO.  # noqa: E501

        List of fields to sort as an array of fieldName=asc|desc  # noqa: E501

        :return: The order_by of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[OrderBy]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ScientificObjectExportDTO.

        List of fields to sort as an array of fieldName=asc|desc  # noqa: E501

        :param order_by: The order_by of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[OrderBy]
        """

        self._order_by = order_by

    @property
    def page_size(self):
        """Gets the page_size of this ScientificObjectExportDTO.  # noqa: E501

        Page size  # noqa: E501

        :return: The page_size of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ScientificObjectExportDTO.

        Page size  # noqa: E501

        :param page_size: The page_size of this ScientificObjectExportDTO.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def uris(self):
        """Gets the uris of this ScientificObjectExportDTO.  # noqa: E501


        :return: The uris of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this ScientificObjectExportDTO.


        :param uris: The uris of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._uris = uris

    @property
    def excluded_uris(self):
        """Gets the excluded_uris of this ScientificObjectExportDTO.  # noqa: E501


        :return: The excluded_uris of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_uris

    @excluded_uris.setter
    def excluded_uris(self, excluded_uris):
        """Sets the excluded_uris of this ScientificObjectExportDTO.


        :param excluded_uris: The excluded_uris of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._excluded_uris = excluded_uris

    @property
    def experiment(self):
        """Gets the experiment of this ScientificObjectExportDTO.  # noqa: E501


        :return: The experiment of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ScientificObjectExportDTO.


        :param experiment: The experiment of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._experiment = experiment

    @property
    def rdf_types(self):
        """Gets the rdf_types of this ScientificObjectExportDTO.  # noqa: E501


        :return: The rdf_types of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._rdf_types

    @rdf_types.setter
    def rdf_types(self, rdf_types):
        """Sets the rdf_types of this ScientificObjectExportDTO.


        :param rdf_types: The rdf_types of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._rdf_types = rdf_types

    @property
    def name(self):
        """Gets the name of this ScientificObjectExportDTO.  # noqa: E501


        :return: The name of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScientificObjectExportDTO.


        :param name: The name of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ScientificObjectExportDTO.  # noqa: E501


        :return: The parent of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ScientificObjectExportDTO.


        :param parent: The parent of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def germplasm(self):
        """Gets the germplasm of this ScientificObjectExportDTO.  # noqa: E501


        :return: The germplasm of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._germplasm

    @germplasm.setter
    def germplasm(self, germplasm):
        """Sets the germplasm of this ScientificObjectExportDTO.


        :param germplasm: The germplasm of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._germplasm = germplasm

    @property
    def factor_levels(self):
        """Gets the factor_levels of this ScientificObjectExportDTO.  # noqa: E501


        :return: The factor_levels of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._factor_levels

    @factor_levels.setter
    def factor_levels(self, factor_levels):
        """Sets the factor_levels of this ScientificObjectExportDTO.


        :param factor_levels: The factor_levels of this ScientificObjectExportDTO.  # noqa: E501
        :type: list[str]
        """

        self._factor_levels = factor_levels

    @property
    def facility(self):
        """Gets the facility of this ScientificObjectExportDTO.  # noqa: E501


        :return: The facility of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this ScientificObjectExportDTO.


        :param facility: The facility of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._facility = facility

    @property
    def existence_date(self):
        """Gets the existence_date of this ScientificObjectExportDTO.  # noqa: E501


        :return: The existence_date of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._existence_date

    @existence_date.setter
    def existence_date(self, existence_date):
        """Sets the existence_date of this ScientificObjectExportDTO.


        :param existence_date: The existence_date of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._existence_date = existence_date

    @property
    def creation_date(self):
        """Gets the creation_date of this ScientificObjectExportDTO.  # noqa: E501


        :return: The creation_date of this ScientificObjectExportDTO.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ScientificObjectExportDTO.


        :param creation_date: The creation_date of this ScientificObjectExportDTO.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

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
        if issubclass(ScientificObjectExportDTO, dict):
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
        if not isinstance(other, ScientificObjectExportDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.order_by import OrderBy


