from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/SkillCreationService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Functionality for creating a new skill.\n */\n\noppia.factory(\'SkillCreationService\', [\n  \'$http\', \'$window\', \'$rootScope\', \'$timeout\', \'AlertsService\',\n  \'UrlInterpolationService\',\n  function(\n      $http, $window, $rootScope, $timeout, AlertsService,\n      UrlInterpolationService) {\n    var CREATE_NEW_SKILL_URL_TEMPLATE = (\n      \'/skill_editor/<skill_id>\');\n    var skillCreationInProgress = false;\n\n    return {\n      createNewSkill: function(description) {\n        if (skillCreationInProgress) {\n          return;\n        }\n        skillCreationInProgress = true;\n        AlertsService.clearWarnings();\n        $rootScope.loadingMessage = \'Creating skill\';\n        $http.post(\'/skill_editor_handler/create_new\', {\n          description: description\n        }).then(function(response) {\n          $timeout(function() {\n            $window.location = UrlInterpolationService.interpolateUrl(\n              CREATE_NEW_SKILL_URL_TEMPLATE, {\n                skill_id: response.data.skillId\n              });\n          }, 150);\n        }, function() {\n          $rootScope.loadingMessage = \'\';\n        });\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''