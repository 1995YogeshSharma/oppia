from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/ParameterMetadataService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for computing parameter metadata.\n */\n\noppia.factory(\'ParameterMetadataService\', [\n  \'ExplorationStatesService\', \'ExpressionInterpolationService\',\n  \'ExplorationParamChangesService\', \'GraphDataService\',\n  function(\n      ExplorationStatesService, ExpressionInterpolationService,\n      ExplorationParamChangesService, GraphDataService) {\n    var PARAM_ACTION_GET = \'get\';\n    var PARAM_ACTION_SET = \'set\';\n\n    var PARAM_SOURCE_ANSWER = \'answer\';\n    var PARAM_SOURCE_CONTENT = \'content\';\n    var PARAM_SOURCE_FEEDBACK = \'feedback\';\n    var PARAM_SOURCE_PARAM_CHANGES = \'param_changes\';\n\n    var getMetadataFromParamChanges = function(paramChanges) {\n      var result = [];\n      for (var i = 0; i < paramChanges.length; i++) {\n        var pc = paramChanges[i];\n        if (pc.generatorId === \'Copier\') {\n          if (!pc.customizationArgs.parse_with_jinja) {\n            result.push({\n              action: PARAM_ACTION_SET,\n              paramName: pc.name,\n              source: PARAM_SOURCE_PARAM_CHANGES,\n              sourceInd: i\n            });\n          } else {\n            var paramsReferenced = (\n              ExpressionInterpolationService.getParamsFromString(\n                pc.customizationArgs.value));\n            for (var j = 0; j < paramsReferenced.length; j++) {\n              result.push({\n                action: PARAM_ACTION_GET,\n                paramName: paramsReferenced[j],\n                source: PARAM_SOURCE_PARAM_CHANGES,\n                sourceInd: i\n              });\n            }\n\n            result.push({\n              action: PARAM_ACTION_SET,\n              paramName: pc.name,\n              source: PARAM_SOURCE_PARAM_CHANGES,\n              sourceInd: i\n            });\n          }\n        } else {\n          // RandomSelector. Elements in the list of possibilities are treated\n          // as raw unicode strings, not expressions.\n          result.push({\n            action: PARAM_ACTION_SET,\n            paramName: pc.name,\n            source: PARAM_SOURCE_PARAM_CHANGES,\n            sourceInd: i\n          });\n        }\n      }\n\n      return result;\n    };\n\n    // Returns a list of set/get actions for parameters in the given state, in\n    // the order that they occur.\n    // TODO(sll): Add trace data (so that it\'s easy to figure out in which rule\n    // an issue occurred, say).\n    var getStateParamMetadata = function(state) {\n      // First, the state param changes are applied: we get their values\n      // and set the params.\n      var result = getMetadataFromParamChanges(state.paramChanges);\n\n      // Next, the content is evaluated.\n      ExpressionInterpolationService.getParamsFromString(\n        state.content.getHtml()).forEach(\n        function(paramName) {\n          result.push({\n            action: PARAM_ACTION_GET,\n            paramName: paramName,\n            source: PARAM_SOURCE_CONTENT\n          });\n        }\n      );\n\n      // Next, the answer is received.\n      result.push({\n        action: PARAM_ACTION_SET,\n        paramName: \'answer\',\n        source: PARAM_SOURCE_ANSWER\n      });\n\n      // Finally, the rule feedback strings are evaluated.\n      state.interaction.answerGroups.forEach(function(group) {\n        for (var k = 0; k < group.outcome.feedback.length; k++) {\n          ExpressionInterpolationService.getParamsFromString(\n            group.outcome.feedback[k]).forEach(\n            function(paramName) {\n              result.push({\n                action: PARAM_ACTION_GET,\n                paramName: paramName,\n                source: PARAM_SOURCE_FEEDBACK,\n                sourceInd: k\n              });\n            }\n          );\n        }\n      });\n\n      return result;\n    };\n\n    // Returns one of null, PARAM_ACTION_SET, PARAM_ACTION_GET depending on\n    // whether this parameter is not used at all in this state, or\n    // whether its first occurrence is a \'set\' or \'get\'.\n    var getParamStatus = function(stateParamMetadata, paramName) {\n      for (var i = 0; i < stateParamMetadata.length; i++) {\n        if (stateParamMetadata[i].paramName === paramName) {\n          return stateParamMetadata[i].action;\n        }\n      }\n      return null;\n    };\n\n    return {\n      // Returns a list of objects, each indicating a parameter for which it is\n      // possible to arrive at a state with that parameter required but unset.\n      // Each object in this list has two keys:\n      // - paramName: the name of the parameter that may be unset\n      // - stateName: the name of one of the states it is possible to reach\n      //     with the parameter being unset, or null if the place where the\n      //     parameter is required is in the initial list of parameter changes\n      //     (e.g. one parameter may be set based on the value assigned to\n      //     another parameter).\n      getUnsetParametersInfo: function(initNodeIds) {\n        var graphData = GraphDataService.getGraphData();\n\n        var states = ExplorationStatesService.getStates();\n\n        // Determine all parameter names that are used within this exploration.\n        var allParamNames = [];\n        var expParamMetadata = getMetadataFromParamChanges(\n          ExplorationParamChangesService.savedMemento);\n        var stateParamMetadatas = {};\n\n        expParamMetadata.forEach(function(expParamMetadataItem) {\n          if (allParamNames.indexOf(expParamMetadataItem.paramName) === -1) {\n            allParamNames.push(expParamMetadataItem.paramName);\n          }\n        });\n\n        states.getStateNames().forEach(function(stateName) {\n          stateParamMetadatas[stateName] = getStateParamMetadata(\n            states.getState(stateName));\n          for (var i = 0; i < stateParamMetadatas[stateName].length; i++) {\n            var pName = stateParamMetadatas[stateName][i].paramName;\n            if (allParamNames.indexOf(pName) === -1) {\n              allParamNames.push(pName);\n            }\n          }\n        });\n\n        // For each parameter, do a BFS to see if it\'s possible to get from\n        // the start node to a node requiring this parameter, without passing\n        // through any nodes that set this parameter.\n        var unsetParametersInfo = [];\n\n        for (var paramInd = 0; paramInd < allParamNames.length; paramInd++) {\n          var paramName = allParamNames[paramInd];\n          var tmpUnsetParameter = null;\n\n          var paramStatusAtOutset = getParamStatus(expParamMetadata, paramName);\n          if (paramStatusAtOutset === PARAM_ACTION_GET) {\n            unsetParametersInfo.push({\n              paramName: paramName,\n              stateName: null\n            });\n            continue;\n          } else if (paramStatusAtOutset === PARAM_ACTION_SET) {\n            // This parameter will remain set for the entirety of the\n            // exploration.\n            continue;\n          }\n\n          var queue = [];\n          var seen = {};\n          for (var i = 0; i < initNodeIds.length; i++) {\n            seen[initNodeIds[i]] = true;\n            var paramStatus = getParamStatus(\n              stateParamMetadatas[initNodeIds[i]], paramName);\n            if (paramStatus === PARAM_ACTION_GET) {\n              tmpUnsetParameter = {\n                paramName: paramName,\n                stateName: initNodeIds[i]\n              };\n              break;\n            } else if (!paramStatus) {\n              queue.push(initNodeIds[i]);\n            }\n          }\n\n          if (tmpUnsetParameter) {\n            unsetParametersInfo.push(angular.copy(tmpUnsetParameter));\n            continue;\n          }\n\n          while (queue.length > 0) {\n            var currNodeId = queue.shift();\n            for (var edgeInd = 0; edgeInd < graphData.links.length; edgeInd++) {\n              var edge = graphData.links[edgeInd];\n              if (edge.source === currNodeId &&\n                  !seen.hasOwnProperty(edge.target)) {\n                seen[edge.target] = true;\n                paramStatus = getParamStatus(\n                  stateParamMetadatas[edge.target], paramName);\n                if (paramStatus === PARAM_ACTION_GET) {\n                  tmpUnsetParameter = {\n                    paramName: paramName,\n                    stateName: edge.target\n                  };\n                  break;\n                } else if (!paramStatus) {\n                  queue.push(edge.target);\n                }\n              }\n            }\n          }\n\n          if (tmpUnsetParameter) {\n            unsetParametersInfo.push(angular.copy(tmpUnsetParameter));\n            continue;\n          }\n        }\n\n        return unsetParametersInfo;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''