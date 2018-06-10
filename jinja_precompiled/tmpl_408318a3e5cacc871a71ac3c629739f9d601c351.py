from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/feedback_tab/ThreadStatusDisplayService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service that provides information about how to display the\n * status label for a thread in the feedback tab of the exploration editor.\n */\n\noppia.factory(\'ThreadStatusDisplayService\', [function() {\n  var _STATUS_CHOICES = [{\n    id: \'open\',\n    text: \'Open\'\n  }, {\n    id: \'fixed\',\n    text: \'Fixed\'\n  }, {\n    id: \'ignored\',\n    text: \'Ignored\'\n  }, {\n    id: \'compliment\',\n    text: \'Compliment\'\n  }, {\n    id: \'not_actionable\',\n    text: \'Not Actionable\'\n  }];\n\n  return {\n    STATUS_CHOICES: angular.copy(_STATUS_CHOICES),\n    getLabelClass: function(status) {\n      if (status === \'open\') {\n        return \'label label-info\';\n      } else {\n        return \'label label-default\';\n      }\n    },\n    getHumanReadableStatus: function(status) {\n      for (var i = 0; i < _STATUS_CHOICES.length; i++) {\n        if (_STATUS_CHOICES[i].id === status) {\n          return _STATUS_CHOICES[i].text;\n        }\n      }\n      return \'\';\n    }\n  };\n}]);'

blocks = {}
debug_info = ''