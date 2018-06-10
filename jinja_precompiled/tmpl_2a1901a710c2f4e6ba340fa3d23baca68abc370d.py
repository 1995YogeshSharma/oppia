from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/LearnerParamsService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview A service that maintains the current set of parameters for the\n * learner.\n */\n\noppia.factory(\'LearnerParamsService\', [function() {\n  var _paramDict = {};\n\n  return {\n    // TODO(sll): Forbid use of \'answer\', \'choices\' as possible keys.\n    init: function(initParamSpecs) {\n      // The initParamSpecs arg is a dict mapping the parameter names used in\n      // the exploration to their default values.\n      _paramDict = angular.copy(initParamSpecs);\n    },\n    getValue: function(paramName) {\n      if (!_paramDict.hasOwnProperty(paramName)) {\n        throw \'Invalid parameter name: \' + paramName;\n      } else {\n        return angular.copy(_paramDict[paramName]);\n      }\n    },\n    setValue: function(paramName, newParamValue) {\n      // TODO(sll): Currently, all parameters are strings. In the future, we\n      // will need to maintain information about parameter types.\n      if (!_paramDict.hasOwnProperty(paramName)) {\n        throw \'Cannot set unknown parameter: \' + paramName;\n      } else {\n        _paramDict[paramName] = String(newParamValue);\n      }\n    },\n    getAllParams: function() {\n      return angular.copy(_paramDict);\n    }\n  };\n}]);'

blocks = {}
debug_info = ''