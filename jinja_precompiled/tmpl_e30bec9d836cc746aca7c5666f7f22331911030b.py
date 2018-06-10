from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/notifications_dashboard/NotificationsDashboard.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Data and controllers for the user\'s notifications dashboard.\n */\n\noppia.controller(\'DashboardNotifications\', [\n  \'$scope\', \'$http\', \'$rootScope\', \'DateTimeFormatService\',\n  function($scope, $http, $rootScope, DateTimeFormatService) {\n    $scope.getItemUrl = function(activityId, notificationType) {\n      return (\n        \'/create/\' + activityId + (\n          notificationType === \'feedback_thread\' ? \'#/feedback\' : \'\'));\n    };\n\n    $scope.navigateToProfile = function($event, username) {\n      $event.stopPropagation();\n      window.location.href = \'/profile/\' + username;\n    };\n\n    $scope.getLocaleAbbreviatedDatetimeString = function(millisSinceEpoch) {\n      return DateTimeFormatService.getLocaleAbbreviatedDatetimeString(\n        millisSinceEpoch);\n    };\n\n    $rootScope.loadingMessage = \'Loading\';\n    $http.get(\'/notificationsdashboardhandler/data\').then(function(response) {\n      var data = response.data;\n      $scope.recentNotifications = data.recent_notifications;\n      $scope.jobQueuedMsec = data.job_queued_msec;\n      $scope.lastSeenMsec = data.last_seen_msec || 0.0;\n      $scope.currentUsername = data.username;\n      $rootScope.loadingMessage = \'\';\n    });\n  }\n]);'

blocks = {}
debug_info = ''