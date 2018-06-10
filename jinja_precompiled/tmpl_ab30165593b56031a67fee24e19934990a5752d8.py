from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/HtmlEscaperService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for HTML serialization and escaping.\n */\n\noppia.factory(\'HtmlEscaperService\', [\'$log\', function($log) {\n  var htmlEscaper = {\n    objToEscapedJson: function(obj) {\n      return this.unescapedStrToEscapedStr(JSON.stringify(obj));\n    },\n    escapedJsonToObj: function(json) {\n      if (!json) {\n        $log.error(\'Empty string was passed to JSON decoder.\');\n        return \'\';\n      }\n      return JSON.parse(this.escapedStrToUnescapedStr(json));\n    },\n    unescapedStrToEscapedStr: function(str) {\n      return String(str)\n        .replace(/&/g, \'&amp;\')\n        .replace(/"/g, \'&quot;\')\n        .replace(/\'/g, \'&#39;\')\n        .replace(/</g, \'&lt;\')\n        .replace(/>/g, \'&gt;\');\n    },\n    escapedStrToUnescapedStr: function(value) {\n      return String(value)\n        .replace(/&quot;/g, \'"\')\n        .replace(/&#39;/g, \'\\\'\')\n        .replace(/&lt;/g, \'<\')\n        .replace(/&gt;/g, \'>\')\n        .replace(/&amp;/g, \'&\');\n    }\n  };\n  return htmlEscaper;\n}]);'

blocks = {}
debug_info = ''