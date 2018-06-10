from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/DateTimeFormatServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit test for DateTimeFormatService.\n */\n\ndescribe(\'Datetime Formatter\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'datetimeformatter\', function() {\n    // This corresponds to Fri, 21 Nov 2014 09:45:00 GMT.\n    var NOW_MILLIS = 1416563100000;\n    var df = null;\n    var OldDate = Date;\n\n    beforeEach(inject(function($injector) {\n      df = $injector.get(\'DateTimeFormatService\');\n\n      // Mock Date() to give a time of NOW_MILLIS in GMT. (Unfortunately, there\n      // doesn\'t seem to be a good way to set the timezone locale directly.)\n      spyOn(window, \'Date\').and.callFake(function() {\n        return new OldDate(NOW_MILLIS);\n      });\n    }));\n\n    it(\'should correctly indicate recency\', function() {\n      // 1 second ago is recent.\n      expect(df.isRecent(NOW_MILLIS - 1)).toBe(true);\n      // 72 hours ago is recent.\n      expect(df.isRecent(NOW_MILLIS - 72 * 60 * 60 * 1000)).toBe(true);\n      // 8 days ago is not recent.\n      expect(df.isRecent(NOW_MILLIS - 8 * 24 * 60 * 60 * 1000)).toBe(false);\n    });\n  });\n});'

blocks = {}
debug_info = ''