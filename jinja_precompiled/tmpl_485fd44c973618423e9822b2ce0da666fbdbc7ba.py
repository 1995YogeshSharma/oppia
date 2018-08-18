from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/OutcomeDestinationEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directives for the outcome destination editor.\n */\n\noppia.directive(\'outcomeDestinationEditor\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        outcomeHasFeedback: \'=\',\n        outcome: \'=\',\n        addState: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/outcome_destination_editor_directive.html\'),\n      controller: [\n        \'$scope\', \'StateEditorService\',\n        \'StateGraphLayoutService\', \'PLACEHOLDER_OUTCOME_DEST\',\n        \'FocusManagerService\', \'EditorFirstTimeEventsService\',\n        \'EXPLORATION_AND_SKILL_ID_PATTERN\',\n        function(\n            $scope, StateEditorService,\n            StateGraphLayoutService, PLACEHOLDER_OUTCOME_DEST,\n            FocusManagerService, EditorFirstTimeEventsService,\n            EXPLORATION_AND_SKILL_ID_PATTERN) {\n          var currentStateName = null;\n          $scope.canAddPrerequisiteSkill = constants.ENABLE_NEW_STRUCTURES;\n\n          $scope.$on(\'saveOutcomeDestDetails\', function() {\n            // Create new state if specified.\n            if ($scope.outcome.dest === PLACEHOLDER_OUTCOME_DEST) {\n              EditorFirstTimeEventsService\n                .registerFirstCreateSecondStateEvent();\n\n              var newStateName = $scope.outcome.newStateName;\n              $scope.outcome.dest = newStateName;\n              delete $scope.outcome.newStateName;\n\n              $scope.addState(newStateName);\n            }\n          });\n\n          // We restrict editing of refresher exploration IDs to\n          // admins/moderators for now, since the feature is still in\n          // development.\n          $scope.canEditRefresherExplorationId = (\n            GLOBALS.isAdmin || GLOBALS.isModerator);\n          $scope.explorationAndSkillIdPattern =\n            EXPLORATION_AND_SKILL_ID_PATTERN;\n\n          $scope.isSelfLoop = function() {\n            return $scope.outcome.dest === currentStateName;\n          };\n\n          $scope.onDestSelectorChange = function() {\n            if ($scope.outcome.dest === PLACEHOLDER_OUTCOME_DEST) {\n              FocusManagerService.setFocus(\'newStateNameInputField\');\n            }\n          };\n\n          $scope.isCreatingNewState = function(outcome) {\n            return outcome.dest === PLACEHOLDER_OUTCOME_DEST;\n          };\n\n          $scope.newStateNamePattern = /^[a-zA-Z0-9.\\s-]+$/;\n          $scope.destChoices = [];\n          $scope.$watch(StateEditorService.getStateNames, function() {\n            currentStateName = StateEditorService.getActiveStateName();\n\n            var questionModeEnabled = StateEditorService.isInQuestionMode();\n            // This is a list of objects, each with an ID and name. These\n            // represent all states, as well as an option to create a\n            // new state.\n            $scope.destChoices = [{\n              id: (questionModeEnabled ? null : currentStateName),\n              text: \'(try again)\'\n            }];\n\n            // Arrange the remaining states based on their order in the state\n            // graph.\n            var lastComputedArrangement = (\n              StateGraphLayoutService.getLastComputedArrangement());\n            var allStateNames = StateEditorService.getStateNames();\n\n            // It is possible that lastComputedArrangement is null if the graph\n            // has never been rendered at the time this computation is being\n            // carried out.\n            var stateNames = angular.copy(allStateNames);\n            if (lastComputedArrangement) {\n              var maxDepth = 0;\n              var maxOffset = 0;\n              for (var stateName in lastComputedArrangement) {\n                maxDepth = Math.max(\n                  maxDepth, lastComputedArrangement[stateName].depth);\n                maxOffset = Math.max(\n                  maxOffset, lastComputedArrangement[stateName].offset);\n              }\n\n              // Higher scores come later.\n              var allStateScores = {};\n              var unarrangedStateCount = 0;\n              for (var i = 0; i < allStateNames.length; i++) {\n                var stateName = allStateNames[i];\n                if (lastComputedArrangement.hasOwnProperty(stateName)) {\n                  allStateScores[stateName] = (\n                    lastComputedArrangement[stateName].depth * (maxOffset + 1) +\n                    lastComputedArrangement[stateName].offset);\n                } else {\n                  // States that have just been added in the rule \'create new\'\n                  // modal are not yet included as part of\n                  // lastComputedArrangement so we account for them here.\n                  allStateScores[stateName] = (\n                    (maxDepth + 1) * (maxOffset + 1) + unarrangedStateCount);\n                  unarrangedStateCount++;\n                }\n              }\n\n              stateNames = allStateNames.sort(function(a, b) {\n                return allStateScores[a] - allStateScores[b];\n              });\n            }\n\n            for (var i = 0; i < stateNames.length; i++) {\n              if (stateNames[i] !== currentStateName) {\n                $scope.destChoices.push({\n                  id: stateNames[i],\n                  text: stateNames[i]\n                });\n              }\n            }\n\n            if (!questionModeEnabled) {\n              $scope.destChoices.push({\n                id: PLACEHOLDER_OUTCOME_DEST,\n                text: \'A New Card Called...\'\n              });\n            }\n          }, true);\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''