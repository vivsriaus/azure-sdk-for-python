﻿# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import unittest

import azure.mgmt.servermanager
from testutils.common_recordingtestcase import record
from tests.mgmt_testcase import HttpStatusCode, AzureMgmtTestCase


class MgmtServerManagerTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtServerManagerTest, self).setUp()
        self.client = self.create_mgmt_client(
            azure.mgmt.servermanager.ServerManagement
        )

    @record
    def test_servermanager_gateways(self):
        self.create_resource_group()
        gateway_name = self.get_resource_name('pygateway')
        region = 'centralus'

        gateway_async = self.client.gateway.create(
            self.group_name,
            gateway_name,
            region
        )
        gateway = gateway_async.result()
        self.assertEqual(gateway.name, gateway_name)

        gateway = self.client.gateway.get(
            self.group_name,
            gateway_name
        )
        self.assertEqual(gateway.name, gateway_name)

        gateways = list(self.client.gateway.list())
        self.assertEqual(len(gateways), 1)
        
            


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
