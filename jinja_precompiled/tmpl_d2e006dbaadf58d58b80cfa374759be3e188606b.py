from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/history_tab/CompareVersionsServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the Compare versions Service.\n */\n\ndescribe(\'Compare versions service\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'compare versions service\', function() {\n    var cvs = null;\n    var vts = null;\n    var treeParents = null;\n    var $httpBackend = null;\n\n    beforeEach(module(\'oppia\', GLOBALS.TRANSLATOR_PROVIDER_FOR_TESTS));\n    beforeEach(function() {\n      mockExplorationData = {\n        explorationId: \'0\'\n      };\n      module(function($provide) {\n        $provide.value(\'ExplorationDataService\', [mockExplorationData][0]);\n      });\n    });\n\n    beforeEach(inject(function($injector) {\n      cvs = $injector.get(\'CompareVersionsService\');\n      vts = $injector.get(\'VersionTreeService\');\n      $httpBackend = $injector.get(\'$httpBackend\');\n    }));\n\n    afterEach(function() {\n      $httpBackend.verifyNoOutstandingExpectation();\n      $httpBackend.verifyNoOutstandingRequest();\n    });\n\n    // Helper function to get states data to pass to getDiffGraphData().\n    // states is an object whose keys are state names and whose values are\n    //  - contentStr: string which is the text content of the state\n    //  - ruleDests: a list of strings which are state names of destinations of\n    //    links\n    // Only information accessed by getDiffGraphData is included in the return\n    // value\n    var _getStatesData = function(statesDetails) {\n      var statesData = {};\n      for (var stateName in statesDetails) {\n        var newStateData = {\n          content: {\n            content_id: \'content\',\n            html: statesDetails[stateName].contentStr\n          },\n          content_ids_to_audio_translations: {\n            content: {},\n            default_outcome: {}\n          },\n          interaction: {\n            answer_groups: [],\n            default_outcome: {\n              dest: \'default\',\n              feedback: {\n                content_id: \'default_outcome\',\n                html: \'\'\n              },\n              labelled_as_correct: false,\n              param_changes: [],\n              refresher_exploration_id: null\n            },\n            hints: []\n          },\n          param_changes: []\n        };\n        newStateData.interaction.answer_groups =\n          statesDetails[stateName].ruleDests.map(function(ruleDestName) {\n            return {\n              outcome: {\n                dest: ruleDestName,\n                feedback: [],\n                labelled_as_correct: false,\n                param_changes: [],\n                refresher_exploration_id: null\n              },\n              rule_specs: []\n            };\n          });\n        statesData[stateName] = newStateData;\n      }\n      return {\n        exploration: {\n          states: statesData\n        }\n      };\n    };\n\n    var testSnapshots1 = [{\n      commit_type: \'create\',\n      version_number: 1\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'A\',\n        new_value: {\n          content_id: \'content\',\n          html: \'Some text\'\n        },\n        old_value: {\n          content_id: \'content\',\n          html: \'\'\n        }\n      }],\n      version_number: 2\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        new_state_name: \'B\',\n        old_state_name: \'A\'\n      }],\n      version_number: 3\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        new_state_name: \'A\',\n        old_state_name: \'B\'\n      }],\n      version_number: 4\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'B\'\n      }],\n      version_number: 5\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        new_state_name: \'C\',\n        old_state_name: \'B\'\n      }],\n      version_number: 6\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'C\',\n        new_value: {\n          content_id: \'content\',\n          html: \'More text\'\n        },\n        old_value: {\n          content_id: \'content\',\n          html: \'\'\n        }\n      }],\n      version_number: 7\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'B\'\n      }],\n      version_number: 8\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'delete_state\',\n        state_name: \'B\'\n      }],\n      version_number: 9\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'B\'\n      }],\n      version_number: 10\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'A\',\n        new_value: {\n          content_id: \'content\',\n          html: \'\'\n        },\n        old_value: {\n          content_id: \'content\',\n          html: \'Some text\'\n        }\n      }],\n      version_number: 11\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        new_state_name: \'D\',\n        old_state_name: \'A\'\n      }],\n      version_number: 12\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'delete_state\',\n        state_name: \'D\'\n      }],\n      version_number: 13\n    }];\n\n    // Information for mock state data for getDiffGraphData() to be passed to\n    // _getStatesData\n    var testExplorationData1 = [{\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      }\n    }, {\n      B: {\n        contentStr: \'Some text\',\n        ruleDests: [\'B\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'Some text\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'Added text\',\n        ruleDests: [\'B\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'Added text\',\n        ruleDests: [\'B\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      B: {\n        contentStr: \'Added text\',\n        ruleDests: [\'B\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'D\']\n      }\n    }, {\n      B: {\n        contentStr: \'Added text\',\n        ruleDests: [\'B\']\n      },\n      C: {\n        contentStr: \'More text\',\n        ruleDests: [\'C\']\n      }\n    }];\n\n    // Tests for getDiffGraphData on linear commits\n    it(\'should detect changed, renamed and added states\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=1\')\n        .respond(_getStatesData(testExplorationData1[0]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=7\')\n        .respond(_getStatesData(testExplorationData1[6]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(1, 7).then(function(data) {\n        nodeData = data.nodes;\n      });\n\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'changed\',\n          originalStateName: \'A\'\n        },\n        2: {\n          newestStateName: \'C\',\n          stateProperty: \'added\',\n          originalStateName: \'B\'\n        }\n      });\n    });\n\n    it(\'should add new state with same name as old name of renamed state\',\n      function() {\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n          .respond(_getStatesData(testExplorationData1[4]));\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=8\')\n          .respond(_getStatesData(testExplorationData1[7]));\n        vts.init(testSnapshots1);\n        var nodeData = null;\n        cvs.getDiffGraphData(5, 8).then(function(data) {\n          nodeData = data.nodes;\n        });\n        $httpBackend.flush();\n        expect(nodeData).toEqual({\n          1: {\n            newestStateName: \'A\',\n            stateProperty: \'unchanged\',\n            originalStateName: \'A\'\n          },\n          2: {\n            newestStateName: \'C\',\n            stateProperty: \'changed\',\n            originalStateName: \'B\'\n          },\n          3: {\n            newestStateName: \'B\',\n            stateProperty: \'added\',\n            originalStateName: \'B\'\n          }\n        });\n      }\n    );\n\n    it(\'should not include added, then deleted state\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=7\')\n        .respond(_getStatesData(testExplorationData1[6]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=9\')\n        .respond(_getStatesData(testExplorationData1[8]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(7, 9).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'A\'\n        },\n        2: {\n          newestStateName: \'C\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'C\'\n        }\n      });\n    });\n\n    it(\'should mark deleted then added states as changed\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=8\')\n        .respond(_getStatesData(testExplorationData1[7]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=10\')\n        .respond(_getStatesData(testExplorationData1[9]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(8, 10).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'A\'\n        },\n        2: {\n          newestStateName: \'B\',\n          stateProperty: \'changed\',\n          originalStateName: \'B\'\n        },\n        3: {\n          newestStateName: \'C\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'C\'\n        }\n      });\n    });\n\n    it(\'should mark renamed then deleted states as deleted\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=11\')\n        .respond(_getStatesData(testExplorationData1[10]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=13\')\n        .respond(_getStatesData(testExplorationData1[12]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(11, 13).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'D\',\n          stateProperty: \'deleted\',\n          originalStateName: \'A\'\n        },\n        2: {\n          newestStateName: \'B\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'B\'\n        },\n        3: {\n          newestStateName: \'C\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'C\'\n        }\n      });\n    });\n\n    it(\'should mark changed state as unchanged when name and content is same\' +\n       \'on both versions\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=1\')\n        .respond(_getStatesData(testExplorationData1[0]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=11\')\n        .respond(_getStatesData(testExplorationData1[10]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(1, 11).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'A\'\n        },\n        2: {\n          newestStateName: \'C\',\n          stateProperty: \'added\',\n          originalStateName: \'B\'\n        },\n        3: {\n          newestStateName: \'B\',\n          stateProperty: \'added\',\n          originalStateName: \'B\'\n        }\n      });\n    });\n\n    it(\'should mark renamed state as not renamed when name is same on both \' +\n       \'versions\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=2\')\n        .respond(_getStatesData(testExplorationData1[1]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=4\')\n        .respond(_getStatesData(testExplorationData1[3]));\n      vts.init(testSnapshots1);\n      var nodeData = null;\n      cvs.getDiffGraphData(2, 4).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'A\'\n        }\n      });\n    });\n\n    it(\'should mark states correctly when a series of changes are applied\',\n      function() {\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=1\')\n          .respond(_getStatesData(testExplorationData1[0]));\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=13\')\n          .respond(_getStatesData(testExplorationData1[12]));\n        vts.init(testSnapshots1);\n        var nodeData = null;\n        cvs.getDiffGraphData(1, 13).then(function(data) {\n          nodeData = data.nodes;\n        });\n        $httpBackend.flush();\n        expect(nodeData).toEqual({\n          1: {\n            newestStateName: \'D\',\n            stateProperty: \'deleted\',\n            originalStateName: \'A\'\n          },\n          2: {\n            newestStateName: \'C\',\n            stateProperty: \'added\',\n            originalStateName: \'B\'\n          },\n          3: {\n            newestStateName: \'B\',\n            stateProperty: \'added\',\n            originalStateName: \'B\'\n          }\n        });\n      }\n    );\n\n    var testSnapshots2 = [{\n      commit_type: \'create\',\n      version_number: 1\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'B\'\n      }],\n      version_number: 2\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        new_state_name: \'C\',\n        old_state_name: \'B\'\n      }],\n      version_number: 3\n    }, {\n      commit_type: \'revert\',\n      commit_cmds: [{\n        cmd: \'AUTO_revert_version_number\',\n        version_number: 2\n      }],\n      version_number: 4\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'delete_state\',\n        state_name: \'B\'\n      }],\n      version_number: 5\n    }, {\n      commit_type: \'revert\',\n      commit_cmds: [{\n        cmd: \'AUTO_revert_version_number\',\n        version_number: 3\n      }],\n      version_number: 6\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'D\'\n      }],\n      version_number: 7\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'D\',\n        new_value: {\n          content_id: \'content\',\n          html: \'Some text\'\n        },\n        old_value: {\n          content_id: \'content\',\n          html: \'\'\n        }\n      }],\n      version_number: 8\n    }];\n\n    // Information for mock state data for getDiffGraphData() to be passed to\n    // _getStatesData\n    var testExplorationData2 = [{\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'C\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'C\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'D\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'C\']\n      },\n      D: {\n        contentStr: \'Some text\',\n        ruleDests: [\'D\']\n      }\n    }];\n\n    // Tests for getDiffGraphData with reversions\n    it(\'should mark states correctly when there is 1 reversion\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=1\')\n        .respond(_getStatesData(testExplorationData2[0]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n        .respond(_getStatesData(testExplorationData2[4]));\n      vts.init(testSnapshots2);\n      var nodeData = null;\n      cvs.getDiffGraphData(1, 5).then(function(data) {\n        nodeData = data.nodes;\n      });\n      $httpBackend.flush();\n      expect(nodeData).toEqual({\n        1: {\n          newestStateName: \'A\',\n          stateProperty: \'unchanged\',\n          originalStateName: \'A\'\n        }\n      });\n    });\n\n    it(\'should mark states correctly when there is 1 reversion to before v1\',\n      function() {\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=3\')\n          .respond(_getStatesData(testExplorationData2[2]));\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n          .respond(_getStatesData(testExplorationData2[4]));\n        vts.init(testSnapshots2);\n        var nodeData = null;\n        cvs.getDiffGraphData(3, 5).then(function(data) {\n          nodeData = data.nodes;\n        });\n        $httpBackend.flush();\n        expect(nodeData).toEqual({\n          1: {\n            newestStateName: \'A\',\n            stateProperty: \'unchanged\',\n            originalStateName: \'A\'\n          },\n          2: {\n            newestStateName: \'B\',\n            stateProperty: \'deleted\',\n            originalStateName: \'C\'\n          }\n        });\n      }\n    );\n\n    it(\'should mark states correctly when compared version is a reversion\',\n      function() {\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=4\')\n          .respond(_getStatesData(testExplorationData2[3]));\n        $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n          .respond(_getStatesData(testExplorationData2[4]));\n        vts.init(testSnapshots2);\n        var nodeData = null;\n        cvs.getDiffGraphData(4, 5).then(function(data) {\n          nodeData = data.nodes;\n        });\n        $httpBackend.flush();\n        expect(nodeData).toEqual({\n          1: {\n            newestStateName: \'A\',\n            stateProperty: \'unchanged\',\n            originalStateName: \'A\'\n          },\n          2: {\n            newestStateName: \'B\',\n            stateProperty: \'deleted\',\n            originalStateName: \'B\'\n          }\n        });\n      }\n    );\n\n    it(\'should mark states correctly when there are 2 reversions\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n        .respond(_getStatesData(testExplorationData2[4]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=8\')\n        .respond(_getStatesData(testExplorationData2[7]));\n      vts.init(testSnapshots2);\n      cvs.getDiffGraphData(5, 8).then(function(data) {\n        expect(data.nodes).toEqual({\n          1: {\n            newestStateName: \'A\',\n            stateProperty: \'unchanged\',\n            originalStateName: \'A\'\n          },\n          2: {\n            newestStateName: \'C\',\n            stateProperty: \'added\',\n            originalStateName: \'B\'\n          },\n          3: {\n            newestStateName: \'D\',\n            stateProperty: \'added\',\n            originalStateName: \'D\'\n          }\n        });\n      });\n      $httpBackend.flush();\n    });\n\n    // Represents snapshots and exploration data for tests for links\n    // Only includes information accessed by getDiffGraphData()\n    var testSnapshots3 = [{\n      commit_type: \'create\',\n      version_number: 1\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'B\'\n      }],\n      version_number: 2\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'C\'\n      }],\n      version_number: 3\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'rename_state\',\n        old_state_name: \'C\',\n        new_state_name: \'D\'\n      }],\n      version_number: 4\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'D\'\n      }],\n      version_number: 5\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'edit_state_property\',\n        state_name: \'D\'\n      }],\n      version_number: 6\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'delete_state\',\n        state_name: \'D\'\n      }],\n      version_number: 7\n    }, {\n      commit_type: \'edit\',\n      commit_cmds: [{\n        cmd: \'add_state\',\n        state_name: \'D\'\n      }],\n      version_number: 8\n    }];\n\n    var testExplorationData3 = [{\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\', \'C\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      },\n      C: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\', \'D\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\', \'D\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'D\', \'END\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'D\', \'END\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'A\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }, {\n      A: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      B: {\n        contentStr: \'\',\n        ruleDests: [\'D\', \'END\']\n      },\n      D: {\n        contentStr: \'\',\n        ruleDests: [\'B\']\n      },\n      END: {\n        contentStr: \'\',\n        ruleDests: [\'END\']\n      }\n    }];\n\n    it(\'should correctly display added links\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=1\')\n        .respond(_getStatesData(testExplorationData3[0]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=2\')\n        .respond(_getStatesData(testExplorationData3[1]));\n      vts.init(testSnapshots3);\n      var linkData = null;\n      cvs.getDiffGraphData(1, 2).then(function(data) {\n        linkData = data.links;\n      });\n      $httpBackend.flush();\n      expect(linkData).toEqual([{\n        source: 1,\n        target: 3,\n        linkProperty: \'added\'\n      }, {\n        source: 3,\n        target: 2,\n        linkProperty: \'added\'\n      }]);\n    });\n\n    it(\'should correctly display deleted links\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n        .respond(_getStatesData(testExplorationData3[4]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=6\')\n        .respond(_getStatesData(testExplorationData3[5]));\n      vts.init(testSnapshots3);\n      var linkData = null;\n      cvs.getDiffGraphData(5, 6).then(function(data) {\n        linkData = data.links;\n      });\n      $httpBackend.flush();\n      expect(linkData).toEqual([{\n        source: 1,\n        target: 2,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 1,\n        target: 3,\n        linkProperty: \'deleted\'\n      }, {\n        source: 2,\n        target: 3,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 2,\n        target: 4,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 3,\n        target: 1,\n        linkProperty: \'unchanged\'\n      }]);\n    });\n\n    it(\'should correctly display links on renamed states\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=3\')\n        .respond(_getStatesData(testExplorationData3[2]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=5\')\n        .respond(_getStatesData(testExplorationData3[4]));\n      vts.init(testSnapshots3);\n      var linkData = null;\n      cvs.getDiffGraphData(3, 5).then(function(data) {\n        linkData = data.links;\n      });\n      $httpBackend.flush();\n      expect(linkData).toEqual([{\n        source: 1,\n        target: 2,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 1,\n        target: 3,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 2,\n        target: 3,\n        linkProperty: \'added\'\n      }, {\n        source: 2,\n        target: 4,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 3,\n        target: 1,\n        linkProperty: \'unchanged\'\n      }]);\n    });\n\n    it(\'should correctly display added, then deleted links\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=2\')\n        .respond(_getStatesData(testExplorationData3[1]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=7\')\n        .respond(_getStatesData(testExplorationData3[6]));\n      vts.init(testSnapshots3);\n      var linkData = null;\n      cvs.getDiffGraphData(2, 7).then(function(data) {\n        linkData = data.links;\n      });\n      $httpBackend.flush();\n      expect(linkData).toEqual([{\n        source: 1,\n        target: 2,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 2,\n        target: 3,\n        linkProperty: \'unchanged\'\n      }]);\n    });\n\n    it(\'should correctly display deleted, then added links\', function() {\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=6\')\n        .respond(_getStatesData(testExplorationData3[5]));\n      $httpBackend.expect(\'GET\', \'/explorehandler/init/0?v=8\')\n        .respond(_getStatesData(testExplorationData3[7]));\n      vts.init(testSnapshots3);\n      var linkData = null;\n      cvs.getDiffGraphData(6, 8).then(function(data) {\n        linkData = data.links;\n      });\n      $httpBackend.flush();\n      expect(linkData).toEqual([{\n        source: 1,\n        target: 2,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 2,\n        target: 3,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 2,\n        target: 4,\n        linkProperty: \'unchanged\'\n      }, {\n        source: 3,\n        target: 1,\n        linkProperty: \'deleted\'\n      }, {\n        source: 3,\n        target: 2,\n        linkProperty: \'added\'\n      }]);\n    });\n  });\n});'

blocks = {}
debug_info = ''