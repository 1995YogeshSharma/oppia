from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/TriggerObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of Trigger\n * domain objects.\n */\n\noppia.factory(\'TriggerObjectFactory\', [function() {\n  var Trigger = function(type, customizationArgs) {\n    this.type = type;\n    this.customizationArgs = customizationArgs;\n  };\n\n  Trigger.prototype.toBackendDict = function() {\n    return {\n      trigger_type: this.type,\n      customization_args: this.customizationArgs\n    };\n  };\n\n  Trigger.createFromBackendDict = function(triggerBackendDict) {\n    return new Trigger(\n      triggerBackendDict.trigger_type,\n      triggerBackendDict.customization_args);\n  };\n\n  return Trigger;\n}]);'

blocks = {}
debug_info = ''