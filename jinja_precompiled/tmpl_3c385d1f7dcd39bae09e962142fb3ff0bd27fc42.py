from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ValueGeneratorEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directives for the parameter generator editors.\n */\n\n// Individual value generator directives can be found in\n// extensions/value_generators/templates.\n\noppia.directive(\'valueGeneratorEditor\', [\'$compile\', function($compile) {\n  return {\n    restrict: \'E\',\n    scope: {\n      customizationArgs: \'=\',\n      generatorId: \'=\',\n      initArgs: \'=\',\n      objType: \'=\'\n    },\n    link: function(scope, element) {\n      scope.$watch(\'generatorId\', function() {\n        var directiveName = scope.generatorId.replace(\n          /([a-z])([A-Z])/g, \'$1-$2\').toLowerCase();\n        scope.getGeneratorId = function() {\n          return scope.generatorId;\n        };\n        scope.getInitArgs = function() {\n          return scope.initArgs;\n        };\n        scope.getObjType = function() {\n          return scope.objType;\n        };\n        element.html(\n          \'<\' + directiveName +\n          \' customization-args="customizationArgs"\' +\n          \' get-generator-id="getGeneratorId()"\' +\n          \' get-init-args="getInitArgs()"\' +\n          \' get-obj-type="getObjType()"\' +\n          \'></\' + directiveName + \'>\');\n        $compile(element.contents())(scope);\n      });\n    }\n  };\n}]);'

blocks = {}
debug_info = ''