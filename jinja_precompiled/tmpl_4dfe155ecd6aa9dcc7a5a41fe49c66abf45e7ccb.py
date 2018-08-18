from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/state_editor/StateEditorServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit test for the Editor state service.\n */\n\ndescribe(\'Editor state service\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'editor state service\', function() {\n    var ecs = null;\n\n    beforeEach(inject(function($injector) {\n      ecs = $injector.get(\'StateEditorService\');\n    }));\n\n    it(\'should correctly set and get state names\', function() {\n      ecs.setActiveStateName(\'A State\');\n      expect(ecs.getActiveStateName()).toBe(\'A State\');\n    });\n\n    it(\'should not allow invalid state names to be set\', function() {\n      ecs.setActiveStateName(\'\');\n      expect(ecs.getActiveStateName()).toBeNull();\n\n      ecs.setActiveStateName(null);\n      expect(ecs.getActiveStateName()).toBeNull();\n    });\n  });\n});'

blocks = {}
debug_info = ''