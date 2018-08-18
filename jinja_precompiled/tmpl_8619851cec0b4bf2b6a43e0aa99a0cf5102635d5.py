from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/statistics_tab/EarlyQuitIssueDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for visualizing early quit issue.\n */\n\noppia.directive(\'earlyQuitIssueDirective\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        // An integer representing the issue index.\n        index: \'&\',\n        // A read-only object representing the issue.\n        issue: \'&\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/exploration_editor/statistics_tab/\' +\n        \'early_quit_issue_directive.html\'),\n      controller: [\n        \'$scope\', \'$uibModal\', \'AlertsService\', \'IssuesService\',\n        function($scope, $uibModal, AlertsService, IssuesService) {\n          $scope.currentIssueIdentifier = $scope.index() + 1;\n\n          var issue = $scope.issue();\n          $scope.issueStatement = IssuesService.renderIssueStatement(issue);\n          $scope.suggestions = IssuesService.renderIssueSuggestions(issue);\n          $scope.playthroughIds = issue.playthroughIds;\n\n          var getPlaythroughIndex = function(playthroughId) {\n            return $scope.playthroughIds.indexOf(playthroughId);\n          };\n\n          $scope.createPlaythroughNavId = function(playthroughId) {\n            return getPlaythroughIndex(playthroughId) + 1;\n          };\n\n          var issueResolved = false;\n          $scope.resolveIssue = function() {\n            if (!issueResolved) {\n              IssuesService.resolveIssue(issue);\n              AlertsService.addSuccessMessage(\n                \'Issue resolved. Refresh the page to view changes.\');\n              issueResolved = true;\n            } else {\n              AlertsService.addSuccessMessage(\n                \'Issue has already been resolved. No need to resolve again. \' +\n                \'Refresh the page to view changes.\');\n            }\n          };\n\n          $scope.showPlaythrough = function(playthroughId) {\n            IssuesService.getPlaythrough(\n              playthroughId\n            ).then(function(playthrough) {\n              $uibModal.open({\n                templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n                  \'/pages/exploration_editor/statistics_tab/\' +\n                  \'playthrough_modal_directive.html\'),\n                backdrop: true,\n                resolve: {\n                  playthrough: function() {\n                    return playthrough;\n                  },\n                  playthroughIndex: function() {\n                    return $scope.playthroughIds.indexOf(playthroughId);\n                  }\n                },\n                controller: [\n                  \'$scope\', \'$uibModalInstance\', \'playthroughIndex\',\n                  \'playthrough\', \'AlertsService\', \'LearnerActionRenderService\',\n                  function(\n                      $scope, $uibModalInstance, playthroughIndex,\n                      playthrough, AlertsService, LearnerActionRenderService) {\n                    $scope.playthroughIndex = playthroughIndex;\n\n                    $scope.displayBlocks =\n                      LearnerActionRenderService.getDisplayBlocks(\n                        playthrough.actions);\n                    $scope.reversedDisplayBlocks =\n                      $scope.displayBlocks.slice().reverse();\n\n                    var blockActionIndexMapping = {};\n                    $scope.displayBlocks.reduce(\n                      function(runningTotal, displayBlock, i) {\n                        blockActionIndexMapping[i] =\n                          runningTotal - displayBlock.length;\n                        return runningTotal - displayBlock.length;\n                      }, playthrough.actions.length + 1);\n\n                    $scope.maxHidden = $scope.displayBlocks.length - 1;\n\n                    $scope.getDisplayBlockIndex = function(displayBlock) {\n                      return $scope.displayBlocks.indexOf(displayBlock);\n                    };\n\n                    $scope.isDisplayBlockOnInitDisplay = function(block) {\n                      return $scope.getDisplayBlockIndex(block) === 0;\n                    };\n\n                    $scope.createDisplayBlockNavId = function(block) {\n                      return $scope.getDisplayBlockIndex(block) + 1;\n                    };\n\n                    $scope.renderBlockHtml = function(displayBlock) {\n                      var index = $scope.getDisplayBlockIndex(displayBlock);\n                      return LearnerActionRenderService.renderDisplayBlockHTML(\n                        displayBlock, blockActionIndexMapping[index]);\n                    };\n\n                    var getRemainingActionsElements = function(pIdx, i) {\n                      return document.getElementById(\n                        \'remainingActions\' + pIdx.toString() + i.toString());\n                    };\n\n                    /**\n                     * Shows the remaining display blocks and the arrow div. If\n                     * there is only one display block, the arrow div is not\n                     * shown at all. If the current shown display block is the\n                     * second last display block, the arrow div is hidden after\n                     * the final display block is shown. Else, the following\n                     * display block is displayed.\n                     */\n                    $scope.showRemainingActions = function(pIdx) {\n                      // If there is only one display block left to be shown,\n                      // the arrow is not required.\n                      if ($scope.maxHidden === 1) {\n                        getRemainingActionsElements(\n                          pIdx, $scope.maxHidden).style.display = \'block\';\n                        document.getElementById(\'arrowDiv\').style.display =\n                          \'none\';\n                      } else {\n                        var currentShown = 0, i;\n                        for (i = $scope.maxHidden; i > 0; i--) {\n                          if (getRemainingActionsElements(\n                            pIdx, i).style.display === \'block\') {\n                            currentShown = i;\n                            break;\n                          }\n                        }\n                        if (currentShown === 0) {\n                          getRemainingActionsElements(\n                            pIdx, currentShown + 1).style.display = \'block\';\n                        } else if (currentShown === $scope.maxHidden - 1) {\n                          getRemainingActionsElements(\n                            pIdx, $scope.maxHidden).style.display = \'block\';\n                          document.getElementById(\n                            \'arrowDiv\').style.display = \'none\';\n                        } else {\n                          getRemainingActionsElements(\n                            pIdx, currentShown + 1).style.display = \'block\';\n                        }\n                      }\n                    };\n\n                    $scope.cancel = function() {\n                      $uibModalInstance.dismiss(\'cancel\');\n                      AlertsService.clearWarnings();\n                    };\n                  }\n                ]\n              });\n            });\n          };\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''