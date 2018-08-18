from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/InteractionObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of Interaction\n * domain objects.\n */\n\noppia.factory(\'InteractionObjectFactory\', [\n  \'AnswerGroupObjectFactory\', \'HintObjectFactory\', \'OutcomeObjectFactory\',\n  \'SolutionObjectFactory\',\n  function(\n      AnswerGroupObjectFactory, HintObjectFactory, OutcomeObjectFactory,\n      SolutionObjectFactory) {\n    var Interaction = function(\n        answerGroups, confirmedUnclassifiedAnswers, customizationArgs,\n        defaultOutcome, hints, id, solution) {\n      this.answerGroups = answerGroups;\n      this.confirmedUnclassifiedAnswers = confirmedUnclassifiedAnswers;\n      this.customizationArgs = customizationArgs;\n      this.defaultOutcome = defaultOutcome;\n      this.hints = hints;\n      this.id = id;\n      this.solution = solution;\n    };\n\n    Interaction.prototype.setId = function(newValue) {\n      this.id = newValue;\n    };\n\n    Interaction.prototype.setAnswerGroups = function(newValue) {\n      this.answerGroups = newValue;\n    };\n\n    Interaction.prototype.setDefaultOutcome = function(newValue) {\n      this.defaultOutcome = newValue;\n    };\n\n    Interaction.prototype.setCustomizationArgs = function(newValue) {\n      this.customizationArgs = newValue;\n    };\n\n    Interaction.prototype.setSolution = function(newValue) {\n      this.solution = newValue;\n    };\n\n    Interaction.prototype.setHints = function(newValue) {\n      this.hints = newValue;\n    };\n\n    Interaction.prototype.toBackendDict = function() {\n      return {\n        answer_groups: this.answerGroups.map(function(answerGroup) {\n          return answerGroup.toBackendDict();\n        }),\n        confirmed_unclassified_answers: this.confirmedUnclassifiedAnswers,\n        customization_args: this.customizationArgs,\n        default_outcome:\n          this.defaultOutcome ? this.defaultOutcome.toBackendDict() : null,\n        hints: this.hints.map(function(hint) {\n          return hint.toBackendDict();\n        }),\n        id: this.id,\n        solution: this.solution ? this.solution.toBackendDict() : null\n      };\n    };\n\n    Interaction.createFromBackendDict = function(interactionDict) {\n      var defaultOutcome;\n      if (interactionDict.default_outcome) {\n        defaultOutcome = OutcomeObjectFactory.createFromBackendDict(\n          interactionDict.default_outcome);\n      } else {\n        defaultOutcome = null;\n      }\n      return new Interaction(\n        generateAnswerGroupsFromBackend(interactionDict.answer_groups),\n        interactionDict.confirmed_unclassified_answers,\n        interactionDict.customization_args,\n        defaultOutcome,\n        generateHintsFromBackend(interactionDict.hints),\n        interactionDict.id,\n        interactionDict.solution ? (\n          generateSolutionFromBackend(interactionDict.solution)) : null);\n    };\n\n    var generateAnswerGroupsFromBackend = function(answerGroupBackendDicts) {\n      return answerGroupBackendDicts.map(function(\n          answerGroupBackendDict) {\n        return AnswerGroupObjectFactory.createFromBackendDict(\n          answerGroupBackendDict);\n      });\n    };\n\n    var generateHintsFromBackend = function(hintBackendDicts) {\n      return hintBackendDicts.map(function(hintBackendDict) {\n        return HintObjectFactory.createFromBackendDict(hintBackendDict);\n      });\n    };\n\n    var generateSolutionFromBackend = function(solutionBackendDict) {\n      return SolutionObjectFactory.createFromBackendDict(solutionBackendDict);\n    };\n\n    return Interaction;\n  }\n]);'

blocks = {}
debug_info = ''