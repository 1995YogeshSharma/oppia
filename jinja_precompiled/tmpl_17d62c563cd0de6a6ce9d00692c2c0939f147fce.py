from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/RuleObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of Rule\n * domain objects.\n */\n\noppia.factory(\'RuleObjectFactory\', [function() {\n  var Rule = function(type, inputs) {\n    this.type = type;\n    this.inputs = inputs;\n  };\n\n  Rule.prototype.toBackendDict = function() {\n    return {\n      rule_type: this.type,\n      inputs: this.inputs\n    };\n  };\n\n  Rule.createNew = function(type, inputs) {\n    return new Rule(type, inputs);\n  };\n\n  Rule.createFromBackendDict = function(ruleDict) {\n    return new Rule(ruleDict.rule_type, ruleDict.inputs);\n  };\n\n  return Rule;\n}]);'

blocks = {}
debug_info = ''