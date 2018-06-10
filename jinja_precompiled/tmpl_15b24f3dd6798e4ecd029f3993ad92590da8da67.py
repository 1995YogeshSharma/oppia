from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/NumberAttemptsServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the number attempts service.\n */\n\ndescribe(\'Number attempts service\', function() {\n  beforeEach(module(\'oppia\'));\n\n  var NumberAttemptsService = null;\n  beforeEach(inject(function($injector) {\n    NumberAttemptsService = $injector.get(\'NumberAttemptsService\');\n  }));\n\n  it(\'should increment number of attempts correctly\', function() {\n    NumberAttemptsService.reset();\n    expect(NumberAttemptsService.getNumberAttempts()).toEqual(0);\n    NumberAttemptsService.submitAttempt();\n    expect(NumberAttemptsService.getNumberAttempts()).toEqual(1);\n  });\n\n  it(\'should properly reset the number of attempts to zero\', function() {\n    NumberAttemptsService.submitAttempt();\n    NumberAttemptsService.reset();\n    expect(NumberAttemptsService.getNumberAttempts()).toEqual(0);\n  });\n});'

blocks = {}
debug_info = ''