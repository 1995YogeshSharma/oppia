from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/SolutionValidityServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for Solution Validity Service.\n */\n\ndescribe(\'Solution Validity Service\', function() {\n  describe(\'SolutionValidityService\', function() {\n    beforeEach(function() {\n      module(\'oppia\');\n    });\n\n    var scope, svs;\n\n    beforeEach(inject(function($injector, $rootScope) {\n      scope = $rootScope.$new();\n      svs = $injector.get(\'SolutionValidityService\');\n\n      it(\'should store validity of the solution correctly\',\n        function() {\n          // Initialize SolutionValidityService.\n          svs.init();\n\n          svs.updateValidity(\'State 1\', true);\n          expect(svs.isSolutionValid(\'State 1\')).toBe(true);\n\n          svs.deleteSolutionValidity(\'State 1\');\n          expect(Object.keys(svs.getAllValidities())).toEqual([]);\n\n          svs.updateValidity(\'State 1\', false);\n          expect(svs.isSolutionValid(\'State 1\')).toBe(false);\n        });\n    }));\n  });\n});'

blocks = {}
debug_info = ''