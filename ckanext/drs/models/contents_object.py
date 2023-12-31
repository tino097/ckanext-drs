# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ckanext.drs.models.base_model import Model
import ckanext.drs.utils as util


class ContentsObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, id=None, drs_uri=None, contents=None):  # noqa: E501
        """ContentsObject - a model defined in OpenAPI

        :param name: The name of this ContentsObject.  # noqa: E501
        :type name: str
        :param id: The id of this ContentsObject.  # noqa: E501
        :type id: str
        :param drs_uri: The drs_uri of this ContentsObject.  # noqa: E501
        :type drs_uri: List[str]
        :param contents: The contents of this ContentsObject.  # noqa: E501
        :type contents: List[ContentsObject]
        """
        self.openapi_types = {
            'name': str,
            'id': str,
            'drs_uri': List[str],
            'contents': List[ContentsObject]
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'drs_uri': 'drs_uri',
            'contents': 'contents'
        }

        self._name = name
        self._id = id
        self._drs_uri = drs_uri
        self._contents = contents

    @classmethod
    def from_dict(cls, dikt) -> 'ContentsObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ContentsObject of this ContentsObject.  # noqa: E501
        :rtype: ContentsObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ContentsObject.

        A name declared by the bundle author that must be used when materialising this object, overriding any name directly associated with the object itself. The name must be unique within the containing bundle. This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].  # noqa: E501

        :return: The name of this ContentsObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentsObject.

        A name declared by the bundle author that must be used when materialising this object, overriding any name directly associated with the object itself. The name must be unique within the containing bundle. This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].  # noqa: E501

        :param name: The name of this ContentsObject.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this ContentsObject.

        A DRS identifier of a `DrsObject` (either a single blob or a nested bundle). If this ContentsObject is an object within a nested bundle, then the id is optional. Otherwise, the id is required.  # noqa: E501

        :return: The id of this ContentsObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentsObject.

        A DRS identifier of a `DrsObject` (either a single blob or a nested bundle). If this ContentsObject is an object within a nested bundle, then the id is optional. Otherwise, the id is required.  # noqa: E501

        :param id: The id of this ContentsObject.
        :type id: str
        """

        self._id = id

    @property
    def drs_uri(self):
        """Gets the drs_uri of this ContentsObject.

        A list of full DRS identifier URI paths that may be used to obtain the object. These URIs may be external to this DRS instance.  # noqa: E501

        :return: The drs_uri of this ContentsObject.
        :rtype: List[str]
        """
        return self._drs_uri

    @drs_uri.setter
    def drs_uri(self, drs_uri):
        """Sets the drs_uri of this ContentsObject.

        A list of full DRS identifier URI paths that may be used to obtain the object. These URIs may be external to this DRS instance.  # noqa: E501

        :param drs_uri: The drs_uri of this ContentsObject.
        :type drs_uri: List[str]
        """

        self._drs_uri = drs_uri

    @property
    def contents(self):
        """Gets the contents of this ContentsObject.

        If this ContentsObject describes a nested bundle and the caller specified \"?expand=true\" on the request, then this contents array must be present and describe the objects within the nested bundle.  # noqa: E501

        :return: The contents of this ContentsObject.
        :rtype: List[ContentsObject]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ContentsObject.

        If this ContentsObject describes a nested bundle and the caller specified \"?expand=true\" on the request, then this contents array must be present and describe the objects within the nested bundle.  # noqa: E501

        :param contents: The contents of this ContentsObject.
        :type contents: List[ContentsObject]
        """

        self._contents = contents
