from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/AnswerClassificationServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the answer classification service\n */\n\ndescribe(\'Answer classification service with string classifier disabled\',\n  function() {\n    beforeEach(module(\'oppia\'));\n\n    beforeEach(function() {\n      module(function($provide) {\n        $provide.constant(\'INTERACTION_SPECS\', {\n          RuleTest: {\n            is_trainable: false\n          }\n        });\n        $provide.constant(\'ENABLE_ML_CLASSIFIERS\', false);\n      });\n    });\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n    var EXPLICIT_CLASSIFICATION, DEFAULT_OUTCOME_CLASSIFICATION;\n    var acs, sof, oof, acrof, stateName, state;\n    beforeEach(inject(function($injector) {\n      acs = $injector.get(\'AnswerClassificationService\');\n      sof = $injector.get(\'StateObjectFactory\');\n      oof = $injector.get(\'OutcomeObjectFactory\');\n      acrof = $injector.get(\'AnswerClassificationResultObjectFactory\');\n      EXPLICIT_CLASSIFICATION = $injector.get(\'EXPLICIT_CLASSIFICATION\');\n      DEFAULT_OUTCOME_CLASSIFICATION = $injector.get(\n        \'DEFAULT_OUTCOME_CLASSIFICATION\');\n\n      stateName = \'stateName\';\n      state = sof.createFromBackendDict(stateName, {\n        content: {\n          html: \'content\',\n          audio_translations: {}\n        },\n        interaction: {\n          id: \'RuleTest\',\n          answer_groups: [{\n            outcome: {\n              dest: \'outcome 1\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            rule_specs: [{\n              inputs: {\n                x: 10\n              },\n              rule_type: \'Equals\'\n            }]\n          }, {\n            outcome: {\n              dest: \'outcome 2\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            rule_specs: [{\n              inputs: {\n                x: 5\n              },\n              rule_type: \'Equals\'\n            }, {\n              inputs: {\n                x: 7\n              },\n              rule_type: \'NotEquals\'\n            }, {\n              inputs: {\n                x: 6\n              },\n              rule_type: \'Equals\'\n            }]\n          }],\n          default_outcome: {\n            dest: \'default\',\n            feedback: {\n              html: \'\',\n              audio_translations: {}\n            },\n            labelled_as_correct: false,\n            param_changes: [],\n            refresher_exploration_id: null\n          },\n          hints: []\n        },\n        param_changes: []\n      });\n    }));\n\n    var explorationId = \'exploration\';\n\n    var rules = {\n      Equals: function(answer, inputs) {\n        return inputs.x === answer;\n      },\n      NotEquals: function(answer, inputs) {\n        return inputs.x !== answer;\n      }\n    };\n\n    it(\'should fail if no frontend rules are provided\', function() {\n      expect(function() {\n        acs.getMatchingClassificationResult(explorationId, stateName, state, 0);\n      }).toThrow();\n    });\n\n    it(\'should return the first matching answer group and first matching rule\' +\n       \'spec\', function() {\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 10, rules)\n      ).toEqual(acrof.createNew(\n        oof.createNew(\'outcome 1\', \'\', []), 0, 0, EXPLICIT_CLASSIFICATION\n      ));\n\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 5, rules)\n      ).toEqual(acrof.createNew(\n        oof.createNew(\'outcome 2\', \'\', []), 1, 0, EXPLICIT_CLASSIFICATION\n      ));\n\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 6, rules)\n      ).toEqual(acrof.createNew(\n        oof.createNew(\'outcome 2\', \'\', []), 1, 1, EXPLICIT_CLASSIFICATION\n      ));\n    });\n\n    it(\'should return the default rule if no answer group matches\', function() {\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 7, rules)\n      ).toEqual(acrof.createNew(\n        oof.createNew(\'default\', \'\', []), 2, 0, DEFAULT_OUTCOME_CLASSIFICATION\n      ));\n    });\n\n    it(\'should fail if no answer group matches and no default rule is \' +\n       \'provided\', function() {\n      var state2 = sof.createFromBackendDict(stateName, {\n        content: {\n          html: \'content\',\n          audio_translations: {}\n        },\n        interaction: {\n          id: \'RuleTest\',\n          answer_groups: [{\n            outcome: {\n              dest: \'outcome 1\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            rule_specs: [{\n              inputs: {\n                x: 10\n              },\n              rule_type: \'Equals\'\n            }]\n          }],\n          default_outcome: {\n            dest: \'default\',\n            feedback: {\n              html: \'\',\n              audio_translations: {}\n            },\n            labelled_as_correct: false,\n            param_changes: [],\n            refresher_exploration_id: null\n          },\n          hints: []\n        },\n        param_changes: []\n      });\n\n      expect(function() {\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 0);\n      }).toThrow();\n    });\n  });\n\ndescribe(\'Answer classification service with string classifier enabled\',\n  function() {\n    beforeEach(module(\'oppia\'));\n\n    beforeEach(function() {\n      module(function($provide) {\n        $provide.constant(\'INTERACTION_SPECS\', {\n          TrainableInteraction: {\n            is_trainable: true\n          },\n          UntrainableInteraction: {\n            is_trainable: false\n          }\n        });\n        $provide.constant(\'ENABLE_ML_CLASSIFIERS\', true);\n        $provide.factory(\'PredictionSampleService\', [function() {\n          return {\n            predict: function(classifierData, answer) {\n              return 1;\n            }\n          };\n        }]);\n      });\n    });\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n    var EXPLICIT_CLASSIFICATION, DEFAULT_OUTCOME_CLASSIFICATION,\n      STATISTICAL_CLASSIFICATION;\n    var acs, scms, sof, oof, acrof, $stateName, state, state2,\n      registryService, stateClassifierMapping;\n    beforeEach(inject(function($injector) {\n      acs = $injector.get(\'AnswerClassificationService\');\n      scms = $injector.get(\'StateClassifierMappingService\');\n      sof = $injector.get(\'StateObjectFactory\');\n      oof = $injector.get(\'OutcomeObjectFactory\');\n      acrof = $injector.get(\'AnswerClassificationResultObjectFactory\');\n      EXPLICIT_CLASSIFICATION = $injector.get(\'EXPLICIT_CLASSIFICATION\');\n      DEFAULT_OUTCOME_CLASSIFICATION = $injector.get(\n        \'DEFAULT_OUTCOME_CLASSIFICATION\');\n      STATISTICAL_CLASSIFICATION = $injector.get(\'STATISTICAL_CLASSIFICATION\');\n      registryService = $injector.get(\'PredictionAlgorithmRegistryService\');\n\n      stateName = \'stateName\';\n      state = sof.createFromBackendDict(stateName, {\n        content: {\n          html: \'content\',\n          audio_translations: {}\n        },\n        interaction: {\n          id: \'TrainableInteraction\',\n          answer_groups: [{\n            outcome: {\n              dest: \'outcome 1\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            rule_specs: [{\n              inputs: {\n                x: 10\n              },\n              rule_type: \'Equals\'\n            }]\n          }, {\n            outcome: {\n              dest: \'outcome 2\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            rule_specs: [{\n              inputs: {\n                x: 5\n              },\n              rule_type: \'Equals\'\n            }, {\n              inputs: {\n                x: 7\n              },\n              rule_type: \'Equals\'\n            }]\n          }],\n          default_outcome: {\n            dest: \'default\',\n            feedback: {\n              html: \'\',\n              audio_translations: {}\n            },\n            labelled_as_correct: false,\n            param_changes: [],\n            refresher_exploration_id: null\n          },\n          hints: []\n        },\n        param_changes: []\n      });\n\n      stateClassifierMapping = {\n        stateName: {\n          algorithm_id: \'TestClassifier\',\n          classifier_data: {},\n          data_schema_version: 1\n        }\n      };\n      scms.init(stateClassifierMapping);\n\n      registryService.setMapping({\n        TestClassifier: {\n          v1: \'PredictionSampleService\'\n        }\n      });\n\n      state2 = angular.copy(state);\n      state2.interaction.id = \'UntrainableInteraction\';\n    }));\n\n    var explorationId = \'exploration\';\n\n    var rules = {\n      Equals: function(answer, inputs) {\n        return inputs.x === answer;\n      },\n      NotEquals: function(answer, inputs) {\n        return inputs.x !== answer;\n      }\n    };\n\n    it(\'should query the prediction service if no answer group matches and \' +\n       \'interaction is trainable\', function() {\n      // The prediction result is the same as default until there is a mapping\n      // in PredictionAlgorithmRegistryService.\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, 0, rules)\n      ).toEqual(\n        acrof.createNew(\n          state.interaction.answerGroups[1].outcome, 1, null,\n          STATISTICAL_CLASSIFICATION)\n      );\n    });\n\n    it(\'should return the default rule if no answer group matches and \' +\n       \'interaction is not trainable\', function() {\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state2, 0, rules)\n      ).toEqual(acrof.createNew(\n        oof.createNew(\'default\', \'\', []), 2, 0, DEFAULT_OUTCOME_CLASSIFICATION\n      ));\n    });\n  }\n);\n\ndescribe(\'Answer classification service with training data classification\',\n  function() {\n    beforeEach(module(\'oppia\'));\n\n    beforeEach(function() {\n      module(function($provide) {\n        $provide.constant(\'INTERACTION_SPECS\', {\n          TrainableInteraction: {\n            is_trainable: true\n          }\n        });\n        $provide.constant(\'ENABLE_ML_CLASSIFIERS\', true);\n        $provide.constant(\'ENABLE_TRAINING_DATA_CLASSIFICATION\', true);\n      });\n    });\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n\n    var EXPLICIT_CLASSIFICATION, TRAINING_DATA_CLASSIFICATION;\n    var acs, sof, oof, acrof, $stateName, state, state2,\n      registryService, stateClassifierMapping;\n    beforeEach(inject(function($injector) {\n      acs = $injector.get(\'AnswerClassificationService\');\n      sof = $injector.get(\'StateObjectFactory\');\n      oof = $injector.get(\'OutcomeObjectFactory\');\n      acrof = $injector.get(\'AnswerClassificationResultObjectFactory\');\n      TRAINING_DATA_CLASSIFICATION = $injector.get(\n        \'TRAINING_DATA_CLASSIFICATION\');\n      EXPLICIT_CLASSIFICATION = $injector.get(\'EXPLICIT_CLASSIFICATION\');\n\n      stateName = \'stateName\';\n      state = sof.createFromBackendDict(stateName, {\n        content: {\n          html: \'content\',\n          audio_translations: {}\n        },\n        interaction: {\n          id: \'TrainableInteraction\',\n          answer_groups: [{\n            outcome: {\n              dest: \'outcome 1\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            training_data: [\'abc\', \'input\'],\n            rule_specs: [{\n              inputs: {\n                x: \'equal\'\n              },\n              rule_type: \'Equals\'\n            }]\n          }, {\n            outcome: {\n              dest: \'outcome 2\',\n              feedback: {\n                html: \'\',\n                audio_translations: {}\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            training_data: [\'xyz\'],\n            rule_specs: [{\n              inputs: {\n                x: \'npu\'\n              },\n              rule_type: \'Contains\'\n            }]\n          }],\n          default_outcome: {\n            dest: \'default\',\n            feedback: {\n              html: \'\',\n              audio_translations: {}\n            },\n            labelled_as_correct: false,\n            param_changes: [],\n            refresher_exploration_id: null\n          },\n          hints: []\n        },\n        param_changes: []\n      });\n    }));\n\n    var explorationId = \'exploration\';\n\n    var rules = {\n      Equals: function(answer, input) {\n        return answer === input;\n      },\n      Contains: function(answer, input) {\n        return answer.toLowerCase().indexOf(\n          input.x.toLowerCase()) !== -1;\n      }\n    };\n\n    it(\'should use training data classification if no answer group matches \' +\n       \'and interaction is trainable\', function() {\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, \'abc\', rules)\n      ).toEqual(\n        acrof.createNew(\n          state.interaction.answerGroups[0].outcome, 0, null,\n          TRAINING_DATA_CLASSIFICATION)\n      );\n\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, \'xyz\', rules)\n      ).toEqual(\n        acrof.createNew(\n          state.interaction.answerGroups[1].outcome, 1, null,\n          TRAINING_DATA_CLASSIFICATION)\n      );\n    });\n\n    it(\'should perform explicit classification before doing training data \' +\n      \'classification\', function() {\n      expect(\n        acs.getMatchingClassificationResult(\n          explorationId, stateName, state, \'input\', rules)\n      ).toEqual(\n        acrof.createNew(\n          state.interaction.answerGroups[1].outcome, 1, 0,\n          EXPLICIT_CLASSIFICATION)\n      );\n    });\n  }\n);'

blocks = {}
debug_info = ''