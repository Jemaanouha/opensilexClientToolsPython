# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientToolsPython
from opensilexClientToolsPython.api.scientific_objects_api import ScientificObjectsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestScientificObjectsApi(unittest.TestCase):
    """ScientificObjectsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.scientific_objects_api.ScientificObjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_scientific_objects(self):
        """Test case for count_scientific_objects

        Count scientific objects  # noqa: E501
        """
        pass

    def test_create_scientific_object(self):
        """Test case for create_scientific_object

        Create a scientific object for the given experiment  # noqa: E501
        """
        pass

    def test_delete_scientific_object(self):
        """Test case for delete_scientific_object

        Delete a scientific object  # noqa: E501
        """
        pass

    def test_export_csv(self):
        """Test case for export_csv

        Export a given list of scientific object URIs to csv data file  # noqa: E501
        """
        pass

    def test_export_geospatial2(self):
        """Test case for export_geospatial2

        Export a given list of scientific object URIs to shapefile or geojson  # noqa: E501
        """
        pass

    def test_get_scientific_object_data_files_provenances(self):
        """Test case for get_scientific_object_data_files_provenances

        Get provenances of datafiles linked to this scientific object  # noqa: E501
        """
        pass

    def test_get_scientific_object_data_provenances(self):
        """Test case for get_scientific_object_data_provenances

        Get provenances of data that have been measured on this scientific object  # noqa: E501
        """
        pass

    def test_get_scientific_object_detail(self):
        """Test case for get_scientific_object_detail

        Get scientific object detail  # noqa: E501
        """
        pass

    def test_get_scientific_object_detail_by_experiments(self):
        """Test case for get_scientific_object_detail_by_experiments

        Get scientific object detail for each experiments, a null value for experiment in response means a properties defined outside of any experiment (shared object).  # noqa: E501
        """
        pass

    def test_get_scientific_object_variables(self):
        """Test case for get_scientific_object_variables

        Get variables measured on this scientific object  # noqa: E501
        """
        pass

    def test_get_scientific_objects_children(self):
        """Test case for get_scientific_objects_children

        Get list of scientific object children  # noqa: E501
        """
        pass

    def test_get_scientific_objects_list_by_uris(self):
        """Test case for get_scientific_objects_list_by_uris

        Get scientific objet list of a given experiment URI  # noqa: E501
        """
        pass

    def test_get_used_types(self):
        """Test case for get_used_types

        get used scientific object types  # noqa: E501
        """
        pass

    def test_import_csv1(self):
        """Test case for import_csv1

        Import a CSV file for the given experiment URI and scientific object type.  # noqa: E501
        """
        pass

    def test_search_scientific_objects(self):
        """Test case for search_scientific_objects

        Search list of scientific objects  # noqa: E501
        """
        pass

    def test_search_scientific_objects_with_geometry_list_by_uris(self):
        """Test case for search_scientific_objects_with_geometry_list_by_uris

        Get scientific objet list with geometry of a given experiment URI  # noqa: E501
        """
        pass

    def test_update_scientific_object(self):
        """Test case for update_scientific_object

        Update a scientific object for the given experiment  # noqa: E501
        """
        pass

    def test_validate_csv3(self):
        """Test case for validate_csv3

        Validate a CSV file for the given experiment URI and scientific object type.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
