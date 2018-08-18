from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/statistics/LearnerActionObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of Learner\n *     Action domain objects.\n */\n\noppia.factory(\'LearnerActionObjectFactory\', [function() {\n  /**\n   * @constructor\n   * @param {string} actionType - type of an action.\n   * @param {Object.<string, *>} actionCustomizationArgs - customization dict\n   *   for an action.\n   * @param {number} schemaVersion - schema version of the class instance.\n   */\n  var LearnerAction = function(\n      actionType, actionCustomizationArgs, schemaVersion) {\n    /** @type {string} */\n    this.actionType = actionType;\n    /** @type {Object.<string, *>} */\n    this.actionCustomizationArgs = actionCustomizationArgs;\n    /** @type {number} */\n    this.schemaVersion = schemaVersion;\n  };\n\n  /**\n   * @property {string} actionType - type of an action\n   * @property {Object.<string, *>} actionCustomizationArgs - customization dict\n   *   for an action\n   * @property {number} schemaVersion - schema version of the class instance\n   * @returns {LearnerAction}\n   */\n  LearnerAction.createNew = function(\n      actionType, actionCustomizationArgs, schemaVersion) {\n    return new LearnerAction(\n      actionType, actionCustomizationArgs, schemaVersion);\n  };\n\n  /**\n   * @typedef LearnerActionBackendDict\n   * @property {string} actionType - type of an action.\n   * @property {Object.<string, *>} actionCustomizationArgs - customization dict\n   *   for an action.\n   * @property {number} schemaVersion - schema version of the class instance.\n   */\n  /**\n   * @param {LearnerActionBackendDict} learnerActionBackendDict\n   * @returns {LearnerAction}\n   */\n  LearnerAction.createFromBackendDict = function(learnerActionBackendDict) {\n    return new LearnerAction(\n      learnerActionBackendDict.action_type,\n      learnerActionBackendDict.action_customization_args,\n      learnerActionBackendDict.schema_version);\n  };\n\n  /** @returns {LearnerActionBackendDict} */\n  LearnerAction.prototype.toBackendDict = function() {\n    return {\n      action_type: this.actionType,\n      action_customization_args: this.actionCustomizationArgs,\n      schema_version: this.schemaVersion\n    };\n  };\n\n  return LearnerAction;\n}]);'

blocks = {}
debug_info = ''