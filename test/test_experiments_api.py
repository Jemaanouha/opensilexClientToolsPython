# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+5.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.experiments_api import ExperimentsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestExperimentsApi(unittest.TestCase):
    """ExperimentsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.experiments_api.ExperimentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_experiment(self):
        """Test case for create_experiment

        Add an experiment  # noqa: E501
        """
        pass

    def test_delete_experiment(self):
        """Test case for delete_experiment

        Delete an experiment  # noqa: E501
        """
        pass

    def test_export_experiment_data_list(self):
        """Test case for export_experiment_data_list

        export experiment data  # noqa: E501
        """
        pass

    def test_get_available_facilities(self):
        """Test case for get_available_facilities

        Get facilities available for an experiment  # noqa: E501
        """
        pass

    def test_get_available_factors(self):
        """Test case for get_available_factors

        Get factors with their levels associated to an experiment  # noqa: E501
        """
        pass

    def test_get_available_species(self):
        """Test case for get_available_species

        Get species present in an experiment  # noqa: E501
        """
        pass

    def test_get_experiment(self):
        """Test case for get_experiment

        Get an experiment  # noqa: E501
        """
        pass

    def test_get_experiments_by_ur_is(self):
        """Test case for get_experiments_by_ur_is

        Get experiments URIs  # noqa: E501
        """
        pass

    def test_get_used_variables1(self):
        """Test case for get_used_variables1

        Get variables involved in an experiment  # noqa: E501
        """
        pass

    def test_import_csv_data1(self):
        """Test case for import_csv_data1

        Import a CSV file for the given experiment URI and scientific object type.  # noqa: E501
        """
        pass

    def test_search_experiment_data_list(self):
        """Test case for search_experiment_data_list

        Search data  # noqa: E501
        """
        pass

    def test_search_experiment_provenances(self):
        """Test case for search_experiment_provenances

        Get provenances involved in an experiment  # noqa: E501
        """
        pass

    def test_search_experiments(self):
        """Test case for search_experiments

        Search experiments  # noqa: E501
        """
        pass

    def test_update_experiment(self):
        """Test case for update_experiment

        Update an experiment  # noqa: E501
        """
        pass

    def test_validate_csv2(self):
        """Test case for validate_csv2

        Import a CSV file for the given experiment URI and scientific object type.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
