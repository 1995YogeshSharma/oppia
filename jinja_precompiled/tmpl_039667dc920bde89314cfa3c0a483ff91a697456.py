from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/UtilsServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Tests that the utility functions are working as expected.\n */\n\ndescribe(\'Utils Service\', function() {\n  var UtilsService;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(inject(function($injector) {\n    UtilsService = $injector.get(\'UtilsService\');\n  }));\n\n  it(\'should check if an object is empty\', function() {\n    expect(UtilsService.isEmpty({\n      a: \'b\'\n    })).toEqual(false);\n\n    expect(UtilsService.isEmpty({})).toEqual(true);\n\n    // Test against invalid inputs.\n    expect(UtilsService.isEmpty(NaN)).toEqual(true);\n    expect(UtilsService.isEmpty(undefined)).toEqual(true);\n    expect(UtilsService.isEmpty(null)).toEqual(true);\n  });\n\n  it(\'should check if the input is a string\', function() {\n    expect(UtilsService.isString(12)).toEqual(false);\n\n    expect(UtilsService.isString(\'\')).toEqual(true);\n    expect(UtilsService.isString(\'xyz\')).toEqual(true);\n    expect(UtilsService.isString(new String())).toEqual(true);\n\n    // Test against invalid inputs\n    expect(UtilsService.isString(NaN)).toEqual(false);\n    expect(UtilsService.isString(undefined)).toEqual(false);\n    expect(UtilsService.isString(null)).toEqual(false);\n    expect(UtilsService.isString({})).toEqual(false);\n  });\n});'

blocks = {}
debug_info = ''