from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/AudioTranslationsEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for the audio translations editor for subtitled HTML.\n */\n\noppia.directive(\'audioTranslationsEditor\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        componentName: \'@\',\n        subtitledHtml: \'=\',\n        // A function that must be called at the outset of every attempt to\n        // edit, even if the action is not subsequently taken through to\n        // completion.\n        getOnStartEditFn: \'&onStartEdit\',\n        // A function that must be called on completion of an action which\n        // changes the audio translation data in a persistent way.\n        getOnChangeFn: \'&onChange\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/forms/audio_translations_editor_directive.html\'),\n      controller: [\n        \'$scope\', \'$uibModal\', \'$sce\', \'stateContentService\',\n        \'EditabilityService\', \'LanguageUtilService\', \'AlertsService\',\n        \'ExplorationContextService\', \'AssetsBackendApiService\',\n        function(\n            $scope, $uibModal, $sce, stateContentService, EditabilityService,\n            LanguageUtilService, AlertsService, ExplorationContextService,\n            AssetsBackendApiService) {\n          $scope.isEditable = EditabilityService.isEditable;\n\n          // The following if-condition is present because, sometimes,\n          // Travis-CI throws an error of the form "Cannot read property\n          // getBindableAudioTranslations of undefined". It looks like there is\n          // a race condition that is causing this directive to get\n          // initialized when it shouldn\'t. This is hard to reproduce\n          // deterministically, hence this guard.\n          if ($scope.subtitledHtml) {\n            $scope.audioTranslations = (\n              $scope.subtitledHtml.getBindableAudioTranslations());\n          }\n\n          var explorationId = ExplorationContextService.getExplorationId();\n\n          $scope.getAudioLanguageDescription = (\n            LanguageUtilService.getAudioLanguageDescription);\n\n          $scope.getAudioTranslationFullUrl = function(filename) {\n            return $sce.trustAsResourceUrl(\n              AssetsBackendApiService.getAudioDownloadUrl(\n                explorationId, filename));\n          };\n\n          $scope.toggleNeedsUpdateAttribute = function(languageCode) {\n            $scope.getOnStartEditFn()();\n            $scope.subtitledHtml.toggleNeedsUpdateAttribute(languageCode);\n            $scope.getOnChangeFn()();\n          };\n\n          $scope.openAddAudioTranslationModal = function() {\n            var allowedAudioLanguageCodes = (\n              LanguageUtilService.getComplementAudioLanguageCodes(\n                $scope.subtitledHtml.getAudioLanguageCodes()));\n\n            if (allowedAudioLanguageCodes.length === 0) {\n              AlertsService.addWarning(\n                \'Sorry, there are no more available languages to translate \' +\n                \'into.\');\n              return;\n            }\n\n            $scope.getOnStartEditFn()();\n            $uibModal.open({\n              templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n                \'/components/forms/\' +\n                \'add_audio_translation_modal_directive.html\'),\n              backdrop: \'static\',\n              resolve: {\n                allowedAudioLanguageCodes: function() {\n                  return allowedAudioLanguageCodes;\n                },\n                componentName: function() {\n                  return $scope.componentName;\n                }\n              },\n              controller: [\n                \'$scope\', \'$window\', \'$uibModalInstance\', \'LanguageUtilService\',\n                \'allowedAudioLanguageCodes\', \'AlertsService\',\n                \'ExplorationContextService\', \'IdGenerationService\',\n                \'componentName\',\n                function(\n                    $scope, $window, $uibModalInstance, LanguageUtilService,\n                    allowedAudioLanguageCodes, AlertsService,\n                    ExplorationContextService, IdGenerationService,\n                    componentName) {\n                  var ERROR_MESSAGE_BAD_FILE_UPLOAD = (\n                    \'There was an error uploading the audio file.\');\n                  var BUTTON_TEXT_SAVE = \'Save\';\n                  var BUTTON_TEXT_SAVING = \'Saving...\';\n                  var prevLanguageCode = $window.localStorage.getItem(\n                    \'last_uploaded_audio_lang\');\n\n                  $scope.languageCodesAndDescriptions = (\n                    allowedAudioLanguageCodes.map(function(languageCode) {\n                      return {\n                        code: languageCode,\n                        description: (\n                          LanguageUtilService.getAudioLanguageDescription(\n                            languageCode))\n                      };\n                    }));\n\n                  // Whether there was an error uploading the audio file.\n                  $scope.errorMessage = null;\n                  $scope.saveButtonText = BUTTON_TEXT_SAVE;\n                  $scope.saveInProgress = false;\n                  $scope.languageCode =\n                    allowedAudioLanguageCodes.indexOf(prevLanguageCode) !== -1 ?\n                      prevLanguageCode : allowedAudioLanguageCodes[0];\n                  var uploadedFile = null;\n\n                  $scope.isAudioTranslationValid = function() {\n                    return (\n                      allowedAudioLanguageCodes.indexOf(\n                        $scope.languageCode) !== -1 &&\n                      uploadedFile !== null &&\n                      uploadedFile.size !== null &&\n                      uploadedFile.size > 0);\n                  };\n\n                  $scope.updateUploadedFile = function(file) {\n                    $scope.errorMessage = null;\n                    uploadedFile = file;\n                  };\n\n                  $scope.clearUploadedFile = function() {\n                    $scope.errorMessage = null;\n                    uploadedFile = null;\n                  };\n\n                  var generateNewFilename = function() {\n                    return componentName + \'-\' +\n                      $scope.languageCode + \'-\' +\n                      IdGenerationService.generateNewId() + \'.mp3\';\n                  };\n\n                  $scope.save = function() {\n                    if ($scope.isAudioTranslationValid()) {\n                      $scope.saveButtonText = BUTTON_TEXT_SAVING;\n                      $scope.saveInProgress = true;\n                      var generatedFilename = generateNewFilename();\n                      $window.localStorage.setItem(\n                        \'last_uploaded_audio_lang\', $scope.languageCode);\n                      var explorationId = (\n                        ExplorationContextService.getExplorationId());\n                      AssetsBackendApiService.saveAudio(\n                        explorationId, generatedFilename, uploadedFile\n                      ).then(function() {\n                        $uibModalInstance.close({\n                          languageCode: $scope.languageCode,\n                          filename: generatedFilename,\n                          fileSizeBytes: uploadedFile.size\n                        });\n                      }, function(errorResponse) {\n                        $scope.errorMessage = (\n                          errorResponse.error || ERROR_MESSAGE_BAD_FILE_UPLOAD);\n                        uploadedFile = null;\n                        $scope.saveButtonText = BUTTON_TEXT_SAVE;\n                        $scope.saveInProgress = false;\n                      });\n                    }\n                  };\n\n                  $scope.cancel = function() {\n                    $uibModalInstance.dismiss(\'cancel\');\n                    AlertsService.clearWarnings();\n                  };\n                }\n              ]\n            }).result.then(function(result) {\n              $scope.subtitledHtml.addAudioTranslation(\n                result.languageCode, result.filename, result.fileSizeBytes);\n              $scope.getOnChangeFn()();\n            });\n          };\n\n          $scope.openDeleteAudioTranslationModal = function(languageCode) {\n            $scope.getOnStartEditFn()();\n\n            $uibModal.open({\n              templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n                \'/components/forms/\' +\n                \'delete_audio_translation_modal_directive.html\'),\n              backdrop: true,\n              resolve: {\n                languageCode: function() {\n                  return languageCode;\n                }\n              },\n              controller: [\n                \'$scope\', \'$uibModalInstance\', \'LanguageUtilService\',\n                \'languageCode\',\n                function(\n                    $scope, $uibModalInstance, LanguageUtilService,\n                    languageCode) {\n                  $scope.languageDescription = (\n                    LanguageUtilService.getAudioLanguageDescription(\n                      languageCode));\n\n                  $scope.reallyDelete = function() {\n                    $uibModalInstance.close();\n                  };\n\n                  $scope.cancel = function() {\n                    $uibModalInstance.dismiss(\'cancel\');\n                    AlertsService.clearWarnings();\n                  };\n                }\n              ]\n            }).result.then(function(result) {\n              $scope.subtitledHtml.deleteAudioTranslation(languageCode);\n              $scope.getOnChangeFn()();\n            });\n          };\n        }\n      ]\n    };\n  }\n]);'

blocks = {}
debug_info = ''