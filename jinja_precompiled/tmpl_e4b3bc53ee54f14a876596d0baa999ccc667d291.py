from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/TranslationLanguageServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit test for the Translation language service.\n */\n\ndescribe(\'Translation language service\', function() {\n  beforeEach(module(\'oppia\', function($provide) {\n    $provide.value(\'LanguageUtilService\', {\n      getAllAudioLanguageCodes: function() {\n        return [\'en\', \'hi\'];\n      }\n    });\n  }));\n\n  describe(\'Translation language service\', function() {\n    var tls = null;\n\n    beforeEach(inject(function($injector) {\n      tls = $injector.get(\'TranslationLanguageService\');\n    }));\n\n    it(\'should correctly set and get state names\', function() {\n      tls.setActiveLanguageCode(\'en\');\n      expect(tls.getActiveLanguageCode()).toBe(\'en\');\n    });\n\n    it(\'should not allow invalid state names to be set\', function() {\n      tls.setActiveLanguageCode(\'eng\');\n      expect(tls.getActiveLanguageCode()).toBeNull();\n\n      tls.setActiveLanguageCode(null);\n      expect(tls.getActiveLanguageCode()).toBeNull();\n    });\n  });\n});'

blocks = {}
debug_info = ''