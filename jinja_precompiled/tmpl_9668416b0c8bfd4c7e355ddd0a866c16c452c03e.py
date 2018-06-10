from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/ParamSpecsObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2017 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating new frontend instances of ParamSpecs\n * domain objects. ParamSpecs map parameter names to the specifications\n * which defines them (represented as ParamSpec objects).\n */\n\noppia.factory(\'ParamSpecsObjectFactory\', [\n  \'ParamSpecObjectFactory\',\n  function(ParamSpecObjectFactory) {\n    /**\n     * @constructor\n     * @param {Object.<String, ParamSpec>} paramDict - params and their specs\n     *    for this object will hold.\n     */\n    var ParamSpecs = function(paramDict) {\n      /** @member {Object.<String, ParamSpec>} */\n      this._paramDict = paramDict;\n    };\n\n    /**\n     * @param {String} paramName - The parameter to fetch.\n     * @returns {ParamSpec} - associated to given parameter name.\n     */\n    ParamSpecs.prototype.getParamSpec = function(paramName) {\n      return this._paramDict[paramName];\n    };\n\n    /**\n     * @returns {Object.<String, ParamSpec>} - the map of params to their specs.\n     */\n    ParamSpecs.prototype.getParamDict = function() {\n      return this._paramDict;\n    };\n\n    /** @returns {Array.<String>} - The names of the current parameter specs. */\n    ParamSpecs.prototype.getParamNames = function() {\n      return Object.keys(this._paramDict);\n    };\n\n    /**\n     * Adds a new parameter only if it didn\'t exist already. Does nothing\n     * otherwise.\n     *\n     * @param {!String} paramName - The parameter to add a spec for.\n     * @param {ParamSpec=} paramSpec - The specification of the parameter.\n     * @returns {Boolean} - True when the parameter was newly added.\n     */\n    ParamSpecs.prototype.addParamIfNew = function(paramName, paramSpec) {\n      if (!this._paramDict.hasOwnProperty(paramName)) {\n        this._paramDict[paramName] =\n          paramSpec || ParamSpecObjectFactory.createDefault();\n        return true;\n      }\n      return false;\n    };\n\n    /**\n     * @callback callback - Is passed the name and corresponding ParamSpec of\n     *    each parameter in the specs.\n     */\n    ParamSpecs.prototype.forEach = function(callback) {\n      var that = this;\n      this.getParamNames().forEach(function(paramName) {\n        callback(paramName, that.getParamSpec(paramName));\n      });\n    };\n\n    /**\n     * @returns {Object.<String, {obj_type: String}>} - Basic dict for backend\n     *    consumption.\n     */\n    ParamSpecs.prototype.toBackendDict = function() {\n      var paramSpecsBackendDict = {};\n      this.forEach(function(paramName, paramSpec) {\n        paramSpecsBackendDict[paramName] = paramSpec.toBackendDict();\n      });\n      return paramSpecsBackendDict;\n    };\n\n    /**\n     * @param {!Object.<String, {obj_type: String}>} paramSpecsBackendDict -\n     *    Basic dict of backend representation.\n     * @returns {ParamSpecs} - An instance with properties from the backend\n     *    dict.\n     */\n    ParamSpecs.createFromBackendDict = function(paramSpecsBackendDict) {\n      var paramDict = {};\n      Object.keys(paramSpecsBackendDict).forEach(function(paramName) {\n        paramDict[paramName] = ParamSpecObjectFactory.createFromBackendDict(\n          paramSpecsBackendDict[paramName]);\n      });\n      return new ParamSpecs(paramDict);\n    };\n\n    return ParamSpecs;\n  }\n]);'

blocks = {}
debug_info = ''