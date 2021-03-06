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


class AdmCredential(Model):
    """Description of a NotificationHub AdmCredential.

    :param properties: Gets or sets properties of NotificationHub
     AdmCredential.
    :type properties: :class:`AdmCredentialProperties
     <azure.mgmt.notificationhubs.models.AdmCredentialProperties>`
    """ 

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'AdmCredentialProperties'},
    }

    def __init__(self, properties=None):
        self.properties = properties
