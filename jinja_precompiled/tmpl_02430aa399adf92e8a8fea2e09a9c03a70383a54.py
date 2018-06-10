from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/sidebar/SidebarStatusService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2015 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for maintaining the open/closed status of the\n * hamburger-menu sidebar.\n */\n\noppia.factory(\'SidebarStatusService\', [\n  \'WindowDimensionsService\', function(WindowDimensionsService) {\n    var pendingSidebarClick = false;\n    var sidebarIsShown = false;\n\n    var _openSidebar = function() {\n      if (WindowDimensionsService.isWindowNarrow() && !sidebarIsShown) {\n        sidebarIsShown = true;\n        pendingSidebarClick = true;\n      }\n    };\n\n    var _closeSidebar = function() {\n      if (sidebarIsShown) {\n        sidebarIsShown = false;\n        pendingSidebarClick = false;\n      }\n    };\n\n    return {\n      isSidebarShown: function() {\n        return sidebarIsShown;\n      },\n      openSidebar: function() {\n        _openSidebar();\n      },\n      closeSidebar: function() {\n        _closeSidebar();\n      },\n      toggleSidebar: function() {\n        if (!sidebarIsShown) {\n          _openSidebar();\n        } else {\n          _closeSidebar();\n        }\n      },\n      onDocumentClick: function() {\n        if (!pendingSidebarClick) {\n          sidebarIsShown = false;\n        } else {\n          pendingSidebarClick = false;\n        }\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''