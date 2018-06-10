from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/CollectionEditor.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Primary controller for the collection editor page.\n */\n\n// TODO(bhenning): These constants should be provided by the backend.\noppia.constant(\n  \'COLLECTION_DATA_URL_TEMPLATE\', \'/collection_handler/data/<collection_id>\');\noppia.constant(\n  \'EDITABLE_COLLECTION_DATA_URL_TEMPLATE\',\n  \'/collection_editor_handler/data/<collection_id>\');\noppia.constant(\n  \'COLLECTION_RIGHTS_URL_TEMPLATE\',\n  \'/collection_editor_handler/rights/<collection_id>\');\n\noppia.constant(\n  \'COLLECTION_TITLE_INPUT_FOCUS_LABEL\', \'collectionTitleInputFocusLabel\');\n\noppia.constant(\n  \'SEARCH_EXPLORATION_URL_TEMPLATE\',\n  \'/exploration/metadata_search?q=<query>\');\n\noppia.controller(\'CollectionEditor\', [\n  \'CollectionEditorStateService\',\n  function(CollectionEditorStateService) {\n    // Load the collection to be edited.\n    CollectionEditorStateService.loadCollection(GLOBALS.collectionId);\n  }\n]);'

blocks = {}
debug_info = ''