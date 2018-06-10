from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/classifier/AnswerClassificationResultObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the AnswerClassificationResultObjectFactory.\n */\n\ndescribe(\'Answer classification result object factory\', function() {\n  var oof, acrof;\n  var DEFAULT_OUTCOME_CLASSIFICATION;\n\n  beforeEach(module(\'oppia\'));\n\n  beforeEach(inject(function($injector) {\n    acrof = $injector.get(\'AnswerClassificationResultObjectFactory\');\n    oof = $injector.get(\'OutcomeObjectFactory\');\n    DEFAULT_OUTCOME_CLASSIFICATION = $injector.get(\n      \'DEFAULT_OUTCOME_CLASSIFICATION\');\n  }));\n\n  it(\'should create a new result\', function() {\n    var answerClassificationResult = acrof.createNew(\n      oof.createNew(\'default\', \'\', []), 1, 0, DEFAULT_OUTCOME_CLASSIFICATION\n    );\n\n    expect(answerClassificationResult.outcome).toEqual(\n      oof.createNew(\'default\', \'\', []));\n    expect(answerClassificationResult.answerGroupIndex).toEqual(1);\n    expect(answerClassificationResult.ruleIndex).toEqual(0);\n    expect(answerClassificationResult.classificationCategorization).toEqual(\n      DEFAULT_OUTCOME_CLASSIFICATION);\n  });\n});'

blocks = {}
debug_info = ''