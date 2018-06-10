from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/PredictionAlgorithmRegistryService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for mapping algorithmId to PredictionAlgorithmService.\n */\n\noppia.factory(\'PredictionAlgorithmRegistryService\', [\n  \'$injector\', function($injector) {\n    /**\n     * This mapping needs to be updated whenever a new prediction service needs\n     * to be added for classification. The mapping is from algorithmId to a\n     * list of objects. The mapping should be of the type:\n     * {\n     *   algorithmId: {\n     *     dataSchemaVersion: predictionService\n     *   }\n     * }\n     */\n    var algorithmIdPredictionServiceMapping = {\n      CodeClassifier: {\n        v1: \'CodeReplPredictionService\'\n      },\n      TextClassifier: {\n        v1: \'TextInputPredictionService\'\n      }\n\n    };\n\n    return {\n      getPredictionService: function(algorithmId, dataSchemaVersion) {\n        if (algorithmIdPredictionServiceMapping.hasOwnProperty(algorithmId)) {\n          // We convert dataSchemaVersion to a string below since JS objects\n          // can\'t have integer properties.\n          var serviceName = (\n            algorithmIdPredictionServiceMapping[algorithmId][\n              \'v\' + dataSchemaVersion.toString()]);\n          return $injector.get(serviceName);\n        } else {\n          return null;\n        }\n      },\n      // The below function is required for running tests with sample\n      // prediction services.\n      setMapping: function(newAlgorithmIdPredictionServiceMapping) {\n        algorithmIdPredictionServiceMapping = (\n          newAlgorithmIdPredictionServiceMapping);\n      }\n    };\n  }]);'

blocks = {}
debug_info = ''