from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/preferences/PreferencesSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\ndescribe(\'Preferences Controller\', function() {\n  describe(\'PreferencesCtrl\', function() {\n    var scope, ctrl, $httpBackend, mockAlertsService;\n\n    beforeEach(function() {\n      module(\'oppia\');\n    });\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n    beforeEach(inject(function($controller, $http, _$httpBackend_, $rootScope) {\n      $httpBackend = _$httpBackend_;\n      $httpBackend.expectGET(\'/preferenceshandler/data\').respond({\n        can_receive_email_updates: false,\n        can_receive_editor_role_email: true,\n        can_receive_feedback_message_email: true\n      });\n\n      mockAlertsService = {};\n\n      scope = $rootScope.$new();\n\n      ctrl = $controller(\'Preferences\', {\n        $scope: scope,\n        $http: $http,\n        $rootScope: $rootScope,\n        AlertsService: mockAlertsService\n      });\n    }));\n\n    it(\'should show that editor role notifications checkbox is true by default\',\n      function() {\n        $httpBackend.flush();\n        expect(scope.canReceiveEditorRoleEmail).toBe(true);\n      });\n\n    it(\'should show that feedback message notifications checkbox is true\' +\n      \'by default\',\n    function() {\n      $httpBackend.flush();\n      expect(scope.canReceiveFeedbackMessageEmail).toBe(true);\n    });\n  });\n});'

blocks = {}
debug_info = ''