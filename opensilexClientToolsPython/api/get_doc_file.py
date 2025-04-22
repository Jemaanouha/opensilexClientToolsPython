from __future__ import print_function
import time
import opensilexClientToolsPython
from opensilexClientToolsPython.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientToolsPython.ApiClient()
pythonClient.connect_to_opensilex_ws(identifier="isabelle.alic@inrae.fr",password="UMR MISTEA",host="https://siduri-dev.migale.inrae.fr/rest")
api_instance = opensilexClientToolsPython.DocumentsApi(pythonClient)
uri = "dev:id/document/informations_srr16993379" # str | Document URI


try:
    # Get document
    result = api_instance.get_document_file(uri)
    print("Document récupéré avec succès !")
    print(result)  # Affiche le contenu brut

except opensilexClientToolsPython.rest.ApiException as e:
    print("Exception when calling DocumentsApi->get_document_file: %s\n" % e)
