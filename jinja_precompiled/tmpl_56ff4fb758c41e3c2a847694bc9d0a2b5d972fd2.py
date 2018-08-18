from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/ExplorationEditorTabSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the controller of the \'State Editor\'.\n */\n\ndescribe(\'Exploration editor tab controller\', function() {\n  describe(\'ExplorationEditorTab\', function() {\n    var scope, ecs, ess, scs;\n\n    beforeEach(module(\'oppia\'));\n    beforeEach(inject(function($controller, $injector, $rootScope) {\n      scope = $rootScope.$new();\n      rootScope = $injector.get(\'$rootScope\');\n      spyOn(rootScope, \'$broadcast\');\n      ecs = $injector.get(\'StateEditorService\');\n      ess = $injector.get(\'ExplorationStatesService\');\n      scs = $injector.get(\'StateContentService\');\n\n      ess.init({\n        \'First State\': {\n          content: {\n            content_id: \'content\',\n            html: \'First State Content\'\n          },\n          content_ids_to_audio_translations: {\n            content: {},\n            default_outcome: {},\n            feedback_1: {}\n          },\n          interaction: {\n            id: \'TextInput\',\n            answer_groups: [{\n              rule_specs: [],\n              outcome: {\n                dest: \'unused\',\n                feedback: {\n                  content_id: \'feedback_1\',\n                  html: \'\'\n                },\n                labelled_as_correct: false,\n                param_changes: [],\n                refresher_exploration_id: null\n              }\n            }],\n            default_outcome: {\n              dest: \'default\',\n              feedback: {\n                content_id: \'default_outcome\',\n                html: \'\'\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            hints: []\n          },\n          param_changes: []\n        },\n        \'Second State\': {\n          content: {\n            content_id: \'content\',\n            html: \'Second State Content\'\n          },\n          content_ids_to_audio_translations: {\n            content: {},\n            default_outcome: {},\n            feedback_1: {}\n          },\n          interaction: {\n            id: \'TextInput\',\n            answer_groups: [{\n              rule_specs: [],\n              outcome: {\n                dest: \'unused\',\n                feedback: {\n                  content_id: \'feedback_1\',\n                  html: \'\'\n                },\n                labelled_as_correct: false,\n                param_changes: [],\n                refresher_exploration_id: null\n              }\n            }],\n            default_outcome: {\n              dest: \'default\',\n              feedback: {\n                content_id: \'default_outcome\',\n                html: \'\'\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            hints: []\n          },\n          param_changes: []\n        },\n        \'Third State\': {\n          content: {\n            content_id: \'content\',\n            html: \'This is some content.\'\n          },\n          content_ids_to_audio_translations: {\n            content: {},\n            default_outcome: {},\n            feedback_1: {}\n          },\n          interaction: {\n            id: \'TextInput\',\n            answer_groups: [{\n              rule_specs: [],\n              outcome: {\n                dest: \'unused\',\n                feedback: {\n                  content_id: \'feedback_1\',\n                  html: \'\'\n                },\n                labelled_as_correct: false,\n                param_changes: [],\n                refresher_exploration_id: null\n              }\n            }],\n            default_outcome: {\n              dest: \'default\',\n              feedback: {\n                content_id: \'default_outcome\',\n                html: \'\'\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            hints: []\n          },\n          param_changes: [{\n            name: \'comparison\',\n            generator_id: \'Copier\',\n            customization_args: {\n              value: \'something clever\',\n              parse_with_jinja: false\n            }\n          }]\n        }\n      });\n\n      $controller(\'ExplorationEditorTab\', {\n        $scope: scope,\n        ExplorationStatesService: ess\n      });\n    }));\n\n    it(\'should correctly broadcast the stateEditorInitialized flag with \' +\n       \'the state data\', function() {\n      ecs.setActiveStateName(\'Third State\');\n      scope.initStateEditor();\n      expect(\n        rootScope.$broadcast\n      ).toHaveBeenCalledWith(\n        \'stateEditorInitialized\', ess.getState(\'Third State\')\n      );\n    });\n  });\n});'

blocks = {}
debug_info = ''