# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ckanext.drs.models.base_model import Model
import ckanext.drs.utils as util


class Authorizations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, supported_types=None, passport_auth_issuers=None, bearer_auth_issuers=None):  # noqa: E501
        """Authorizations - a model defined in OpenAPI

        :param supported_types: The supported_types of this Authorizations.  # noqa: E501
        :type supported_types: List[str]
        :param passport_auth_issuers: The passport_auth_issuers of this Authorizations.  # noqa: E501
        :type passport_auth_issuers: List[str]
        :param bearer_auth_issuers: The bearer_auth_issuers of this Authorizations.  # noqa: E501
        :type bearer_auth_issuers: List[str]
        """
        self.openapi_types = {
            'supported_types': List[str],
            'passport_auth_issuers': List[str],
            'bearer_auth_issuers': List[str]
        }

        self.attribute_map = {
            'supported_types': 'supported_types',
            'passport_auth_issuers': 'passport_auth_issuers',
            'bearer_auth_issuers': 'bearer_auth_issuers'
        }

        self._supported_types = supported_types
        self._passport_auth_issuers = passport_auth_issuers
        self._bearer_auth_issuers = bearer_auth_issuers

    @classmethod
    def from_dict(cls, dikt) -> 'Authorizations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Authorizations of this Authorizations.  # noqa: E501
        :rtype: Authorizations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def supported_types(self):
        """Gets the supported_types of this Authorizations.

        An Optional list of support authorization types. More than one can be supported and tried in sequence. Defaults to `None` if empty or missing.  # noqa: E501

        :return: The supported_types of this Authorizations.
        :rtype: List[str]
        """
        return self._supported_types

    @supported_types.setter
    def supported_types(self, supported_types):
        """Sets the supported_types of this Authorizations.

        An Optional list of support authorization types. More than one can be supported and tried in sequence. Defaults to `None` if empty or missing.  # noqa: E501

        :param supported_types: The supported_types of this Authorizations.
        :type supported_types: List[str]
        """
        allowed_values = ["None", "BasicAuth", "BearerAuth", "PassportAuth"]  # noqa: E501
        if not set(supported_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_types = supported_types

    @property
    def passport_auth_issuers(self):
        """Gets the passport_auth_issuers of this Authorizations.

        If authorizations contain `PassportAuth` this is a required list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller must only provide passports that contain visas from this list. It is strongly recommended that the caller validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.  # noqa: E501

        :return: The passport_auth_issuers of this Authorizations.
        :rtype: List[str]
        """
        return self._passport_auth_issuers

    @passport_auth_issuers.setter
    def passport_auth_issuers(self, passport_auth_issuers):
        """Sets the passport_auth_issuers of this Authorizations.

        If authorizations contain `PassportAuth` this is a required list of visa issuers (as found in a visa's `iss` claim) that may authorize access to this object. The caller must only provide passports that contain visas from this list. It is strongly recommended that the caller validate that it is appropriate to send the requested passport/visa to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.  # noqa: E501

        :param passport_auth_issuers: The passport_auth_issuers of this Authorizations.
        :type passport_auth_issuers: List[str]
        """

        self._passport_auth_issuers = passport_auth_issuers

    @property
    def bearer_auth_issuers(self):
        """Gets the bearer_auth_issuers of this Authorizations.

        If authorizations contain `BearerAuth` this is an optional list of issuers that may authorize access to this object. The caller must provide a token from one of these issuers. If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly recommended that the caller validate that it is appropriate to send the requested token to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.  # noqa: E501

        :return: The bearer_auth_issuers of this Authorizations.
        :rtype: List[str]
        """
        return self._bearer_auth_issuers

    @bearer_auth_issuers.setter
    def bearer_auth_issuers(self, bearer_auth_issuers):
        """Sets the bearer_auth_issuers of this Authorizations.

        If authorizations contain `BearerAuth` this is an optional list of issuers that may authorize access to this object. The caller must provide a token from one of these issuers. If this is empty or missing it assumed the caller knows which token to send via other means. It is strongly recommended that the caller validate that it is appropriate to send the requested token to the DRS server to mitigate attacks by malicious DRS servers requesting credentials they should not have.  # noqa: E501

        :param bearer_auth_issuers: The bearer_auth_issuers of this Authorizations.
        :type bearer_auth_issuers: List[str]
        """

        self._bearer_auth_issuers = bearer_auth_issuers
