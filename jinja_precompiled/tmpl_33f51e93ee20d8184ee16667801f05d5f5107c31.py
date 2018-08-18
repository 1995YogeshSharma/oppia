from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationRightsServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the exploration rights service\n * of the exploration editor page.\n */\n\ndescribe(\'Exploration rights service\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'exploration rights service\', function() {\n    var ers = null;\n\n    beforeEach(inject(function($injector) {\n      ers = $injector.get(\'ExplorationRightsService\');\n    }));\n\n    it(\'correctly initializes the service\', function() {\n      expect(ers.ownerNames).toBeUndefined();\n      expect(ers.editorNames).toBeUndefined();\n      expect(ers.translatorNames).toBeUndefined();\n      expect(ers.viewerNames).toBeUndefined();\n      expect(ers._status).toBeUndefined();\n      expect(ers._clonedFrom).toBeUndefined();\n      expect(ers._isCommunityOwned).toBeUndefined();\n      expect(ers._viewableIfPrivate).toBeUndefined();\n\n      ers.init([\'abc\'], [], [], [], \'private\', \'e1234\', true, true);\n\n      expect(ers.ownerNames).toEqual([\'abc\']);\n      expect(ers.editorNames).toEqual([]);\n      expect(ers.translatorNames).toEqual([]);\n      expect(ers.viewerNames).toEqual([]);\n      expect(ers._status).toEqual(\'private\');\n      expect(ers._clonedFrom).toEqual(\'e1234\');\n      expect(ers._isCommunityOwned).toBe(true);\n      expect(ers._viewableIfPrivate).toBe(true);\n    });\n\n    it(\'reports the correct cloning status\', function() {\n      ers.init([\'abc\'], [], [], [], \'public\', \'1234\', true);\n      expect(ers.isCloned()).toBe(true);\n      expect(ers.clonedFrom()).toEqual(\'1234\');\n\n      ers.init([\'abc\'], [], [], [], \'public\', null, true);\n      expect(ers.isCloned()).toBe(false);\n      expect(ers.clonedFrom()).toBeNull();\n    });\n\n    it(\'reports the correct community-owned status\', function() {\n      ers.init([\'abc\'], [], [], [], \'public\', \'1234\', false);\n      expect(ers.isCommunityOwned()).toBe(false);\n\n      ers.init([\'abc\'], [], [], [], \'public\', \'1234\', true);\n      expect(ers.isCommunityOwned()).toBe(true);\n    });\n\n    it(\'reports the correct derived statuses\', function() {\n      ers.init([\'abc\'], [], [], [], \'private\', \'e1234\', true);\n      expect(ers.isPrivate()).toBe(true);\n      expect(ers.isPublic()).toBe(false);\n\n      ers.init([\'abc\'], [], [], [], \'public\', \'e1234\', true);\n      expect(ers.isPrivate()).toBe(false);\n      expect(ers.isPublic()).toBe(true);\n    });\n  });\n});'

blocks = {}
debug_info = ''