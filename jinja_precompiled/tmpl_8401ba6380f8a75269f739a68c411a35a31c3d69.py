from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/HintAndSolutionModalService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for showing the hint and solution modals.\n */\n\noppia.factory(\'HintAndSolutionModalService\', [\n  \'$uibModal\', \'UrlInterpolationService\', \'HintsAndSolutionManagerService\',\n  \'ExplorationPlayerService\', \'PlayerPositionService\',\n  \'AudioTranslationManagerService\', \'AudioPlayerService\',\n  \'EVENT_AUTOPLAY_AUDIO\', \'COMPONENT_NAME_HINT\',\n  \'COMPONENT_NAME_SOLUTION\', \'AutogeneratedAudioPlayerService\',\n  function(\n      $uibModal, UrlInterpolationService, HintsAndSolutionManagerService,\n      ExplorationPlayerService, PlayerPositionService,\n      AudioTranslationManagerService, AudioPlayerService,\n      EVENT_AUTOPLAY_AUDIO, COMPONENT_NAME_HINT,\n      COMPONENT_NAME_SOLUTION, AutogeneratedAudioPlayerService) {\n    return {\n      displayHintModal: function(index) {\n        return $uibModal.open({\n          templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n            \'/pages/exploration_player/hint_and_solution_modal_directive.html\'),\n          backdrop: \'static\',\n          controller: [\n            \'$scope\', \'$rootScope\', \'$uibModalInstance\',\n            function($scope, $rootScope, $uibModalInstance) {\n              $scope.isHint = true;\n              $scope.hint = HintsAndSolutionManagerService.displayHint(index);\n              AudioTranslationManagerService.setSecondaryAudioTranslations(\n                $scope.hint.getBindableAudioTranslations(),\n                $scope.hint.getHtml(),\n                COMPONENT_NAME_HINT);\n              $rootScope.$broadcast(EVENT_AUTOPLAY_AUDIO);\n              $scope.closeModal = function() {\n                AudioPlayerService.stop();\n                AutogeneratedAudioPlayerService.cancel();\n                AudioTranslationManagerService\n                  .clearSecondaryAudioTranslations();\n                $uibModalInstance.dismiss(\'cancel\');\n              };\n            }\n          ]\n        });\n      },\n      displaySolutionModal: function() {\n        return $uibModal.open({\n          templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n            \'/pages/exploration_player/hint_and_solution_modal_directive.html\'),\n          backdrop: \'static\',\n          controller: [\n            \'$scope\', \'$rootScope\', \'$uibModalInstance\',\n            function($scope, $rootScope, $uibModalInstance) {\n              $scope.isHint = false;\n              var solution = HintsAndSolutionManagerService.displaySolution();\n              AudioTranslationManagerService.setSecondaryAudioTranslations(\n                solution.explanation.getBindableAudioTranslations(),\n                solution.explanation.getHtml(),\n                COMPONENT_NAME_SOLUTION);\n              $rootScope.$broadcast(EVENT_AUTOPLAY_AUDIO);\n              var interaction = ExplorationPlayerService.getInteraction(\n                PlayerPositionService.getCurrentStateName());\n              $scope.shortAnswerHtml = solution.getOppiaShortAnswerResponseHtml(\n                interaction);\n              $scope.solutionExplanationHtml =\n                solution.getOppiaSolutionExplanationResponseHtml();\n              $scope.closeModal = function() {\n                AudioPlayerService.stop();\n                AutogeneratedAudioPlayerService.cancel();\n                AudioTranslationManagerService\n                  .clearSecondaryAudioTranslations();\n                $uibModalInstance.dismiss(\'cancel\');\n              };\n            }\n          ]\n        });\n      },\n      displaySolutionInterstitialModal: function() {\n        return $uibModal.open({\n          templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n            \'/pages/exploration_player/\' +\n            \'solution_interstitial_modal_directive.html\'),\n          backdrop: \'static\',\n          controller: [\n            \'$scope\', \'$uibModalInstance\',\n            function($scope, $uibModalInstance) {\n              $scope.continueToSolution = function() {\n                $uibModalInstance.close();\n              };\n\n              $scope.cancel = function() {\n                $uibModalInstance.dismiss(\'cancel\');\n              };\n            }\n          ]\n        });\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''