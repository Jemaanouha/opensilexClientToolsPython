# coding: utf-8

# flake8: noqa
"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0-rc+6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models with dependencies into model package first

from opensilexClientToolsPython.models.activity_creation_dto import ActivityCreationDTO

from opensilexClientToolsPython.models.activity_get_dto import ActivityGetDTO

from opensilexClientToolsPython.models.agent_model import AgentModel

from opensilexClientToolsPython.models.annotation_creation_dto import AnnotationCreationDTO



from opensilexClientToolsPython.models.annotation_update_dto import AnnotationUpdateDTO

from opensilexClientToolsPython.models.api_contact_info_dto import ApiContactInfoDTO

from opensilexClientToolsPython.models.api_external_docs_dto import ApiExternalDocsDTO

from opensilexClientToolsPython.models.api_git_commit_dto import ApiGitCommitDTO

from opensilexClientToolsPython.models.api_license_info_dto import ApiLicenseInfoDTO

from opensilexClientToolsPython.models.api_modules_info import ApiModulesInfo







from opensilexClientToolsPython.models.authentication_dto import AuthenticationDTO

from opensilexClientToolsPython.models.csv_cell import CSVCell

from opensilexClientToolsPython.models.csv_datatype_error import CSVDatatypeError

from opensilexClientToolsPython.models.csv_duplicate_uri_error import CSVDuplicateURIError

from opensilexClientToolsPython.models.csvuri_not_found_error import CSVURINotFoundError





from opensilexClientToolsPython.models.call import Call

from opensilexClientToolsPython.models.characteristic_creation_dto import CharacteristicCreationDTO

from opensilexClientToolsPython.models.characteristic_details_dto import CharacteristicDetailsDTO

from opensilexClientToolsPython.models.characteristic_get_dto import CharacteristicGetDTO

from opensilexClientToolsPython.models.characteristic_update_dto import CharacteristicUpdateDTO

from opensilexClientToolsPython.models.contact import Contact

from opensilexClientToolsPython.models.count_item_dto import CountItemDTO



from opensilexClientToolsPython.models.credential_dto import CredentialDTO



from opensilexClientToolsPython.models.crs import Crs

from opensilexClientToolsPython.models.csv_header import CsvHeader





from opensilexClientToolsPython.models.data_confidence_dto import DataConfidenceDTO









from opensilexClientToolsPython.models.data_link import DataLink











from opensilexClientToolsPython.models.document_get_dto import DocumentGetDTO

from opensilexClientToolsPython.models.documentation_link import DocumentationLink

from opensilexClientToolsPython.models.entity_creation_dto import EntityCreationDTO

from opensilexClientToolsPython.models.entity_details_dto import EntityDetailsDTO

from opensilexClientToolsPython.models.entity_get_dto import EntityGetDTO

from opensilexClientToolsPython.models.entity_update_dto import EntityUpdateDTO

from opensilexClientToolsPython.models.error_dto import ErrorDTO







from opensilexClientToolsPython.models.event_get_dto import EventGetDTO



from opensilexClientToolsPython.models.experiment_creation_dto import ExperimentCreationDTO



from opensilexClientToolsPython.models.experiment_get_list_dto import ExperimentGetListDTO

from opensilexClientToolsPython.models.facility_address_dto import FacilityAddressDTO





from opensilexClientToolsPython.models.facility_named_dto import FacilityNamedDTO



from opensilexClientToolsPython.models.factor_category_get_dto import FactorCategoryGetDTO





from opensilexClientToolsPython.models.factor_get_dto import FactorGetDTO

from opensilexClientToolsPython.models.factor_level_creation_dto import FactorLevelCreationDTO

from opensilexClientToolsPython.models.factor_level_get_dto import FactorLevelGetDTO

from opensilexClientToolsPython.models.factor_level_get_detail_dto import FactorLevelGetDetailDTO



from opensilexClientToolsPython.models.font_config_dto import FontConfigDTO



from opensilexClientToolsPython.models.geo_json_object import GeoJsonObject

from opensilexClientToolsPython.models.germplasm_creation_dto import GermplasmCreationDTO

from opensilexClientToolsPython.models.germplasm_dto import GermplasmDTO

from opensilexClientToolsPython.models.germplasm_get_all_dto import GermplasmGetAllDTO

from opensilexClientToolsPython.models.germplasm_get_single_dto import GermplasmGetSingleDTO



from opensilexClientToolsPython.models.germplasm_update_dto import GermplasmUpdateDTO







from opensilexClientToolsPython.models.group_user_profile_dto import GroupUserProfileDTO

from opensilexClientToolsPython.models.interest_entity_creation_dto import InterestEntityCreationDTO

from opensilexClientToolsPython.models.interest_entity_details_dto import InterestEntityDetailsDTO

from opensilexClientToolsPython.models.interest_entity_get_dto import InterestEntityGetDTO

from opensilexClientToolsPython.models.interest_entity_update_dto import InterestEntityUpdateDTO

from opensilexClientToolsPython.models.level import Level

from opensilexClientToolsPython.models.list_item_dto import ListItemDTO

from opensilexClientToolsPython.models.lng_lat_alt import LngLatAlt

from opensilexClientToolsPython.models.location import Location







from opensilexClientToolsPython.models.method_creation_dto import MethodCreationDTO

from opensilexClientToolsPython.models.method_details_dto import MethodDetailsDTO

from opensilexClientToolsPython.models.method_get_dto import MethodGetDTO

from opensilexClientToolsPython.models.method_update_dto import MethodUpdateDTO



from opensilexClientToolsPython.models.motivation_get_dto import MotivationGetDTO







from opensilexClientToolsPython.models.named_resource_dto import NamedResourceDTO

from opensilexClientToolsPython.models.named_resource_dto_experiment_model import NamedResourceDTOExperimentModel

from opensilexClientToolsPython.models.named_resource_dto_facility_model import NamedResourceDTOFacilityModel

from opensilexClientToolsPython.models.named_resource_dto_factor_level_model import NamedResourceDTOFactorLevelModel

from opensilexClientToolsPython.models.named_resource_dto_group_model import NamedResourceDTOGroupModel

from opensilexClientToolsPython.models.named_resource_dto_organization_model import NamedResourceDTOOrganizationModel

from opensilexClientToolsPython.models.named_resource_dto_project_model import NamedResourceDTOProjectModel

from opensilexClientToolsPython.models.named_resource_dto_site_model import NamedResourceDTOSiteModel

from opensilexClientToolsPython.models.named_resource_dto_variable_model import NamedResourceDTOVariableModel

from opensilexClientToolsPython.models.owl_class_property_restriction_dto import OWLClassPropertyRestrictionDTO







from opensilexClientToolsPython.models.observation_treatment import ObservationTreatment



from opensilexClientToolsPython.models.observation_unit_xref import ObservationUnitXref





from opensilexClientToolsPython.models.order_by import OrderBy

from opensilexClientToolsPython.models.organization_creation_dto import OrganizationCreationDTO



from opensilexClientToolsPython.models.organization_update_dto import OrganizationUpdateDTO

from opensilexClientToolsPython.models.pagination_dto import PaginationDTO







from opensilexClientToolsPython.models.profile_creation_dto import ProfileCreationDTO

from opensilexClientToolsPython.models.profile_get_dto import ProfileGetDTO

from opensilexClientToolsPython.models.profile_update_dto import ProfileUpdateDTO

from opensilexClientToolsPython.models.project_creation_dto import ProjectCreationDTO

from opensilexClientToolsPython.models.project_get_dto import ProjectGetDTO

from opensilexClientToolsPython.models.project_get_detail_dto import ProjectGetDetailDTO

from opensilexClientToolsPython.models.prov_entity_model import ProvEntityModel







from opensilexClientToolsPython.models.rdf_object_relation_dto import RDFObjectRelationDTO

from opensilexClientToolsPython.models.rdf_property_dto import RDFPropertyDTO

from opensilexClientToolsPython.models.rdf_property_get_dto import RDFPropertyGetDTO

from opensilexClientToolsPython.models.rdf_type_dto import RDFTypeDTO

from opensilexClientToolsPython.models.rdf_type_translated_dto import RDFTypeTranslatedDTO

from opensilexClientToolsPython.models.resource_dag_dto import ResourceDagDTO



from opensilexClientToolsPython.models.route_dto import RouteDTO

















from opensilexClientToolsPython.models.season import Season

from opensilexClientToolsPython.models.site_address_dto import SiteAddressDTO







from opensilexClientToolsPython.models.species_dto import SpeciesDTO













from opensilexClientToolsPython.models.token_get_dto import TokenGetDTO



from opensilexClientToolsPython.models.uri_types_dto import URITypesDTO

from opensilexClientToolsPython.models.ur_is_list_post_dto import URIsListPostDTO

from opensilexClientToolsPython.models.unit_creation_dto import UnitCreationDTO

from opensilexClientToolsPython.models.unit_details_dto import UnitDetailsDTO

from opensilexClientToolsPython.models.unit_get_dto import UnitGetDTO

from opensilexClientToolsPython.models.unit_update_dto import UnitUpdateDTO

from opensilexClientToolsPython.models.user_creation_dto import UserCreationDTO



from opensilexClientToolsPython.models.user_get_dto import UserGetDTO

from opensilexClientToolsPython.models.user_update_dto import UserUpdateDTO

from opensilexClientToolsPython.models.variable_creation_dto import VariableCreationDTO

from opensilexClientToolsPython.models.variable_datatype_dto import VariableDatatypeDTO





from opensilexClientToolsPython.models.variable_update_dto import VariableUpdateDTO

from opensilexClientToolsPython.models.variables_group_creation_dto import VariablesGroupCreationDTO



from opensilexClientToolsPython.models.variables_group_update_dto import VariablesGroupUpdateDTO



from opensilexClientToolsPython.models.vue_data_type_dto import VueDataTypeDTO





from opensilexClientToolsPython.models.vue_rdf_type_parameter_dto import VueRDFTypeParameterDTO

from opensilexClientToolsPython.models.vue_rdf_type_property_dto import VueRDFTypePropertyDTO



















# import the rest of the models into model package 





from opensilexClientToolsPython.models.annotation_get_dto import AnnotationGetDTO







from opensilexClientToolsPython.models.area_creation_dto import AreaCreationDTO
from opensilexClientToolsPython.models.area_creation_dto import AreaCreationDTO

from opensilexClientToolsPython.models.area_get_dto import AreaGetDTO
from opensilexClientToolsPython.models.area_get_dto import AreaGetDTO

from opensilexClientToolsPython.models.area_update_dto import AreaUpdateDTO
from opensilexClientToolsPython.models.area_update_dto import AreaUpdateDTO






from opensilexClientToolsPython.models.csv_validation_dto import CSVValidationDTO

from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel
from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel
from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel
from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel
from opensilexClientToolsPython.models.csv_validation_model import CSVValidationModel








from opensilexClientToolsPython.models.count_list_item_dto import CountListItemDTO


from opensilexClientToolsPython.models.credentials_group_dto import CredentialsGroupDTO



from opensilexClientToolsPython.models.data_csv_validation_dto import DataCSVValidationDTO
from opensilexClientToolsPython.models.data_csv_validation_dto import DataCSVValidationDTO

from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel
from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel
from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel
from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel
from opensilexClientToolsPython.models.data_csv_validation_model import DataCSVValidationModel


from opensilexClientToolsPython.models.data_creation_dto import DataCreationDTO

from opensilexClientToolsPython.models.data_file_get_dto import DataFileGetDTO

from opensilexClientToolsPython.models.data_file_path_creation_dto import DataFilePathCreationDTO

from opensilexClientToolsPython.models.data_get_dto import DataGetDTO


from opensilexClientToolsPython.models.data_provenance_model import DataProvenanceModel

from opensilexClientToolsPython.models.data_update_dto import DataUpdateDTO

from opensilexClientToolsPython.models.device_creation_dto import DeviceCreationDTO

from opensilexClientToolsPython.models.device_get_dto import DeviceGetDTO

from opensilexClientToolsPython.models.device_get_details_dto import DeviceGetDetailsDTO








from opensilexClientToolsPython.models.error_response import ErrorResponse
from opensilexClientToolsPython.models.error_response import ErrorResponse

from opensilexClientToolsPython.models.event_creation_dto import EventCreationDTO

from opensilexClientToolsPython.models.event_details_dto import EventDetailsDTO


from opensilexClientToolsPython.models.event_update_dto import EventUpdateDTO


from opensilexClientToolsPython.models.experiment_get_dto import ExperimentGetDTO
from opensilexClientToolsPython.models.experiment_get_dto import ExperimentGetDTO
from opensilexClientToolsPython.models.experiment_get_dto import ExperimentGetDTO



from opensilexClientToolsPython.models.facility_creation_dto import FacilityCreationDTO
from opensilexClientToolsPython.models.facility_creation_dto import FacilityCreationDTO

from opensilexClientToolsPython.models.facility_get_dto import FacilityGetDTO
from opensilexClientToolsPython.models.facility_get_dto import FacilityGetDTO
from opensilexClientToolsPython.models.facility_get_dto import FacilityGetDTO
from opensilexClientToolsPython.models.facility_get_dto import FacilityGetDTO
from opensilexClientToolsPython.models.facility_get_dto import FacilityGetDTO


from opensilexClientToolsPython.models.facility_update_dto import FacilityUpdateDTO
from opensilexClientToolsPython.models.facility_update_dto import FacilityUpdateDTO


from opensilexClientToolsPython.models.factor_creation_dto import FactorCreationDTO

from opensilexClientToolsPython.models.factor_details_get_dto import FactorDetailsGetDTO





from opensilexClientToolsPython.models.factor_update_dto import FactorUpdateDTO


from opensilexClientToolsPython.models.front_config_dto import FrontConfigDTO






from opensilexClientToolsPython.models.germplasm_search_filter import GermplasmSearchFilter


from opensilexClientToolsPython.models.group_creation_dto import GroupCreationDTO

from opensilexClientToolsPython.models.group_dto import GroupDTO

from opensilexClientToolsPython.models.group_update_dto import GroupUpdateDTO










from opensilexClientToolsPython.models.menu_item_dto import MenuItemDTO
from opensilexClientToolsPython.models.menu_item_dto import MenuItemDTO

from opensilexClientToolsPython.models.metadata_dto import MetadataDTO
from opensilexClientToolsPython.models.metadata_dto import MetadataDTO

from opensilexClientToolsPython.models.method import Method





from opensilexClientToolsPython.models.metric_dto import MetricDTO


from opensilexClientToolsPython.models.move_creation_dto import MoveCreationDTO
from opensilexClientToolsPython.models.move_creation_dto import MoveCreationDTO

from opensilexClientToolsPython.models.move_details_dto import MoveDetailsDTO
from opensilexClientToolsPython.models.move_details_dto import MoveDetailsDTO
from opensilexClientToolsPython.models.move_details_dto import MoveDetailsDTO

from opensilexClientToolsPython.models.move_update_dto import MoveUpdateDTO
from opensilexClientToolsPython.models.move_update_dto import MoveUpdateDTO











from opensilexClientToolsPython.models.object_uri_response import ObjectUriResponse

from opensilexClientToolsPython.models.observation_dto import ObservationDTO

from opensilexClientToolsPython.models.observation_summary import ObservationSummary


from opensilexClientToolsPython.models.observation_unit_dto import ObservationUnitDTO
from opensilexClientToolsPython.models.observation_unit_dto import ObservationUnitDTO
from opensilexClientToolsPython.models.observation_unit_dto import ObservationUnitDTO


from opensilexClientToolsPython.models.observation_variable_dto import ObservationVariableDTO
from opensilexClientToolsPython.models.observation_variable_dto import ObservationVariableDTO
from opensilexClientToolsPython.models.observation_variable_dto import ObservationVariableDTO

from opensilexClientToolsPython.models.ontology_reference import OntologyReference



from opensilexClientToolsPython.models.organization_get_dto import OrganizationGetDTO
from opensilexClientToolsPython.models.organization_get_dto import OrganizationGetDTO
from opensilexClientToolsPython.models.organization_get_dto import OrganizationGetDTO
from opensilexClientToolsPython.models.organization_get_dto import OrganizationGetDTO
from opensilexClientToolsPython.models.organization_get_dto import OrganizationGetDTO



from opensilexClientToolsPython.models.position_creation_dto import PositionCreationDTO

from opensilexClientToolsPython.models.position_get_dto import PositionGetDTO
from opensilexClientToolsPython.models.position_get_dto import PositionGetDTO

from opensilexClientToolsPython.models.position_get_detail_dto import PositionGetDetailDTO








from opensilexClientToolsPython.models.provenance_creation_dto import ProvenanceCreationDTO
from opensilexClientToolsPython.models.provenance_creation_dto import ProvenanceCreationDTO

from opensilexClientToolsPython.models.provenance_get_dto import ProvenanceGetDTO
from opensilexClientToolsPython.models.provenance_get_dto import ProvenanceGetDTO

from opensilexClientToolsPython.models.provenance_update_dto import ProvenanceUpdateDTO
from opensilexClientToolsPython.models.provenance_update_dto import ProvenanceUpdateDTO







from opensilexClientToolsPython.models.resource_tree_dto import ResourceTreeDTO


from opensilexClientToolsPython.models.scale import Scale

from opensilexClientToolsPython.models.scientific_object_creation_dto import ScientificObjectCreationDTO
from opensilexClientToolsPython.models.scientific_object_creation_dto import ScientificObjectCreationDTO

from opensilexClientToolsPython.models.scientific_object_detail_by_experiments_dto import ScientificObjectDetailByExperimentsDTO
from opensilexClientToolsPython.models.scientific_object_detail_by_experiments_dto import ScientificObjectDetailByExperimentsDTO
from opensilexClientToolsPython.models.scientific_object_detail_by_experiments_dto import ScientificObjectDetailByExperimentsDTO

from opensilexClientToolsPython.models.scientific_object_detail_dto import ScientificObjectDetailDTO
from opensilexClientToolsPython.models.scientific_object_detail_dto import ScientificObjectDetailDTO
from opensilexClientToolsPython.models.scientific_object_detail_dto import ScientificObjectDetailDTO

from opensilexClientToolsPython.models.scientific_object_node_dto import ScientificObjectNodeDTO

from opensilexClientToolsPython.models.scientific_object_node_with_children_dto import ScientificObjectNodeWithChildrenDTO

from opensilexClientToolsPython.models.scientific_object_search_dto import ScientificObjectSearchDTO

from opensilexClientToolsPython.models.scientific_object_update_dto import ScientificObjectUpdateDTO
from opensilexClientToolsPython.models.scientific_object_update_dto import ScientificObjectUpdateDTO



from opensilexClientToolsPython.models.site_creation_dto import SiteCreationDTO

from opensilexClientToolsPython.models.site_get_dto import SiteGetDTO
from opensilexClientToolsPython.models.site_get_dto import SiteGetDTO
from opensilexClientToolsPython.models.site_get_dto import SiteGetDTO
from opensilexClientToolsPython.models.site_get_dto import SiteGetDTO
from opensilexClientToolsPython.models.site_get_dto import SiteGetDTO

from opensilexClientToolsPython.models.site_update_dto import SiteUpdateDTO


from opensilexClientToolsPython.models.status_dto import StatusDTO

from opensilexClientToolsPython.models.study_dto import StudyDTO

from opensilexClientToolsPython.models.study_details_dto import StudyDetailsDTO
from opensilexClientToolsPython.models.study_details_dto import StudyDetailsDTO
from opensilexClientToolsPython.models.study_details_dto import StudyDetailsDTO
from opensilexClientToolsPython.models.study_details_dto import StudyDetailsDTO

from opensilexClientToolsPython.models.target_position_creation_dto import TargetPositionCreationDTO

from opensilexClientToolsPython.models.target_position_get_dto import TargetPositionGetDTO

from opensilexClientToolsPython.models.theme_config_dto import ThemeConfigDTO


from opensilexClientToolsPython.models.trait import Trait








from opensilexClientToolsPython.models.user_front_config_dto import UserFrontConfigDTO





from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO
from opensilexClientToolsPython.models.variable_details_dto import VariableDetailsDTO

from opensilexClientToolsPython.models.variable_get_dto import VariableGetDTO
from opensilexClientToolsPython.models.variable_get_dto import VariableGetDTO
from opensilexClientToolsPython.models.variable_get_dto import VariableGetDTO
from opensilexClientToolsPython.models.variable_get_dto import VariableGetDTO
from opensilexClientToolsPython.models.variable_get_dto import VariableGetDTO



from opensilexClientToolsPython.models.variables_group_get_dto import VariablesGroupGetDTO


from opensilexClientToolsPython.models.version_info_dto import VersionInfoDTO
from opensilexClientToolsPython.models.version_info_dto import VersionInfoDTO
from opensilexClientToolsPython.models.version_info_dto import VersionInfoDTO
from opensilexClientToolsPython.models.version_info_dto import VersionInfoDTO
from opensilexClientToolsPython.models.version_info_dto import VersionInfoDTO


from opensilexClientToolsPython.models.vue_object_type_dto import VueObjectTypeDTO

from opensilexClientToolsPython.models.vue_rdf_type_dto import VueRDFTypeDTO



from opensilexClientToolsPython.models.feature import Feature

from opensilexClientToolsPython.models.feature_collection import FeatureCollection
from opensilexClientToolsPython.models.feature_collection import FeatureCollection

from opensilexClientToolsPython.models.geometry_collection import GeometryCollection

from opensilexClientToolsPython.models.line_string import LineString
from opensilexClientToolsPython.models.line_string import LineString

from opensilexClientToolsPython.models.multi_line_string import MultiLineString
from opensilexClientToolsPython.models.multi_line_string import MultiLineString

from opensilexClientToolsPython.models.multi_point import MultiPoint
from opensilexClientToolsPython.models.multi_point import MultiPoint

from opensilexClientToolsPython.models.multi_polygon import MultiPolygon
from opensilexClientToolsPython.models.multi_polygon import MultiPolygon

from opensilexClientToolsPython.models.point import Point
from opensilexClientToolsPython.models.point import Point

from opensilexClientToolsPython.models.polygon import Polygon
from opensilexClientToolsPython.models.polygon import Polygon

