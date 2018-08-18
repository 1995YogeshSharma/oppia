from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/story/StoryContentsObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating and mutating instances of frontend\n * story contents domain objects.\n */\n\noppia.factory(\'StoryContentsObjectFactory\', [\n  \'StoryNodeObjectFactory\', \'NODE_ID_PREFIX\',\n  function(StoryNodeObjectFactory, NODE_ID_PREFIX) {\n    var StoryContents = function(initialNodeId, nodes, nextNodeId) {\n      this._initialNodeId = initialNodeId;\n      this._nodes = nodes;\n      this._nextNodeId = nextNodeId;\n    };\n\n    var getIncrementedNodeId = function(nodeId) {\n      var index = parseInt(nodeId.replace(NODE_ID_PREFIX, \'\'));\n      ++index;\n      return NODE_ID_PREFIX + index;\n    };\n\n    // Instance methods\n\n    StoryContents.prototype.getInitialNodeId = function() {\n      return this._initialNodeId;\n    };\n\n    StoryContents.prototype.getNextNodeId = function() {\n      return this._nextNodeId;\n    };\n\n    StoryContents.prototype.getNodes = function() {\n      return this._nodes;\n    };\n\n    StoryContents.prototype.validate = function() {\n      var issues = [];\n      var nodes = this._nodes;\n      for (var i = 0; i < nodes.length; i++) {\n        var nodeIssues = nodes[i].validate();\n        issues = issues.concat(nodeIssues);\n      }\n      if (issues.length > 0) {\n        return issues;\n      }\n\n      // Provided the nodes list is valid and each node in it is valid, the\n      // preliminary checks are done to see if the story node graph obtained is\n      // valid.\n      var nodeIds = nodes.map(function(node) {\n        return node.getId();\n      });\n      for (var i = 0; i < nodeIds.length; i++) {\n        var nodeId = nodeIds[i];\n        if (nodeIds.indexOf(nodeId) < nodeIds.lastIndexOf(nodeId)) {\n          throw Error(\n            \'The node with id \' + nodeId + \' is duplicated in the story\');\n        }\n      }\n      var nextNodeIdNumber = parseInt(\n        this._nextNodeId.replace(NODE_ID_PREFIX, \'\'));\n      var initialNodeIsPresent = false;\n      for (var i = 0; i < nodes.length; i++) {\n        var nodeIdNumber = parseInt(\n          nodes[i].getId().replace(NODE_ID_PREFIX, \'\'));\n        if (nodes[i].getId() === this._initialNodeId) {\n          initialNodeIsPresent = true;\n        }\n        if (nodeIdNumber > nextNodeIdNumber) {\n          throw Error(\n            \'Node id out of bounds for node with id \' + nodes[i].getId());\n        }\n        for (var j = 0; j < nodes[i].getDestinationNodeIds().length; j++) {\n          if (nodeIds.indexOf(nodes[i].getDestinationNodeIds()[j]) === -1) {\n            issues.push(\n              \'The node with id \' + nodes[i].getDestinationNodeIds()[j] +\n              \' doesn\\\'t exist\');\n          }\n        }\n      }\n      if (!initialNodeIsPresent) {\n        throw Error(\n          \'Initial node - \' + this._initialNodeId +\n          \' - is not present in the story\');\n      }\n\n      // All the validations above should be successfully completed before going\n      // to validating the story node graph.\n      if (issues.length > 0) {\n        return issues;\n      }\n\n      // nodesQueue stores the pending nodes to visit in a queue form.\n      var nodesQueue = [];\n      var nodeIsVisited = new Array(nodeIds.length).fill(false);\n      var startingNode = nodes[this.getNodeIndex(this._initialNodeId)];\n      nodesQueue.push(startingNode.getId());\n\n      // The user is assumed to have all the prerequisite skills of the\n      // starting node before starting the story. Also, this list models the\n      // skill IDs acquired by a learner as they progress through the story.\n      simulatedSkillIds = new Set(startingNode.getPrerequisiteSkillIds());\n\n      // The following loop employs a Breadth First Search from the given\n      // starting node and makes sure that the user has acquired all the\n      // prerequisite skills required by the destination nodes \'unlocked\' by\n      // visiting a particular node by the time that node is finished.\n      while (nodesQueue.length > 0) {\n        var currentNodeIndex = this.getNodeIndex(nodesQueue.shift());\n        nodeIsVisited[currentNodeIndex] = true;\n        var currentNode = nodes[currentNodeIndex];\n\n        startingNode.getAcquiredSkillIds().forEach(function(skillId) {\n          simulatedSkillIds.add(skillId);\n        });\n        for (var i = 0; i < currentNode.getDestinationNodeIds().length; i++) {\n          var nodeId = currentNode.getDestinationNodeIds()[i];\n          var nodeIndex = this.getNodeIndex(nodeId);\n          // The following condition checks whether the destination node\n          // for a particular node, has already been visited, in which case\n          // the story would have loops, which are not allowed.\n          if (nodeIsVisited[nodeIndex]) {\n            issues.push(\'Loops are not allowed in the node graph\');\n            // If a loop is encountered, then all further checks are halted,\n            // since it can lead to same error being reported again.\n            return issues;\n          }\n          var destinationNode = nodes[nodeIndex];\n          destinationNode.getPrerequisiteSkillIds().forEach(function(skillId) {\n            if (!simulatedSkillIds.has(skillId)) {\n              issues.push(\n                \'The prerequisite skill with id \' + skillId +\n                \' was not completed before node with id \' + nodeId +\n                \' was unlocked\');\n            }\n          });\n          nodesQueue.push(nodeId);\n        }\n      }\n      for (var i = 0; i < nodeIsVisited.length; i++){\n        if (!nodeIsVisited[i]) {\n          issues.push(\n            \'The node with id \' + nodeIds[i] +\n            \' is disconnected from the graph\');\n        }\n      }\n      return issues;\n    };\n\n    StoryContents.prototype.setInitialNodeId = function(nodeId) {\n      if (this.getNodeIndex(nodeId) === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      return this._initialNodeId = nodeId;\n    };\n\n    StoryContents.prototype.addNode = function() {\n      this._nodes.push(StoryNodeObjectFactory.createFromId(this._nextNodeId));\n      this._nextNodeId = getIncrementedNodeId(this._nextNodeId);\n    };\n\n    StoryContents.prototype.getNodeIndex = function(nodeId) {\n      for (var i = 0; i < this._nodes.length; i++) {\n        if (this._nodes[i].getId() === nodeId) {\n          return i;\n        }\n      }\n      return -1;\n    };\n\n    StoryContents.prototype.deleteNode = function(nodeId) {\n      if (this.getNodeIndex(nodeId) === -1) {\n        throw Error(\'The node does not exist\');\n      }\n      if (nodeId === this._initialNodeId) {\n        throw Error(\'Cannot delete initial story node\');\n      }\n      for (var i = 0; i < this._nodes.length; i++) {\n        if (this._nodes[i].getDestinationNodeIds().indexOf(nodeId) !== -1) {\n          this._nodes[i].removeDestinationNodeId(nodeId);\n        }\n      }\n      this._nodes.splice(this.getNodeIndex(nodeId), 1);\n    };\n\n    StoryContents.prototype.setNodeOutline = function(nodeId, outline) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].setOutline(outline);\n    };\n\n    StoryContents.prototype.setNodeExplorationId = function(\n        nodeId, explorationId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      for (var i = 0; i < this._nodes.length; i++) {\n        if (this._nodes[i].getExplorationId() === explorationId) {\n          throw Error(\'The given exploration already exists in the story.\');\n        }\n      }\n      this._nodes[index].setExplorationId(explorationId);\n    };\n\n    StoryContents.prototype.markNodeOutlineAsFinalized = function(nodeId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].markOutlineAsFinalized();\n    };\n\n    StoryContents.prototype.markNodeOutlineAsNotFinalized = function(nodeId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].markOutlineAsNotFinalized();\n    };\n\n    StoryContents.prototype.addPrerequisiteSkillIdToNode = function(\n        nodeId, skillId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].addPrerequisiteSkillId(skillId);\n    };\n\n    StoryContents.prototype.removePrerequisiteSkillIdFromNode = function(\n        nodeId, skillId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].removePrerequisiteSkillId(skillId);\n    };\n\n    StoryContents.prototype.addAcquiredSkillIdToNode = function(\n        nodeId, skillId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].addAcquiredSkillId(skillId);\n    };\n\n    StoryContents.prototype.removeAcquiredSkillIdFromNode = function(\n        nodeId, skillId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].removeAcquiredSkillId(skillId);\n    };\n\n    StoryContents.prototype.addDestinationNodeIdToNode = function(\n        nodeId, destinationNodeId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      if (this.getNodeIndex(destinationNodeId) === -1) {\n        throw Error(\'The destination node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].addDestinationNodeId(destinationNodeId);\n    };\n\n    StoryContents.prototype.removeDestinationNodeIdFromNode = function(\n        nodeId, destinationNodeId) {\n      var index = this.getNodeIndex(nodeId);\n      if (index === -1) {\n        throw Error(\'The node with given id doesn\\\'t exist\');\n      }\n      this._nodes[index].removeDestinationNodeId(destinationNodeId);\n    };\n\n    // Static class methods. Note that "this" is not available in static\n    // contexts. This function takes a JSON object which represents a backend\n    // story python dict.\n    StoryContents.createFromBackendDict = function(storyContentsBackendObject) {\n      var nodes = [];\n      for (var i = 0; i < storyContentsBackendObject.nodes.length; i++) {\n        nodes.push(\n          StoryNodeObjectFactory.createFromBackendDict(\n            storyContentsBackendObject.nodes[i]));\n      }\n      return new StoryContents(\n        storyContentsBackendObject.initial_node_id, nodes,\n        storyContentsBackendObject.next_node_id\n      );\n    };\n    return StoryContents;\n  }\n]);'

blocks = {}
debug_info = ''