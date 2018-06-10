from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/issues_overview.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div>\n  <span style="font-size: 16px;">\n    <strong>Issues Overview</strong>\n  </span>\n\n  <md-card style="background-color: white; margin: 20px 0px; padding: 8px;">\n    <unresolved-answers-overview/>\n  </md-card>\n</div>'

blocks = {}
debug_info = ''