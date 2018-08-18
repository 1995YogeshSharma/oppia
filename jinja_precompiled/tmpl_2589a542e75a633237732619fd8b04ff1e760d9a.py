from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/TopicEditor.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Primary controller for the topic editor page.\n */\n\noppia.constant(\'INTERACTION_SPECS\', GLOBALS.INTERACTION_SPECS);\noppia.constant(\n  \'EDITABLE_TOPIC_DATA_URL_TEMPLATE\', \'/topic_editor_handler/data/<topic_id>\');\noppia.constant(\n  \'TOPIC_MANAGER_RIGHTS_URL_TEMPLATE\',\n  \'/rightshandler/assign_topic_manager/<topic_id>/<assignee_id>\');\noppia.constant(\n  \'TOPIC_RIGHTS_URL_TEMPLATE\', \'/rightshandler/get_topic_rights/<topic_id>\');\noppia.constant(\n  \'SUBTOPIC_PAGE_EDITOR_DATA_URL_TEMPLATE\',\n  \'/subtopic_page_editor_handler/data/<topic_id>/<subtopic_id>\');\n\noppia.constant(\n  \'TOPIC_NAME_INPUT_FOCUS_LABEL\', \'topicNameInputFocusLabel\');\n\noppia.controller(\'TopicEditor\', [\n  \'$scope\', \'TopicEditorStateService\', \'UrlService\',\n  function($scope, TopicEditorStateService, UrlService) {\n    TopicEditorStateService.loadTopic(UrlService.getTopicIdFromUrl());\n  }\n]);'

blocks = {}
debug_info = ''