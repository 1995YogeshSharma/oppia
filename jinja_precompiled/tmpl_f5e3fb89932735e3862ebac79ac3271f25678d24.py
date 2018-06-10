from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/HtmlSelectDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for the select supporting html\n */\n\n// This directive allows user to put html into select\'s options.\n// \'options\' should be an array of objects containing attributes \'id\' and \'val\'\n// Attribute \'val\' is presented to the user. After user selection, the\n// corresponding attribute \'id\' is assigned to \'selection\'\n\noppia.directive(\'htmlSelect\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        options: \'=\',\n        selection: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/forms/html_select_directive.html\'),\n      controller: [\'$scope\', function($scope) {\n        $scope.select = function(id) {\n          $scope.selection = id;\n        };\n\n        $scope.getSelectionIndex = function() {\n          for (var index = 0; index < $scope.options.length; index++) {\n            if ($scope.options[index].id === $scope.selection) {\n              return index;\n            }\n          }\n        };\n      }]\n    };\n  }\n]);'

blocks = {}
debug_info = ''