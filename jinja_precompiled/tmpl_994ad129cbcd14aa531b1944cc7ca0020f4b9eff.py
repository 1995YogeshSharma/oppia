from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/PlayerPositionService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for keeping track of the learner\'s position.\n */\n\noppia.factory(\'PlayerPositionService\', [\n  \'PlayerTranscriptService\', function(PlayerTranscriptService) {\n    var activeCardIndex = null;\n    var onChangeCallback = null;\n    var learnerJustSubmittedAnAnswer = false;\n\n    return {\n      init: function(callback) {\n        activeCardIndex = null;\n        onChangeCallback = callback;\n      },\n      getCurrentStateName: function() {\n        return PlayerTranscriptService.getCard(activeCardIndex).getStateName();\n      },\n      setActiveCardIndex: function(index) {\n        var oldIndex = activeCardIndex;\n        activeCardIndex = index;\n\n        if (oldIndex !== activeCardIndex) {\n          onChangeCallback();\n        }\n      },\n      getActiveCardIndex: function() {\n        return activeCardIndex;\n      },\n      recordAnswerSubmission: function() {\n        learnerJustSubmittedAnAnswer = true;\n      },\n      recordNavigationButtonClick: function() {\n        learnerJustSubmittedAnAnswer = false;\n      },\n      hasLearnerJustSubmittedAnAnswer: function() {\n        return learnerJustSubmittedAnAnswer;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''