from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/DebouncerService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for debouncing function calls.\n */\n\noppia.factory(\'DebouncerService\', [function() {\n  return {\n    // Returns a function that will not be triggered as long as it continues to\n    // be invoked. The function only gets executed after it stops being called\n    // for `wait` milliseconds.\n    debounce: function(func, millisecsToWait) {\n      var timeout;\n      var context = this;\n      var args = arguments;\n      var timestamp;\n      var result;\n\n      var later = function() {\n        var last = new Date().getTime() - timestamp;\n        if (last < millisecsToWait) {\n          timeout = setTimeout(later, millisecsToWait - last);\n        } else {\n          timeout = null;\n          result = func.apply(context, args);\n          if (!timeout) {\n            context = null;\n            args = null;\n          }\n        }\n      };\n\n      return function() {\n        context = this;\n        args = arguments;\n        timestamp = new Date().getTime();\n        if (!timeout) {\n          timeout = setTimeout(later, millisecsToWait);\n        }\n        return result;\n      };\n    }\n  };\n}]);'

blocks = {}
debug_info = ''