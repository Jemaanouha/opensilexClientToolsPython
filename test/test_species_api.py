# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.species_api import SpeciesApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestSpeciesApi(unittest.TestCase):
    """SpeciesApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.species_api.SpeciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_species(self):
        """Test case for get_all_species

        get species (no pagination)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
