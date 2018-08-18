from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/moderator/Moderator.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n* @fileoverview Data and controllers for the Oppia moderator page.\n*/\n\noppia.controller(\'Moderator\', [\n  \'$scope\', \'$http\', \'$rootScope\', \'DateTimeFormatService\', \'AlertsService\',\n  function($scope, $http, $rootScope, DateTimeFormatService, AlertsService) {\n    $rootScope.loadingMessage = \'Loading\';\n    $scope.getDatetimeAsString = function(millisSinceEpoch) {\n      return DateTimeFormatService.getLocaleAbbreviatedDatetimeString(\n        millisSinceEpoch);\n    };\n\n    $scope.getExplorationCreateUrl = function(explorationId) {\n      return \'/create/\' + explorationId;\n    };\n\n    $scope.getActivityCreateUrl = function(reference) {\n      return (\n        (reference.type === \'exploration\' ? \'/create\' : \'/create_collection\') +\n        \'/\' + reference.id);\n    };\n\n    $scope.allCommits = [];\n    $scope.allFeedbackMessages = [];\n    // Map of exploration ids to objects containing a single key: title.\n    $scope.explorationData = {};\n\n    $scope.displayedFeaturedActivityReferences = [];\n    $scope.lastSavedFeaturedActivityReferences = [];\n    $scope.FEATURED_ACTIVITY_REFERENCES_SCHEMA = {\n      type: \'list\',\n      items: {\n        type: \'dict\',\n        properties: [{\n          name: \'type\',\n          schema: {\n            type: \'unicode\',\n            choices: [\'exploration\', \'collection\']\n          }\n        }, {\n          name: \'id\',\n          schema: {\n            type: \'unicode\'\n          }\n        }]\n      }\n    };\n\n    var RECENT_COMMITS_URL = (\n      \'/recentcommitshandler/recent_commits\' +\n      \'?query_type=all_non_private_commits\');\n    // TODO(sll): Update this to also support collections.\n    $http.get(RECENT_COMMITS_URL).then(function(response) {\n      // Update the explorationData object with information about newly-\n      // discovered explorations.\n      var data = response.data;\n      var explorationIdsToExplorationData = data.exp_ids_to_exp_data;\n      for (var expId in explorationIdsToExplorationData) {\n        if (!$scope.explorationData.hasOwnProperty(expId)) {\n          $scope.explorationData[expId] = (\n            explorationIdsToExplorationData[expId]);\n        }\n      }\n      $scope.allCommits = data.results;\n      $rootScope.loadingMessage = \'\';\n    });\n\n    $http.get(\'/recent_feedback_messages\').then(function(response) {\n      $scope.allFeedbackMessages = response.data.results;\n    });\n\n    $http.get(\'/moderatorhandler/featured\').then(function(response) {\n      $scope.displayedFeaturedActivityReferences = (\n        response.data.featured_activity_references);\n      $scope.lastSavedFeaturedActivityReferences = angular.copy(\n        $scope.displayedFeaturedActivityReferences);\n    });\n\n    $scope.isSaveFeaturedActivitiesButtonDisabled = function() {\n      return angular.equals(\n        $scope.displayedFeaturedActivityReferences,\n        $scope.lastSavedFeaturedActivityReferences);\n    };\n\n    $scope.saveFeaturedActivityReferences = function() {\n      AlertsService.clearWarnings();\n\n      var activityReferencesToSave = angular.copy(\n        $scope.displayedFeaturedActivityReferences);\n      $http.post(\'/moderatorhandler/featured\', {\n        featured_activity_reference_dicts: activityReferencesToSave\n      }).then(function() {\n        $scope.lastSavedFeaturedActivityReferences = activityReferencesToSave;\n        AlertsService.addSuccessMessage(\'Featured activities saved.\');\n      });\n    };\n  }\n]);'

blocks = {}
debug_info = ''