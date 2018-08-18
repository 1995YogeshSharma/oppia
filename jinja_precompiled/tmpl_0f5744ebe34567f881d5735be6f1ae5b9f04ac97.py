from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationSaveService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for exploration saving & publication functionality.\n */\n\noppia.factory(\'ExplorationSaveService\', [\n  \'$uibModal\', \'$timeout\', \'$rootScope\', \'$log\', \'$q\',\n  \'AlertsService\', \'ExplorationDataService\', \'ExplorationStatesService\',\n  \'ExplorationTagsService\', \'ExplorationTitleService\',\n  \'ExplorationObjectiveService\', \'ExplorationCategoryService\',\n  \'ExplorationLanguageCodeService\', \'ExplorationRightsService\',\n  \'ExplorationWarningsService\', \'ExplorationDiffService\',\n  \'ExplorationInitStateNameService\', \'RouterService\',\n  \'FocusManagerService\', \'ChangeListService\', \'siteAnalyticsService\',\n  \'StatesObjectFactory\', \'UrlInterpolationService\',\n  \'AutosaveInfoModalsService\',\n  function(\n      $uibModal, $timeout, $rootScope, $log, $q,\n      AlertsService, ExplorationDataService, ExplorationStatesService,\n      ExplorationTagsService, ExplorationTitleService,\n      ExplorationObjectiveService, ExplorationCategoryService,\n      ExplorationLanguageCodeService, ExplorationRightsService,\n      ExplorationWarningsService, ExplorationDiffService,\n      ExplorationInitStateNameService, RouterService,\n      FocusManagerService, ChangeListService, siteAnalyticsService,\n      StatesObjectFactory, UrlInterpolationService,\n      AutosaveInfoModalsService) {\n    // Whether or not a save action is currently in progress\n    // (request has been sent to backend but no reply received yet)\n    var saveIsInProgress = false;\n\n    // This flag is used to ensure only one save exploration modal can be open\n    // at any one time.\n    var modalIsOpen = false;\n\n    var diffData = null;\n\n    var isAdditionalMetadataNeeded = function() {\n      return (\n        !ExplorationTitleService.savedMemento ||\n        !ExplorationObjectiveService.savedMemento ||\n        !ExplorationCategoryService.savedMemento ||\n        ExplorationLanguageCodeService.savedMemento ===\n          constants.DEFAULT_LANGUAGE_CODE ||\n        ExplorationTagsService.savedMemento.length === 0);\n    };\n\n    var areRequiredFieldsFilled = function() {\n      if (!ExplorationTitleService.displayed) {\n        AlertsService.addWarning(\'Please specify a title\');\n        return false;\n      }\n      if (!ExplorationObjectiveService.displayed) {\n        AlertsService.addWarning(\'Please specify an objective\');\n        return false;\n      }\n      if (!ExplorationCategoryService.displayed) {\n        AlertsService.addWarning(\'Please specify a category\');\n        return false;\n      }\n\n      return true;\n    };\n\n    var showCongratulatorySharingModal = function() {\n      return $uibModal.open({\n        templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n          \'/pages/exploration_editor/\' +\n          \'post_publish_modal_directive.html\'),\n        backdrop: true,\n        controller: [\n          \'$scope\', \'$window\', \'$uibModalInstance\',\n          \'ContextService\',\n          function(\n              $scope, $window, $uibModalInstance,\n              ContextService) {\n            $scope.congratsImgUrl = UrlInterpolationService.getStaticImageUrl(\n              \'/general/congrats.svg\');\n            $scope.DEFAULT_TWITTER_SHARE_MESSAGE_EDITOR = (\n              GLOBALS.DEFAULT_TWITTER_SHARE_MESSAGE_EDITOR);\n            $scope.close = function() {\n              $uibModalInstance.dismiss(\'cancel\');\n            };\n            $scope.explorationId = (\n              ContextService.getExplorationId());\n            $scope.explorationLink = (\n              $window.location.protocol + \'//\' +\n              $window.location.host + \'/explore/\' + $scope.explorationId);\n            $scope.selectText = function(evt) {\n              var codeDiv = evt.currentTarget;\n              var range = document.createRange();\n              range.setStartBefore(codeDiv.firstChild);\n              range.setEndAfter(codeDiv.lastChild);\n              var selection = window.getSelection();\n              selection.removeAllRanges();\n              selection.addRange(range);\n            };\n          }\n        ]\n      });\n    };\n\n    var openPublishExplorationModal = function(\n        onStartSaveCallback, onSaveDoneCallback) {\n      // This is resolved when modal is closed.\n      var whenModalClosed = $q.defer();\n\n      var publishModalInstance = $uibModal.open({\n        templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n          \'/pages/exploration_editor/\' +\n          \'exploration_publish_modal_directive.html\'),\n        backdrop: true,\n        controller: [\n          \'$scope\', \'$uibModalInstance\', function($scope, $uibModalInstance) {\n            $scope.publish = $uibModalInstance.close;\n\n            $scope.cancel = function() {\n              $uibModalInstance.dismiss(\'cancel\');\n              AlertsService.clearWarnings();\n              whenModalClosed.resolve();\n            };\n          }\n        ]\n      });\n\n      publishModalInstance.result.then(function() {\n        if (onStartSaveCallback) {\n          onStartSaveCallback();\n        }\n\n        ExplorationRightsService.publish().then(\n          function() {\n            if (onSaveDoneCallback) {\n              onSaveDoneCallback();\n            }\n\n            showCongratulatorySharingModal();\n            siteAnalyticsService.registerPublishExplorationEvent(\n              ExplorationDataService.explorationId);\n            whenModalClosed.resolve();\n          });\n      });\n\n      return whenModalClosed.promise;\n    };\n\n    var saveDraftToBackend = function(commitMessage) {\n      // Resolved when save is done\n      // (regardless of success or failure of the operation).\n      var whenSavingDone = $q.defer();\n\n      var changeList = ChangeListService.getChangeList();\n\n      if (ExplorationRightsService.isPrivate()) {\n        siteAnalyticsService.registerCommitChangesToPrivateExplorationEvent(\n          ExplorationDataService.explorationId);\n      } else {\n        siteAnalyticsService.registerCommitChangesToPublicExplorationEvent(\n          ExplorationDataService.explorationId);\n      }\n\n      if (ExplorationWarningsService.countWarnings() === 0) {\n        siteAnalyticsService.registerSavePlayableExplorationEvent(\n          ExplorationDataService.explorationId);\n      }\n      saveIsInProgress = true;\n\n      ExplorationDataService.save(\n        changeList, commitMessage,\n        function(isDraftVersionValid, draftChanges) {\n          if (isDraftVersionValid === false &&\n              draftChanges !== null &&\n              draftChanges.length > 0) {\n            AutosaveInfoModalsService.showVersionMismatchModal(changeList);\n            return;\n          }\n          $log.info(\'Changes to this exploration were saved successfully.\');\n          ChangeListService.discardAllChanges();\n          $rootScope.$broadcast(\'initExplorationPage\');\n          $rootScope.$broadcast(\'refreshVersionHistory\', {\n            forceRefresh: true\n          });\n          AlertsService.addSuccessMessage(\'Changes saved.\');\n          saveIsInProgress = false;\n          whenSavingDone.resolve();\n        }, function() {\n          saveIsInProgress = false;\n          whenSavingDone.resolve();\n        }\n      );\n      return whenSavingDone.promise;\n    };\n\n    return {\n      isExplorationSaveable: function() {\n        return (\n          ChangeListService.isExplorationLockedForEditing() &&\n          !saveIsInProgress && (\n            (ExplorationRightsService.isPrivate() &&\n              !ExplorationWarningsService.hasCriticalWarnings()) ||\n            (!ExplorationRightsService.isPrivate() &&\n              ExplorationWarningsService.countWarnings() === 0)\n          )\n        );\n      },\n\n      discardChanges: function() {\n        $uibModal.open({\n          templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n            \'/pages/exploration_editor/\' +\n            \'confirm_discard_changes_modal_directive.html\'),\n          backdrop: \'static\',\n          keyboard: false,\n          controller: [\n            \'$scope\', \'$uibModalInstance\', function($scope, $uibModalInstance) {\n              $scope.cancel = function() {\n                $uibModalInstance.dismiss();\n              };\n              $scope.confirmDiscard = function() {\n                $uibModalInstance.close();\n              };\n            }\n          ]\n        }).result.then(function() {\n          AlertsService.clearWarnings();\n          $rootScope.$broadcast(\'externalSave\');\n\n          $uibModal.open({\n            templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n              \'/pages/exploration_editor/\' +\n              \'editor_reloading_modal_directive.html\'),\n            backdrop: \'static\',\n            keyboard: false,\n            controller: [\n              \'$scope\', \'$uibModalInstance\',\n              function($scope, $uibModalInstance) {\n                $timeout(function() {\n                  $uibModalInstance.dismiss(\'cancel\');\n                }, 2500);\n              }\n            ],\n            windowClass: \'oppia-loading-modal\'\n          });\n\n          ChangeListService.discardAllChanges();\n          AlertsService.addSuccessMessage(\'Changes discarded.\');\n          $rootScope.$broadcast(\'initExplorationPage\');\n\n          // The reload is necessary because, otherwise, the\n          // exploration-with-draft-changes will be reloaded\n          // (since it is already cached in ExplorationDataService).\n          location.reload();\n        });\n      },\n\n      showPublishExplorationModal: function(\n          onStartLoadingCallback, onEndLoadingCallback) {\n        // This is resolved after publishing modals are closed,\n        // so we can remove the loading-dots.\n        var whenModalsClosed = $q.defer();\n\n        siteAnalyticsService.registerOpenPublishExplorationModalEvent(\n          ExplorationDataService.explorationId);\n        AlertsService.clearWarnings();\n\n        // If the metadata has not yet been specified, open the pre-publication\n        // \'add exploration metadata\' modal.\n        if (isAdditionalMetadataNeeded()) {\n          var modalInstance = $uibModal.open({\n            templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n              \'/pages/exploration_editor/\' +\n              \'exploration_metadata_modal_directive.html\'),\n            backdrop: \'static\',\n            controller: [\n              \'$scope\', \'$uibModalInstance\', \'ExplorationObjectiveService\',\n              \'ExplorationTitleService\', \'ExplorationCategoryService\',\n              \'ExplorationStatesService\', \'ALL_CATEGORIES\',\n              \'ExplorationLanguageCodeService\', \'ExplorationTagsService\',\n              function($scope, $uibModalInstance, ExplorationObjectiveService,\n                  ExplorationTitleService, ExplorationCategoryService,\n                  ExplorationStatesService, ALL_CATEGORIES,\n                  ExplorationLanguageCodeService, ExplorationTagsService) {\n                $scope.explorationTitleService = ExplorationTitleService;\n                $scope.explorationObjectiveService =\n                  ExplorationObjectiveService;\n                $scope.explorationCategoryService =\n                  ExplorationCategoryService;\n                $scope.explorationLanguageCodeService = (\n                  ExplorationLanguageCodeService);\n                $scope.explorationTagsService = ExplorationTagsService;\n\n                $scope.objectiveHasBeenPreviouslyEdited = (\n                  ExplorationObjectiveService.savedMemento.length > 0);\n\n                $scope.requireTitleToBeSpecified = (\n                  !ExplorationTitleService.savedMemento);\n                $scope.requireObjectiveToBeSpecified = (\n                  ExplorationObjectiveService.savedMemento.length < 15);\n                $scope.requireCategoryToBeSpecified = (\n                  !ExplorationCategoryService.savedMemento);\n                $scope.askForLanguageCheck = (\n                  ExplorationLanguageCodeService.savedMemento ===\n                  constants.DEFAULT_LANGUAGE_CODE);\n                $scope.askForTags = (\n                  ExplorationTagsService.savedMemento.length === 0);\n\n                $scope.TAG_REGEX = GLOBALS.TAG_REGEX;\n\n                $scope.CATEGORY_LIST_FOR_SELECT2 = [];\n\n                for (var i = 0; i < ALL_CATEGORIES.length; i++) {\n                  $scope.CATEGORY_LIST_FOR_SELECT2.push({\n                    id: ALL_CATEGORIES[i],\n                    text: ALL_CATEGORIES[i]\n                  });\n                }\n\n                if (ExplorationStatesService.isInitialized()) {\n                  var categoryIsInSelect2 = $scope.CATEGORY_LIST_FOR_SELECT2\n                    .some(\n                      function(categoryItem) {\n                        return categoryItem.id ===\n                      ExplorationCategoryService.savedMemento;\n                      }\n                    );\n\n                  // If the current category is not in the dropdown, add it\n                  // as the first option.\n                  if (!categoryIsInSelect2 &&\n                      ExplorationCategoryService.savedMemento) {\n                    $scope.CATEGORY_LIST_FOR_SELECT2.unshift({\n                      id: ExplorationCategoryService.savedMemento,\n                      text: ExplorationCategoryService.savedMemento\n                    });\n                  }\n                }\n\n                $scope.isSavingAllowed = function() {\n                  return Boolean(\n                    ExplorationTitleService.displayed &&\n                    ExplorationObjectiveService.displayed &&\n                    ExplorationObjectiveService.displayed.length >= 15 &&\n                    ExplorationCategoryService.displayed &&\n                    ExplorationLanguageCodeService.displayed);\n                };\n\n                $scope.save = function() {\n                  if (!areRequiredFieldsFilled()) {\n                    return;\n                  }\n\n                  // Record any fields that have changed.\n                  var metadataList = [];\n                  if (ExplorationTitleService.hasChanged()) {\n                    metadataList.push(\'title\');\n                  }\n                  if (ExplorationObjectiveService.hasChanged()) {\n                    metadataList.push(\'objective\');\n                  }\n                  if (ExplorationCategoryService.hasChanged()) {\n                    metadataList.push(\'category\');\n                  }\n                  if (ExplorationLanguageCodeService.hasChanged()) {\n                    metadataList.push(\'language\');\n                  }\n                  if (ExplorationTagsService.hasChanged()) {\n                    metadataList.push(\'tags\');\n                  }\n\n                  // Save all the displayed values.\n                  ExplorationTitleService.saveDisplayedValue();\n                  ExplorationObjectiveService.saveDisplayedValue();\n                  ExplorationCategoryService.saveDisplayedValue();\n                  ExplorationLanguageCodeService.saveDisplayedValue();\n                  ExplorationTagsService.saveDisplayedValue();\n\n                  // TODO(sll): Get rid of the $timeout here.\n                  // It\'s currently used because there is a race condition: the\n                  // saveDisplayedValue() calls above result in autosave calls.\n                  // These race with the discardDraft() call that\n                  // will be called when the draft changes entered here\n                  // are properly saved to the backend.\n                  $timeout(function() {\n                    $uibModalInstance.close(metadataList);\n                  }, 500);\n                };\n\n                $scope.cancel = function() {\n                  whenModalsClosed.resolve();\n                  ExplorationTitleService.restoreFromMemento();\n                  ExplorationObjectiveService.restoreFromMemento();\n                  ExplorationCategoryService.restoreFromMemento();\n                  ExplorationLanguageCodeService.restoreFromMemento();\n                  ExplorationTagsService.restoreFromMemento();\n\n                  $uibModalInstance.dismiss(\'cancel\');\n                  AlertsService.clearWarnings();\n                };\n              }\n            ]\n          });\n\n          modalInstance.opened.then(function() {\n            // Toggle loading dots off after modal is opened\n            if (onEndLoadingCallback) {\n              onEndLoadingCallback();\n            }\n          });\n\n          modalInstance.result.then(function(metadataList) {\n            if (metadataList.length > 0) {\n              var commitMessage = (\n                \'Add metadata: \' + metadataList.join(\', \') + \'.\');\n\n              if (onStartLoadingCallback) {\n                onStartLoadingCallback();\n              }\n\n              saveDraftToBackend(commitMessage).then(function() {\n                if (onEndLoadingCallback) {\n                  onEndLoadingCallback();\n                }\n                openPublishExplorationModal(\n                  onStartLoadingCallback, onEndLoadingCallback)\n                  .then(function() {\n                    whenModalsClosed.resolve();\n                  });\n              });\n            } else {\n              openPublishExplorationModal(\n                onStartLoadingCallback, onEndLoadingCallback)\n                .then(function() {\n                  whenModalsClosed.resolve();\n                });\n            }\n          });\n        } else {\n          // No further metadata is needed. Open the publish modal immediately.\n          openPublishExplorationModal(\n            onStartLoadingCallback, onEndLoadingCallback)\n            .then(function() {\n              whenModalsClosed.resolve();\n            });\n        }\n        return whenModalsClosed.promise;\n      },\n\n      saveChanges: function(onStartLoadingCallback, onEndLoadingCallback) {\n        // This is marked as resolved after modal is closed, so we can change\n        // controller \'saveIsInProgress\' back to false.\n        var whenModalClosed = $q.defer();\n\n        RouterService.savePendingChanges();\n\n        if (!ExplorationRightsService.isPrivate() &&\n            ExplorationWarningsService.countWarnings() > 0) {\n          // If the exploration is not private, warnings should be fixed before\n          // it can be saved.\n          AlertsService.addWarning(ExplorationWarningsService.getWarnings()[0]);\n          return;\n        }\n\n        ExplorationDataService.getLastSavedData().then(function(data) {\n          var oldStates = StatesObjectFactory.createFromBackendDict(\n            data.states).getStateObjects();\n          var newStates = ExplorationStatesService.getStates()\n            .getStateObjects();\n          var diffGraphData = ExplorationDiffService.getDiffGraphData(\n            oldStates, newStates, [{\n              changeList: ChangeListService.getChangeList(),\n              directionForwards: true\n            }]);\n          diffData = {\n            nodes: diffGraphData.nodes,\n            links: diffGraphData.links,\n            finalStateIds: diffGraphData.finalStateIds,\n            v1InitStateId: diffGraphData.originalStateIds[data.init_state_name],\n            v2InitStateId: diffGraphData.stateIds[\n              ExplorationInitStateNameService.displayed],\n            v1States: oldStates,\n            v2States: newStates\n          };\n\n          // TODO(wxy): after diff supports exploration metadata, add a check to\n          // exit if changes cancel each other out.\n\n          AlertsService.clearWarnings();\n\n          // If the modal is open, do not open another one.\n          if (modalIsOpen) {\n            return;\n          }\n\n          var modalInstance = $uibModal.open({\n            templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n              \'/pages/exploration_editor/\' +\n              \'exploration_save_modal_directive.html\'),\n            backdrop: true,\n            resolve: {\n              isExplorationPrivate: function() {\n                return ExplorationRightsService.isPrivate();\n              },\n              diffData: function() {\n                return diffData;\n              }\n            },\n            windowClass: \'oppia-save-exploration-modal\',\n            controller: [\n              \'$scope\', \'$uibModalInstance\', \'isExplorationPrivate\',\n              function(\n                  $scope, $uibModalInstance, isExplorationPrivate) {\n                $scope.showDiff = false;\n                $scope.onClickToggleDiffButton = function() {\n                  $scope.showDiff = !$scope.showDiff;\n                  if ($scope.showDiff) {\n                    $(\'.oppia-save-exploration-modal\').addClass(\n                      \'oppia-save-exploration-wide-modal\');\n                  } else {\n                    $(\'.oppia-save-exploration-modal\').removeClass(\n                      \'oppia-save-exploration-wide-modal\');\n                  }\n                };\n\n                $scope.diffData = diffData;\n                $scope.isExplorationPrivate = isExplorationPrivate;\n\n                $scope.earlierVersionHeader = \'Last saved\';\n                $scope.laterVersionHeader = \'New changes\';\n\n                $scope.save = function(commitMessage) {\n                  $uibModalInstance.close(commitMessage);\n                };\n                $scope.cancel = function() {\n                  $uibModalInstance.dismiss(\'cancel\');\n                  AlertsService.clearWarnings();\n                };\n              }\n            ]\n          });\n\n          // Modal is Opened\n          modalIsOpen = true;\n\n          modalInstance.opened.then(function() {\n            // Toggle loading dots off after modal is opened\n            if (onEndLoadingCallback) {\n              onEndLoadingCallback();\n            }\n            // The $timeout seems to be needed\n            // in order to give the modal time to render.\n            $timeout(function() {\n              FocusManagerService.setFocus(\'saveChangesModalOpened\');\n            });\n          });\n\n          modalInstance.result.then(function(commitMessage) {\n            modalIsOpen = false;\n\n            // Toggle loading dots back on for loading from backend.\n            if (onStartLoadingCallback) {\n              onStartLoadingCallback();\n            }\n\n            saveDraftToBackend(commitMessage).then(function() {\n              whenModalClosed.resolve();\n            });\n          }, function() {\n            modalIsOpen = false;\n            whenModalClosed.resolve();\n          });\n        });\n        return whenModalClosed.promise;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''