# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.organizations_api import OrganizationsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.organizations_api.OrganizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_infrastructure(self):
        """Test case for create_infrastructure

        Create an organisation  # noqa: E501
        """
        pass

    def test_create_infrastructure_facility(self):
        """Test case for create_infrastructure_facility

        Create a facility  # noqa: E501
        """
        pass

    def test_create_site(self):
        """Test case for create_site

        Create a site  # noqa: E501
        """
        pass

    def test_delete_infrastructure(self):
        """Test case for delete_infrastructure

        Delete an organisation  # noqa: E501
        """
        pass

    def test_delete_infrastructure_facility(self):
        """Test case for delete_infrastructure_facility

        Delete a facility  # noqa: E501
        """
        pass

    def test_delete_site(self):
        """Test case for delete_site

        Delete a site  # noqa: E501
        """
        pass

    def test_get_all_facilities(self):
        """Test case for get_all_facilities

        Get all facilities  # noqa: E501
        """
        pass

    def test_get_facilities_by_uri(self):
        """Test case for get_facilities_by_uri

        Get facilities by their URIs  # noqa: E501
        """
        pass

    def test_get_infrastructure(self):
        """Test case for get_infrastructure

        Get an organisation   # noqa: E501
        """
        pass

    def test_get_infrastructure_facility(self):
        """Test case for get_infrastructure_facility

        Get a facility  # noqa: E501
        """
        pass

    def test_get_site(self):
        """Test case for get_site

        Get a site  # noqa: E501
        """
        pass

    def test_get_sites_by_uri(self):
        """Test case for get_sites_by_uri

        Get a list of sites  # noqa: E501
        """
        pass

    def test_search_infrastructure_facilities(self):
        """Test case for search_infrastructure_facilities

        Search facilities  # noqa: E501
        """
        pass

    def test_search_infrastructures(self):
        """Test case for search_infrastructures

        Search organisations  # noqa: E501
        """
        pass

    def test_search_sites(self):
        """Test case for search_sites

        Search all sites  # noqa: E501
        """
        pass

    def test_update_infrastructure(self):
        """Test case for update_infrastructure

        Update an organisation  # noqa: E501
        """
        pass

    def test_update_infrastructure_facility(self):
        """Test case for update_infrastructure_facility

        Update a facility  # noqa: E501
        """
        pass

    def test_update_site(self):
        """Test case for update_site

        Update a site  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
