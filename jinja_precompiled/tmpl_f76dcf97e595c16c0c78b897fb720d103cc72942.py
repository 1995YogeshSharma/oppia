from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/collection/SearchExplorationsBackendApiService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to search explorations metadata.\n */\n\noppia.factory(\'SearchExplorationsBackendApiService\', [\n  \'$http\', \'$q\', \'AlertsService\', \'SEARCH_EXPLORATION_URL_TEMPLATE\',\n  \'UrlInterpolationService\',\n  function(\n      $http, $q, AlertsService, SEARCH_EXPLORATION_URL_TEMPLATE,\n      UrlInterpolationService) {\n    var _fetchExplorations = function(\n        searchQuery, successCallback, errorCallback) {\n      queryUrl = UrlInterpolationService.interpolateUrl(\n        SEARCH_EXPLORATION_URL_TEMPLATE, {\n          query: btoa(searchQuery)\n        }\n      );\n      $http.get(queryUrl).then(function(response) {\n        successCallback(response.data);\n      }, function(errorResponse) {\n        errorCallback(errorResponse.data);\n      });\n    };\n    return {\n      /**\n       * Returns exploration\'s metadata dict, given a search query. Search\n       * queries are tokens that will be matched against exploration\'s title\n       * and objective.\n       */\n      fetchExplorations: function(searchQuery) {\n        return $q(function(resolve, reject) {\n          _fetchExplorations(searchQuery, resolve, reject);\n        });\n      }\n    };\n  }]);'

blocks = {}
debug_info = ''