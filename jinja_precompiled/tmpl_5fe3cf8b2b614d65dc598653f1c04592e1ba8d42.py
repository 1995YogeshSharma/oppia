from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/alerts/AlertMessageDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for Alert Messages\n */\n\noppia.directive(\'alertMessage\', [function() {\n  return {\n    restrict: \'E\',\n    scope: {\n      getMessage: \'&messageObject\',\n      getMessageIndex: \'&messageIndex\'\n    },\n    template: \'<div class="oppia-alert-message"></div>\',\n    controller: [\n      \'$scope\', \'AlertsService\', \'toastr\',\n      function($scope, AlertsService, toastr) {\n        $scope.AlertsService = AlertsService;\n        $scope.toastr = toastr;\n      }\n    ],\n    link: function(scope) {\n      var message = scope.getMessage();\n      if (message.type === \'info\') {\n        scope.toastr.info(message.content, {\n          timeOut: message.timeout,\n          onHidden: function() {\n            scope.AlertsService.deleteMessage(message);\n          }\n        });\n      } else if (message.type === \'success\') {\n        scope.toastr.success(message.content, {\n          timeOut: message.timeout,\n          onHidden: function() {\n            scope.AlertsService.deleteMessage(message);\n          }\n        });\n      }\n    }\n  };\n}]);'

blocks = {}
debug_info = ''