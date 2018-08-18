from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/TopicsAndSkillsDashboardNavbarBreadcrumbDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Controller for the navbar breadcrumb of the collection editor.\n */\noppia.directive(\'topicsAndSkillsDashboardNavbarBreadcrumb\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {},\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/pages/topics_and_skills_dashboard/\' +\n        \'topics_and_skills_dashboard_navbar_breadcrumb_directive.html\'),\n      controller: [\n        function() {}\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''