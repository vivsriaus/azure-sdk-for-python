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


class ApplicationCreateParameters(Model):
    """Request parameters for create a new application.

    :param available_to_other_tenants: Indicates if the application will be
     available to other tenants
    :type available_to_other_tenants: bool
    :param display_name: Application display name
    :type display_name: str
    :param homepage: Application homepage
    :type homepage: str
    :param identifier_uris: Application Uris
    :type identifier_uris: list of str
    :param reply_urls: Application reply Urls
    :type reply_urls: list of str
    :param key_credentials: the list of KeyCredential objects
    :type key_credentials: list of :class:`KeyCredential
     <azure.graphrbac.models.KeyCredential>`
    :param password_credentials: the list of PasswordCredential objects
    :type password_credentials: list of :class:`PasswordCredential
     <azure.graphrbac.models.PasswordCredential>`
    """ 

    _validation = {
        'available_to_other_tenants': {'required': True},
        'display_name': {'required': True},
        'identifier_uris': {'required': True},
    }

    _attribute_map = {
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'homepage': {'key': 'homepage', 'type': 'str'},
        'identifier_uris': {'key': 'identifierUris', 'type': '[str]'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'key_credentials': {'key': 'keyCredentials', 'type': '[KeyCredential]'},
        'password_credentials': {'key': 'passwordCredentials', 'type': '[PasswordCredential]'},
    }

    def __init__(self, available_to_other_tenants, display_name, identifier_uris, homepage=None, reply_urls=None, key_credentials=None, password_credentials=None):
        self.available_to_other_tenants = available_to_other_tenants
        self.display_name = display_name
        self.homepage = homepage
        self.identifier_uris = identifier_uris
        self.reply_urls = reply_urls
        self.key_credentials = key_credentials
        self.password_credentials = password_credentials
