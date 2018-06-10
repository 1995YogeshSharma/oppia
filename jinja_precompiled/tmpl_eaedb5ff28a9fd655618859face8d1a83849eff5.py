from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/AnswerGroupsCacheService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n* @fileoverview A state-specific cache for interaction handlers. It stores\n* handlers corresponding to an interaction id so that they can be restored if\n* the interaction is changed back while the user is still in this state.\n* This cache should be reset each time the state editor is initialized.\n*/\n\noppia.factory(\'AnswerGroupsCacheService\', [function() {\n  var _cache = {};\n  return {\n    reset: function() {\n      _cache = {};\n    },\n    contains: function(interactionId) {\n      return _cache.hasOwnProperty(interactionId);\n    },\n    set: function(interactionId, answerGroups) {\n      _cache[interactionId] = angular.copy(answerGroups);\n    },\n    get: function(interactionId) {\n      if (!_cache.hasOwnProperty(interactionId)) {\n        return null;\n      }\n      return angular.copy(_cache[interactionId]);\n    }\n  };\n}]);'

blocks = {}
debug_info = ''