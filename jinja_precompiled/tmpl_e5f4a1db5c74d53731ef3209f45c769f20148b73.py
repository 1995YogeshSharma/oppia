from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/AudioPlayerService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to operate the playback of audio.\n */\n\noppia.factory(\'AudioPlayerService\', [\n  \'$q\', \'$timeout\', \'ngAudio\', \'AssetsBackendApiService\',\n  \'ExplorationContextService\', \'AudioTranslationManagerService\',\n  function(\n      $q, $timeout, ngAudio, AssetsBackendApiService,\n      ExplorationContextService, AudioTranslationManagerService) {\n    var _currentTrackFilename = null;\n    var _currentTrack = null;\n\n    var _load = function(\n        filename, successCallback, errorCallback) {\n      if (filename !== _currentTrackFilename) {\n        AssetsBackendApiService.loadAudio(\n          ExplorationContextService.getExplorationId(), filename)\n          .then(function(loadedAudiofile) {\n            var blobUrl = URL.createObjectURL(loadedAudiofile.data);\n            _currentTrack = ngAudio.load(blobUrl);\n            _currentTrackFilename = filename;\n\n            // ngAudio doesn\'t seem to provide any way of detecting\n            // when native audio object has finished loading. It seems\n            // that after creating an ngAudio object, the native audio\n            // object is asynchronously loaded. So we use a timeout\n            // to grab native audio.\n            // TODO(tjiang11): Look for a better way to handle this.\n            $timeout(function() {\n              // _currentTrack could be null if the learner stops audio\n              // shortly after loading a new card or language. In such\n              // cases, we do not want to attempt setting the \'onended\'\n              // property of the audio.\n              if (_currentTrack !== null) {\n                _currentTrack.audio.onended = function() {\n                  _currentTrack = null;\n                  _currentTrackFilename = null;\n                  AudioTranslationManagerService\n                    .clearSecondaryAudioTranslations();\n                };\n              }\n            }, 100);\n\n            successCallback();\n          }, function(reason) {\n            errorCallback(reason);\n          });\n      }\n    };\n\n    var _play = function() {\n      if (_currentTrack) {\n        _currentTrack.play();\n      }\n    };\n\n    var _pause = function() {\n      if (_currentTrack) {\n        _currentTrack.pause();\n      }\n    };\n\n    var _stop = function() {\n      if (_currentTrack) {\n        _currentTrack.stop();\n        _currentTrackFilename = null;\n        _currentTrack = null;\n      }\n    };\n\n    var _rewind = function(seconds) {\n      if (_currentTrack) {\n        var currentSeconds = _currentTrack.progress * _currentTrack.duration;\n        var rewindedProgress =\n          (currentSeconds - seconds) / _currentTrack.duration;\n        _currentTrack.progress = rewindedProgress;\n      }\n    };\n\n    return {\n      load: function(filename) {\n        return $q(function(resolve, reject) {\n          _load(filename, resolve, reject);\n        });\n      },\n      play: function() {\n        _play();\n      },\n      pause: function() {\n        _pause();\n      },\n      stop: function() {\n        _stop();\n      },\n      rewind: function(seconds) {\n        _rewind(seconds);\n      },\n      getProgress: function() {\n        if (!_currentTrack) {\n          return 0;\n        }\n        return _currentTrack.progress;\n      },\n      setProgress: function(progress) {\n        if (_currentTrack) {\n          _currentTrack.progress = progress;\n        }\n      },\n      isPlaying: function() {\n        return Boolean(_currentTrack && !_currentTrack.paused);\n      },\n      isTrackLoaded: function() {\n        return Boolean(_currentTrack);\n      },\n      clear: function() {\n        _currentTrack = null;\n        _currentTrackFilename = null;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''