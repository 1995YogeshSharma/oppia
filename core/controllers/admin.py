# Copyright 2014 The Oppia Authors. All Rights Reserved.
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

"""Controllers for the admin view."""

import logging

import jinja2

from core import jobs
from core import jobs_registry
from core.controllers import base
from core.controllers import editor
from core.domain import collection_services
from core.domain import config_domain
from core.domain import config_services
from core.domain import exp_services
from core.domain import recommendations_services
from core.domain import rights_manager
from core.domain import role_services
from core.domain import rte_component_registry
from core.domain import user_services
from core.platform import models
import feconf
import utils

current_user_services = models.Registry.import_current_user_services()


def require_super_admin(handler):
    """Decorator that checks if the current user is a super admin."""
    def test_super_admin(self, **kwargs):
        """Checks if the user is logged in and is a super admin."""
        if not self.user_id:
            self.redirect(
                current_user_services.create_login_url(self.request.uri))
            return
        if not current_user_services.is_current_user_super_admin():
            raise self.UnauthorizedUserException(
                '%s is not a super admin of this application', self.user_id)
        return handler(self, **kwargs)

    return test_super_admin


def check_and_update_config_role(old_list, new_list, role):
    """Changes roles for users in old_list and new_list. If user belongs to
    new_list but not in old list, its role is changed to specified role. If a
    user belongs to old list but not new list, its role is changed to
    exploration editor.

    Args:
        old_list: list(str). Existing list of usernames with given
            role.
        new_list: list(str). Updated list of usernames with given role.
        role: str. The role to be used for users in these lists.
    """
    for username in old_list:
        if username not in new_list:
            user_services.update_user_role(
                user_services.get_user_id_from_username(username),
                feconf.ROLE_EXPLORATION_EDITOR)

    for username in new_list:
        if username not in old_list:
            user_services.update_user_role(
                user_services.get_user_id_from_username(username),
                role)


class AdminPage(base.BaseHandler):
    """Admin page shown in the App Engine admin console."""
    @require_super_admin
    def get(self):
        """Handles GET requests."""
        demo_exploration_ids = feconf.DEMO_EXPLORATIONS.keys()

        recent_job_data = jobs.get_data_for_recent_jobs()
        unfinished_job_data = jobs.get_data_for_unfinished_jobs()
        for job in unfinished_job_data:
            job['can_be_canceled'] = job['is_cancelable'] and any([
                klass.__name__ == job['job_type']
                for klass in jobs_registry.ONE_OFF_JOB_MANAGERS])

        queued_or_running_job_types = set([
            job['job_type'] for job in unfinished_job_data])
        one_off_job_specs = [{
            'job_type': klass.__name__,
            'is_queued_or_running': (
                klass.__name__ in queued_or_running_job_types)
        } for klass in jobs_registry.ONE_OFF_JOB_MANAGERS]

        continuous_computations_data = jobs.get_continuous_computations_info(
            jobs_registry.ALL_CONTINUOUS_COMPUTATION_MANAGERS)
        for computation in continuous_computations_data:
            if computation['last_started_msec']:
                computation['human_readable_last_started'] = (
                    utils.get_human_readable_time_string(
                        computation['last_started_msec']))
            if computation['last_stopped_msec']:
                computation['human_readable_last_stopped'] = (
                    utils.get_human_readable_time_string(
                        computation['last_stopped_msec']))
            if computation['last_finished_msec']:
                computation['human_readable_last_finished'] = (
                    utils.get_human_readable_time_string(
                        computation['last_finished_msec']))

        self.values.update({
            'continuous_computations_data': continuous_computations_data,
            'demo_collections': sorted(feconf.DEMO_COLLECTIONS.iteritems()),
            'demo_explorations': sorted(feconf.DEMO_EXPLORATIONS.iteritems()),
            'demo_exploration_ids': demo_exploration_ids,
            'human_readable_current_time': (
                utils.get_human_readable_time_string(
                    utils.get_current_time_in_millisecs())),
            'one_off_job_specs': one_off_job_specs,
            'recent_job_data': recent_job_data,
            'rte_components_html': jinja2.utils.Markup(
                rte_component_registry.Registry.get_html_for_all_components()),
            'unfinished_job_data': unfinished_job_data,
            'value_generators_js': jinja2.utils.Markup(
                editor.get_value_generators_js()),
            'updatable_roles': {
                role: role_services.get_human_readable_role(role)
                for role in role_services.UPDATABLE_ROLES
            },
            'viewable_roles': {
                role: role_services.get_human_readable_role(role)
                for role in role_services.VIEWABLE_ROLES
            },
            'role_graph_data': role_services.get_role_graph_data()
        })

        self.render_template('pages/admin/admin.html')


class AdminHandler(base.BaseHandler):
    """Handler for the admin page."""

    GET_HANDLER_ERROR_RETURN_TYPE = feconf.HANDLER_TYPE_JSON

    role_sync_dict = {
        'WHITELISTED_EMAIL_SENDERS': {
            'name': 'whitelisted_email_senders',
            'role': feconf.ROLE_ADMIN
        },
        'ADMIN_USERNAMES': {
            'name': 'admin_usernames',
            'role': feconf.ROLE_ADMIN
        },
        'COLLECTION_EDITOR_WHITELIST': {
            'name': 'collection_editor_whitelist',
            'role': feconf.ROLE_COLLECTION_EDITOR
        },
        'BANNED_USERNAMES': {
            'name': 'banned_usernames',
            'role': feconf.ROLE_BANNED_USER
        },
        'MODERATOR_USERNAMES': {
            'name': 'moderator_usernames',
            'role': feconf.ROLE_MODERATOR
        }
    }

    @require_super_admin
    def get(self):
        """Handles GET requests."""

        self.render_json({
            'config_properties': (
                config_domain.Registry.get_config_property_schemas()),
        })

    @require_super_admin
    def post(self):
        """Handles POST requests."""
        try:
            if self.payload.get('action') == 'reload_exploration':
                exploration_id = self.payload.get('exploration_id')
                self._reload_exploration(exploration_id)
            elif self.payload.get('action') == 'reload_collection':
                collection_id = self.payload.get('collection_id')
                self._reload_collection(collection_id)
            elif self.payload.get('action') == 'clear_search_index':
                exp_services.clear_search_index()
            elif self.payload.get('action') == 'save_config_properties':
                new_config_property_values = self.payload.get(
                    'new_config_property_values')
                logging.info('[ADMIN] %s saved config property values: %s' %
                             (self.user_id, new_config_property_values))
                config_properties = (
                    config_domain.Registry.get_config_property_schemas())
                for (name, value) in new_config_property_values.iteritems():
                    config_services.set_property(self.user_id, name, value)
                    # Below checks are for maintaining the sync between roles
                    # in old and new authorization system.
                    # TODO (1995YogeshSharma): Remove this block of code once
                    # the new system takes over.
                    for key in self.role_sync_dict:
                        if name == self.role_sync_dict[key]['name']:
                            check_and_update_config_role(
                                config_properties[name]['value'], value,
                                self.role_sync_dict[key]['role'])
                    # if name == 'whitelisted_email_senders':
                    #     check_and_update_config_role(
                    #         config_properties[name]['value'], value,
                    #         feconf.ROLE_ADMIN)
                    # if name == 'admin_usernames':
                    #     check_and_update_config_role(
                    #         config_properties[name]['value'], value,
                    #         feconf.ROLE_ADMIN)
                    # if name == 'collection_editor_whitelist':
                    #     check_and_update_config_role(
                    #         config_properties[name]['value'], value,
                    #         feconf.ROLE_COLLECTION_EDITOR)
                    # if name == 'banned_usernames':
                    #     check_and_update_config_role(
                    #         config_properties[name]['value'], value,
                    #         feconf.ROLE_BANNED_USER)
                    # if name == 'moderator_usernames':
                    #     check_and_update_config_role(
                    #         config_properties[name]['value'], value,
                    #         feconf.ROLE_MODERATOR)
            elif self.payload.get('action') == 'revert_config_property':
                config_property_id = self.payload.get('config_property_id')
                config_property = config_domain.Registry.get_config_property(
                    config_property_id)
                config_value = config_property.value
                logging.info('[ADMIN] %s reverted config property: %s' %
                             (self.user_id, config_property_id))
                config_services.revert_property(
                    self.user_id, config_property_id)

                # Below checks are for maintaining the sync between roles
                # in old and new authorization system.
                # TODO (1995YogeshSharma): Remove this block of code once
                # the new system takes over.
                for key in self.role_sync_dict:
                    if config_property_id == self.role_sync_dict[key]['name']:
                        check_and_update_config_role(
                            config_value, config_property.default_value,
                            self.role_sync_dict[key]['role'])

                # if config_property_id == 'whitelisted_email_senders':
                #     check_and_update_config_role(
                #         config_value, config_property.default_value,
                #         feconf.ROLE_ADMIN)
                # if config_property_id == 'admin_usernames':
                #     check_and_update_config_role(
                #         config_value, config_property.default_value,
                #         feconf.ROLE_ADMIN)
                # if config_property_id == 'collection_editor_whitelist':
                #     check_and_update_config_role(
                #         config_value, config_property.default_value,
                #         feconf.ROLE_COLLECTION_EDITOR)
                # if config_property_id == 'banned_usernames':
                #     check_and_update_config_role(
                #         config_value, config_property.default_value,
                #         feconf.ROLE_BANNED_USER)
                # if config_property_id == 'moderator_usernames':
                #     check_and_update_config_role(
                #         config_value, config_property.default_value,
                #         feconf.ROLE_MODERATOR)
            elif self.payload.get('action') == 'start_new_job':
                for klass in jobs_registry.ONE_OFF_JOB_MANAGERS:
                    if klass.__name__ == self.payload.get('job_type'):
                        klass.enqueue(klass.create_new())
                        break
            elif self.payload.get('action') == 'cancel_job':
                job_id = self.payload.get('job_id')
                job_type = self.payload.get('job_type')
                for klass in jobs_registry.ONE_OFF_JOB_MANAGERS:
                    if klass.__name__ == job_type:
                        klass.cancel(job_id, self.user_id)
                        break
            elif self.payload.get('action') == 'start_computation':
                computation_type = self.payload.get('computation_type')
                for klass in jobs_registry.ALL_CONTINUOUS_COMPUTATION_MANAGERS:
                    if klass.__name__ == computation_type:
                        klass.start_computation()
                        break
            elif self.payload.get('action') == 'stop_computation':
                computation_type = self.payload.get('computation_type')
                for klass in jobs_registry.ALL_CONTINUOUS_COMPUTATION_MANAGERS:
                    if klass.__name__ == computation_type:
                        klass.stop_computation(self.user_id)
                        break
            elif self.payload.get('action') == 'upload_topic_similarities':
                data = self.payload.get('data')
                recommendations_services.update_topic_similarities(data)
            self.render_json({})
        except Exception as e:
            self.render_json({'error': unicode(e)})
            raise

    def _reload_exploration(self, exploration_id):
        if feconf.DEV_MODE:
            logging.info(
                '[ADMIN] %s reloaded exploration %s' %
                (self.user_id, exploration_id))
            exp_services.load_demo(unicode(exploration_id))
            rights_manager.release_ownership_of_exploration(
                feconf.SYSTEM_COMMITTER_ID, unicode(exploration_id))
        else:
            raise Exception('Cannot reload an exploration in production.')

    def _reload_collection(self, collection_id):
        if feconf.DEV_MODE:
            logging.info(
                '[ADMIN] %s reloaded collection %s' %
                (self.user_id, collection_id))
            collection_services.load_demo(unicode(collection_id))
            rights_manager.release_ownership_of_collection(
                feconf.SYSTEM_COMMITTER_ID, unicode(collection_id))
        else:
            raise Exception('Cannot reload a collection in production.')


class AdminRoleHandler(base.BaseHandler):
    """Handler for roles tab of admin page. Used to view and update roles."""

    @require_super_admin
    def get(self):
        view_method = self.request.params['method']

        if view_method == feconf.VIEW_METHOD_ROLE:
            role = self.request.params[feconf.VIEW_METHOD_ROLE]
            users_by_role = {
                username: role
                for username in user_services.get_usernames_by_role(role)
            }
            role_services.store_role_query(
                self.user_id, feconf.VIEW_ROLE, method=feconf.VIEW_METHOD_ROLE,
                role=role)
            self.render_json(users_by_role)
        elif view_method == feconf.VIEW_METHOD_USERNAME:
            username = self.request.params[feconf.VIEW_METHOD_USERNAME]
            user_id = user_services.get_user_id_from_username(username)
            role_services.store_role_query(
                self.user_id, feconf.VIEW_ROLE,
                method=feconf.VIEW_METHOD_USERNAME, username=username)
            if user_id is None:
                self.render_json({})
            else:
                user_role_dict = {
                    username: user_services.get_user_role_from_id(user_id)
                }
                self.render_json(user_role_dict)
        else:
            self.render_json({'error': 'Invalid method to view'})

    @require_super_admin
    def post(self):
        try:
            username = self.payload.get('username')
            role = self.payload.get('role')
            user_id = user_services.get_user_id_from_username(username)
            user_services.update_user_role(user_id, role)
            role_services.store_role_query(
                self.user_id, feconf.UPDATE_ROLE, role=role,
                username=username)
            self.render_json({})
        except Exception as e:
            self.render_json({'error': unicode(e)})
            raise e


class AdminJobOutput(base.BaseHandler):
    """Retrieves job output to show on the admin page."""

    GET_HANDLER_ERROR_RETURN_TYPE = feconf.HANDLER_TYPE_JSON

    @require_super_admin
    def get(self):
        """Handles GET requests."""
        job_id = self.request.get('job_id')
        self.render_json({
            'output': jobs.get_job_output(job_id)
        })


class AdminTopicsCsvDownloadHandler(base.BaseHandler):
    """Retrieves topic similarity data for download."""

    @require_super_admin
    def get(self):
        self.response.headers['Content-Type'] = 'text/csv'
        self.response.headers['Content-Disposition'] = (
            'attachment; filename=topic_similarities.csv')
        self.response.write(
            recommendations_services.get_topic_similarities_as_csv())
