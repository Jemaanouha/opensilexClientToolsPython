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
from opensilexClientToolsPython.api.security_api import SecurityApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.security_api.SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_group(self):
        """Test case for create_group

        Add a group  # noqa: E501
        """
        pass

    def test_create_profile(self):
        """Test case for create_profile

        Add a profile  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Add an user  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete a group  # noqa: E501
        """
        pass

    def test_delete_profile(self):
        """Test case for delete_profile

        Delete a profile  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Delete an user  # noqa: E501
        """
        pass

    def test_get_all_profiles(self):
        """Test case for get_all_profiles

        Get all profiles  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get a group  # noqa: E501
        """
        pass

    def test_get_groups_by_uri(self):
        """Test case for get_groups_by_uri

        Get groups by their URIs  # noqa: E501
        """
        pass

    def test_get_profile(self):
        """Test case for get_profile

        Get a profile  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get an user  # noqa: E501
        """
        pass

    def test_get_user_groups(self):
        """Test case for get_user_groups

        Get groups of an user  # noqa: E501
        """
        pass

    def test_get_users_by_uri(self):
        """Test case for get_users_by_uri

        Get users by their URIs  # noqa: E501
        """
        pass

    def test_search_groups(self):
        """Test case for search_groups

        Search groups  # noqa: E501
        """
        pass

    def test_search_profiles(self):
        """Test case for search_profiles

        Search profiles  # noqa: E501
        """
        pass

    def test_search_users(self):
        """Test case for search_users

        Search users  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update a group  # noqa: E501
        """
        pass

    def test_update_profile(self):
        """Test case for update_profile

        Update a profile  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update an user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
