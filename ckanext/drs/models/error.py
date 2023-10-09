# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ckanext.drs.models.base_model import Model
import ckanext.drs.utils as util


class Error(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, msg=None, status_code=None):  # noqa: E501
        """Error - a model defined in OpenAPI

        :param msg: The msg of this Error.  # noqa: E501
        :type msg: str
        :param status_code: The status_code of this Error.  # noqa: E501
        :type status_code: int
        """
        self.openapi_types = {
            'msg': str,
            'status_code': int
        }

        self.attribute_map = {
            'msg': 'msg',
            'status_code': 'status_code'
        }

        self._msg = msg
        self._status_code = status_code

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def msg(self):
        """Gets the msg of this Error.

        A detailed error message.  # noqa: E501

        :return: The msg of this Error.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this Error.

        A detailed error message.  # noqa: E501

        :param msg: The msg of this Error.
        :type msg: str
        """

        self._msg = msg

    @property
    def status_code(self):
        """Gets the status_code of this Error.

        The integer representing the HTTP status code (e.g. 200, 404).  # noqa: E501

        :return: The status_code of this Error.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Error.

        The integer representing the HTTP status code (e.g. 200, 404).  # noqa: E501

        :param status_code: The status_code of this Error.
        :type status_code: int
        """

        self._status_code = status_code
