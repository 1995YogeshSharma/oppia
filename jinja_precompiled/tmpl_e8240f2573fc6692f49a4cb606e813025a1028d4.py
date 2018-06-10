from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'appSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for generic services.\n */\n\ndescribe(\'Constants Generating\', function() {\n  beforeEach(module(\'oppia\'));\n\n  var $injector = null;\n  beforeEach(inject(function(_$injector_) {\n    $injector = _$injector_.get(\'$injector\');\n  }));\n\n  it(\'should transform all key value pairs to angular constants\', function() {\n    for (var constantName in constants) {\n      expect($injector.has(constantName)).toBe(true);\n      expect($injector.get(constantName)).toBe(constants[constantName]);\n    }\n  });\n});'

blocks = {}
debug_info = ''