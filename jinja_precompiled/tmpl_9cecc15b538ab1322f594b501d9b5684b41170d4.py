from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/editor_tab.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="row">\n  <div class="col-lg-8 col-md-8 col-sm-8">\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/exploration_editor_tab.html', 'pages/exploration_editor/editor_tab/editor_tab.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </div>\n  <div class="col-lg-4 col-md-4 col-sm-4">\n    <div class="oppia-editor-sidebar hidden-xs hidden-sm">\n      '
    template = environment.get_template('pages/exploration_editor/editor_tab/exploration_graph.html', 'pages/exploration_editor/editor_tab/editor_tab.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n      <unresolved-answers-overview></unresolved-answers-overview>\n    </div>\n  </div>\n  <attribution-guide></attribution-guide>\n</div>'

blocks = {}
debug_info = '3=11&7=15'