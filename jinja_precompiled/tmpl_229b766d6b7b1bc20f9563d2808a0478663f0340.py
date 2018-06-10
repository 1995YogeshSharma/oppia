from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/utilities/StopwatchObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Object factory for creating stopwatches.\n */\n\n// A simple service that provides stopwatch instances. Each stopwatch can be\n// independently reset and queried for the current time.\noppia.factory(\'StopwatchObjectFactory\', [\'$log\', function($log) {\n  var Stopwatch = function() {\n    this.startTime = null;\n  };\n\n  Stopwatch.prototype = {\n    _getCurrentTime: function() {\n      return Date.now();\n    },\n    reset: function() {\n      this.startTime = this._getCurrentTime();\n    },\n    getTimeInSecs: function() {\n      if (this.startTime === null) {\n        $log.error(\n          \'Tried to retrieve the elapsed time, but no start time was set.\');\n        return null;\n      }\n      return (this._getCurrentTime() - this.startTime) / 1000;\n    }\n  };\n\n  return {\n    create: function() {\n      return new Stopwatch();\n    }\n  };\n}]);'

blocks = {}
debug_info = ''