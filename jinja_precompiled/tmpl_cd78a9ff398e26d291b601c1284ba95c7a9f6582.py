from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationTagsService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/** @fileoverview A data service that stores tags for the exploration. */\n\noppia.factory(\'ExplorationTagsService\', [\n  \'ExplorationPropertyService\',\n  function(ExplorationPropertyService) {\n    var child = Object.create(ExplorationPropertyService);\n    child.propertyName = \'tags\';\n    child._normalize = function(value) {\n      for (var i = 0; i < value.length; i++) {\n        value[i] = value[i].trim().replace(/\\s+/g, \' \');\n      }\n      // TODO(sll): Prevent duplicate tags from being added.\n      return value;\n    };\n    child._isValid = function(value) {\n      // Every tag should match the TAG_REGEX.\n      for (var i = 0; i < value.length; i++) {\n        var tagRegex = new RegExp(GLOBALS.TAG_REGEX);\n        if (!value[i].match(tagRegex)) {\n          return false;\n        }\n      }\n\n      return true;\n    };\n    return child;\n  }\n]);'

blocks = {}
debug_info = ''