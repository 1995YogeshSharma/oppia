from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/StateTranslationDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive containing the exploration material to be translated.\n */\n\noppia.directive(\'stateTranslation\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        isTranslationTabBusy: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/exploration_editor/translation_tab/\' +\n        \'state_translation_directive.html\'),\n      controller: [\n        \'$scope\', \'$filter\', \'$rootScope\', \'StateEditorService\',\n        \'ExplorationStatesService\', \'ExplorationInitStateNameService\',\n        \'ExplorationCorrectnessFeedbackService\', \'RouterService\',\n        \'TranslationStatusService\', \'COMPONENT_NAME_CONTENT\',\n        \'COMPONENT_NAME_FEEDBACK\', \'COMPONENT_NAME_HINT\',\n        \'COMPONENT_NAME_SOLUTION\', \'INTERACTION_SPECS\',\n        \'RULE_SUMMARY_WRAP_CHARACTER_COUNT\',\n        function(\n            $scope, $filter, $rootScope, StateEditorService,\n            ExplorationStatesService, ExplorationInitStateNameService,\n            ExplorationCorrectnessFeedbackService, RouterService,\n            TranslationStatusService, COMPONENT_NAME_CONTENT,\n            COMPONENT_NAME_FEEDBACK, COMPONENT_NAME_HINT,\n            COMPONENT_NAME_SOLUTION, INTERACTION_SPECS,\n            RULE_SUMMARY_WRAP_CHARACTER_COUNT) {\n          // Define tab constants.\n          $scope.TAB_ID_CONTENT = COMPONENT_NAME_CONTENT;\n          $scope.TAB_ID_FEEDBACK = COMPONENT_NAME_FEEDBACK;\n          $scope.TAB_ID_HINTS = COMPONENT_NAME_HINT;\n          $scope.TAB_ID_SOLUTION = COMPONENT_NAME_SOLUTION;\n\n          $scope.ExplorationCorrectnessFeedbackService =\n            ExplorationCorrectnessFeedbackService;\n\n          // Activates Content tab by default.\n          $scope.activatedTabId = $scope.TAB_ID_CONTENT;\n\n          $scope.activeHintIndex = null;\n          $scope.activeAnswerGroupIndex = null;\n          $scope.stateContent = null;\n          $scope.stateInteractionId = null;\n          $scope.stateAnswerGroups = [];\n          $scope.stateDefaultOutcome = null;\n          $scope.stateHints = [];\n          $scope.stateSolution = null;\n          $scope.activeContentId = null;\n          $scope.needsUpdateTooltipMessage = \'Audio needs update to match \' +\n            \'text. Please record new audio.\';\n\n          $scope.isActive = function(tabId) {\n            return ($scope.activatedTabId === tabId);\n          };\n\n          $scope.navigateToState = function(stateName) {\n            RouterService.navigateToMainTab(stateName);\n          };\n\n          $scope.onTabClick = function(tabId) {\n            if ($scope.isTranslationTabBusy) {\n              $rootScope.$broadcast(\'showTranslationTabBusyModal\');\n              return;\n            }\n            if (tabId === $scope.TAB_ID_CONTENT) {\n              $scope.activeContentId = $scope.stateContent.getContentId();\n            } else if (tabId === $scope.TAB_ID_FEEDBACK) {\n              $scope.activeAnswerGroupIndex = 0;\n              if ($scope.stateAnswerGroups.length > 0) {\n                $scope.activeContentId = $scope.stateAnswerGroups[0]\n                  .outcome.feedback.getContentId();\n              } else {\n                $scope.activeContentId = $scope.stateDefaultOutcome\n                  .feedback.getContentId();\n              }\n            } else if (tabId === $scope.TAB_ID_HINTS) {\n              $scope.activeHintIndex = 0;\n              $scope.activeContentId = $scope.stateHints[0]\n                .hintContent.getContentId();\n            } else if (tabId === $scope.TAB_ID_SOLUTION) {\n              $scope.activeContentId = $scope.stateSolution.explanation\n                .getContentId();\n            }\n            $scope.activatedTabId = tabId;\n          };\n\n          $scope.summarizeDefaultOutcome = function(\n              defaultOutcome, interactionId, answerGroupCount, shortenRule) {\n            if (!defaultOutcome) {\n              return \'\';\n            }\n\n            var summary = \'\';\n            var hasFeedback = defaultOutcome.hasNonemptyFeedback();\n\n            if (interactionId && INTERACTION_SPECS[interactionId].is_linear) {\n              summary =\n                INTERACTION_SPECS[interactionId].default_outcome_heading;\n            } else if (answerGroupCount > 0) {\n              summary = \'All other answers\';\n            } else {\n              summary = \'All answers\';\n            }\n\n            if (hasFeedback && shortenRule) {\n              summary = $filter(\'wrapTextWithEllipsis\')(\n                summary, RULE_SUMMARY_WRAP_CHARACTER_COUNT);\n            }\n            summary = \'[\' + summary + \'] \';\n\n            if (hasFeedback) {\n              summary +=\n                $filter(\n                  \'convertToPlainText\'\n                )(defaultOutcome.feedback.getHtml());\n            }\n            return summary;\n          };\n\n          $scope.summarizeAnswerGroup = function(\n              answerGroup, interactionId, answerChoices, shortenRule) {\n            var summary = \'\';\n            var outcome = answerGroup.outcome;\n            var hasFeedback = outcome.hasNonemptyFeedback();\n\n            if (answerGroup.rules) {\n              var firstRule = $filter(\'convertToPlainText\')(\n                $filter(\'parameterizeRuleDescription\')(\n                  answerGroup.rules[0], interactionId, answerChoices));\n              summary = \'Answer \' + firstRule;\n\n              if (hasFeedback && shortenRule) {\n                summary = $filter(\'wrapTextWithEllipsis\')(\n                  summary, RULE_SUMMARY_WRAP_CHARACTER_COUNT);\n              }\n              summary = \'[\' + summary + \'] \';\n            }\n\n            if (hasFeedback) {\n              summary += (\n                shortenRule ?\n                  $filter(\'truncate\')(outcome.feedback.getHtml(), 30) :\n                  $filter(\'convertToPlainText\')(outcome.feedback.getHtml()));\n            }\n            return summary;\n          };\n\n          $scope.isDisabled = function(tabId) {\n            if (tabId === $scope.TAB_ID_CONTENT) {\n              return false;\n            }\n            // This is used to prevent users from adding unwanted audio for\n            // default_outcome and hints in Continue and EndExploration\n            // interaction.\n            if (!$scope.stateInteractionId ||\n              INTERACTION_SPECS[$scope.stateInteractionId].is_linear ||\n              INTERACTION_SPECS[$scope.stateInteractionId].is_terminal\n            ) {\n              return true;\n            } else if (tabId === $scope.TAB_ID_FEEDBACK) {\n              if (!$scope.stateDefaultOutcome) {\n                return true;\n              } else {\n                return false;\n              }\n            } else if (tabId === $scope.TAB_ID_HINTS) {\n              if ($scope.stateHints.length <= 0) {\n                return true;\n              } else {\n                return false;\n              }\n            } else if (tabId === $scope.TAB_ID_SOLUTION) {\n              if (!$scope.stateSolution) {\n                return true;\n              } else {\n                return false;\n              }\n            }\n          };\n\n          $scope.changeActiveHintIndex = function(newIndex) {\n            if ($scope.isTranslationTabBusy) {\n              $rootScope.$broadcast(\'showTranslationTabBusyModal\');\n              return;\n            }\n            if ($scope.activeHintIndex === newIndex) {\n              return;\n            }\n            $scope.activeHintIndex = newIndex;\n            $scope.activeContentId = $scope.stateHints[newIndex]\n              .hintContent.getContentId();\n          };\n\n          $scope.changeActiveAnswerGroupIndex = function(newIndex) {\n            if ($scope.isTranslationTabBusy) {\n              $rootScope.$broadcast(\'showTranslationTabBusyModal\');\n              return;\n            }\n            if ($scope.activeAnswerGroupIndex === newIndex) {\n              return;\n            }\n            $scope.activeAnswerGroupIndex = newIndex;\n            if (newIndex === $scope.stateAnswerGroups.length) {\n              $scope.activeContentId = $scope.stateDefaultOutcome\n                .feedback.getContentId();\n            } else {\n              $scope.activeContentId = $scope.stateAnswerGroups[newIndex]\n                .outcome.feedback.getContentId();\n            }\n          };\n\n          $scope.tabStatusColorStyle = function(tabId) {\n            if (!$scope.isDisabled(tabId)) {\n              var color = TranslationStatusService\n                .getActiveStateComponentStatusColor(tabId);\n              return {\'border-top-color\': color};\n            }\n          };\n\n          $scope.tabNeedUpdatesStatus = function(tabId) {\n            if (!$scope.isDisabled(tabId)) {\n              return TranslationStatusService\n                .getActiveStateComponentNeedsUpdateStatus(tabId);\n            }\n          };\n          $scope.contentIdNeedUpdates = function(contentId) {\n            return TranslationStatusService\n              .getActiveStateContentIdNeedsUpdateStatus(contentId);\n          };\n          $scope.contentIdStatusColorStyle = function(contentId) {\n            var color = TranslationStatusService\n              .getActiveStateContentIdStatusColor(contentId);\n            return {\'border-left\': \'3px solid \' + color};\n          };\n\n          $scope.getHtmlSummary = function(subtitledHtml) {\n            var htmlAsPlainText = $filter(\n              \'formatRtePreview\')(subtitledHtml.getHtml());\n            return htmlAsPlainText;\n          };\n\n          $scope.$on(\'refreshStateTranslation\', function() {\n            $scope.initStateTranslation();\n          });\n\n          $scope.initStateTranslation = function() {\n            $scope.activatedTabId = $scope.TAB_ID_CONTENT;\n\n            if (!StateEditorService.getActiveStateName()) {\n              StateEditorService.setActiveStateName(\n                ExplorationInitStateNameService.displayed);\n            }\n\n            var stateName = StateEditorService.getActiveStateName();\n\n            $scope.stateContent = ExplorationStatesService\n              .getStateContentMemento(stateName);\n            $scope.stateSolution = ExplorationStatesService\n              .getSolutionMemento(stateName);\n            $scope.stateHints = ExplorationStatesService\n              .getHintsMemento(stateName);\n            $scope.stateAnswerGroups = ExplorationStatesService\n              .getInteractionAnswerGroupsMemento(stateName);\n            $scope.stateDefaultOutcome = ExplorationStatesService\n              .getInteractionDefaultOutcomeMemento(stateName);\n            $scope.stateInteractionId = ExplorationStatesService\n              .getInteractionIdMemento(stateName);\n            $scope.activeHintIndex = null;\n            $scope.activeAnswerGroupIndex = null;\n\n            $scope.onTabClick($scope.TAB_ID_CONTENT);\n          };\n\n          // TODO(DubeySandeep): We need to call initStateTranslation() here in\n          // case the listener that receives \'refreshStateTranslation\' is not\n          // set by the time it is broadcasted from ExplorationEditor.js. Figure\n          // out a solution that does not rely on covering the race condition.\n          if (ExplorationStatesService.isInitialized()) {\n            $scope.initStateTranslation();\n          }\n          $rootScope.loadingMessage = \'\';\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''