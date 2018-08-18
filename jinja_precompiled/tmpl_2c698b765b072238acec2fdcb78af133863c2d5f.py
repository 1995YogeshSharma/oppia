from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/StateTopAnswersStatsService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for maintaining the statistics of the top answers for\n * each state of an exploration.\n */\n\noppia.factory(\'StateTopAnswersStatsService\', [\n  \'$injector\', \'AngularNameService\', \'AnswerClassificationService\',\n  \'AnswerStatsObjectFactory\', \'ContextService\',\n  \'ExplorationStatesService\',\n  function(\n      $injector, AngularNameService, AnswerClassificationService,\n      AnswerStatsObjectFactory, ContextService,\n      ExplorationStatesService) {\n    /**\n     * @typedef AnswerStatsCache\n     * @property {AnswerStats[]} allAnswers\n     * @property {AnswerStats[]} unresolvedAnswers\n     */\n\n    /** @type {Object.<string, AnswerStatsCache[]>} */\n    var stateTopAnswersStatsCache = {};\n\n    /** @type {boolean} */\n    var isInitialized = false;\n\n    /**\n     * Updates the addressed info of all the answers cached for the given state\n     * to reflect the state\'s current answer groups.\n     * @param {string} stateName\n     */\n    var refreshAddressedInfo = function(stateName) {\n      var explorationId = ContextService.getExplorationId();\n      var state = ExplorationStatesService.getState(stateName);\n      var interactionRulesService = $injector.get(\n        AngularNameService.getNameOfInteractionRulesService(\n          state.interaction.id));\n      var allAnswersCacheEntry =\n        stateTopAnswersStatsCache[stateName].allAnswers;\n      var unresolvedAnswersCacheEntry =\n        stateTopAnswersStatsCache[stateName].unresolvedAnswers;\n\n      // Clear the unresolvedAnswers array since many answers may now have\n      // different "addressed" values.\n      unresolvedAnswersCacheEntry.length = 0;\n\n      // Update the isAddressed data of each answer and put any unaddressed\n      // answers into the unresolvedAnswers array.\n      allAnswersCacheEntry.forEach(function(answerStats) {\n        answerStats.isAddressed =\n          AnswerClassificationService.isClassifiedExplicitlyOrGoesToNewState(\n            stateName, state, answerStats.answer,\n            interactionRulesService);\n        if (!answerStats.isAddressed) {\n          unresolvedAnswersCacheEntry.push(answerStats);\n        }\n      });\n    };\n\n    var onStateAdded = function(stateName) {\n      stateTopAnswersStatsCache[stateName] = {\n        allAnswers: [],\n        unresolvedAnswers: []\n      };\n    };\n\n    var onStateDeleted = function(stateName) {\n      delete stateTopAnswersStatsCache[stateName];\n    };\n\n    var onStateRenamed = function(oldStateName, newStateName) {\n      stateTopAnswersStatsCache[newStateName] =\n        stateTopAnswersStatsCache[oldStateName];\n      delete stateTopAnswersStatsCache[oldStateName];\n    };\n\n    var onStateAnswerGroupsSaved = function(stateName) {\n      refreshAddressedInfo(stateName);\n    };\n\n    return {\n      /**\n       * Calls the backend asynchronously to setup the answer statistics of each\n       * state this exploration contains.\n       *\n       * @param {Object.<string, *>} stateTopAnswersStatsBackendDict - The\n       *    backend representation of the state top answers statistics.\n       */\n      init: function(stateTopAnswersStatsBackendDict) {\n        if (isInitialized) {\n          return;\n        }\n        stateTopAnswersStatsCache = {};\n        for (var stateName in stateTopAnswersStatsBackendDict.answers) {\n          stateTopAnswersStatsCache[stateName] = {\n            allAnswers: stateTopAnswersStatsBackendDict.answers[stateName].map(\n              AnswerStatsObjectFactory.createFromBackendDict),\n            unresolvedAnswers: []\n          };\n          // Still need to manually refresh the addressed information.\n          refreshAddressedInfo(stateName);\n        }\n        ExplorationStatesService.registerOnStateAddedCallback(onStateAdded);\n        ExplorationStatesService.registerOnStateDeletedCallback(onStateDeleted);\n        ExplorationStatesService.registerOnStateRenamedCallback(onStateRenamed);\n        ExplorationStatesService.registerOnStateAnswerGroupsSavedCallback(\n          onStateAnswerGroupsSaved);\n        isInitialized = true;\n      },\n\n      /** @returns {boolean} - Whether the cache is ready for use. */\n      isInitialized: function() {\n        return isInitialized;\n      },\n\n      /**\n       * @returns {boolean} - Whether the cache contains any answers for the\n       * given state.\n       */\n      hasStateStats: function(stateName) {\n        return isInitialized &&\n          stateTopAnswersStatsCache.hasOwnProperty(stateName);\n      },\n\n      /** @returns {string[]} - list of state names with recorded stats. */\n      getStateNamesWithStats: function() {\n        return Object.keys(stateTopAnswersStatsCache);\n      },\n\n      /**\n       * @param {string} stateName\n       * @returns {AnswerStats[]} - list of the statistics for the top answers.\n       */\n      getStateStats: function(stateName) {\n        if (!stateTopAnswersStatsCache.hasOwnProperty(stateName)) {\n          throw Error(stateName + \' does not exist.\');\n        }\n        return stateTopAnswersStatsCache[stateName].allAnswers;\n      },\n\n      /**\n       * @param {string} stateName\n       * @returns {AnswerStats[]} - list of stats for answers that are\n       *    unresolved.\n       */\n      getUnresolvedStateStats: function(stateName) {\n        if (!stateTopAnswersStatsCache.hasOwnProperty(stateName)) {\n          throw Error(stateName + \' does not exist.\');\n        }\n        return stateTopAnswersStatsCache[stateName].unresolvedAnswers;\n      },\n    };\n  }\n]);'

blocks = {}
debug_info = ''