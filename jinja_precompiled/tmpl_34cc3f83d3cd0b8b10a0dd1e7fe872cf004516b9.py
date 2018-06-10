from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/utilities/BrowserCheckerService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Utility service for checking web browser type.\n */\n\noppia.factory(\'BrowserCheckerService\', [\n  \'AUTOGENERATED_AUDIO_LANGUAGES\',\n  function(AUTOGENERATED_AUDIO_LANGUAGES) {\n    // For details on the reliability of this check, see\n    // https://stackoverflow.com/questions/9847580/\n    // how-to-detect-safari-chrome-ie-firefox-and-opera-browser#answer-9851769\n    var isSafari = /constructor/i.test(window.HTMLElement) || (\n      function(p) {\n        return p.toString() === \'[object SafariRemoteNotification]\';\n      })(\n      !window.safari ||\n        (typeof safari !== \'undefined\' && safari.pushNotification)\n    );\n\n    var _supportsSpeechSynthesis = function() {\n      supportLang = false;\n      if (window.hasOwnProperty(\'speechSynthesis\')) {\n        speechSynthesis.getVoices().forEach(function(voice) {\n          AUTOGENERATED_AUDIO_LANGUAGES.forEach(function(audioLanguage) {\n            if (voice.lang === audioLanguage.speech_synthesis_code ||\n                (_isMobileDevice() &&\n                voice.lang === audioLanguage.speech_synthesis_code_mobile)) {\n              supportLang = true;\n            }\n          });\n        });\n      }\n      return supportLang;\n    };\n\n    var _isMobileDevice = function() {\n      var userAgent = navigator.userAgent || navigator.vendor || window.opera;\n      return userAgent.match(/iPhone/i) || userAgent.match(/Android/i);\n    };\n\n    return {\n      supportsSpeechSynthesis: function() {\n        return _supportsSpeechSynthesis();\n      },\n      supportsAudioPlayback: function() {\n        return !isSafari;\n      },\n      isMobileDevice: function() {\n        return _isMobileDevice();\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''