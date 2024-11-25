# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.area_api import AreaApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestAreaApi(unittest.TestCase):
    """AreaApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.area_api.AreaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_area(self):
        """Test case for create_area

        Add an area  # noqa: E501
        """
        pass

    def test_delete_area(self):
        """Test case for delete_area

        Delete an area  # noqa: E501
        """
        pass

    def test_export_geospatial(self):
        """Test case for export_geospatial

        Export a given list of areas URIs to shapefile  # noqa: E501
        """
        pass

    def test_get_by_uri(self):
        """Test case for get_by_uri

        Get an area  # noqa: E501
        """
        pass

    def test_search_intersects(self):
        """Test case for search_intersects

        Get area whose geometry corresponds to the Intersections  # noqa: E501
        """
        pass

    def test_update_area(self):
        """Test case for update_area

        Update an area  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
