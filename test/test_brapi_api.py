# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.2-rdg
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.brapi_api import BRAPIApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestBRAPIApi(unittest.TestCase):
    """BRAPIApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.brapi_api.BRAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_calls(self):
        """Test case for get_calls

        Check the available BrAPI calls  # noqa: E501
        """
        pass

    def test_get_germplasm_by_search(self):
        """Test case for get_germplasm_by_search

        Submit a search request for germplasm (type accession in OpenSILEX  # noqa: E501
        """
        pass

    def test_get_observation_units(self):
        """Test case for get_observation_units

        List all the observation units measured in the study.  # noqa: E501
        """
        pass

    def test_get_observation_variables(self):
        """Test case for get_observation_variables

        List all the observation variables measured in the study.  # noqa: E501
        """
        pass

    def test_get_observations(self):
        """Test case for get_observations

        Get the observations associated to a specific study  # noqa: E501
        """
        pass

    def test_get_studies(self):
        """Test case for get_studies

        Retrieve studies information  # noqa: E501
        """
        pass

    def test_get_studies_search(self):
        """Test case for get_studies_search

        Retrieve studies information  # noqa: E501
        """
        pass

    def test_get_study_details(self):
        """Test case for get_study_details

        Retrieve study details  # noqa: E501
        """
        pass

    def test_get_variable_details(self):
        """Test case for get_variable_details

        Retrieve variable details by id  # noqa: E501
        """
        pass

    def test_get_variables_list(self):
        """Test case for get_variables_list

        BrAPIv1CallDTO to retrieve a list of observationVariables available in the system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
