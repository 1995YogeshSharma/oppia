from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/exploration/ParamMetadataObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n* @fileoverview Unit tests for ParamMetadataObjectFactory.\n*/\n\ndescribe(\'ParameterMetadata object factory\', function() {\n  var parameterMetadata = null;\n  var pmof = null;\n  beforeEach(module(\'oppia\'));\n  beforeEach(inject(function($injector) {\n    pmof = $injector.get(\'ParamMetadataObjectFactory\');\n  }));\n\n  it(\'should have correct metadata for SET action\', function() {\n    parameterMetadata = pmof.createWithSetAction(\'answer\', \'param_changes\', 1);\n    expect(parameterMetadata.action).toEqual(\'set\');\n    expect(parameterMetadata.paramName).toEqual(\'answer\');\n    expect(parameterMetadata.source).toEqual(\'param_changes\');\n    expect(parameterMetadata.sourceInd).toEqual(1);\n  });\n\n  it(\'should have correct metadata for GET action\', function() {\n    parameterMetadata = pmof.createWithGetAction(\'x\', \'content\', 5);\n    expect(parameterMetadata.action).toEqual(\'get\');\n    expect(parameterMetadata.paramName).toEqual(\'x\');\n    expect(parameterMetadata.source).toEqual(\'content\');\n    expect(parameterMetadata.sourceInd).toEqual(5);\n  });\n});'

blocks = {}
debug_info = ''