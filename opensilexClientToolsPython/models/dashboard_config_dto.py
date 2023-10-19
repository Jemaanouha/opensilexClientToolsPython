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


class DashboardConfigDTO(object):
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
        'show_metrics': 'bool',
        'graph1': 'GraphConfigDTO',
        'graph2': 'GraphConfigDTO',
        'graph3': 'GraphConfigDTO'
    }

    attribute_map = {
        'show_metrics': 'showMetrics',
        'graph1': 'graph1',
        'graph2': 'graph2',
        'graph3': 'graph3'
    }
    def __init__(self,
        show_metrics : 'bool' = None,
        graph1 : 'GraphConfigDTO' = None,
        graph2 : 'GraphConfigDTO' = None,
        graph3 : 'GraphConfigDTO' = None):  # noqa: E501
        """DashboardConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._show_metrics = None
        self._graph1 = None
        self._graph2 = None
        self._graph3 = None
        self.discriminator = None

        if show_metrics is not None:
            self.show_metrics = show_metrics
        if graph1 is not None:
            self.graph1 = graph1
        if graph2 is not None:
            self.graph2 = graph2
        if graph3 is not None:
            self.graph3 = graph3

    @property
    def show_metrics(self):
        """Gets the show_metrics of this DashboardConfigDTO.  # noqa: E501


        :return: The show_metrics of this DashboardConfigDTO.  # noqa: E501
        :rtype: bool
        """
        return self._show_metrics

    @show_metrics.setter
    def show_metrics(self, show_metrics):
        """Sets the show_metrics of this DashboardConfigDTO.


        :param show_metrics: The show_metrics of this DashboardConfigDTO.  # noqa: E501
        :type: bool
        """

        self._show_metrics = show_metrics

    @property
    def graph1(self):
        """Gets the graph1 of this DashboardConfigDTO.  # noqa: E501


        :return: The graph1 of this DashboardConfigDTO.  # noqa: E501
        :rtype: GraphConfigDTO
        """
        return self._graph1

    @graph1.setter
    def graph1(self, graph1):
        """Sets the graph1 of this DashboardConfigDTO.


        :param graph1: The graph1 of this DashboardConfigDTO.  # noqa: E501
        :type: GraphConfigDTO
        """

        self._graph1 = graph1

    @property
    def graph2(self):
        """Gets the graph2 of this DashboardConfigDTO.  # noqa: E501


        :return: The graph2 of this DashboardConfigDTO.  # noqa: E501
        :rtype: GraphConfigDTO
        """
        return self._graph2

    @graph2.setter
    def graph2(self, graph2):
        """Sets the graph2 of this DashboardConfigDTO.


        :param graph2: The graph2 of this DashboardConfigDTO.  # noqa: E501
        :type: GraphConfigDTO
        """

        self._graph2 = graph2

    @property
    def graph3(self):
        """Gets the graph3 of this DashboardConfigDTO.  # noqa: E501


        :return: The graph3 of this DashboardConfigDTO.  # noqa: E501
        :rtype: GraphConfigDTO
        """
        return self._graph3

    @graph3.setter
    def graph3(self, graph3):
        """Sets the graph3 of this DashboardConfigDTO.


        :param graph3: The graph3 of this DashboardConfigDTO.  # noqa: E501
        :type: GraphConfigDTO
        """

        self._graph3 = graph3

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
        if issubclass(DashboardConfigDTO, dict):
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
        if not isinstance(other, DashboardConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.graph_config_dto import GraphConfigDTO
from opensilexClientToolsPython.models.graph_config_dto import GraphConfigDTO
from opensilexClientToolsPython.models.graph_config_dto import GraphConfigDTO


