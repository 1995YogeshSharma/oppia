from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/topics_and_skills_dashboard/TopicsAndSkillsDashboardBackendApiServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for CreatorDashboardBackendApiService.\n */\n\ndescribe(\'Topics and Skills Dashboard backend API service\', function() {\n  var TopicsAndSkillsDashboardBackendApiService = null;\n  var $httpBackend = null;\n  var SAMPLE_TOPIC_ID = \'hyuy4GUlvTqJ\';\n\n  var sampleDataResults = {\n    topic_summary_dicts: [{\n      id: SAMPLE_TOPIC_ID,\n      name: \'Sample Name\',\n      language_code: \'en\',\n      version: 1,\n      canonical_story_count: 3,\n      additional_story_count: 0,\n      uncategorized_skill_count: 3,\n      subtopic_count: 3,\n      topic_model_created_on: 1466178691847.67,\n      topic_model_last_updated: 1466178759209.839\n    }],\n    skill_summary_dicts: []\n  };\n\n  var TOPICS_AND_SKILLS_DASHBOARD_DATA_URL =\n    \'/topics_and_skills_dashboard/data\';\n  var ERROR_STATUS_CODE = 500;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n  beforeEach(inject(function($injector) {\n    TopicsAndSkillsDashboardBackendApiService = $injector.get(\n      \'TopicsAndSkillsDashboardBackendApiService\');\n    UrlInterpolationService = $injector.get(\'UrlInterpolationService\');\n    $httpBackend = $injector.get(\'$httpBackend\');\n  }));\n\n  afterEach(function() {\n    $httpBackend.verifyNoOutstandingExpectation();\n    $httpBackend.verifyNoOutstandingRequest();\n  });\n\n  it(\'should successfully fetch topics and skills dashboard data from the \' +\n      \'backend\',\n  function() {\n    var successHandler = jasmine.createSpy(\'success\');\n    var failHandler = jasmine.createSpy(\'fail\');\n\n    $httpBackend.expect(\'GET\', TOPICS_AND_SKILLS_DASHBOARD_DATA_URL).respond(\n      sampleDataResults);\n    TopicsAndSkillsDashboardBackendApiService.fetchDashboardData().then(\n      successHandler, failHandler);\n    $httpBackend.flush();\n\n    expect(successHandler).toHaveBeenCalled();\n    expect(failHandler).not.toHaveBeenCalled();\n  });\n\n  it(\'should use rejection handler if dashboard data backend request failed\',\n    function() {\n      var successHandler = jasmine.createSpy(\'success\');\n      var failHandler = jasmine.createSpy(\'fail\');\n\n      $httpBackend.expect(\'GET\', TOPICS_AND_SKILLS_DASHBOARD_DATA_URL).respond(\n        ERROR_STATUS_CODE, \'Error loading dashboard data.\');\n      TopicsAndSkillsDashboardBackendApiService.fetchDashboardData().then(\n        successHandler, failHandler);\n      $httpBackend.flush();\n\n      expect(successHandler).not.toHaveBeenCalled();\n      expect(failHandler).toHaveBeenCalled();\n    }\n  );\n});'

blocks = {}
debug_info = ''