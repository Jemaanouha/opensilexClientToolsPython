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


class BrAPIv1ObservationUnitTreatmentDTO(object):
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
        'factor': 'str',
        'modality': 'str'
    }

    attribute_map = {
        'factor': 'factor',
        'modality': 'modality'
    }
    def __init__(self,
        factor : 'str' = None,
        modality : 'str' = None):  # noqa: E501
        """BrAPIv1ObservationUnitTreatmentDTO - a model defined in Swagger"""  # noqa: E501

        self._factor = None
        self._modality = None
        self.discriminator = None

        if factor is not None:
            self.factor = factor
        if modality is not None:
            self.modality = modality

    @property
    def factor(self):
        """Gets the factor of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501


        :return: The factor of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501
        :rtype: str
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this BrAPIv1ObservationUnitTreatmentDTO.


        :param factor: The factor of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501
        :type: str
        """

        self._factor = factor

    @property
    def modality(self):
        """Gets the modality of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501


        :return: The modality of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this BrAPIv1ObservationUnitTreatmentDTO.


        :param modality: The modality of this BrAPIv1ObservationUnitTreatmentDTO.  # noqa: E501
        :type: str
        """

        self._modality = modality

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
        if issubclass(BrAPIv1ObservationUnitTreatmentDTO, dict):
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
        if not isinstance(other, BrAPIv1ObservationUnitTreatmentDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other




