from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/utilities/UrlInterpolationService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to construct URLs by inserting variables within them as\n * necessary to have a fully-qualified URL.\n */\n\noppia.factory(\'UrlInterpolationService\', [\n  \'AlertsService\', \'UtilsService\', function(AlertsService, UtilsService) {\n    var validateResourcePath = function(resourcePath) {\n      if (!resourcePath) {\n        AlertsService.fatalWarning(\'Empty path passed in method.\');\n      }\n\n      var RESOURCE_PATH_STARTS_WITH_FORWARD_SLASH = /^\\//;\n      // Ensure that resourcePath starts with a forward slash.\n      if (!resourcePath.match(RESOURCE_PATH_STARTS_WITH_FORWARD_SLASH)) {\n        AlertsService.fatalWarning(\n          \'Path must start with \\\'\\/\\\': \\\'\' + resourcePath + \'\\\'.\');\n      }\n    };\n\n    /**\n     * Given a resource path relative to subfolder in /,\n     * returns resource path with cache slug.\n     */\n    var getUrlWithSlug = function(resourcePath) {\n      if (!GLOBALS.DEV_MODE) {\n        if (hashes[resourcePath]) {\n          var index = resourcePath.lastIndexOf(\'.\');\n          return (resourcePath.slice(0, index) + \'.\' + hashes[resourcePath] +\n                  resourcePath.slice(index));\n        }\n      }\n      return resourcePath;\n    };\n\n    /**\n     * Given a resource path relative to subfolder in /,\n     * returns complete resource path with cache slug and prefixed with url\n     * depending on dev/prod mode.\n     */\n    var getCompleteUrl = function(prefix, path) {\n      return GLOBALS.ASSET_DIR_PREFIX + prefix + getUrlWithSlug(path);\n    };\n\n    /**\n     * Given a resource path relative to extensions folder,\n     * returns the complete url path to that resource.\n     */\n    var getExtensionResourceUrl = function(resourcePath) {\n      validateResourcePath(resourcePath);\n      return getCompleteUrl(\'/extensions\', resourcePath);\n    };\n\n    return {\n      /**\n       * Given a formatted URL, interpolates the URL by inserting values the URL\n       * needs using the interpolationValues object. For example, urlTemplate\n       * might be:\n       *\n       *   /createhandler/resolved_answers/<exploration_id>/<escaped_state_name>\n       *\n       * interpolationValues is an object whose keys are variables within the\n       * URL. For the above example, interpolationValues may look something\n       * like:\n       *\n       *   { \'exploration_id\': \'0\', \'escaped_state_name\': \'InputBinaryNumber\' }\n       *\n       * If a URL requires a value which is not keyed within the\n       * interpolationValues object, this will return null.\n       */\n      interpolateUrl: function(urlTemplate, interpolationValues) {\n        if (!urlTemplate) {\n          AlertsService.fatalWarning(\n            \'Invalid or empty URL template passed in: \\\'\' + urlTemplate + \'\\\'\');\n          return null;\n        }\n\n        // http://stackoverflow.com/questions/4775722\n        if (!(interpolationValues instanceof Object) || (\n          Object.prototype.toString.call(\n            interpolationValues) === \'[object Array]\')) {\n          AlertsService.fatalWarning(\n            \'Expected an object of interpolation values to be passed into \' +\n            \'interpolateUrl.\');\n          return null;\n        }\n\n        // Valid pattern: <alphanum>\n        var INTERPOLATION_VARIABLE_REGEX = /<(\\w+)>/;\n\n        // Invalid patterns: <<stuff>>, <stuff>>>, <>\n        var EMPTY_VARIABLE_REGEX = /<>/;\n        var INVALID_VARIABLE_REGEX = /(<{2,})(\\w*)(>{2,})/;\n\n        // Parameter values can only contain alphanumerical characters, spaces,\n        // hyphens, underscores, periods or the equal to symbol.\n        var VALID_URL_PARAMETER_VALUE_REGEX = /^(\\w| |_|-|[.]|=)+$/;\n\n        if (urlTemplate.match(INVALID_VARIABLE_REGEX) ||\n            urlTemplate.match(EMPTY_VARIABLE_REGEX)) {\n          AlertsService.fatalWarning(\n            \'Invalid URL template received: \\\'\' + urlTemplate + \'\\\'\');\n          return null;\n        }\n\n        var escapedInterpolationValues = {};\n        for (var varName in interpolationValues) {\n          var value = interpolationValues[varName];\n          if (!UtilsService.isString(value)) {\n            AlertsService.fatalWarning(\n              \'Parameters passed into interpolateUrl must be strings.\');\n            return null;\n          }\n\n          // Ensure the value is valid.\n          if (!value.match(VALID_URL_PARAMETER_VALUE_REGEX)) {\n            AlertsService.fatalWarning(\n              \'Parameter values passed into interpolateUrl must only contain \' +\n              \'alphanumerical characters, hyphens, underscores or spaces: \\\'\' +\n              value + \'\\\'\');\n            return null;\n          }\n\n          escapedInterpolationValues[varName] = encodeURIComponent(value);\n        }\n\n        // Ensure the URL has no nested brackets (which would lead to\n        // indirection in the interpolated variables).\n        var filledUrl = angular.copy(urlTemplate);\n        var match = filledUrl.match(INTERPOLATION_VARIABLE_REGEX);\n        while (match) {\n          var varName = match[1];\n          if (!escapedInterpolationValues.hasOwnProperty(varName)) {\n            AlertsService.fatalWarning(\'Expected variable \\\'\' + varName +\n              \'\\\' when interpolating URL.\');\n            return null;\n          }\n          filledUrl = filledUrl.replace(\n            INTERPOLATION_VARIABLE_REGEX,\n            escapedInterpolationValues[varName]);\n          match = filledUrl.match(INTERPOLATION_VARIABLE_REGEX);\n        }\n        return filledUrl;\n      },\n\n      /**\n       * Given an image path relative to /assets/images folder,\n       * returns the complete url path to that image.\n       */\n      getStaticImageUrl: function(imagePath) {\n        validateResourcePath(imagePath);\n        return getCompleteUrl(\'/assets\', \'/images\' + imagePath);\n      },\n\n      /**\n       * Given a path relative to /assets folder, returns the complete url path\n       * to that asset.\n       */\n      getStaticAssetUrl: function(assetPath) {\n        validateResourcePath(assetPath);\n        return getCompleteUrl(\'/assets\', assetPath);\n      },\n\n      /**\n       * Given an interaction id, returns the complete url path to\n       * the thumbnail image for the interaction.\n       */\n      getInteractionThumbnailImageUrl: function(interactionId) {\n        if (!interactionId) {\n          AlertsService.fatalWarning(\n            \'Empty interactionId passed in getInteractionThumbnailImageUrl.\');\n        }\n        return getExtensionResourceUrl(\'/interactions/\' + interactionId +\n          \'/static/\' + interactionId + \'.png\');\n      },\n\n      /**\n       * Given a directive path relative to head folder,\n       * returns the complete url path to that directive.\n       */\n      getDirectiveTemplateUrl: function(path) {\n        validateResourcePath(path);\n        return GLOBALS.TEMPLATE_DIR_PREFIX + getUrlWithSlug(path);\n      },\n\n      getExtensionResourceUrl: getExtensionResourceUrl,\n\n      _getUrlWithSlug: getUrlWithSlug,\n      _getCompleteUrl: getCompleteUrl\n    };\n  }\n]);'

blocks = {}
debug_info = ''