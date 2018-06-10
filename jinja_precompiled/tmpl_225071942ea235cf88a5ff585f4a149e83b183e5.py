from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ExplorationDiffService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for computing diffs of explorations.\n */\n\noppia.factory(\'ExplorationDiffService\', [\n  \'INTERACTION_SPECS\', function(INTERACTION_SPECS) {\n    var STATE_PROPERTY_ADDED = \'added\';\n    var STATE_PROPERTY_DELETED = \'deleted\';\n    var STATE_PROPERTY_CHANGED = \'changed\';\n    var STATE_PROPERTY_UNCHANGED = \'unchanged\';\n    var _maxId = 0;\n\n    // Functions to assign ids to states\n    var _resetMaxId = function() {\n      _maxId = 0;\n    };\n    var _generateNewId = function() {\n      _maxId++;\n      return _maxId;\n    };\n\n    var _generateInitialStateIdsAndData = function(statesDict) {\n      var result = {\n        stateIds: {},\n        stateData: {}\n      };\n\n      _resetMaxId();\n\n      for (var stateName in statesDict) {\n        var stateId = _generateNewId();\n        result.stateData[stateId] = {\n          newestStateName: stateName,\n          originalStateName: stateName,\n          stateProperty: STATE_PROPERTY_UNCHANGED\n        };\n        result.stateIds[stateName] = stateId;\n      }\n      return result;\n    };\n\n    var _postprocessStateIdsAndData = function(\n        originalStateIds, stateIds, stateData, v1States, v2States) {\n      // Ignore changes that were canceled out by later changes\n      for (var stateId in stateData) {\n        if (stateData[stateId].stateProperty === STATE_PROPERTY_CHANGED &&\n            v1States.hasOwnProperty(stateData[stateId].originalStateName) &&\n            v2States.hasOwnProperty(stateData[stateId].newestStateName) &&\n            angular.equals(v1States[stateData[stateId].originalStateName],\n              v2States[stateData[stateId].newestStateName])) {\n          stateData[stateId].stateProperty = STATE_PROPERTY_UNCHANGED;\n        }\n      }\n\n      // Delete states not present in both v1 and v2\n      for (var stateId in stateData) {\n        if (!v1States.hasOwnProperty(\n          stateData[stateId].originalStateName) &&\n          !v2States.hasOwnProperty(stateData[stateId].newestStateName)) {\n          delete stateData[stateId];\n        }\n      }\n\n      // Track whether terminal nodes in v1 or v2\n      // TODO(bhenning): could show changes to terminal nodes in diff\n      var finalStateIds = [];\n      for (var stateId in stateData) {\n        var oldState = v1States[stateData[stateId].originalStateName];\n        var newState = v2States[stateData[stateId].newestStateName];\n        var oldStateIsTerminal = false;\n        var newStateIsTerminal = false;\n        if (oldState) {\n          oldStateIsTerminal = (\n            oldState.interaction.id &&\n            INTERACTION_SPECS[oldState.interaction.id].is_terminal);\n        }\n        if (newState) {\n          newStateIsTerminal = (\n            newState.interaction.id &&\n            INTERACTION_SPECS[newState.interaction.id].is_terminal);\n        }\n        if (oldStateIsTerminal || newStateIsTerminal) {\n          finalStateIds.push(stateId);\n        }\n      }\n\n      var links = _compareLinks(\n        v1States, originalStateIds, v2States, stateIds);\n\n      return {\n        nodes: stateData,\n        links: links,\n        originalStateIds: originalStateIds,\n        stateIds: stateIds,\n        finalStateIds: finalStateIds\n      };\n    };\n\n    /**\n     * A helper function that takes a list of changes and uses them to modify\n     * stateIds and stateData accordingly.\n     *\n     * stateIds is an object whose keys are the newest state name and whose\n     * values are the assigned state id.\n     * stateData an object whose keys are state IDs and whose value is an object\n     * with these keys:\n     *  - \'newestStateName\': the latest name of the state\n     *  - \'originalStateName\': the first encountered name for the state\n     *  - \'stateProperty\': \'changed\', \'unchanged\', \'added\' or \'deleted\'\n     * changeListData is a list of objects, each with two keys:\n     * - changeList: the change list to apply.\n     * - directionForwards: true if changes are compared in increasing version\n     * number, and false if changes are compared in decreasing version number.\n     */\n    var _getDiffGraphData = function(v1States, v2States, changeListData) {\n      var v1Info = _generateInitialStateIdsAndData(v1States);\n      var stateData = v1Info.stateData;\n      var stateIds = v1Info.stateIds;\n      var originalStateIds = angular.copy(stateIds);\n\n      changeListData.forEach(function(changeListDatum) {\n        var changeList = changeListDatum.changeList;\n        var directionForwards = changeListDatum.directionForwards;\n\n        changeList.forEach(function(change) {\n          if ((directionForwards && change.cmd === \'add_state\') ||\n              (!directionForwards && change.cmd === \'delete_state\')) {\n            if (!stateIds.hasOwnProperty(change.state_name)) {\n              var newId = _generateNewId();\n              stateIds[change.state_name] = newId;\n            }\n            var currentStateId = stateIds[change.state_name];\n            if (stateData.hasOwnProperty(currentStateId) &&\n                stateData[currentStateId].stateProperty ===\n                  STATE_PROPERTY_DELETED) {\n              stateData[currentStateId].stateProperty = STATE_PROPERTY_CHANGED;\n              stateData[currentStateId].newestStateName = change.state_name;\n            } else {\n              stateData[currentStateId] = {\n                newestStateName: change.state_name,\n                originalStateName: change.state_name,\n                stateProperty: STATE_PROPERTY_ADDED\n              };\n            }\n          } else if ((directionForwards && change.cmd === \'delete_state\') ||\n              (!directionForwards && change.cmd === \'add_state\')) {\n            if (stateData[stateIds[change.state_name]].stateProperty ===\n                STATE_PROPERTY_ADDED) {\n              stateData[stateIds[change.state_name]].stateProperty = (\n                STATE_PROPERTY_CHANGED);\n            } else {\n              stateData[stateIds[change.state_name]].stateProperty = (\n                STATE_PROPERTY_DELETED);\n            }\n          } else if (change.cmd === \'rename_state\') {\n            var newStateName = null;\n            var oldStateName = null;\n            if (directionForwards) {\n              newStateName = change.new_state_name;\n              oldStateName = change.old_state_name;\n            } else {\n              newStateName = change.old_state_name;\n              oldStateName = change.new_state_name;\n            }\n            stateIds[newStateName] = stateIds[oldStateName];\n            delete stateIds[oldStateName];\n            stateData[stateIds[newStateName]].newestStateName = newStateName;\n          } else if (change.cmd === \'edit_state_property\') {\n            if (stateData[stateIds[change.state_name]].stateProperty ===\n                STATE_PROPERTY_UNCHANGED) {\n              stateData[stateIds[change.state_name]].stateProperty = (\n                STATE_PROPERTY_CHANGED);\n            }\n          } else if (\n            change.cmd !== \'migrate_states_schema_to_latest_version\' &&\n            change.cmd !== \'AUTO_revert_version_number\' &&\n            change.cmd !== \'edit_exploration_property\') {\n            throw new Error(\'Invalid change command: \' + change.cmd);\n          }\n        });\n      });\n\n      return _postprocessStateIdsAndData(\n        originalStateIds, stateIds, stateData, v1States, v2States);\n    };\n\n    /**\n     * Returns an adjacency matrix, adjMatrix, of links between states\n     * (represented by ids). adjMatrix[state1Id][state2Id] is true if there\n     * is a link from state 1 to state 2 and false otherwise.\n     *\n     * Args:\n     * - states: an object whose keys are state names and values are objects\n     *     representing the state.\n     * - stateIds: an object whose keys are state names and values are state\n     *     ids.\n     * - maxId: the maximum id in states and stateIds.\n     */\n    var _getAdjMatrix = function(states, stateIds, maxId) {\n      adjMatrix = {};\n      for (var stateId = 1; stateId <= maxId; stateId++) {\n        adjMatrix[stateId] = {};\n      }\n      for (var state1Id = 1; state1Id <= maxId; state1Id++) {\n        for (var state2Id = 1; state2Id <= maxId; state2Id++) {\n          adjMatrix[state1Id][state2Id] = false;\n        }\n      }\n      for (var stateName in states) {\n        var interaction = states[stateName].interaction;\n        var groups = interaction.answerGroups;\n        for (var h = 0; h < groups.length; h++) {\n          var dest = groups[h].outcome.dest;\n          adjMatrix[stateIds[stateName]][stateIds[dest]] = true;\n        }\n        if (interaction.defaultOutcome) {\n          var defaultDest = interaction.defaultOutcome.dest;\n          adjMatrix[stateIds[stateName]][stateIds[defaultDest]] = true;\n        }\n      }\n      return adjMatrix;\n    };\n\n    /**\n     * Returns a list of objects representing links in the diff graph.\n     * Each object represents one link, and has keys:\n     *  - \'source\': source state of link\n     *  - \'target\': target state of link\n     *  - \'linkProperty\': \'added\', \'deleted\' or \'unchanged\'\n     */\n    var _compareLinks = function(\n        v1States, originalStateIds, v2States, newestStateIds) {\n      links = [];\n      var adjMatrixV1 = _getAdjMatrix(v1States, originalStateIds, _maxId);\n      var adjMatrixV2 = _getAdjMatrix(v2States, newestStateIds, _maxId);\n\n      for (var i = 1; i <= _maxId; i++) {\n        for (var j = 1; j <= _maxId; j++) {\n          if (i !== j && (adjMatrixV1[i][j] || adjMatrixV2[i][j])) {\n            links.push({\n              source: i,\n              target: j,\n              linkProperty: (\n                adjMatrixV1[i][j] && adjMatrixV2[i][j] ? \'unchanged\' :\n                !adjMatrixV1[i][j] && adjMatrixV2[i][j] ? \'added\' : \'deleted\')\n            });\n          }\n        }\n      }\n\n      return links;\n    };\n\n    return {\n      getDiffGraphData: function(oldStates, newStates, changeListData) {\n        return _getDiffGraphData(\n          oldStates,\n          newStates,\n          changeListData);\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''