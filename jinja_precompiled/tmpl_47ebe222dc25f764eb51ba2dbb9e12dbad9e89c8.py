from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationLanguageCodeService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/** @fileoverview A data service that stores the exploration language code. */\n\noppia.factory(\'ExplorationLanguageCodeService\', [\n  \'ExplorationPropertyService\', function(ExplorationPropertyService) {\n    var child = Object.create(ExplorationPropertyService);\n    child.propertyName = \'language_code\';\n    child.getAllLanguageCodes = function() {\n      // TODO(sll): Update this once the App Engine search service supports\n      // 3-letter language codes.\n      return constants.ALL_LANGUAGE_CODES.filter(function(languageCodeDict) {\n        return languageCodeDict.code.length === 2;\n      });\n    };\n    child.getCurrentLanguageDescription = function() {\n      for (var i = 0; i < constants.ALL_LANGUAGE_CODES.length; i++) {\n        if (constants.ALL_LANGUAGE_CODES[i].code === child.displayed) {\n          return constants.ALL_LANGUAGE_CODES[i].description;\n        }\n      }\n    };\n    child._isValid = function(value) {\n      return constants.ALL_LANGUAGE_CODES.some(function(elt) {\n        // TODO(sll): Remove the second clause once the App Engine search\n        // service supports 3-letter language codes.\n        return elt.code === value && elt.code.length === 2;\n      });\n    };\n    return child;\n  }\n]);'

blocks = {}
debug_info = ''