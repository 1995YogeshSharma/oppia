from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationCorrectnessFeedbackService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for checking the correctness feedback for an\n * exploration.\n */\n\noppia.factory(\'ExplorationCorrectnessFeedbackService\', [\n  \'ExplorationPropertyService\', function(ExplorationPropertyService) {\n    var child = Object.create(ExplorationPropertyService);\n    child.propertyName = \'correctness_feedback_enabled\';\n\n    child._isValid = function(value) {\n      return (typeof value === \'boolean\');\n    };\n\n    child.isEnabled = function() {\n      return child.savedMemento;\n    };\n\n    child.toggleCorrectnessFeedback = function() {\n      child.displayed = !child.displayed;\n      child.saveDisplayedValue();\n    };\n\n    return child;\n  }\n]);'

blocks = {}
debug_info = ''