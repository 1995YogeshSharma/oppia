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

"""Controllers for the learner dashboard."""

from core.controllers import base
from core.domain import config_domain
from core.domain import feedback_services
from core.domain import learner_progress_services
from core.domain import subscription_services
from core.domain import summary_services
from core.domain import user_services
import feconf
import utils


class LearnerDashboardPage(base.BaseHandler):
    """Page showing the user's learner dashboard."""

    @base.require_user
    def get(self):
        if self.username in config_domain.BANNED_USERNAMES.value:
            raise self.UnauthorizedUserException(
                'You do not have the credentials to access this page.')
        elif user_services.has_fully_registered(self.user_id):
            self.values.update({
                'nav_mode': feconf.NAV_MODE_LEARNER_DASHBOARD
            })
            self.render_template(
                'pages/learner_dashboard/learner_dashboard.html',
                redirect_url_on_logout='/')
        else:
            self.redirect(utils.set_url_query_parameter(
                feconf.SIGNUP_URL, 'return_url', feconf.LEARNER_DASHBOARD_URL))


class LearnerDashboardHandler(base.BaseHandler):
    """Provides data for the user's learner dashboard page."""

    GET_HANDLER_ERROR_RETURN_TYPE = feconf.HANDLER_TYPE_JSON

    @base.require_user
    def get(self):
        """Handles GET requests."""
        (learner_progress, number_of_deleted_activities,
         completed_to_incomplete_collections) = (
             learner_progress_services.get_activity_progress(self.user_id))

        completed_exp_summary_dicts = (
            summary_services.get_displayable_exp_summary_dicts(
                learner_progress.completed_exp_summaries))

        incomplete_exp_summary_dicts = (
            summary_services.get_displayable_exp_summary_dicts(
                learner_progress.incomplete_exp_summaries))

        completed_collection_summary_dicts = (
            learner_progress_services.get_collection_summary_dicts(
                learner_progress.completed_collection_summaries))
        incomplete_collection_summary_dicts = (
            learner_progress_services.get_collection_summary_dicts(
                learner_progress.incomplete_collection_summaries))

        creators_subscribed_to = (
            subscription_services.get_all_creators_subscribed_to(self.user_id))
        creators_settings = user_services.get_users_settings(
            creators_subscribed_to)
        subscription_list = []

        for index, creator_settings in enumerate(creators_settings):
            subscription_summary = {
                'creator_picture_data_url': (
                    creator_settings.profile_picture_data_url),
                'creator_username': creator_settings.username,
                'creator_impact': (
                    user_services.get_user_impact_score(
                        creators_subscribed_to[index]))
            }

            subscription_list.append(subscription_summary)

        self.values.update({
            'completed_explorations_list': completed_exp_summary_dicts,
            'completed_collections_list': completed_collection_summary_dicts,
            'incomplete_explorations_list': incomplete_exp_summary_dicts,
            'incomplete_collections_list': incomplete_collection_summary_dicts,
            'number_of_deleted_activities': number_of_deleted_activities,
            'completed_to_incomplete_collections': (
                completed_to_incomplete_collections),
            'subscription_list': subscription_list
        })
        self.render_json(self.values)


class LearnerDashboardFeedbackThreadHandler(base.BaseHandler):
    """Gets all the messages in a thread."""

    @base.require_user
    def get(self, exploration_id, thread_id):
        """Handles GET requests."""
        messages = feedback_services.get_messages(
            exploration_id, thread_id)
        author_ids = [m.author_id for m in messages]
        authors_settings = user_services.get_users_settings(author_ids)

        message_ids = [m.message_id for m in messages]
        feedback_services.update_messages_read_by_the_user(
            self.user_id, exploration_id, thread_id, message_ids)

        message_summary_list = []
        for m, author_settings in zip(messages, authors_settings):
            message_summary = {
                'text': m.text,
                'author_username': author_settings.username,
                'author_picture_data_url': (
                    author_settings.profile_picture_data_url)
            }
            message_summary_list.append(message_summary)

        self.render_json({
            'message_summary_list': message_summary_list
        })
