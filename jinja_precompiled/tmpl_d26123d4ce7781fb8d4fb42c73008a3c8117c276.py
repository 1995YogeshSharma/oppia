from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/editor_tab/CollectionLinearizerService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service to maintain the state of a single collection shared\n * throughout the collection editor. This service provides functionality for\n * retrieving the collection, saving it, and listening for changes.\n */\n\noppia.factory(\'CollectionLinearizerService\', [\n  \'CollectionUpdateService\',\n  function(CollectionUpdateService) {\n    var _getNextExplorationId = function(collection, completedExpIds) {\n      var explorationIds = collection.getExplorationIds();\n\n      for (var i = 0; i < explorationIds.length; i++) {\n        if (completedExpIds.indexOf(explorationIds[i]) === -1) {\n          return explorationIds[i];\n        }\n      }\n      return null;\n    };\n\n    // Given a non linear collection input, the function will linearize it by\n    // picking the first node it encounters on the branch and ignore the others.\n    var _getCollectionNodesInPlayableOrder = function(collection) {\n      return collection.getCollectionNodes();\n    };\n\n    var addAfter = function(collection, curExplorationId, newExplorationId) {\n      var curCollectionNode = collection.getCollectionNodeByExplorationId(\n        curExplorationId);\n    };\n\n    var findNodeIndex = function(linearNodeList, explorationId) {\n      var index = -1;\n      for (var i = 0; i < linearNodeList.length; i++) {\n        if (linearNodeList[i].getExplorationId() === explorationId) {\n          index = i;\n          break;\n        }\n      }\n      return index;\n    };\n\n    // Swap the node at the specified index with the node immediately to the\n    // left of it.\n    var swapLeft = function(collection, linearNodeList, nodeIndex) {\n      var node = linearNodeList[nodeIndex];\n      var leftNodeIndex = nodeIndex > 0 ? nodeIndex - 1 : null;\n\n      if (leftNodeIndex === null) {\n        return;\n      }\n\n      CollectionUpdateService.swapNodes(collection, leftNodeIndex, nodeIndex);\n    };\n    var swapRight = function(collection, linearNodeList, nodeIndex) {\n      // Swapping right is the same as swapping the node one to the right\n      // leftward.\n      if (nodeIndex < linearNodeList.length - 1) {\n        swapLeft(collection, linearNodeList, nodeIndex + 1);\n      }\n      // Otherwise it is a no-op (cannot swap the last node right).\n    };\n\n    var shiftNode = function(collection, explorationId, swapFunction) {\n      // There is nothing to shift if the collection has only 1 node.\n      if (collection.getCollectionNodeCount() > 1) {\n        var linearNodeList = _getCollectionNodesInPlayableOrder(collection);\n        var nodeIndex = findNodeIndex(linearNodeList, explorationId);\n        if (nodeIndex === -1) {\n          return false;\n        }\n        swapFunction(collection, linearNodeList, nodeIndex);\n      }\n      return true;\n    };\n\n    return {\n      /**\n       * Given a collection and a list of completed exploration IDs within the\n       * context of that collection, returns a list of which explorations in the\n       * collection is immediately playable by the user. NOTE: This function\n       * does not assume that the collection is linear.\n       */\n      getNextExplorationId: function(collection, completedExpIds) {\n        return _getNextExplorationId(collection, completedExpIds);\n      },\n\n      /**\n       * Given a collection, returns a linear list of collection nodes which\n       * represents a valid path for playing through this collection.\n       */\n      getCollectionNodesInPlayableOrder: function(collection) {\n        return _getCollectionNodesInPlayableOrder(collection);\n      },\n\n      /**\n       * Inserts a new collection node at the end of the collection\'s playable\n       * list of explorations, based on the specified exploration ID and\n       * exploration summary backend object.\n       */\n      appendCollectionNode: function(\n          collection, explorationId, summaryBackendObject) {\n        var linearNodeList = _getCollectionNodesInPlayableOrder(collection);\n        CollectionUpdateService.addCollectionNode(\n          collection, explorationId, summaryBackendObject);\n        if (linearNodeList.length > 0) {\n          var lastNode = linearNodeList[linearNodeList.length - 1];\n          addAfter(collection, lastNode.getExplorationId(), explorationId);\n        }\n      },\n\n      /**\n       * Remove a collection node from a given collection which maps to the\n       * specified exploration ID. This function ensures the linear structure of\n       * the collection is maintained. Returns whether the provided exploration\n       * ID is contained within the linearly playable path of the specified\n       * collection.\n       */\n      removeCollectionNode: function(collection, explorationId) {\n        if (!collection.containsCollectionNode(explorationId)) {\n          return false;\n        }\n\n        // Delete the node\n        CollectionUpdateService.deleteCollectionNode(collection, explorationId);\n        return true;\n      },\n\n      /**\n       * Looks up a collection node given an exploration ID in the specified\n       * collection and attempts to shift it left in the linear ordering of the\n       * collection. If the node is the first exploration played by the player,\n       * then this function is a no-op. Returns false if the specified\n       * exploration ID does not associate to any nodes in the collection.\n       */\n      shiftNodeLeft: function(collection, explorationId) {\n        return shiftNode(collection, explorationId, swapLeft);\n      },\n\n      /**\n       * Looks up a collection node given an exploration ID in the specified\n       * collection and attempts to shift it right in the linear ordering of the\n       * collection. If the node is the last exploration played by the player,\n       * then this function is a no-op. Returns false if the specified\n       * exploration ID does not associate to any nodes in the collection.\n       */\n      shiftNodeRight: function(collection, explorationId) {\n        return shiftNode(collection, explorationId, swapRight);\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''