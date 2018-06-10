from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/HtmlEscaperServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for HTML serialization and escaping services.\n */\n\ndescribe(\'HTML escaper\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'HTML escaper service\', function() {\n    var ohe = null;\n\n    beforeEach(inject(function($injector) {\n      ohe = $injector.get(\'HtmlEscaperService\');\n    }));\n\n    it(\'should correctly translate between escaped and unescaped strings\',\n      function() {\n        var strs = [\'abc\', \'a&b<html>\', \'&&&&&\'];\n        for (var i = 0; i < strs.length; i++) {\n          expect(ohe.escapedStrToUnescapedStr(\n            ohe.unescapedStrToEscapedStr(strs[i]))).toEqual(strs[i]);\n        }\n      }\n    );\n\n    it(\'should correctly escape and unescape JSON\', function() {\n      var objs = [{\n        a: \'b\'\n      }, [\'a\', \'b\'], 2, true, \'abc\'];\n      for (var i = 0; i < objs.length; i++) {\n        expect(ohe.escapedJsonToObj(\n          ohe.objToEscapedJson(objs[i]))).toEqual(objs[i]);\n      }\n    });\n  });\n});'

blocks = {}
debug_info = ''