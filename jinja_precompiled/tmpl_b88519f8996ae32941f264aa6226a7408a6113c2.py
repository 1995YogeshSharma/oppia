from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/AnswerGroupObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of AnswerGroup\n * domain objects.\n */\n\noppia.factory(\'AnswerGroupObjectFactory\', [\n  \'RuleObjectFactory\', \'OutcomeObjectFactory\',\n  function(RuleObjectFactory, OutcomeObjectFactory) {\n    var AnswerGroup = function(\n        rules, outcome, trainingData, taggedMisconceptionId) {\n      this.rules = rules;\n      this.outcome = outcome;\n      this.trainingData = trainingData;\n      this.taggedMisconceptionId = taggedMisconceptionId;\n    };\n\n    AnswerGroup.prototype.toBackendDict = function() {\n      return {\n        rule_specs: this.rules.map(function(rule) {\n          return rule.toBackendDict();\n        }),\n        outcome: this.outcome.toBackendDict(),\n        training_data: this.trainingData,\n        tagged_misconception_id: this.taggedMisconceptionId\n      };\n    };\n\n    // Static class methods. Note that "this" is not available in\n    // static contexts.\n    AnswerGroup.createNew = function(\n        rules, outcome, trainingData, taggedMisconceptionId) {\n      return new AnswerGroup(\n        rules, outcome, trainingData, taggedMisconceptionId);\n    };\n\n    AnswerGroup.createFromBackendDict = function(answerGroupBackendDict) {\n      return new AnswerGroup(\n        generateRulesFromBackend(answerGroupBackendDict.rule_specs),\n        OutcomeObjectFactory.createFromBackendDict(\n          answerGroupBackendDict.outcome),\n        answerGroupBackendDict.training_data,\n        answerGroupBackendDict.tagged_misconception_id);\n    };\n\n    var generateRulesFromBackend = function(ruleBackendDicts) {\n      return ruleBackendDicts.map(function(ruleBackendDict) {\n        return RuleObjectFactory.createFromBackendDict(ruleBackendDict);\n      });\n    };\n\n    return AnswerGroup;\n  }\n]);'

blocks = {}
debug_info = ''