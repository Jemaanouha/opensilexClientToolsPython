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
from opensilexClientToolsPython.api.documents_api import DocumentsApi  # noqa: E501
from opensilexClientToolsPython.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientToolsPython.api.documents_api.DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_documents(self):
        """Test case for count_documents

        Count documents  # noqa: E501
        """
        pass

    def test_create_document(self):
        """Test case for create_document

        Add a document  # noqa: E501
        """
        pass

    def test_delete_document(self):
        """Test case for delete_document

        Delete a document  # noqa: E501
        """
        pass

    def test_get_document_file(self):
        """Test case for get_document_file

        Get document  # noqa: E501
        """
        pass

    def test_get_document_metadata(self):
        """Test case for get_document_metadata

        Get document's description  # noqa: E501
        """
        pass

    def test_search_documents(self):
        """Test case for search_documents

        Search documents  # noqa: E501
        """
        pass

    def test_update_document(self):
        """Test case for update_document

        Update document's description  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
