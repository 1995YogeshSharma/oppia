from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/SolutionValidityService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n// Service for keeping track of solution validity.\noppia.factory(\'SolutionValidityService\', [\n  function() {\n    return {\n      init: function(stateNames) {\n        this.solutionValidities = {};\n        var self = this;\n        stateNames.forEach(function(stateName) {\n          self.solutionValidities[stateName] = true;\n        });\n      },\n      onRenameState: function(newStateName, oldStateName) {\n        this.solutionValidities[newStateName] =\n          this.solutionValidities[oldStateName];\n        this.deleteSolutionValidity(oldStateName);\n      },\n      updateValidity: function(stateName, solutionIsValid) {\n        this.solutionValidities[stateName] = solutionIsValid;\n      },\n      isSolutionValid: function(stateName) {\n        if (this.solutionValidities.hasOwnProperty(stateName)) {\n          return this.solutionValidities[stateName];\n        }\n      },\n      deleteSolutionValidity: function(stateName) {\n        delete this.solutionValidities[stateName];\n      },\n      getAllValidities: function() {\n        return this.solutionValidities;\n      }\n    };\n  }]);'

blocks = {}
debug_info = ''