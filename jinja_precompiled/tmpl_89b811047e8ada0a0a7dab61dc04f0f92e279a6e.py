from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/StateClassifierMappingServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the State classifier mapping service.\n */\n\ndescribe(\'State classifier mapping service\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'Test correct retrieval of classifier details\', function() {\n    var mappingService;\n    beforeEach(inject(function($injector) {\n      mappingService = $injector.get(\'StateClassifierMappingService\');\n\n      mappingService.init({\n        stateName1: {\n          algorithm_id: \'TestClassifier\',\n          classifier_data: {},\n          data_schema_version: 1\n        }\n      });\n    }));\n\n    it(\'should return correct classifier details.\', function() {\n      var stateName = \'stateName1\';\n      var retrievedClassifier = mappingService.getClassifier(stateName);\n\n      expect(retrievedClassifier.algorithmId).toEqual(\'TestClassifier\');\n      expect(retrievedClassifier.classifierData).toEqual({});\n      expect(retrievedClassifier.dataSchemaVersion).toEqual(1);\n    });\n  });\n});'

blocks = {}
debug_info = ''