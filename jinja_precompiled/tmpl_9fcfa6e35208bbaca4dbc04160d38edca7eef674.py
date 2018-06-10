from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/signup/SignupSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the editor prerequisites page.\n */\n\ndescribe(\'Signup controller\', function() {\n  describe(\'SignupCtrl\', function() {\n    var scope, ctrl, $httpBackend, rootScope, mockAlertsService, urlParams;\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n    beforeEach(inject(function($controller, $http, _$httpBackend_, $rootScope) {\n      $httpBackend = _$httpBackend_;\n      $httpBackend.expectGET(\'/signuphandler/data\').respond({\n        username: \'myUsername\',\n        has_agreed_to_latest_terms: false\n      });\n      rootScope = $rootScope;\n\n      mockAlertsService = {\n        addWarning: function() {}\n      };\n      spyOn(mockAlertsService, \'addWarning\');\n\n      scope = {\n        getUrlParams: function() {\n          return {\n            return_url: \'return_url\'\n          };\n        }\n      };\n\n      ctrl = $controller(\'Signup\', {\n        $scope: scope,\n        $http: $http,\n        $rootScope: rootScope,\n        AlertsService: mockAlertsService\n      });\n    }));\n\n    it(\'should show warning if user has not agreed to terms\', function() {\n      scope.submitPrerequisitesForm(false, null);\n      expect(mockAlertsService.addWarning).toHaveBeenCalledWith(\n        \'I18N_SIGNUP_ERROR_MUST_AGREE_TO_TERMS\');\n    });\n\n    it(\'should get data correctly from the server\', function() {\n      $httpBackend.flush();\n      expect(scope.username).toBe(\'myUsername\');\n      expect(scope.hasAgreedToLatestTerms).toBe(false);\n    });\n\n    it(\'should show a loading message until the data is retrieved\', function() {\n      expect(rootScope.loadingMessage).toBe(\'I18N_SIGNUP_LOADING\');\n      $httpBackend.flush();\n      expect(rootScope.loadingMessage).toBeFalsy();\n    });\n\n    it(\'should show warning if terms are not agreed to\', function() {\n      scope.submitPrerequisitesForm(false, \'\');\n      expect(mockAlertsService.addWarning).toHaveBeenCalledWith(\n        \'I18N_SIGNUP_ERROR_MUST_AGREE_TO_TERMS\');\n    });\n\n    it(\'should show warning if no username provided\', function() {\n      scope.updateWarningText(\'\');\n      expect(scope.warningI18nCode).toEqual(\'I18N_SIGNUP_ERROR_NO_USERNAME\');\n\n      scope.submitPrerequisitesForm(false);\n      expect(scope.warningI18nCode).toEqual(\'I18N_SIGNUP_ERROR_NO_USERNAME\');\n    });\n\n    it(\'should show warning if username is too long\', function() {\n      scope.updateWarningText(\n        \'abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba\');\n      expect(scope.warningI18nCode).toEqual(\n        \'I18N_SIGNUP_ERROR_USERNAME_MORE_50_CHARS\');\n    });\n\n    it(\'should show warning if username has non-alphanumeric characters\',\n      function() {\n        scope.updateWarningText(\'a-a\');\n        expect(scope.warningI18nCode).toEqual(\n          \'I18N_SIGNUP_ERROR_USERNAME_ONLY_ALPHANUM\');\n      }\n    );\n\n    it(\'should show warning if username has \\\'admin\\\' in it\', function() {\n      scope.updateWarningText(\'administrator\');\n      expect(scope.warningI18nCode).toEqual(\n        \'I18N_SIGNUP_ERROR_USERNAME_WITH_ADMIN\');\n    });\n  });\n});'

blocks = {}
debug_info = ''