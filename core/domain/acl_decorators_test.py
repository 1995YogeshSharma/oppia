# coding: utf-8
#
# Copyright 2016 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from core.domain import acl_decorators
from core.controllers import base
from core.domain import rights_manager
from core.tests import test_utils
import feconf
import webtest
import webapp2


class PlayExplorationDecoratorTest(test_utils.GenericTestBase):
    """Tests for play exploration decorator."""
    published_exp_id = 'exp_id_1'
    private_exp_id = 'exp_id_2'

    def mock_fun(self, obj, act_id):
        return act_id

    class MockHandler(base.BaseHandler):
        @acl_decorators.can_play_exploration
        def get(self, exploration_id):
            return self.render_json({'exploration_id': exploration_id})

    def setUp(self):
        super(PlayExplorationDecoratorTest, self).setUp()
        self.signup(self.OWNER_EMAIL, self.OWNER_USERNAME)
        self.signup(self.ADMIN_EMAIL, self.ADMIN_USERNAME)
        self.OWNER_ID = self.get_user_id_from_email(self.OWNER_EMAIL)
        self.set_admins([self.ADMIN_USERNAME])
        self.testapp = webtest.TestApp(webapp2.WSGIApplication(
            [webapp2.Route('/mock/<exploration_id>', self.MockHandler)],
            debug=feconf.DEBUG,
        ))
        self.save_new_valid_exploration(
            self.published_exp_id, self.OWNER_ID)
        self.save_new_valid_exploration(
            self.private_exp_id, self.OWNER_ID)
        rights_manager.publish_exploration(
            self.OWNER_ID, self.published_exp_id)

    def test_guest_can_access_published_exploration(self):
        response = self.get_json('/mock/%s' % self.published_exp_id)
        self.assertEqual(response['exploration_id'], self.published_exp_id)

    def test_admin_can_access_private_exploration(self):
        self.login(self.ADMIN_EMAIL)
        response = self.get_json('/mock/%s' % self.private_exp_id)
        self.assertEqual(response['exploration_id'], self.private_exp_id)
        self.logout()

    def test_owner_can_access_private_exploration(self):
        self.login(self.OWNER_EMAIL)
        response = self.get_json('/mock/%s' % self.private_exp_id)
        self.assertEqual(response['exploration_id'], self.private_exp_id)
        self.logout()


class PlayCollectionDecoratorTest(test_utils.GenericTestBase):
    """Tests for play collection decorator."""
    published_exp_id = 'exp_id_1'
    private_exp_id = 'exp_id_2'
    published_col_id = 'col_id_1'
    private_col_id = 'col_id_2'

    def mock_fun(self, obj, act_id):
        return act_id

    class MockHandler(base.BaseHandler):
        @acl_decorators.can_play_collection
        def get(self, collection_id):
            return self.render_json({'collection_id': collection_id})

    def setUp(self):
        super(PlayCollectionDecoratorTest, self).setUp()
        self.signup(self.OWNER_EMAIL, self.OWNER_USERNAME)
        self.signup(self.ADMIN_EMAIL, self.ADMIN_USERNAME)
        self.OWNER_ID = self.get_user_id_from_email(self.OWNER_EMAIL)
        self.set_admins([self.ADMIN_USERNAME])
        self.testapp = webtest.TestApp(webapp2.WSGIApplication(
            [webapp2.Route('/mock/<collection_id>', self.MockHandler)],
            debug=feconf.DEBUG,
        ))
        self.save_new_valid_exploration(
            self.published_exp_id, self.OWNER_ID)
        self.save_new_valid_exploration(
            self.private_exp_id, self.OWNER_ID)
        self.save_new_valid_collection(
            self.published_col_id, self.OWNER_ID,
            exploration_id=self.published_col_id)
        self.save_new_valid_collection(
            self.private_col_id, self.OWNER_ID,
            exploration_id=self.private_col_id)
        rights_manager.publish_exploration(
            self.OWNER_ID, self.published_exp_id)
        rights_manager.publish_collection(
            self.OWNER_ID, self.published_col_id)

    def test_guest_can_access_published_collection(self):
        response = self.get_json('/mock/%s' % self.published_col_id)
        self.assertEqual(response['collection_id'], self.published_col_id)

    def test_admin_can_access_private_collection(self):
        self.login(self.ADMIN_EMAIL)
        response = self.get_json('/mock/%s' % self.private_col_id)
        self.assertEqual(response['collection_id'], self.private_col_id)
        self.logout()

    def test_owner_can_access_private_collection(self):
        self.login(self.OWNER_EMAIL)
        response = self.get_json('/mock/%s' % self.private_col_id)
        self.assertEqual(response['collection_id'], self.private_col_id)
        self.logout()
