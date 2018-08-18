from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/EditabilityService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for checking the ability to edit an exploration.\n */\n\n// TODO(sll): Should this depend on a versioning service that keeps track of\n// the current active version? Previous versions should not be editable.\n// TODO(SD): Remove translatable part from this service after translation tab\n// will get implemented.\noppia.factory(\'EditabilityService\', [function() {\n  var isEditable = false;\n  var isTranslatable = false;\n  var inTutorialMode = false;\n\n  return {\n    isEditable: function() {\n      return isEditable && !inTutorialMode;\n    },\n    isTranslatable: function() {\n      return isTranslatable && !inTutorialMode;\n    },\n    isEditableOutsideTutorialMode: function() {\n      return isEditable;\n    },\n    markEditable: function() {\n      isEditable = true;\n    },\n    markTranslatable: function() {\n      isTranslatable = true;\n    },\n    markNotEditable: function() {\n      isEditable = false;\n    },\n    onEndTutorial: function() {\n      inTutorialMode = false;\n    },\n    onStartTutorial: function() {\n      inTutorialMode = true;\n    }\n  };\n}]);'

blocks = {}
debug_info = ''