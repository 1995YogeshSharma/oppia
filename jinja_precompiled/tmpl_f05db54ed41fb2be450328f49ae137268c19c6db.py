from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/collection/ReadOnlyCollectionBackendApiServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for ReadOnlyCollectionBackendApiService.\n */\n\ndescribe(\'Read only collection backend API service\', function() {\n  var ReadOnlyCollectionBackendApiService = null;\n  var sampleDataResults = null;\n  var $rootScope = null;\n  var $scope = null;\n  var $httpBackend = null;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n  beforeEach(inject(function($injector) {\n    ReadOnlyCollectionBackendApiService = $injector.get(\n      \'ReadOnlyCollectionBackendApiService\');\n    $rootScope = $injector.get(\'$rootScope\');\n    $scope = $rootScope.$new();\n    $httpBackend = $injector.get(\'$httpBackend\');\n\n    // Sample collection object returnable from the backend\n    sampleDataResults = {\n      collection: {\n        id: \'0\',\n        title: \'Collection Under Test\',\n        category: \'Test\',\n        objective: \'To pass\',\n        schema_version: \'1\',\n        nodes: [{\n          exploration_id: \'0\'\n        }],\n        next_exploration_ids: [],\n        completed_exploration_ids: []\n      }\n    };\n  }));\n\n  afterEach(function() {\n    $httpBackend.verifyNoOutstandingExpectation();\n    $httpBackend.verifyNoOutstandingRequest();\n  });\n\n  it(\'should successfully fetch an existing collection from the backend\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      $httpBackend.expect(\'GET\', \'/collection_handler/data/0\').respond(\n        sampleDataResults);\n      ReadOnlyCollectionBackendApiService.fetchCollection(\'0\').then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n      expect(failHandler).not.toHaveBeenCalled();\n    }\n  );\n\n  it(\'should load a cached collection after fetching it from the backend\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      // Loading a collection the first time should fetch it from the backend.\n      $httpBackend.expect(\'GET\', \'/collection_handler/data/0\').respond(\n        sampleDataResults);\n      ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n      expect(failHandler).not.toHaveBeenCalled();\n\n      // Loading a collection the second time should not fetch it.\n      ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n        successHandler, failHandler);\n\n      expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n      expect(failHandler).not.toHaveBeenCalled();\n    }\n  );\n\n  it(\'should use the rejection handler if the backend request failed\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      // Loading a collection the first time should fetch it from the backend.\n      $httpBackend.expect(\'GET\', \'/collection_handler/data/0\').respond(\n        500, \'Error loading collection 0.\');\n      ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).not.toHaveBeenCalled();\n      expect(failHandler).toHaveBeenCalledWith(\'Error loading collection 0.\');\n    }\n  );\n\n  it(\'should report caching and support clearing the cache\', function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    // The collection should not currently be cached.\n    expect(ReadOnlyCollectionBackendApiService.isCached(\'0\')).toBeFalsy();\n\n    // Loading a collection the first time should fetch it from the backend.\n    $httpBackend.expect(\'GET\', \'/collection_handler/data/0\').respond(\n      sampleDataResults);\n    ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n      successHandler, failHandler);\n    $httpBackend.flush();\n\n    expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n    expect(failHandler).not.toHaveBeenCalled();\n\n    // The collection should now be cached.\n    expect(ReadOnlyCollectionBackendApiService.isCached(\'0\')).toBeTruthy();\n\n    // The collection should be loadable from the cache.\n    ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n      successHandler, failHandler);\n    expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n    expect(failHandler).not.toHaveBeenCalled();\n\n    // Resetting the cache will cause another fetch from the backend.\n    ReadOnlyCollectionBackendApiService.clearCollectionCache();\n    expect(ReadOnlyCollectionBackendApiService.isCached(\'0\')).toBeFalsy();\n\n    $httpBackend.expect(\'GET\', \'/collection_handler/data/0\').respond(\n      sampleDataResults);\n    ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n      successHandler, failHandler);\n    $httpBackend.flush();\n\n    expect(successHandler).toHaveBeenCalledWith(sampleDataResults.collection);\n    expect(failHandler).not.toHaveBeenCalled();\n  });\n\n  it(\'should report a cached collection after caching it\', function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    // The collection should not currently be cached.\n    expect(ReadOnlyCollectionBackendApiService.isCached(\'0\')).toBeFalsy();\n\n    // Cache a collection.\n    ReadOnlyCollectionBackendApiService.cacheCollection(\'0\', {\n      id: \'0\',\n      nodes: []\n    });\n\n    // It should now be cached.\n    expect(ReadOnlyCollectionBackendApiService.isCached(\'0\')).toBeTruthy();\n\n    // A new collection should not have been fetched from the backend. Also,\n    // the returned collection should match the expected collection object.\n    ReadOnlyCollectionBackendApiService.loadCollection(\'0\').then(\n      successHandler, failHandler);\n\n    // http://brianmcd.com/2014/03/27/\n    // a-tip-for-angular-unit-tests-with-promises.html\n    $rootScope.$digest();\n\n    expect(successHandler).toHaveBeenCalledWith({\n      id: \'0\',\n      nodes: []\n    });\n    expect(failHandler).not.toHaveBeenCalled();\n  });\n});'

blocks = {}
debug_info = ''