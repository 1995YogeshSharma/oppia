from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/SchemaBasedIntEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for a schema-based editor for integers.\n */\n\noppia.directive(\'schemaBasedIntEditor\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      scope: {\n        localValue: \'=\',\n        isDisabled: \'&\',\n        validators: \'&\',\n        labelForFocusTarget: \'&\',\n        onInputBlur: \'=\',\n        onInputFocus: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/forms/schema_editors/\' +\n        \'schema_based_int_editor_directive.html\'),\n      restrict: \'E\',\n      controller: [\n        \'$scope\', function($scope) {\n          if ($scope.localValue === undefined) {\n            $scope.localValue = 0;\n          }\n\n          $scope.onKeypress = function(evt) {\n            if (evt.keyCode === 13) {\n              $scope.$emit(\'submittedSchemaBasedIntForm\');\n            }\n          };\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''