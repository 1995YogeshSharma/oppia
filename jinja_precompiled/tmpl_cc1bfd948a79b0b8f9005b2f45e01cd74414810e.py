from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/TranslationFileHashLoaderService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to load the i18n translation file.\n */\n\noppia.factory(\'TranslationFileHashLoaderService\', [\n  \'$http\', \'$q\', \'UrlInterpolationService\',\n  function($http, $q, UrlInterpolationService) {\n    /* Options object contains:\n     *  prefix: added before key, defined by developer\n     *  key: language key, determined internally by i18n library\n     *  suffix: added after key, defined by developer\n     */\n    return function(options) {\n      var fileUrl = [\n        options.prefix,\n        options.key,\n        options.suffix\n      ].join(\'\');\n      return $http.get(\n        UrlInterpolationService.getStaticAssetUrl(fileUrl)\n      ).then(function(result) {\n        return result.data;\n      }, function() {\n        return $q.reject(options.key);\n      });\n    };\n  }\n]);'

blocks = {}
debug_info = ''