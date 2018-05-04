# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryOptions(Model):
    """Additional parameters for a set of operations.

    :param top: Maximum number of records to return.
    :type top: int
    :param order_by: Ordering expression using OData notation. One or more
     comma-separated column names with an optional "desc" (the default) or
     "asc", e.g. "$orderby=PolicyAssignmentId, ResourceId asc".
    :type order_by: str
    :param select: Select expression using OData notation. Limits the columns
     on each record to just those requested, e.g. "$select=PolicyAssignmentId,
     ResourceId".
    :type select: str
    :param from_property: ISO 8601 formatted timestamp specifying the start
     time of the interval to query. When not specified, the service uses ($to -
     1-day).
    :type from_property: datetime
    :param to: ISO 8601 formatted timestamp specifying the end time of the
     interval to query. When not specified, the service uses request time.
    :type to: datetime
    :param filter: OData filter expression.
    :type filter: str
    :param apply: OData apply expression for aggregations.
    :type apply: str
    """

    _attribute_map = {
        'top': {'key': '', 'type': 'int'},
        'order_by': {'key': '', 'type': 'str'},
        'select': {'key': '', 'type': 'str'},
        'from_property': {'key': '', 'type': 'iso-8601'},
        'to': {'key': '', 'type': 'iso-8601'},
        'filter': {'key': '', 'type': 'str'},
        'apply': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, top: int=None, order_by: str=None, select: str=None, from_property=None, to=None, filter: str=None, apply: str=None, **kwargs) -> None:
        super(QueryOptions, self).__init__(**kwargs)
        self.top = top
        self.order_by = order_by
        self.select = select
        self.from_property = from_property
        self.to = to
        self.filter = filter
        self.apply = apply
