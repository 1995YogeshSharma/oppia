// Copyright 2016 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Directive for the jobs tab in the admin panel.
 */

oppia.directive('adminRolesTab', [
  '$http', 'UrlInterpolationService', 'ADMIN_HANDLER_URL',
  function(
      $http, UrlInterpolationService, ADMIN_HANDLER_URL) {
    return {
      restrict: 'E',
      scope: {
        setStatusMessage: '='
      },
      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(
        '/pages/admin/roles_tab/' +
        'admin_roles_tab_directive.html'),
      controller: ['$scope', function($scope) {
        $scope.graphData = function() {
          console.log('called');
          return {
            finalStateIds: ["SUPER_ADMIN"],
            initStateId: "DEFAULT",
            links: [{source: "DEFAULT", target: "BANNED_USER", ifFallback: false},
              {source: "BANNED_USER", target: "EXPLORATION_EDITOR", ifFallback: false},
              {source: "EXPLORATION_EDITOR", target: "COLLECTION_EDITOR", ifFallback: false},
              {source: "COLLECTION_EDITOR", target: "MODERATOR", ifFallback: false},
              {source: "MODERATOR", target: "ADMIN", ifFallback: false},
              {source: "ADMIN", target: "SUPER_ADMIN", ifFallback: false}
              ],
            nodes: {
              DEFAULT: "DEFAULT",
              BANNED_USER: "BANNED_USER",
              EXPLORATION_EDITOR: "EXPLORATION_EDITOR",
              COLLECTION_EDITOR: "COLLECTION_EDITOR",
              MODERATOR: "MODERATOR",
              ADMIN: "ADMIN",
              SUPER_ADMIN: "SUPER_ADMIN"
            }
          };
        }
        $scope.currentStateId = function() {
          return "default";
        }   
      }]
    };
  }
]);
