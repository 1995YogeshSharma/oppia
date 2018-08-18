from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/QuestionCreationService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to create the question.\n */\n\noppia.factory(\'QuestionCreationService\', [\n  \'$http\', \'$q\', \'UrlInterpolationService\',\n  function($http, $q, UrlInterpolationService) {\n    var QUESTION_CREATOR_URL = \'/question_editor_handler/create_new\';\n\n    var _createNew = function(\n        backendQuestionDict, successCallback, errorCallback) {\n      var postData = {\n        question_dict: backendQuestionDict\n      };\n      $http.post(QUESTION_CREATOR_URL, postData).then(function(response) {\n        if (successCallback) {\n          successCallback();\n        }\n      }, function(errorResponse) {\n        if (errorCallback) {\n          errorCallback(errorResponse.data);\n        }\n      });\n    };\n\n    return {\n      createNew: function(backendQuestionDict) {\n        return $q(function(resolve, reject) {\n          _createNew(backendQuestionDict, resolve, reject);\n        });\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''