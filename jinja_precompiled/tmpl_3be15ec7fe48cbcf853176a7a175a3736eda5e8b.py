from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/SubtitledHtmlObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of SubtitledHtml\n * domain objects.\n */\n\noppia.factory(\'SubtitledHtmlObjectFactory\', [\n  \'AudioTranslationObjectFactory\',\n  function(AudioTranslationObjectFactory) {\n    var SubtitledHtml = function(html, contentId) {\n      this._html = html;\n      this._contentId = contentId;\n    };\n\n    SubtitledHtml.prototype.getHtml = function() {\n      return this._html;\n    };\n\n    SubtitledHtml.prototype.getContentId = function() {\n      return this._contentId;\n    };\n\n    SubtitledHtml.prototype.setHtml = function(newHtml) {\n      this._html = newHtml;\n    };\n\n    SubtitledHtml.prototype.hasNoHtml = function() {\n      return !this._html;\n    };\n\n    SubtitledHtml.prototype.toBackendDict = function() {\n      return {\n        html: this._html,\n        content_id: this._contentId\n      };\n    };\n\n    SubtitledHtml.prototype.isEmpty = function() {\n      return this.hasNoHtml();\n    };\n\n    SubtitledHtml.createFromBackendDict = function(subtitledHtmlBackendDict) {\n      return new SubtitledHtml(\n        subtitledHtmlBackendDict.html, subtitledHtmlBackendDict.content_id);\n    };\n\n    SubtitledHtml.createDefault = function(html, contentId) {\n      return new SubtitledHtml(html, contentId);\n    };\n\n    return SubtitledHtml;\n  }\n]);'

blocks = {}
debug_info = ''