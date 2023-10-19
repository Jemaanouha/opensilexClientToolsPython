# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from typing import List, Dict


class FrontConfigDTO(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path_prefix': 'str',
        'home_component': 'str',
        'not_found_component': 'str',
        'header_component': 'str',
        'login_component': 'str',
        'menu_component': 'str',
        'footer_component': 'str',
        'routes': 'list[RouteDTO]',
        'theme_module': 'str',
        'theme_name': 'str',
        'open_id_authentication_uri': 'str',
        'open_id_connection_title': 'str',
        'saml_proxy_login_uri': 'str',
        'saml_connection_title': 'str',
        'activate_reset_password': 'bool',
        'geocoding_service': 'str',
        'menu_exclusions': 'list[str]',
        'version_label': 'str',
        'application_name': 'str',
        'connect_as_guest': 'bool',
        'dashboard': 'DashboardConfigDTO'
    }

    attribute_map = {
        'path_prefix': 'pathPrefix',
        'home_component': 'homeComponent',
        'not_found_component': 'notFoundComponent',
        'header_component': 'headerComponent',
        'login_component': 'loginComponent',
        'menu_component': 'menuComponent',
        'footer_component': 'footerComponent',
        'routes': 'routes',
        'theme_module': 'themeModule',
        'theme_name': 'themeName',
        'open_id_authentication_uri': 'openIDAuthenticationURI',
        'open_id_connection_title': 'openIDConnectionTitle',
        'saml_proxy_login_uri': 'samlProxyLoginURI',
        'saml_connection_title': 'samlConnectionTitle',
        'activate_reset_password': 'activateResetPassword',
        'geocoding_service': 'geocodingService',
        'menu_exclusions': 'menuExclusions',
        'version_label': 'versionLabel',
        'application_name': 'applicationName',
        'connect_as_guest': 'connectAsGuest',
        'dashboard': 'dashboard'
    }
    def __init__(self,
        path_prefix : 'str',
        home_component : 'str',
        not_found_component : 'str',
        header_component : 'str',
        login_component : 'str',
        menu_component : 'str',
        footer_component : 'str',
        routes : 'List[RouteDTO]',
        theme_module : 'str' = None,
        theme_name : 'str' = None,
        open_id_authentication_uri : 'str' = None,
        open_id_connection_title : 'str' = None,
        saml_proxy_login_uri : 'str' = None,
        saml_connection_title : 'str' = None,
        activate_reset_password : 'bool' = None,
        geocoding_service : 'str' = None,
        menu_exclusions : 'List[str]' = None,
        version_label : 'str' = None,
        application_name : 'str' = None,
        connect_as_guest : 'bool' = None,
        dashboard : 'DashboardConfigDTO' = None):  # noqa: E501
        """FrontConfigDTO - a model defined in Swagger"""  # noqa: E501

        self._path_prefix = None
        self._home_component = None
        self._not_found_component = None
        self._header_component = None
        self._login_component = None
        self._menu_component = None
        self._footer_component = None
        self._routes = None
        self._theme_module = None
        self._theme_name = None
        self._open_id_authentication_uri = None
        self._open_id_connection_title = None
        self._saml_proxy_login_uri = None
        self._saml_connection_title = None
        self._activate_reset_password = None
        self._geocoding_service = None
        self._menu_exclusions = None
        self._version_label = None
        self._application_name = None
        self._connect_as_guest = None
        self._dashboard = None
        self.discriminator = None

        self.path_prefix = path_prefix
        self.home_component = home_component
        self.not_found_component = not_found_component
        self.header_component = header_component
        self.login_component = login_component
        self.menu_component = menu_component
        self.footer_component = footer_component
        self.routes = routes
        if theme_module is not None:
            self.theme_module = theme_module
        if theme_name is not None:
            self.theme_name = theme_name
        if open_id_authentication_uri is not None:
            self.open_id_authentication_uri = open_id_authentication_uri
        if open_id_connection_title is not None:
            self.open_id_connection_title = open_id_connection_title
        if saml_proxy_login_uri is not None:
            self.saml_proxy_login_uri = saml_proxy_login_uri
        if saml_connection_title is not None:
            self.saml_connection_title = saml_connection_title
        if activate_reset_password is not None:
            self.activate_reset_password = activate_reset_password
        if geocoding_service is not None:
            self.geocoding_service = geocoding_service
        if menu_exclusions is not None:
            self.menu_exclusions = menu_exclusions
        if version_label is not None:
            self.version_label = version_label
        if application_name is not None:
            self.application_name = application_name
        if connect_as_guest is not None:
            self.connect_as_guest = connect_as_guest
        if dashboard is not None:
            self.dashboard = dashboard

    @property
    def path_prefix(self):
        """Gets the path_prefix of this FrontConfigDTO.  # noqa: E501

        Application url path prefix  # noqa: E501

        :return: The path_prefix of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        """Sets the path_prefix of this FrontConfigDTO.

        Application url path prefix  # noqa: E501

        :param path_prefix: The path_prefix of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if path_prefix is None:
            raise ValueError("Invalid value for `path_prefix`, must not be `None`")  # noqa: E501

        self._path_prefix = path_prefix

    @property
    def home_component(self):
        """Gets the home_component of this FrontConfigDTO.  # noqa: E501

        Home component identifier  # noqa: E501

        :return: The home_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._home_component

    @home_component.setter
    def home_component(self, home_component):
        """Sets the home_component of this FrontConfigDTO.

        Home component identifier  # noqa: E501

        :param home_component: The home_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if home_component is None:
            raise ValueError("Invalid value for `home_component`, must not be `None`")  # noqa: E501

        self._home_component = home_component

    @property
    def not_found_component(self):
        """Gets the not_found_component of this FrontConfigDTO.  # noqa: E501

        Not found component identifier  # noqa: E501

        :return: The not_found_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._not_found_component

    @not_found_component.setter
    def not_found_component(self, not_found_component):
        """Sets the not_found_component of this FrontConfigDTO.

        Not found component identifier  # noqa: E501

        :param not_found_component: The not_found_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if not_found_component is None:
            raise ValueError("Invalid value for `not_found_component`, must not be `None`")  # noqa: E501

        self._not_found_component = not_found_component

    @property
    def header_component(self):
        """Gets the header_component of this FrontConfigDTO.  # noqa: E501

        Header component identifier  # noqa: E501

        :return: The header_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._header_component

    @header_component.setter
    def header_component(self, header_component):
        """Sets the header_component of this FrontConfigDTO.

        Header component identifier  # noqa: E501

        :param header_component: The header_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if header_component is None:
            raise ValueError("Invalid value for `header_component`, must not be `None`")  # noqa: E501

        self._header_component = header_component

    @property
    def login_component(self):
        """Gets the login_component of this FrontConfigDTO.  # noqa: E501

        Login component identifier  # noqa: E501

        :return: The login_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._login_component

    @login_component.setter
    def login_component(self, login_component):
        """Sets the login_component of this FrontConfigDTO.

        Login component identifier  # noqa: E501

        :param login_component: The login_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if login_component is None:
            raise ValueError("Invalid value for `login_component`, must not be `None`")  # noqa: E501

        self._login_component = login_component

    @property
    def menu_component(self):
        """Gets the menu_component of this FrontConfigDTO.  # noqa: E501

        Menu component identifier  # noqa: E501

        :return: The menu_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._menu_component

    @menu_component.setter
    def menu_component(self, menu_component):
        """Sets the menu_component of this FrontConfigDTO.

        Menu component identifier  # noqa: E501

        :param menu_component: The menu_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if menu_component is None:
            raise ValueError("Invalid value for `menu_component`, must not be `None`")  # noqa: E501

        self._menu_component = menu_component

    @property
    def footer_component(self):
        """Gets the footer_component of this FrontConfigDTO.  # noqa: E501

        Footer component identifier  # noqa: E501

        :return: The footer_component of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._footer_component

    @footer_component.setter
    def footer_component(self, footer_component):
        """Sets the footer_component of this FrontConfigDTO.

        Footer component identifier  # noqa: E501

        :param footer_component: The footer_component of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        if footer_component is None:
            raise ValueError("Invalid value for `footer_component`, must not be `None`")  # noqa: E501

        self._footer_component = footer_component

    @property
    def routes(self):
        """Gets the routes of this FrontConfigDTO.  # noqa: E501

        List of configured routes  # noqa: E501

        :return: The routes of this FrontConfigDTO.  # noqa: E501
        :rtype: list[RouteDTO]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this FrontConfigDTO.

        List of configured routes  # noqa: E501

        :param routes: The routes of this FrontConfigDTO.  # noqa: E501
        :type: list[RouteDTO]
        """
        if routes is None:
            raise ValueError("Invalid value for `routes`, must not be `None`")  # noqa: E501

        self._routes = routes

    @property
    def theme_module(self):
        """Gets the theme_module of this FrontConfigDTO.  # noqa: E501

        Theme module identifier  # noqa: E501

        :return: The theme_module of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._theme_module

    @theme_module.setter
    def theme_module(self, theme_module):
        """Sets the theme_module of this FrontConfigDTO.

        Theme module identifier  # noqa: E501

        :param theme_module: The theme_module of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._theme_module = theme_module

    @property
    def theme_name(self):
        """Gets the theme_name of this FrontConfigDTO.  # noqa: E501

        Theme module name  # noqa: E501

        :return: The theme_name of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._theme_name

    @theme_name.setter
    def theme_name(self, theme_name):
        """Sets the theme_name of this FrontConfigDTO.

        Theme module name  # noqa: E501

        :param theme_name: The theme_name of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._theme_name = theme_name

    @property
    def open_id_authentication_uri(self):
        """Gets the open_id_authentication_uri of this FrontConfigDTO.  # noqa: E501

        OpenID Authorization URI  # noqa: E501

        :return: The open_id_authentication_uri of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._open_id_authentication_uri

    @open_id_authentication_uri.setter
    def open_id_authentication_uri(self, open_id_authentication_uri):
        """Sets the open_id_authentication_uri of this FrontConfigDTO.

        OpenID Authorization URI  # noqa: E501

        :param open_id_authentication_uri: The open_id_authentication_uri of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._open_id_authentication_uri = open_id_authentication_uri

    @property
    def open_id_connection_title(self):
        """Gets the open_id_connection_title of this FrontConfigDTO.  # noqa: E501


        :return: The open_id_connection_title of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._open_id_connection_title

    @open_id_connection_title.setter
    def open_id_connection_title(self, open_id_connection_title):
        """Sets the open_id_connection_title of this FrontConfigDTO.


        :param open_id_connection_title: The open_id_connection_title of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._open_id_connection_title = open_id_connection_title

    @property
    def saml_proxy_login_uri(self):
        """Gets the saml_proxy_login_uri of this FrontConfigDTO.  # noqa: E501


        :return: The saml_proxy_login_uri of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._saml_proxy_login_uri

    @saml_proxy_login_uri.setter
    def saml_proxy_login_uri(self, saml_proxy_login_uri):
        """Sets the saml_proxy_login_uri of this FrontConfigDTO.


        :param saml_proxy_login_uri: The saml_proxy_login_uri of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._saml_proxy_login_uri = saml_proxy_login_uri

    @property
    def saml_connection_title(self):
        """Gets the saml_connection_title of this FrontConfigDTO.  # noqa: E501


        :return: The saml_connection_title of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._saml_connection_title

    @saml_connection_title.setter
    def saml_connection_title(self, saml_connection_title):
        """Sets the saml_connection_title of this FrontConfigDTO.


        :param saml_connection_title: The saml_connection_title of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._saml_connection_title = saml_connection_title

    @property
    def activate_reset_password(self):
        """Gets the activate_reset_password of this FrontConfigDTO.  # noqa: E501


        :return: The activate_reset_password of this FrontConfigDTO.  # noqa: E501
        :rtype: bool
        """
        return self._activate_reset_password

    @activate_reset_password.setter
    def activate_reset_password(self, activate_reset_password):
        """Sets the activate_reset_password of this FrontConfigDTO.


        :param activate_reset_password: The activate_reset_password of this FrontConfigDTO.  # noqa: E501
        :type: bool
        """

        self._activate_reset_password = activate_reset_password

    @property
    def geocoding_service(self):
        """Gets the geocoding_service of this FrontConfigDTO.  # noqa: E501

        Geocoding service  # noqa: E501

        :return: The geocoding_service of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._geocoding_service

    @geocoding_service.setter
    def geocoding_service(self, geocoding_service):
        """Sets the geocoding_service of this FrontConfigDTO.

        Geocoding service  # noqa: E501

        :param geocoding_service: The geocoding_service of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._geocoding_service = geocoding_service

    @property
    def menu_exclusions(self):
        """Gets the menu_exclusions of this FrontConfigDTO.  # noqa: E501

        Menu exclusions  # noqa: E501

        :return: The menu_exclusions of this FrontConfigDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._menu_exclusions

    @menu_exclusions.setter
    def menu_exclusions(self, menu_exclusions):
        """Sets the menu_exclusions of this FrontConfigDTO.

        Menu exclusions  # noqa: E501

        :param menu_exclusions: The menu_exclusions of this FrontConfigDTO.  # noqa: E501
        :type: list[str]
        """

        self._menu_exclusions = menu_exclusions

    @property
    def version_label(self):
        """Gets the version_label of this FrontConfigDTO.  # noqa: E501

        Version label to use in the header  # noqa: E501

        :return: The version_label of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """Sets the version_label of this FrontConfigDTO.

        Version label to use in the header  # noqa: E501

        :param version_label: The version_label of this FrontConfigDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEVELOP", "RELEASE"]  # noqa: E501
        if version_label not in allowed_values:
            raise ValueError(
                "Invalid value for `version_label` ({0}), must be one of {1}"  # noqa: E501
                .format(version_label, allowed_values)
            )

        self._version_label = version_label

    @property
    def application_name(self):
        """Gets the application_name of this FrontConfigDTO.  # noqa: E501

        Name of the application to display  # noqa: E501

        :return: The application_name of this FrontConfigDTO.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this FrontConfigDTO.

        Name of the application to display  # noqa: E501

        :param application_name: The application_name of this FrontConfigDTO.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def connect_as_guest(self):
        """Gets the connect_as_guest of this FrontConfigDTO.  # noqa: E501

        Ability to be logged as guest  # noqa: E501

        :return: The connect_as_guest of this FrontConfigDTO.  # noqa: E501
        :rtype: bool
        """
        return self._connect_as_guest

    @connect_as_guest.setter
    def connect_as_guest(self, connect_as_guest):
        """Sets the connect_as_guest of this FrontConfigDTO.

        Ability to be logged as guest  # noqa: E501

        :param connect_as_guest: The connect_as_guest of this FrontConfigDTO.  # noqa: E501
        :type: bool
        """

        self._connect_as_guest = connect_as_guest

    @property
    def dashboard(self):
        """Gets the dashboard of this FrontConfigDTO.  # noqa: E501


        :return: The dashboard of this FrontConfigDTO.  # noqa: E501
        :rtype: DashboardConfigDTO
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this FrontConfigDTO.


        :param dashboard: The dashboard of this FrontConfigDTO.  # noqa: E501
        :type: DashboardConfigDTO
        """

        self._dashboard = dashboard

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FrontConfigDTO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FrontConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other


from opensilexClientToolsPython.models.route_dto import RouteDTO
from opensilexClientToolsPython.models.dashboard_config_dto import DashboardConfigDTO


