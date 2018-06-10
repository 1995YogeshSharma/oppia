from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/EditorNavigationDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for showing Editor Navigation\n * in editor.\n */\n\noppia.directive(\'editorNavigation\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/exploration_editor/editor_navigation_directive.html\'),\n      controller: [\n        \'$scope\', \'$rootScope\', \'$timeout\', \'$uibModal\',\n        \'RouterService\', \'ExplorationRightsService\',\n        \'ExplorationWarningsService\',\n        \'StateEditorTutorialFirstTimeService\',\n        \'ThreadDataService\', \'siteAnalyticsService\',\n        \'ExplorationContextService\', \'WindowDimensionsService\',\n        function(\n            $scope, $rootScope, $timeout, $uibModal,\n            RouterService, ExplorationRightsService,\n            ExplorationWarningsService,\n            StateEditorTutorialFirstTimeService,\n            ThreadDataService, siteAnalyticsService,\n            ExplorationContextService, WindowDimensionsService) {\n          $scope.popoverControlObject = {\n            postTutorialHelpPopoverIsShown: false\n          };\n          $scope.isLargeScreen = (WindowDimensionsService.getWidth() >= 1024);\n\n          $scope.$on(\'openPostTutorialHelpPopover\', function() {\n            if ($scope.isLargeScreen) {\n              $scope.popoverControlObject.postTutorialHelpPopoverIsShown = true;\n              $timeout(function() {\n                $scope.popoverControlObject\n                  .postTutorialHelpPopoverIsShown = false;\n              }, 5000);\n            } else {\n              $scope.popoverControlObject\n                .postTutorialHelpPopoverIsShown = false;\n            }\n          });\n\n          $scope.userIsLoggedIn = GLOBALS.userIsLoggedIn;\n\n          $scope.showUserHelpModal = function() {\n            var explorationId = ExplorationContextService.getExplorationId();\n            siteAnalyticsService.registerClickHelpButtonEvent(explorationId);\n            var modalInstance = $uibModal.open({\n              templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n                \'/pages/exploration_editor/\' +\n                \'help_modal_directive.html\'),\n              backdrop: true,\n              controller: [\n                \'$scope\', \'$uibModalInstance\',\n                \'siteAnalyticsService\', \'ExplorationContextService\',\n                function(\n                    $scope, $uibModalInstance,\n                    siteAnalyticsService, ExplorationContextService) {\n                  var explorationId = (\n                    ExplorationContextService.getExplorationId());\n\n                  $scope.beginTutorial = function() {\n                    siteAnalyticsService\n                      .registerOpenTutorialFromHelpCenterEvent(\n                        explorationId);\n                    $uibModalInstance.close();\n                  };\n\n                  $scope.goToHelpCenter = function() {\n                    siteAnalyticsService.registerVisitHelpCenterEvent(\n                      explorationId);\n                    $uibModalInstance.dismiss(\'cancel\');\n                  };\n                }\n              ],\n              windowClass: \'oppia-help-modal\'\n            });\n\n            modalInstance.result.then(function() {\n              $rootScope.$broadcast(\'openEditorTutorial\');\n            }, function() {\n              StateEditorTutorialFirstTimeService.markTutorialFinished();\n            });\n          };\n\n          $scope.countWarnings = ExplorationWarningsService.countWarnings;\n          $scope.getWarnings = ExplorationWarningsService.getWarnings;\n          $scope.hasCriticalWarnings = (\n            ExplorationWarningsService.hasCriticalWarnings);\n\n          $scope.ExplorationRightsService = ExplorationRightsService;\n          $scope.getTabStatuses = RouterService.getTabStatuses;\n          $scope.selectMainTab = RouterService.navigateToMainTab;\n          $scope.selectPreviewTab = RouterService.navigateToPreviewTab;\n          $scope.selectSettingsTab = RouterService.navigateToSettingsTab;\n          $scope.selectStatsTab = RouterService.navigateToStatsTab;\n          $scope.selectHistoryTab = RouterService.navigateToHistoryTab;\n          $scope.selectFeedbackTab = RouterService.navigateToFeedbackTab;\n          $scope.getOpenThreadsCount = ThreadDataService.getOpenThreadsCount;\n\n          WindowDimensionsService.registerOnResizeHook(function() {\n            $scope.isLargeScreen = (WindowDimensionsService.getWidth() >= 1024);\n          });\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''