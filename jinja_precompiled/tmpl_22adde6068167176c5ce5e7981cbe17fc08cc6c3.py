from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/AudioPreloaderService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to preload audio into AssetsBackendApiService\'s cache.\n */\n\noppia.factory(\'AudioPreloaderService\', [\n  \'$uibModal\', \'ExplorationContextService\', \'AssetsBackendApiService\',\n  \'ExplorationPlayerStateService\', \'UrlInterpolationService\',\n  \'AudioTranslationLanguageService\', \'LanguageUtilService\',\n  \'ComputeGraphService\',\n  function($uibModal, ExplorationContextService, AssetsBackendApiService,\n      ExplorationPlayerStateService, UrlInterpolationService,\n      AudioTranslationLanguageService, LanguageUtilService,\n      ComputeGraphService) {\n    var MAX_NUM_AUDIO_FILES_TO_DOWNLOAD_SIMULTANEOUSLY = 3;\n\n    var _filenamesOfAudioCurrentlyDownloading = [];\n    var _filenamesOfAudioToBeDownloaded = [];\n    var _exploration = null;\n    var _audioLoadedCallback = null;\n    var _mostRecentlyRequestedAudioFilename = null;\n\n    var _init = function(exploration) {\n      _exploration = exploration;\n    };\n\n    var _getAudioFilenamesInBfsOrder = function(sourceStateName) {\n      var languageCode = AudioTranslationLanguageService\n        .getCurrentAudioLanguageCode();\n      var stateNamesInBfsOrder =\n        ComputeGraphService.computeBfsTraversalOfStates(\n          _exploration.getInitialState().name,\n          _exploration.getStates(),\n          sourceStateName);\n      var audioFilenames = [];\n      allAudioTranslations = _exploration.getAllAudioTranslations(\n        languageCode);\n      stateNamesInBfsOrder.forEach(function(stateName) {\n        var allAudioTranslationsForState = allAudioTranslations[stateName];\n        allAudioTranslationsForState.forEach(function(audioTranslation) {\n          audioFilenames.push(audioTranslation.filename);\n        });\n      });\n      return audioFilenames;\n    };\n\n    var _loadAudio = function(audioFilename) {\n      AssetsBackendApiService.loadAudio(\n        ExplorationContextService.getExplorationId(), audioFilename\n      ).then(function(loadedAudio) {\n        for (var i = 0;\n          i < _filenamesOfAudioCurrentlyDownloading.length; i++) {\n          if (_filenamesOfAudioCurrentlyDownloading[i] ===\n              loadedAudio.filename) {\n            _filenamesOfAudioCurrentlyDownloading.splice(i, 1);\n            break;\n          }\n        }\n        if (_filenamesOfAudioToBeDownloaded.length > 0) {\n          var nextAudioFilename = _filenamesOfAudioToBeDownloaded.shift();\n          _filenamesOfAudioCurrentlyDownloading.push(nextAudioFilename);\n          _loadAudio(nextAudioFilename);\n        }\n        if (_audioLoadedCallback) {\n          _audioLoadedCallback(loadedAudio.filename);\n        }\n      });\n    };\n\n    var _kickOffAudioPreloader = function(sourceStateName) {\n      _filenamesOfAudioToBeDownloaded =\n        _getAudioFilenamesInBfsOrder(sourceStateName);\n      while (_filenamesOfAudioCurrentlyDownloading.length <\n          MAX_NUM_AUDIO_FILES_TO_DOWNLOAD_SIMULTANEOUSLY &&\n          _filenamesOfAudioToBeDownloaded.length > 0) {\n        var audioFilename = _filenamesOfAudioToBeDownloaded.shift();\n        _filenamesOfAudioCurrentlyDownloading.push(audioFilename);\n        _loadAudio(audioFilename);\n      }\n    };\n\n    var _cancelPreloading = function() {\n      AssetsBackendApiService.abortAllCurrentAudioDownloads();\n      _filenamesOfAudioCurrentlyDownloading = [];\n    };\n\n    return {\n      init: function(exploration) {\n        _init(exploration);\n      },\n      kickOffAudioPreloader: function(sourceStateName) {\n        _kickOffAudioPreloader(sourceStateName);\n      },\n      isLoadingAudioFile: function(filename) {\n        return _filenamesOfAudioCurrentlyDownloading.indexOf(filename) !== -1;\n      },\n      restartAudioPreloader: function(sourceStateName) {\n        _cancelPreloading();\n        _kickOffAudioPreloader(sourceStateName);\n      },\n      setAudioLoadedCallback: function(audioLoadedCallback) {\n        _audioLoadedCallback = audioLoadedCallback;\n      },\n      setMostRecentlyRequestedAudioFilename: function(\n          mostRecentlyRequestedAudioFilename) {\n        _mostRecentlyRequestedAudioFilename =\n          mostRecentlyRequestedAudioFilename;\n      },\n      clearMostRecentlyRequestedAudioFilename: function() {\n        _mostRecentlyRequestedAudioFilename = null;\n      },\n      getMostRecentlyRequestedAudioFilename: function() {\n        return _mostRecentlyRequestedAudioFilename;\n      },\n      getFilenamesOfAudioCurrentlyDownloading: function() {\n        return _filenamesOfAudioCurrentlyDownloading;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''