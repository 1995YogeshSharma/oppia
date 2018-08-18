from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/GenerateContentIdServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for GenerateContentIdService.\n */\n\ndescribe(\'GenerateContentIdService\', function() {\n  beforeEach(module(\'oppia\', function($provide) {\n    $provide.value(\'COMPONENT_NAME_FEEDBACK\', \'feedback\');\n    $provide.value(\'COMPONENT_NAME_HINT\', \'hint\');\n  }));\n  var gcis = null;\n  var citatDict = {\n    content: {},\n    default_outcome: {},\n    feedback_1: {},\n    hint_1: {},\n    solution: {}\n  };\n\n  beforeEach(inject(function($injector) {\n    gcis = $injector.get(\'GenerateContentIdService\');\n    scitat = $injector.get(\'StateContentIdsToAudioTranslationsService\');\n    citatof = $injector.get(\'ContentIdsToAudioTranslationsObjectFactory\');\n    scitat.displayed = citatof.createFromBackendDict(citatDict);\n  }));\n\n  it(\'should generate content id for new feedbacks\', function(){\n    expect(gcis.getNextId(\'feedback\')).toEqual(\'feedback_2\');\n  });\n\n  it(\'should generate content id for new hint\', function(){\n    expect(gcis.getNextId(\'hint\')).toEqual(\'hint_2\');\n  });\n\n  it(\'should throw error for unknown content id\', function(){\n    expect(function() {\n      gcis.getNextId(\'xyz\');\n    }).toThrowError(\'Unknown component name provided.\');\n  });\n});'

blocks = {}
debug_info = ''