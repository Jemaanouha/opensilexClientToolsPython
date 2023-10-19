# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.factors_api import FactorsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestFactorsApi(unittest.TestCase):
    """FactorsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.factors_api.FactorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_factors(self):
        """Test case for count_factors

        Count factors  # noqa: E501
        """
        pass

    def test_create_factor(self):
        """Test case for create_factor

        Create a factor  # noqa: E501
        """
        pass

    def test_delete_factor(self):
        """Test case for delete_factor

        Delete a factor  # noqa: E501
        """
        pass

    def test_delete_factor_level(self):
        """Test case for delete_factor_level

        Delete a factor level  # noqa: E501
        """
        pass

    def test_get_factor_associated_experiments(self):
        """Test case for get_factor_associated_experiments

        Get factor associated experiments  # noqa: E501
        """
        pass

    def test_get_factor_by_uri(self):
        """Test case for get_factor_by_uri

        Get a factor  # noqa: E501
        """
        pass

    def test_get_factor_level(self):
        """Test case for get_factor_level

        Get a factor level  # noqa: E501
        """
        pass

    def test_get_factor_level_detail(self):
        """Test case for get_factor_level_detail

        Get a factor level  # noqa: E501
        """
        pass

    def test_get_factor_levels(self):
        """Test case for get_factor_levels

        Get factor levels  # noqa: E501
        """
        pass

    def test_get_factors_by_ur_is(self):
        """Test case for get_factors_by_ur_is

        Get a list of factors by their URIs  # noqa: E501
        """
        pass

    def test_search_categories(self):
        """Test case for search_categories

        Search categories  # noqa: E501
        """
        pass

    def test_search_factor_levels(self):
        """Test case for search_factor_levels

        Search factors levels  # noqa: E501
        """
        pass

    def test_search_factors(self):
        """Test case for search_factors

        Search factors  # noqa: E501
        """
        pass

    def test_update_factor(self):
        """Test case for update_factor

        Update a factor  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
