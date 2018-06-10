from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/ObjectEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directives for the object editors.\n */\n\n// Individual object editor directives are in extensions/objects/templates.\n\noppia.directive(\'objectEditor\', [\'$compile\', \'$log\', function($compile, $log) {\n  return {\n    scope: {\n      alwaysEditable: \'@\',\n      initArgs: \'=\',\n      isEditable: \'@\',\n      objType: \'@\',\n      value: \'=\'\n    },\n    link: function(scope, element) {\n      // Converts a camel-cased string to a lower-case hyphen-separated string.\n      var directiveName = scope.objType.replace(\n        /([a-z])([A-Z])/g, \'$1-$2\').toLowerCase();\n      if (directiveName) {\n        element.html(\n          \'<\' + directiveName + \'-editor></\' + directiveName + \'-editor>\');\n        $compile(element.contents())(scope);\n      } else {\n        $log.error(\'Error in objectEditor: no editor type supplied.\');\n      }\n    },\n    restrict: \'E\'\n  };\n}]);'

blocks = {}
debug_info = ''