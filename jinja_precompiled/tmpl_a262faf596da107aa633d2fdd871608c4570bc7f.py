from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/StateNameEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for the state name editor section of the state\n * editor.\n */\noppia.directive(\'stateNameEditor\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      link: function(scope, element) {\n        // This allows the scope to be retrievable during Karma unit testing.\n        // See http://stackoverflow.com/a/29833832 for more details.\n        element[0].getControllerScope = function() {\n          return scope;\n        };\n      },\n      scope: {},\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/exploration_editor/editor_tab/\' +\n        \'state_name_editor_directive.html\'),\n      controller: [\n        \'$scope\', \'$filter\', \'$rootScope\', \'EditabilityService\',\n        \'StateEditorService\', \'FocusManagerService\', \'ExplorationStatesService\',\n        \'RouterService\',\n        function(\n            $scope, $filter, $rootScope, EditabilityService,\n            StateEditorService, FocusManagerService, ExplorationStatesService,\n            RouterService) {\n          $scope.EditabilityService = EditabilityService;\n          var _stateNameMemento = null;\n          $scope.stateNameEditorIsShown = false;\n          $scope.$on(\'stateEditorInitialized\', function() {\n            $scope.initStateNameEditor();\n          });\n\n          $scope.initStateNameEditor = function() {\n            _stateNameMemento = null;\n            $scope.stateNameEditorIsShown = false;\n            $scope.stateName = StateEditorService.getActiveStateName();\n          };\n\n          $scope.openStateNameEditor = function() {\n            $scope.stateNameEditorIsShown = true;\n            $scope.tmpStateName = $scope.stateName;\n            _stateNameMemento = $scope.stateName;\n            FocusManagerService.setFocus(\'stateNameEditorOpened\');\n          };\n\n          $scope.saveStateName = function(newStateName) {\n            var normalizedNewName =\n              $scope._getNormalizedStateName(newStateName);\n            if (!_isNewStateNameValid(normalizedNewName)) {\n              return false;\n            }\n\n            if (_stateNameMemento === normalizedNewName) {\n              $scope.stateNameEditorIsShown = false;\n              return false;\n            } else {\n              ExplorationStatesService.renameState(\n                StateEditorService.getActiveStateName(), normalizedNewName);\n              $scope.stateNameEditorIsShown = false;\n              // Save the contents of other open fields.\n              $rootScope.$broadcast(\'externalSave\');\n              $scope.initStateNameEditor();\n              return true;\n            }\n          };\n\n          $scope.$on(\'externalSave\', function() {\n            if ($scope.stateNameEditorIsShown) {\n              $scope.saveStateName($scope.tmpStateName);\n            }\n          });\n\n          $scope._getNormalizedStateName = function(newStateName) {\n            return $filter(\'normalizeWhitespace\')(newStateName);\n          };\n\n          var _isNewStateNameValid = function(stateName) {\n            if (stateName === StateEditorService.getActiveStateName()) {\n              return true;\n            }\n            return ExplorationStatesService.isNewStateNameValid(\n              stateName, true);\n          };\n\n          $scope.saveStateNameAndRefresh = function(newStateName) {\n            var normalizedStateName =\n              $scope._getNormalizedStateName(newStateName);\n            var valid = $scope.saveStateName(normalizedStateName);\n            if (valid) {\n              RouterService.navigateToMainTab(normalizedStateName);\n            }\n          };\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''