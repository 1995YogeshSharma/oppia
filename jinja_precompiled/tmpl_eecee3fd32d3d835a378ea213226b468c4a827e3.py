from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/topics_and_skills_dashboard_navbar_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<ul class="nav navbar-nav oppia-navbar-nav navbar-right ng-cloak" style="margin-right: 0em;">\n\n  <li ng-mouseover="blurNavigationLinks($event)">\n    <div class="oppia-navbar-button-container">\n      <button ng-click="createTopic()" ng-if="userCanCreateTopic"\n              class="btn oppia-navbar-button oppia-transition-200">\n        <span class="oppia-navbar-tab-content">Create Topic</span>\n      </button>\n    </div>\n  </li>\n  <li ng-mouseover="blurNavigationLinks($event)">\n    <div class="oppia-navbar-button-container">\n      <button ng-click="createSkill()" ng-if="userCanCreateSkill"\n              class="btn oppia-navbar-button oppia-transition-200">\n        <span class="oppia-navbar-tab-content">Create Skill</span>\n      </button>\n    </div>\n  </li>\n</ul>'

blocks = {}
debug_info = ''