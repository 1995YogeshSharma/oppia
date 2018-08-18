from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/HintObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of Hint\n * domain objects.\n */\n\noppia.factory(\'HintObjectFactory\', [\n  \'SubtitledHtmlObjectFactory\',\n  function(SubtitledHtmlObjectFactory) {\n    var Hint = function(hintContent) {\n      this.hintContent = hintContent;\n    };\n\n    Hint.prototype.toBackendDict = function() {\n      return {\n        hint_content: this.hintContent.toBackendDict()\n      };\n    };\n\n    Hint.createFromBackendDict = function(hintBackendDict) {\n      return new Hint(\n        SubtitledHtmlObjectFactory.createFromBackendDict(\n          hintBackendDict.hint_content));\n    };\n\n    Hint.createNew = function(hintContentId, hintContent) {\n      return new Hint(\n        SubtitledHtmlObjectFactory.createDefault(hintContent, hintContentId));\n    };\n\n    return Hint;\n  }\n]);'

blocks = {}
debug_info = ''