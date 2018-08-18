from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/skill/MisconceptionObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n* @fileoverview Unit tests for MisconceptionObjectFacfory.\n*/\n\ndescribe(\'Misconception object factory\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'MisconceptionObjectFacfory\', function() {\n    var MisconceptionObjectFactory;\n    var misconceptionDict;\n\n    beforeEach(inject(function($injector) {\n      MisconceptionObjectFactory = $injector.get(\'MisconceptionObjectFactory\');\n      misconceptionDict = {\n        id: \'1\',\n        name: \'test name\',\n        notes: \'test notes\',\n        feedback: \'test feedback\'\n      };\n    }));\n\n    it(\'should create a new misconception\', function() {\n      var misconception =\n        MisconceptionObjectFactory.createFromBackendDict(misconceptionDict);\n      expect(misconception.getId()).toEqual(\'1\');\n      expect(misconception.getName()).toEqual(\'test name\');\n      expect(misconception.getNotes()).toEqual(\'test notes\');\n      expect(misconception.getFeedback()).toEqual(\'test feedback\');\n    });\n\n    it(\'should convert to a backend dictionary\', function() {\n      var misconception =\n        MisconceptionObjectFactory.createFromBackendDict(misconceptionDict);\n      expect(misconception.toBackendDict()).toEqual(misconceptionDict);\n    });\n  });\n});'

blocks = {}
debug_info = ''