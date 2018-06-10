from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/RatingComputationServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Tests that average ratings are being computed correctly.\n */\n\ndescribe(\'Rating computation service\', function() {\n  var RatingComputationService;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(inject(function($injector) {\n    RatingComputationService = $injector.get(\'RatingComputationService\');\n  }));\n\n  it(\n    \'should show an average rating only if there are enough individual ones\',\n    function() {\n      // Don\'t show an average rating if there are too few ratings.\n      expect(RatingComputationService.computeAverageRating({\n        1: 0,\n        2: 0,\n        3: 0,\n        4: 0,\n        5: 0\n      })).toBe(undefined);\n\n      // Show an average rating once the minimum is reached.\n      expect(RatingComputationService.computeAverageRating({\n        1: 1,\n        2: 0,\n        3: 0,\n        4: 0,\n        5: 0\n      })).toBe(1.0);\n\n      // Continue showing an average rating if additional ratings are added.\n      expect(RatingComputationService.computeAverageRating({\n        1: 1,\n        2: 0,\n        3: 0,\n        4: 0,\n        5: 1\n      })).toBe(3.0);\n    }\n  );\n\n  it(\'should compute average ratings correctly\', function() {\n    expect(RatingComputationService.computeAverageRating({\n      1: 6,\n      2: 3,\n      3: 8,\n      4: 12,\n      5: 11\n    })).toBe(3.475);\n  });\n});'

blocks = {}
debug_info = ''