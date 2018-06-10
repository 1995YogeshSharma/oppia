from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/EditableExplorationBackendApiServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for EditableExplorationBackendApiService.\n */\n\ndescribe(\'Editable exploration backend API service\', function() {\n  var EditableExplorationBackendApiService = null;\n  var ReadOnlyExplorationBackendApiService = null;\n  var sampleDataResults = null;\n  var $rootScope = null;\n  var $scope = null;\n  var $httpBackend = null;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n  beforeEach(inject(function($injector) {\n    EditableExplorationBackendApiService = $injector.get(\n      \'EditableExplorationBackendApiService\');\n    ReadOnlyExplorationBackendApiService = $injector.get(\n      \'ReadOnlyExplorationBackendApiService\');\n    $rootScope = $injector.get(\'$rootScope\');\n    $scope = $rootScope.$new();\n    $httpBackend = $injector.get(\'$httpBackend\');\n\n    // Sample exploration object returnable from the backend\n    sampleDataResults = {\n      exploration_id: \'0\',\n      init_state_name: \'Introduction\',\n      language_code: \'en\',\n      states: {\n        Introduction: {\n          param_changes: [],\n          content: {\n            html: \'\',\n            audio_translations: {}\n          },\n          unresolved_answers: {},\n          interaction: {\n            customization_args: {},\n            answer_groups: [],\n            default_outcome: {\n              param_changes: [],\n              dest: \'Introduction\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              }\n            },\n            confirmed_unclassified_answers: [],\n            id: null\n          }\n        }\n      },\n      username: \'test\',\n      user_email: \'test@example.com\',\n      version: 1\n    };\n  }));\n\n  afterEach(function() {\n    $httpBackend.verifyNoOutstandingExpectation();\n    $httpBackend.verifyNoOutstandingRequest();\n  });\n\n  it(\'should successfully fetch an existing exploration from the backend\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      $httpBackend.expect(\'GET\', \'/createhandler/data/0\').respond(\n        sampleDataResults);\n      EditableExplorationBackendApiService.fetchExploration(\'0\').then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(sampleDataResults);\n      expect(failHandler).not.toHaveBeenCalled();\n    }\n  );\n\n  it(\'should fetch and apply the draft of an exploration\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      // Loading a exploration the first time should fetch it from the backend.\n      $httpBackend.expect(\n        \'GET\', \'/createhandler/data/0?apply_draft=true\').respond(\n        sampleDataResults);\n\n      EditableExplorationBackendApiService.fetchApplyDraftExploration(\n        \'0\').then(successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(sampleDataResults);\n      expect(failHandler).not.toHaveBeenCalled();\n    }\n  );\n\n  it(\'should use the rejection handler if the backend request failed\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      // Loading a exploration the first time should fetch it from the backend.\n      $httpBackend.expect(\'GET\', \'/createhandler/data/1\').respond(\n        500, \'Error loading exploration 1.\');\n      EditableExplorationBackendApiService.fetchExploration(\'1\').then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).not.toHaveBeenCalled();\n      expect(failHandler).toHaveBeenCalledWith(\'Error loading exploration 1.\');\n    }\n  );\n\n  it(\'should update a exploration after fetching it from the backend\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      // Loading a exploration the first time should fetch it from the backend.\n      $httpBackend.expect(\'GET\', \'/createhandler/data/0\').respond(\n        sampleDataResults);\n\n      EditableExplorationBackendApiService.fetchExploration(\'0\').then(\n        function(data) {\n          exploration = data;\n        });\n      $httpBackend.flush();\n\n      exploration.title = \'New Title\';\n      exploration.version = \'2\';\n\n      $httpBackend.expect(\'PUT\', \'/createhandler/data/0\').respond(\n        exploration);\n\n      // Send a request to update exploration\n      EditableExplorationBackendApiService.updateExploration(\n        exploration.exploration_id, exploration.version,\n        exploration.title, []\n      ).then(successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(exploration);\n      expect(failHandler).not.toHaveBeenCalled();\n    }\n  );\n\n  it(\'should not cache exploration from backend into read only service\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0\')\n        .respond(sampleDataResults);\n\n      ReadOnlyExplorationBackendApiService.loadLatestExploration(\'0\')\n        .then(function(data) {\n          exploration = data;\n        });\n      $httpBackend.flush();\n\n      expect(ReadOnlyExplorationBackendApiService.isCached(\'0\')).toBe(true);\n\n      exploration.title = \'New Title\';\n      exploration.version = \'2\';\n\n      $httpBackend.expect(\'PUT\', \'/createhandler/data/0\')\n        .respond(exploration);\n\n      // Send a request to update exploration\n      EditableExplorationBackendApiService.updateExploration(\n        exploration.exploration_id,\n        exploration.version,\n        exploration.title, []\n      ).then(successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(exploration);\n      expect(failHandler).not.toHaveBeenCalled();\n\n      expect(ReadOnlyExplorationBackendApiService.isCached(\'0\')).toBe(false);\n    }\n  );\n\n  it(\'should delete exploration from the backend\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      $httpBackend.expect(\'GET\', \'/createhandler/data/0\')\n        .respond(sampleDataResults);\n\n      EditableExplorationBackendApiService.fetchExploration(\'0\')\n        .then(function(data) {\n          exploration = data;\n        });\n      $httpBackend.flush();\n\n      exploration.title = \'New Title\';\n      exploration.version = \'2\';\n\n      $httpBackend.expect(\'PUT\', \'/createhandler/data/0\')\n        .respond(exploration);\n\n      // Send a request to update exploration\n      EditableExplorationBackendApiService.updateExploration(\n        exploration.exploration_id,\n        exploration.version,\n        \'Minor edits\', []\n      ).then(successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(exploration);\n      expect(failHandler).not.toHaveBeenCalled();\n\n      $httpBackend.expect(\'DELETE\', \'/createhandler/data/0\')\n        .respond({});\n      EditableExplorationBackendApiService\n        .deleteExploration(exploration.exploration_id)\n        .then(successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith({});\n      expect(failHandler).not.toHaveBeenCalled();\n\n      expect(ReadOnlyExplorationBackendApiService.isCached(\'0\')).toBe(false);\n    }\n  );\n});'

blocks = {}
debug_info = ''