from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/misc_tab/AdminMiscTabDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for the miscellaneous tab in the admin panel.\n */\n\noppia.directive(\'adminMiscTab\', [\n  \'$http\', \'$window\', \'AdminTaskManagerService\', \'ADMIN_HANDLER_URL\',\n  \'ADMIN_TOPICS_CSV_DOWNLOAD_HANDLER_URL\', \'UrlInterpolationService\',\n  function(\n      $http, $window, AdminTaskManagerService, ADMIN_HANDLER_URL,\n      ADMIN_TOPICS_CSV_DOWNLOAD_HANDLER_URL, UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        setStatusMessage: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/admin/misc_tab/\' +\n        \'admin_misc_tab_directive.html\'),\n      controller: [\'$scope\', function($scope) {\n        var DATA_EXTRACTION_QUERY_HANDLER_URL = (\n          \'/explorationdataextractionhandler\');\n\n        $scope.clearSearchIndex = function() {\n          if (AdminTaskManagerService.isTaskRunning()) {\n            return;\n          }\n          if (!confirm(\'This action is irreversible. Are you sure?\')) {\n            return;\n          }\n\n          $scope.setStatusMessage(\'Clearing search index...\');\n\n          AdminTaskManagerService.startTask();\n          $http.post(ADMIN_HANDLER_URL, {\n            action: \'clear_search_index\'\n          }).then(function() {\n            $scope.setStatusMessage(\'Index successfully cleared.\');\n            AdminTaskManagerService.finishTask();\n          }, function(errorResponse) {\n            $scope.setStatusMessage(\n              \'Server error: \' + errorResponse.data.error);\n            AdminTaskManagerService.finishTask();\n          });\n        };\n\n        $scope.uploadTopicSimilaritiesFile = function() {\n          var file = document.getElementById(\'topicSimilaritiesFile\').files[0];\n          var reader = new FileReader();\n          reader.onload = function(e) {\n            var data = e.target.result;\n            $http.post(ADMIN_HANDLER_URL, {\n              action: \'upload_topic_similarities\',\n              data: data\n            }).then(function() {\n              $scope.setStatusMessage(\n                \'Topic similarities uploaded successfully.\');\n            }, function(errorResponse) {\n              $scope.setStatusMessage(\n                \'Server error: \' + errorResponse.data.error);\n            });\n          };\n          reader.readAsText(file);\n        };\n\n        $scope.downloadTopicSimilaritiesFile = function() {\n          $window.location.href = ADMIN_TOPICS_CSV_DOWNLOAD_HANDLER_URL;\n        };\n\n        var setDataExtractionQueryStatusMessage = function(message) {\n          $scope.showDataExtractionQueryStatus = true;\n          $scope.dataExtractionQueryStatusMessage = message;\n        };\n\n        $scope.submitQuery = function() {\n          var STATUS_PENDING = (\n            \'Data extraction query has been submitted. Please wait.\');\n          var STATUS_FINISHED = \'Loading the extracted data ...\';\n          var STATUS_FAILED = \'Error, \';\n\n          setDataExtractionQueryStatusMessage(STATUS_PENDING);\n\n          var downloadUrl = DATA_EXTRACTION_QUERY_HANDLER_URL + \'?\';\n\n          downloadUrl += \'exp_id=\' + encodeURIComponent($scope.expId);\n          downloadUrl += \'&exp_version=\' + encodeURIComponent(\n            $scope.expVersion);\n          downloadUrl += \'&state_name=\' + encodeURIComponent(\n            $scope.stateName);\n          downloadUrl += \'&num_answers=\' + encodeURIComponent(\n            $scope.numAnswers);\n\n          $window.open(downloadUrl);\n        };\n\n        $scope.resetForm = function() {\n          $scope.expId = \'\';\n          $scope.expVersion = 0;\n          $scope.stateName = \'\';\n          $scope.numAnswers = 0;\n          $scope.showDataExtractionQueryStatus = false;\n        };\n      }]\n    };\n  }\n]);'

blocks = {}
debug_info = ''