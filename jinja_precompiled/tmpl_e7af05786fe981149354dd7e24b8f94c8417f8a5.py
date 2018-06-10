from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_navbar_breadcrumb_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<ul class="nav navbar-nav oppia-navbar-breadcrumb ng-cloak">\n  <li>\n    <span class="oppia-navbar-breadcrumb-separator"></span>\n    <span ng-if="navbarTitle">\n      <[navbarTitle]>\n      <span class="oppia-navbar-breadcrumb-separator" style="margin-left: 5px;"></span>\n      <span>\n        <[getCurrentTabName()]>\n      </span>\n    </span>\n    <span ng-if="navbarTitle === \'\'" ng-click="editTitle()" style="opacity: 0.6;">\n      Untitled Exploration\n    </span>\n    <span ng-if="navbarTitle === null">\n      Loading...\n    </span>\n  </li>\n</ul>'

blocks = {}
debug_info = ''