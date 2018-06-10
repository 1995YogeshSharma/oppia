from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/collection/CollectionObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating and mutating instances of frontend\n * collection domain objects.\n */\n\noppia.factory(\'CollectionObjectFactory\', [\n  \'CollectionNodeObjectFactory\',\n  function(CollectionNodeObjectFactory) {\n    var Collection = function(collectionBackendObject) {\n      this._id = collectionBackendObject.id;\n      this._title = collectionBackendObject.title;\n      this._objective = collectionBackendObject.objective;\n      this._languageCode = collectionBackendObject.language_code;\n      this._tags = collectionBackendObject.tags;\n      this._category = collectionBackendObject.category;\n      this._version = collectionBackendObject.version;\n      this._nodes = [];\n\n      // This map acts as a fast way of looking up a collection node for a given\n      // exploration ID.\n      this._explorationIdToNodeIndexMap = {};\n      for (var i = 0; i < collectionBackendObject.nodes.length; i++) {\n        this._nodes[i] = CollectionNodeObjectFactory.create(\n          collectionBackendObject.nodes[i]);\n        var explorationId = this._nodes[i].getExplorationId();\n        this._explorationIdToNodeIndexMap[explorationId] = i;\n      }\n    };\n\n    // Instance methods\n\n    Collection.prototype.getId = function() {\n      return this._id;\n    };\n\n    Collection.prototype.getTitle = function() {\n      return this._title;\n    };\n\n    Collection.prototype.setTitle = function(title) {\n      this._title = title;\n    };\n\n    Collection.prototype.getCategory = function() {\n      return this._category;\n    };\n\n    Collection.prototype.setCategory = function(category) {\n      this._category = category;\n    };\n\n    Collection.prototype.getObjective = function() {\n      return this._objective;\n    };\n\n    Collection.prototype.setObjective = function(objective) {\n      this._objective = objective;\n    };\n\n    Collection.prototype.getLanguageCode = function() {\n      return this._languageCode;\n    };\n\n    Collection.prototype.setLanguageCode = function(languageCode) {\n      this._languageCode = languageCode;\n    };\n\n    Collection.prototype.getTags = function() {\n      return this._tags;\n    };\n\n    Collection.prototype.setTags = function(tags) {\n      this._tags = tags;\n    };\n\n    Collection.prototype.getVersion = function() {\n      return this._version;\n    };\n\n    // Adds a new frontend collection node domain object to this collection.\n    // This will return true if the node was successfully added, or false if the\n    // given collection node references an exploration ID already referenced by\n    // another node within this collection. Changes to the provided object will\n    // be reflected in this collection.\n    Collection.prototype.addCollectionNode = function(collectionNodeObject) {\n      var explorationId = collectionNodeObject.getExplorationId();\n      if (!this._explorationIdToNodeIndexMap.hasOwnProperty(explorationId)) {\n        this._explorationIdToNodeIndexMap[explorationId] = this._nodes.length;\n        this._nodes.push(collectionNodeObject);\n        return true;\n      }\n      return false;\n    };\n\n    // This will swap 2 nodes of the collection and update the exploration id\n    // to node index map accordingly.\n    Collection.prototype.swapCollectionNodes = function(\n        firstIndex, secondIndex) {\n      if (firstIndex >= this._nodes.length ||\n          secondIndex >= this._nodes.length ||\n          firstIndex < 0 ||\n          secondIndex < 0) {\n        return false;\n      }\n\n      var firstIndexId = this._nodes[firstIndex].getExplorationId();\n      var secondIndexId = this._nodes[secondIndex].getExplorationId();\n      var temp = this._nodes[firstIndex];\n      this._nodes[firstIndex] = this._nodes[secondIndex];\n      this._nodes[secondIndex] = temp;\n\n      this._explorationIdToNodeIndexMap[firstIndexId] = secondIndex;\n      this._explorationIdToNodeIndexMap[secondIndexId] = firstIndex;\n      return true;\n    };\n\n    // Attempts to remove a collection node from this collection given the\n    // specified exploration ID. Returns whether the collection node was\n    // removed, which depends on whether any collection nodes reference the\n    // given exploration ID.\n    Collection.prototype.deleteCollectionNode = function(explorationId) {\n      // TODO(bhenning): Consider whether the removed collection node should be\n      // invalidated, leading to errors if its mutated in the future. This might\n      // help prevent bugs where collection nodes are stored and changed after\n      // being removed from a collection.\n      if (this._explorationIdToNodeIndexMap.hasOwnProperty(explorationId)) {\n        var nodeIndex = this._explorationIdToNodeIndexMap[explorationId];\n        delete this._explorationIdToNodeIndexMap[explorationId];\n        this._nodes.splice(nodeIndex, 1);\n\n        // Update all node exploration ID map references past the removed index\n        // to ensure they are still pointing to correct indexes.\n        for (var i = nodeIndex; i < this._nodes.length; i++) {\n          var nodeExpId = this._nodes[i].getExplorationId();\n          this._explorationIdToNodeIndexMap[nodeExpId] = i;\n        }\n        return true;\n      }\n      return false;\n    };\n\n    // Deletes all collection nodes within this collection.\n    Collection.prototype.clearCollectionNodes = function() {\n      // Clears the existing array in-place, since there may be Angular bindings\n      // to this array and they can\'t be reset to empty arrays.See for context:\n      // http://stackoverflow.com/a/1232046\n      this._nodes.length = 0;\n      this._explorationIdToNodeIndexMap = {};\n    };\n\n    // Returns whether any collection nodes in this collection reference the\n    // provided exploration ID.\n    Collection.prototype.containsCollectionNode = function(explorationId) {\n      return this._explorationIdToNodeIndexMap.hasOwnProperty(explorationId);\n    };\n\n    // Returns a collection node given an exploration ID, or undefined if no\n    // collection node within this collection references the provided\n    // exploration ID.\n    Collection.prototype.getCollectionNodeByExplorationId = function(expId) {\n      return this._nodes[this._explorationIdToNodeIndexMap[expId]];\n    };\n\n    // Returns a list of collection node objects for this collection. Changes to\n    // nodes returned by this function will be reflected in the collection.\n    // Changes to the list itself will not be reflected in this collection.\n    Collection.prototype.getCollectionNodes = function() {\n      return this._nodes.slice();\n    };\n\n    Collection.prototype.getCollectionNodeCount = function() {\n      return this._nodes.length;\n    };\n\n    // Returns the reference to the internal nodes array; this function is only\n    // meant to be used for Angular bindings and should never be used in code.\n    // Please use getCollectionNodes() and related functions, instead. Please\n    // also be aware this exposes internal state of the collection domain\n    // object, so changes to the array itself may internally break the domain\n    // object.\n    Collection.prototype.getBindableCollectionNodes = function() {\n      return this._nodes;\n    };\n\n    // Returns the collection node which is initially available to play\n    // by the player.\n    Collection.prototype.getStartingCollectionNode = function() {\n      if (this._nodes.length === 0) {\n        return null;\n      } else {\n        return this._nodes[0];\n      }\n    };\n\n    // Returns a list of all exploration IDs referenced by this collection.\n    // Changes to the list itself will not be reflected in this collection.\n    Collection.prototype.getExplorationIds = function() {\n      return angular.copy(Object.keys(this._explorationIdToNodeIndexMap));\n    };\n\n\n    // Reassigns all values within this collection to match the existing\n    // collection. This is performed as a deep copy such that none of the\n    // internal, bindable objects are changed within this collection. Note that\n    // the collection nodes within this collection will be completely redefined\n    // as copies from the specified collection.\n    Collection.prototype.copyFromCollection = function(otherCollection) {\n      this._id = otherCollection.getId();\n      this.setTitle(otherCollection.getTitle());\n      this.setCategory(otherCollection.getCategory());\n      this.setObjective(otherCollection.getObjective());\n      this.setLanguageCode(otherCollection.getLanguageCode());\n      this.setTags(otherCollection.getTags());\n      this._version = otherCollection.getVersion();\n      this.clearCollectionNodes();\n\n      var nodes = otherCollection.getCollectionNodes();\n      for (var i = 0; i < nodes.length; i++) {\n        this.addCollectionNode(angular.copy(nodes[i]));\n      }\n    };\n\n    // Static class methods. Note that "this" is not available in static\n    // contexts. This function takes a JSON object which represents a backend\n    // collection python dict.\n    Collection.create = function(collectionBackendObject) {\n      return new Collection(collectionBackendObject);\n    };\n\n    // Create a new, empty collection. This is not guaranteed to pass validation\n    // tests.\n    Collection.createEmptyCollection = function() {\n      return new Collection({\n        nodes: [],\n      });\n    };\n\n    return Collection;\n  }\n]);'

blocks = {}
debug_info = ''