from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/ExplorationDraftObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview unit tests for the local save services.\n */\n\ndescribe(\'ExplorationDraftObjectFactory\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'exploration draft object factory\', function() {\n    var ExplorationDraftObjectFactory = null;\n    var explorationId = \'100\';\n    var draftChangeListId = 2;\n    var changeList = [];\n    var draftDict = {\n      draftChanges: changeList,\n      draftChangeListId: draftChangeListId\n    };\n    var draft = null;\n\n    beforeEach(inject(function($injector) {\n      ExplorationDraftObjectFactory = $injector.get(\n        \'ExplorationDraftObjectFactory\');\n      draft = (\n        ExplorationDraftObjectFactory.createFromLocalStorageDict(\n          draftDict));\n    }));\n\n    it(\'should determine if the draft is valid\', function() {\n      expect(draft.isValid(\n        draftChangeListId)).toBeTruthy();\n      expect(draft.isValid(\n        draftChangeListId + 1)).toBeFalsy();\n    });\n\n    it(\'should return the correct changeList\', function() {\n      expect(draft.getChanges()).toEqual(changeList);\n    });\n\n    it(\'should create a valid local storage dict\', function() {\n      expect(ExplorationDraftObjectFactory.toLocalStorageDict(\n        changeList, draftChangeListId)).toEqual(draftDict);\n    });\n  });\n});'

blocks = {}
debug_info = ''