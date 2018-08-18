from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/stateful/FocusManagerServiceSpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Unit tests for the FocusManagerService.\n */\n\ndescribe(\'Focus Manager Service\', function() {\n  var FocusManagerService;\n  var DeviceInfoService;\n  var IdGenerationService;\n  var rootScope;\n  var $timeout;\n  var clearLabel;\n  var focusLabel = \'FocusLabel\';\n  var focusLabelTwo = \'FocusLabelTwo\';\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(inject(function($injector) {\n    clearLabel = $injector.get(\'LABEL_FOR_CLEARING_FOCUS\');\n    FocusManagerService = $injector.get(\'FocusManagerService\');\n    DeviceInfoService = $injector.get(\'DeviceInfoService\');\n    IdGenerationService = $injector.get(\'IdGenerationService\');\n    rootScope = $injector.get(\'$rootScope\');\n    $timeout = $injector.get(\'$timeout\');\n    spyOn(rootScope, \'$broadcast\');\n  }));\n\n  it(\'should generate a random string for focus label\', function() {\n    spyOn(IdGenerationService, \'generateNewId\');\n    FocusManagerService.generateFocusLabel();\n    expect(IdGenerationService.generateNewId).toHaveBeenCalled();\n  });\n\n  it(\'should set focus label and broadcast it\', function() {\n    FocusManagerService.setFocus(focusLabel);\n    $timeout(function() {\n      expect(rootScope.$broadcast).toHaveBeenCalledWith(\'focusOn\', focusLabel);\n    });\n    $timeout.flush();\n  });\n\n  it(\'should not set focus label if _nextLabelToFocusOn is set\', function() {\n    FocusManagerService.setFocus(focusLabel);\n    expect(FocusManagerService.setFocus(focusLabelTwo)).toEqual(undefined);\n    $timeout.flush();\n    $timeout.verifyNoPendingTasks();\n    expect(rootScope.$broadcast).toHaveBeenCalledWith(\'focusOn\', focusLabel);\n  });\n\n  it(\'should set label to clear focus and broadcast it\', function() {\n    FocusManagerService.clearFocus();\n    $timeout(function() {\n      expect(rootScope.$broadcast).toHaveBeenCalledWith(\'focusOn\', clearLabel);\n    });\n    $timeout.flush();\n  });\n\n  it(\'should set focus label if on desktop and broadcast it\', function() {\n    FocusManagerService.setFocusIfOnDesktop(focusLabel);\n    if (!DeviceInfoService.isMobileDevice()) {\n      $timeout(function() {\n        expect(rootScope.$broadcast).toHaveBeenCalledWith(\n          \'focusOn\', focusLabel);\n      });\n      $timeout.flush();\n    }\n  });\n});'

blocks = {}
debug_info = ''