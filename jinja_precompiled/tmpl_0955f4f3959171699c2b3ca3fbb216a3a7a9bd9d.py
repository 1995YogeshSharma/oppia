from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/ExplorationCreationService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Functionality for the create exploration button and upload\n * modal.\n */\n\noppia.factory(\'ExplorationCreationService\', [\n  \'$http\', \'$uibModal\', \'$timeout\', \'$rootScope\', \'$window\',\n  \'AlertsService\', \'siteAnalyticsService\', \'UrlInterpolationService\',\n  function(\n      $http, $uibModal, $timeout, $rootScope, $window,\n      AlertsService, siteAnalyticsService, UrlInterpolationService) {\n    var CREATE_NEW_EXPLORATION_URL_TEMPLATE = \'/create/<exploration_id>\';\n\n    var explorationCreationInProgress = false;\n\n    return {\n      createNewExploration: function() {\n        if (explorationCreationInProgress) {\n          return;\n        }\n\n        explorationCreationInProgress = true;\n        AlertsService.clearWarnings();\n        $rootScope.loadingMessage = \'Creating exploration\';\n\n        $http.post(\'/contributehandler/create_new\', {\n        }).then(function(response) {\n          siteAnalyticsService.registerCreateNewExplorationEvent(\n            response.data.explorationId);\n          $timeout(function() {\n            $window.location = UrlInterpolationService.interpolateUrl(\n              CREATE_NEW_EXPLORATION_URL_TEMPLATE, {\n                exploration_id: response.data.explorationId\n              }\n            );\n          }, 150);\n          return false;\n        }, function() {\n          $rootScope.loadingMessage = \'\';\n          explorationCreationInProgress = false;\n        });\n      },\n      showUploadExplorationModal: function() {\n        AlertsService.clearWarnings();\n\n        $uibModal.open({\n          backdrop: true,\n          templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n            \'/pages/creator_dashboard/\' +\n            \'upload_activity_modal_directive.html\'),\n          controller: [\n            \'$scope\', \'$uibModalInstance\', function($scope, $uibModalInstance) {\n              $scope.save = function() {\n                var returnObj = {};\n                var file = document.getElementById(\'newFileInput\').files[0];\n                if (!file || !file.size) {\n                  AlertsService.addWarning(\'Empty file detected.\');\n                  return;\n                }\n                returnObj.yamlFile = file;\n\n                $uibModalInstance.close(returnObj);\n              };\n\n              $scope.cancel = function() {\n                $uibModalInstance.dismiss(\'cancel\');\n                AlertsService.clearWarnings();\n              };\n            }\n          ]\n        }).result.then(function(result) {\n          var yamlFile = result.yamlFile;\n\n          $rootScope.loadingMessage = \'Creating exploration\';\n\n          var form = new FormData();\n          form.append(\'yaml_file\', yamlFile);\n          form.append(\'payload\', JSON.stringify({}));\n          form.append(\'csrf_token\', GLOBALS.csrf_token);\n\n          $.ajax({\n            contentType: false,\n            data: form,\n            dataFilter: function(data) {\n              // Remove the XSSI prefix.\n              return JSON.parse(data.substring(5));\n            },\n            dataType: \'text\',\n            processData: false,\n            type: \'POST\',\n            url: \'contributehandler/upload\'\n          }).done(function(data) {\n            $window.location = UrlInterpolationService.interpolateUrl(\n              CREATE_NEW_EXPLORATION_URL_TEMPLATE, {\n                exploration_id: data.explorationId\n              }\n            );\n          }).fail(function(data) {\n            var transformedData = data.responseText.substring(5);\n            var parsedResponse = JSON.parse(transformedData);\n            AlertsService.addWarning(\n              parsedResponse.error || \'Error communicating with server.\');\n            $rootScope.loadingMessage = \'\';\n            $scope.$apply();\n          });\n        });\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''