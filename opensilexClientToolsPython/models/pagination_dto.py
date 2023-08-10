# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: BUILD-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict




class PaginationDTO(object):
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
        'page_size': 'int',
        'current_page': 'int',
        'total_count': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'page_size': 'pageSize',
        'current_page': 'currentPage',
        'total_count': 'totalCount',
        'total_pages': 'totalPages'
    }
    def __init__(self,
        page_size : 'int' = None,
        current_page : 'int' = None,
        total_count : 'int' = None,
        total_pages : 'int' = None):  # noqa: E501
        """PaginationDTO - a model defined in Swagger"""  # noqa: E501

        self._page_size = None
        self._current_page = None
        self._total_count = None
        self._total_pages = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page
        if total_count is not None:
            self.total_count = total_count
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def page_size(self):
        """Gets the page_size of this PaginationDTO.  # noqa: E501


        :return: The page_size of this PaginationDTO.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PaginationDTO.


        :param page_size: The page_size of this PaginationDTO.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this PaginationDTO.  # noqa: E501


        :return: The current_page of this PaginationDTO.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this PaginationDTO.


        :param current_page: The current_page of this PaginationDTO.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def total_count(self):
        """Gets the total_count of this PaginationDTO.  # noqa: E501


        :return: The total_count of this PaginationDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginationDTO.


        :param total_count: The total_count of this PaginationDTO.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def total_pages(self):
        """Gets the total_pages of this PaginationDTO.  # noqa: E501


        :return: The total_pages of this PaginationDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PaginationDTO.


        :param total_pages: The total_pages of this PaginationDTO.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

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
        if issubclass(PaginationDTO, dict):
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
        if not isinstance(other, PaginationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

