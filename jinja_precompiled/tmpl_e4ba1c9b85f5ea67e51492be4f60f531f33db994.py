from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/EditabilityServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for EditabilityService.\n */\n\ndescribe(\'EditabilityService\', function() {\n  var EditabilityService = null;\n\n  beforeEach(module(\'oppia\'));\n\n  beforeEach(inject(function($injector) {\n    EditabilityService = $injector.get(\'EditabilityService\');\n  }));\n\n  it(\'should allow to edit an exploration after the tutorial ends\', function() {\n    EditabilityService.onEndTutorial();\n    EditabilityService.markEditable();\n    expect(EditabilityService.isEditable()).toBe(true);\n  });\n\n  it(\'should allow to edit an exploration outside the tutorial mode\',\n    function() {\n      EditabilityService.markEditable();\n      expect(EditabilityService.isEditableOutsideTutorialMode()).toBe(true);\n    });\n\n  it(\'should not allow to edit an exploration during tutorial mode\',\n    function() {\n      EditabilityService.onStartTutorial();\n      expect(EditabilityService.isEditable()).toBe(false);\n    });\n\n  it(\'should not allow to edit an uneditable exploration\', function() {\n    EditabilityService.markNotEditable();\n    expect(EditabilityService.isEditable()).toBe(false);\n  });\n});'

blocks = {}
debug_info = ''