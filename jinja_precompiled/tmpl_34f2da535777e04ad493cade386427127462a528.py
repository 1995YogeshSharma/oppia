from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/SchemaDefaultValueService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service provides correct default value for\n * SchemaBasedList item.\n */\n\noppia.factory(\'SchemaDefaultValueService\', [function() {\n  return {\n    // TODO(sll): Rewrite this to take validators into account, so that\n    // we always start with a valid value.\n    getDefaultValue: function(schema) {\n      if (schema.choices) {\n        return schema.choices[0];\n      } else if (schema.type === \'bool\') {\n        return false;\n      } else if (schema.type === \'unicode\' || schema.type === \'html\') {\n        return \'\';\n      } else if (schema.type === \'list\') {\n        return [this.getDefaultValue(schema.items)];\n      } else if (schema.type === \'dict\') {\n        var result = {};\n        for (var i = 0; i < schema.properties.length; i++) {\n          result[schema.properties[i].name] = this.getDefaultValue(\n            schema.properties[i].schema);\n        }\n        return result;\n      } else if (schema.type === \'int\' || schema.type === \'float\') {\n        return 0;\n      } else {\n        console.error(\'Invalid schema type: \' + schema.type);\n      }\n    }\n  };\n}]);'

blocks = {}
debug_info = ''