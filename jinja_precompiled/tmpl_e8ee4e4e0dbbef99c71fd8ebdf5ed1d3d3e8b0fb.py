from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/collection/CollectionRightsBackendApiServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for CollectionRightsBackendApiService.\n */\n\ndescribe(\'Collection rights backend API service\', function() {\n  var CollectionRightsBackendApiService = null;\n  var sampleDataResults = null;\n  var $rootScope = null;\n  var $scope = null;\n  var $httpBackend = null;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n  beforeEach(inject(function($injector) {\n    CollectionRightsBackendApiService = $injector.get(\n      \'CollectionRightsBackendApiService\');\n    $rootScope = $injector.get(\'$rootScope\');\n    $scope = $rootScope.$new();\n    $httpBackend = $injector.get(\'$httpBackend\');\n  }));\n\n  afterEach(function() {\n    $httpBackend.verifyNoOutstandingExpectation();\n    $httpBackend.verifyNoOutstandingRequest();\n  });\n\n  it(\'should successfully set a collection to be public\', function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    // TODO(bhenning): Figure out how to test the actual payload sent with the\n    // PUT request. The typical expect() syntax with a passed-in object payload\n    // does not seem to be working correctly.\n    $httpBackend.expect(\n      \'PUT\', \'/collection_editor_handler/publish/0\').respond(200);\n    CollectionRightsBackendApiService.setCollectionPublic(\'0\', 1).then(\n      successHandler, failHandler);\n    $httpBackend.flush();\n    $rootScope.$digest();\n\n    expect(successHandler).toHaveBeenCalled();\n    expect(failHandler).not.toHaveBeenCalled();\n  });\n\n  it(\'should call the provided fail handler on HTTP failure\', function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    $httpBackend.expect(\n      \'PUT\', \'/collection_editor_handler/publish/0\').respond(\n      500, \'Error loading collection 0.\');\n    CollectionRightsBackendApiService.setCollectionPublic(\'0\', 1).then(\n      successHandler, failHandler);\n    $httpBackend.flush();\n    $rootScope.$digest();\n\n    expect(successHandler).not.toHaveBeenCalled();\n    expect(failHandler).toHaveBeenCalled();\n  });\n\n  it(\'should report a cached collection rights after caching it\', function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    // The collection should not currently be cached.\n    expect(CollectionRightsBackendApiService.isCached(\'0\')).toBe(false);\n\n    // Cache a collection.\n    CollectionRightsBackendApiService.cacheCollectionRights(\'0\', {\n      collection_id: 0,\n      can_edit: true,\n      can_unpublish: false,\n      is_private: true,\n      owner_names: [\'A\']\n    });\n\n    // It should now be cached.\n    expect(CollectionRightsBackendApiService.isCached(\'0\')).toBe(true);\n\n    // A new collection should not have been fetched from the backend. Also,\n    // the returned collection should match the expected collection object.\n    CollectionRightsBackendApiService.loadCollectionRights(\'0\').then(\n      successHandler, failHandler);\n\n    // http://brianmcd.com/2014/03/27/\n    // a-tip-for-angular-unit-tests-with-promises.html\n    $rootScope.$digest();\n\n    expect(successHandler).toHaveBeenCalledWith({\n      collection_id: 0,\n      can_edit: true,\n      can_unpublish: false,\n      is_private: true,\n      owner_names: [\'A\']\n    });\n    expect(failHandler).not.toHaveBeenCalled();\n  });\n});'

blocks = {}
debug_info = ''