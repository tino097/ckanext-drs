# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ckanext.drs.models.base_model import Model
from ckanext.drs.models.service_organization import ServiceOrganization
from ckanext.drs.models.service_type import ServiceType

import ckanext.drs.utils as util

class Service(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, type=None, description=None, organization=None, contact_url=None, documentation_url=None, created_at=None, updated_at=None, environment=None, version=None):  # noqa: E501
        """Service - a model defined in OpenAPI

        :param id: The id of this Service.  # noqa: E501
        :type id: str
        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param type: The type of this Service.  # noqa: E501
        :type type: ServiceType
        :param description: The description of this Service.  # noqa: E501
        :type description: str
        :param organization: The organization of this Service.  # noqa: E501
        :type organization: ServiceOrganization
        :param contact_url: The contact_url of this Service.  # noqa: E501
        :type contact_url: str
        :param documentation_url: The documentation_url of this Service.  # noqa: E501
        :type documentation_url: str
        :param created_at: The created_at of this Service.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Service.  # noqa: E501
        :type updated_at: datetime
        :param environment: The environment of this Service.  # noqa: E501
        :type environment: str
        :param version: The version of this Service.  # noqa: E501
        :type version: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'type': ServiceType,
            'description': str,
            'organization': ServiceOrganization,
            'contact_url': str,
            'documentation_url': str,
            'created_at': datetime,
            'updated_at': datetime,
            'environment': str,
            'version': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'organization': 'organization',
            'contact_url': 'contactUrl',
            'documentation_url': 'documentationUrl',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'environment': 'environment',
            'version': 'version'
        }

        self._id = id
        self._name = name
        self._type = type
        self._description = description
        self._organization = organization
        self._contact_url = contact_url
        self._documentation_url = documentation_url
        self._created_at = created_at
        self._updated_at = updated_at
        self._environment = environment
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'Service':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Service of this Service.  # noqa: E501
        :rtype: Service
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Service.

        Unique ID of this service. Reverse domain name notation is recommended, though not required. The identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service Registry.  # noqa: E501

        :return: The id of this Service.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.

        Unique ID of this service. Reverse domain name notation is recommended, though not required. The identifier should attempt to be globally unique so it can be used in downstream aggregator services e.g. Service Registry.  # noqa: E501

        :param id: The id of this Service.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Service.

        Name of this service. Should be human readable.  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.

        Name of this service. Should be human readable.  # noqa: E501

        :param name: The name of this Service.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Service.


        :return: The type of this Service.
        :rtype: ServiceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Service.


        :param type: The type of this Service.
        :type type: ServiceType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this Service.

        Description of the service. Should be human readable and provide information about the service.  # noqa: E501

        :return: The description of this Service.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Service.

        Description of the service. Should be human readable and provide information about the service.  # noqa: E501

        :param description: The description of this Service.
        :type description: str
        """

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this Service.


        :return: The organization of this Service.
        :rtype: ServiceOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Service.


        :param organization: The organization of this Service.
        :type organization: ServiceOrganization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def contact_url(self):
        """Gets the contact_url of this Service.

        URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format).  # noqa: E501

        :return: The contact_url of this Service.
        :rtype: str
        """
        return self._contact_url

    @contact_url.setter
    def contact_url(self, contact_url):
        """Sets the contact_url of this Service.

        URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format).  # noqa: E501

        :param contact_url: The contact_url of this Service.
        :type contact_url: str
        """

        self._contact_url = contact_url

    @property
    def documentation_url(self):
        """Gets the documentation_url of this Service.

        URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication.  # noqa: E501

        :return: The documentation_url of this Service.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this Service.

        URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication.  # noqa: E501

        :param documentation_url: The documentation_url of this Service.
        :type documentation_url: str
        """

        self._documentation_url = documentation_url

    @property
    def created_at(self):
        """Gets the created_at of this Service.

        Timestamp describing when the service was first deployed and available (RFC 3339 format)  # noqa: E501

        :return: The created_at of this Service.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Service.

        Timestamp describing when the service was first deployed and available (RFC 3339 format)  # noqa: E501

        :param created_at: The created_at of this Service.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Service.

        Timestamp describing when the service was last updated (RFC 3339 format)  # noqa: E501

        :return: The updated_at of this Service.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Service.

        Timestamp describing when the service was last updated (RFC 3339 format)  # noqa: E501

        :param updated_at: The updated_at of this Service.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def environment(self):
        """Gets the environment of this Service.

        Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced.  # noqa: E501

        :return: The environment of this Service.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Service.

        Environment the service is running in. Use this to distinguish between production, development and testing/staging deployments. Suggested values are prod, test, dev, staging. However this is advised and not enforced.  # noqa: E501

        :param environment: The environment of this Service.
        :type environment: str
        """

        self._environment = environment

    @property
    def version(self):
        """Gets the version of this Service.

        Version of the service being described. Semantic versioning is recommended, but other identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the service is updated.  # noqa: E501

        :return: The version of this Service.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Service.

        Version of the service being described. Semantic versioning is recommended, but other identifiers, such as dates or commit hashes, are also allowed. The version should be changed whenever the service is updated.  # noqa: E501

        :param version: The version of this Service.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
