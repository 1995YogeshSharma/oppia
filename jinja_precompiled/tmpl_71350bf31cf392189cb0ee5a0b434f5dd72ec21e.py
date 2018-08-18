from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/story_editor/story_editor_navbar_breadcrumb_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="nav navbar-nav oppia-navbar-breadcrumb ng-cloak">\n  <span class="oppia-navbar-breadcrumb-separator"></span>\n  <span>\n    <[story.getTitle()]> (v<[story.getVersion()]>)\n  </span>\n</div>'

blocks = {}
debug_info = ''