from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/AudioBarDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for a set of audio controls for a specific\n * audio translation in the learner view.\n */\n\noppia.directive(\'audioBar\', [\n  \'UrlInterpolationService\', \'AudioPreloaderService\',\n  function(UrlInterpolationService, AudioPreloaderService) {\n    return {\n      restrict: \'E\',\n      scope: {},\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/exploration_player/\' +\n        \'audio_bar_directive.html\'),\n      controller: [\n        \'$scope\', \'$interval\', \'$timeout\', \'AudioTranslationLanguageService\',\n        \'AudioPlayerService\', \'LanguageUtilService\', \'AssetsBackendApiService\',\n        \'AutogeneratedAudioPlayerService\', \'PlayerPositionService\',\n        \'WindowDimensionsService\', \'AudioTranslationManagerService\',\n        \'EVENT_AUTOPLAY_AUDIO\', \'BrowserCheckerService\',\n        function(\n            $scope, $interval, $timeout, AudioTranslationLanguageService,\n            AudioPlayerService, LanguageUtilService, AssetsBackendApiService,\n            AutogeneratedAudioPlayerService, PlayerPositionService,\n            WindowDimensionsService, AudioTranslationManagerService,\n            EVENT_AUTOPLAY_AUDIO, BrowserCheckerService) {\n          $scope.audioBarIsExpanded = false;\n          $scope.hasPressedPlayButtonAtLeastOnce = false;\n\n          $scope.languagesInExploration =\n            AudioTranslationLanguageService.getLanguageOptionsForDropdown();\n          $scope.selectedLanguage = {\n            value: AudioTranslationLanguageService.getCurrentAudioLanguageCode()\n          };\n\n          $scope.$on(EVENT_AUTOPLAY_AUDIO, function(e, params) {\n            if ($scope.audioBarIsExpanded) {\n              AudioPlayerService.stop();\n              AutogeneratedAudioPlayerService.cancel();\n\n              // We use a timeout to allow for any previous audio to have\n              // their \'onend\' callback called. This is primarily used to\n              // address delays with autogenerated audio callbacks.\n              $timeout(function() {\n                if (params) {\n                  AudioTranslationManagerService.setSecondaryAudioTranslations(\n                    params.audioTranslations,\n                    params.html,\n                    params.componentName);\n                }\n                $scope.onPlayButtonClicked();\n              }, 100);\n            }\n          });\n\n          $scope.isAudioBarAvailable = function() {\n            return (\n              BrowserCheckerService.supportsAudioPlayback() &&\n              $scope.languagesInExploration.length > 0);\n          };\n\n          $scope.onNewLanguageSelected = function() {\n            AudioTranslationLanguageService.setCurrentAudioLanguageCode(\n              $scope.selectedLanguage.value);\n            AudioPlayerService.stop();\n            AudioPlayerService.clear();\n            AutogeneratedAudioPlayerService.cancel();\n            if ($scope.isAudioAvailableInCurrentLanguage() &&\n                !isAutogeneratedLanguageCodeSelected()) {\n              var audioTranslation =\n                getAudioTranslationInCurrentLanguage();\n              AudioPreloaderService.setMostRecentlyRequestedAudioFilename(\n                audioTranslation.filename);\n              AudioPreloaderService.restartAudioPreloader(\n                PlayerPositionService.getCurrentStateName());\n            }\n          };\n\n          $scope.expandAudioBar = function() {\n            $scope.audioBarIsExpanded = true;\n          };\n\n          $scope.collapseAudioBar = function() {\n            $scope.audioBarIsExpanded = false;\n            AudioPlayerService.stop();\n            AudioPlayerService.clear();\n            AutogeneratedAudioPlayerService.cancel();\n          };\n\n          var lastScrollTop = 0;\n\n          $(window).scroll(function(event) {\n            if (WindowDimensionsService.isWindowNarrow()) {\n              updateAudioHeaderPosition();\n            }\n          });\n\n          var updateAudioHeaderPosition = function() {\n            var scrollTop = $(this).scrollTop();\n            var audioHeader = angular.element($(\'.audio-header:first\'));\n            if (scrollTop > lastScrollTop) {\n              audioHeader.addClass(\'audio-bar-nav-up\');\n              if (!$scope.audioBarIsExpanded) {\n                audioHeader.addClass(\'audio-bar-nav-hidden\');\n              }\n            } else if (scrollTop === 0 ||\n                       scrollTop + $(window).height() < $(document).height()) {\n              audioHeader.removeClass(\'audio-bar-nav-up\');\n              audioHeader.removeClass(\'audio-bar-nav-hidden\');\n            }\n            lastScrollTop = scrollTop;\n          };\n\n          var getCurrentAudioLanguageCode = function() {\n            return AudioTranslationLanguageService\n              .getCurrentAudioLanguageCode();\n          };\n\n          $scope.getCurrentAudioLanguageDescription = function() {\n            return AudioTranslationLanguageService\n              .getCurrentAudioLanguageDescription();\n          };\n\n          var getAudioTranslationInCurrentLanguage = function() {\n            return AudioTranslationManagerService.getCurrentAudioTranslations()[\n              AudioTranslationLanguageService.getCurrentAudioLanguageCode()];\n          };\n\n          $scope.isAudioPlaying = function() {\n            return AudioPlayerService.isPlaying() ||\n              AutogeneratedAudioPlayerService.isPlaying();\n          };\n\n          $scope.audioLoadingIndicatorIsShown = false;\n\n          $scope.AudioPlayerService = AudioPlayerService;\n\n          $scope.isAudioAvailableInCurrentLanguage = function() {\n            return Boolean(getAudioTranslationInCurrentLanguage()) ||\n              isAutogeneratedLanguageCodeSelected();\n          };\n\n          $scope.doesCurrentAudioTranslationNeedUpdate = function() {\n            if (!isAutogeneratedLanguageCodeSelected()) {\n              var audioTranslation = getAudioTranslationInCurrentLanguage();\n              return (audioTranslation && audioTranslation.needsUpdate);\n            } else {\n              return false;\n            }\n          };\n\n          var isAutogeneratedLanguageCodeSelected = function() {\n            return AudioTranslationLanguageService\n              .isAutogeneratedLanguageCodeSelected();\n          };\n\n          $scope.onPlayButtonClicked = function() {\n            $scope.hasPressedPlayButtonAtLeastOnce = true;\n            if (isAutogeneratedLanguageCodeSelected()) {\n              playPauseAutogeneratedAudioTranslation();\n            } else {\n              var audioTranslation = getAudioTranslationInCurrentLanguage();\n              if (audioTranslation) {\n                playPauseUploadedAudioTranslation(\n                  getCurrentAudioLanguageCode());\n              }\n            }\n          };\n\n          $scope.track = {\n            progress: function(progressPercentage) {\n              // Returns the current track progress. In addition, sets the\n              // track progress if the progressPercentage argument is defined.\n              if (angular.isDefined(progressPercentage)) {\n                AudioPlayerService.setProgress(progressPercentage / 100);\n              }\n              return AudioPlayerService.getProgress() * 100;\n            }\n          };\n\n          var isCached = function(audioTranslation) {\n            return AssetsBackendApiService.isCached(audioTranslation.filename);\n          };\n\n          var playPauseAudioTranslation = function(languageCode) {\n            if (AudioTranslationLanguageService\n              .isAutogeneratedLanguageCodeSelected()) {\n              playPauseAutogeneratedAudioTranslation();\n            } else {\n              playPauseUploadedAudioTranslation(languageCode);\n            }\n          };\n\n          var playPauseAutogeneratedAudioTranslation = function() {\n            // SpeechSynthesis in Chrome seems to have a bug\n            // where if you pause the utterance, wait for around\n            // 15 or more seconds, then try resuming, nothing\n            // will sound. As a temporary fix, just restart the\n            // utterance from the beginning instead of resuming.\n            if (AutogeneratedAudioPlayerService.isPlaying()) {\n              AutogeneratedAudioPlayerService.cancel();\n            } else {\n              AutogeneratedAudioPlayerService.play(\n                AudioTranslationManagerService\n                  .getCurrentHtmlForAutogeneratedAudio(),\n                AudioTranslationLanguageService\n                  .getSpeechSynthesisLanguageCode(),\n                function() {\n                  // Used to update bindings to show a silent speaker after\n                  // autogenerated audio has finished playing.\n                  $scope.$applyAsync();\n                  AudioTranslationManagerService\n                    .clearSecondaryAudioTranslations();\n                });\n            }\n          };\n\n          var playPauseUploadedAudioTranslation = function(languageCode) {\n            if (!AudioPlayerService.isPlaying()) {\n              if (AudioPlayerService.isTrackLoaded()) {\n                AudioPlayerService.play();\n              } else {\n                loadAndPlayAudioTranslation();\n              }\n            } else {\n              AudioPlayerService.pause();\n            }\n          };\n\n          var playCachedAudioTranslation = function(audioFilename) {\n            AudioPlayerService.load(audioFilename)\n              .then(function() {\n                $scope.audioLoadingIndicatorIsShown = false;\n                AudioPlayerService.play();\n              });\n          };\n\n          /**\n           * Called when an audio file finishes loading.\n           * @param {string} audioFilename - Filename of the audio file that\n           *                                 finished loading.\n           */\n          var onFinishedLoadingAudio = function(audioFilename) {\n            var mostRecentlyRequestedAudioFilename =\n              AudioPreloaderService.getMostRecentlyRequestedAudioFilename();\n            if ($scope.audioLoadingIndicatorIsShown &&\n                audioFilename === mostRecentlyRequestedAudioFilename) {\n              playCachedAudioTranslation(audioFilename);\n            }\n          };\n\n          AudioPreloaderService.setAudioLoadedCallback(onFinishedLoadingAudio);\n\n          var loadAndPlayAudioTranslation = function() {\n            $scope.audioLoadingIndicatorIsShown = true;\n            var audioTranslation = getAudioTranslationInCurrentLanguage();\n            AudioPreloaderService.setMostRecentlyRequestedAudioFilename(\n              audioTranslation.filename);\n            if (audioTranslation) {\n              if (isCached(audioTranslation)) {\n                playCachedAudioTranslation(\n                  audioTranslation.filename);\n              } else if (!AudioPreloaderService.isLoadingAudioFile(\n                audioTranslation.filename)) {\n                AudioPreloaderService.restartAudioPreloader(\n                  PlayerPositionService.getCurrentStateName());\n              }\n            }\n          };\n        }]\n    };\n  }\n]);'

blocks = {}
debug_info = ''