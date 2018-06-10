from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/error/disabled_exploration.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/error/disabled_exploration.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-content">\n    <br>\n\n    <div class="oppia-wide-panel">\n      <div class="oppia-wide-panel-content protractor-test-error-container">\n        <h1 translate="I18N_ERROR_DISABLED_EXPLORATION"></h1>\n        <br>\n        <span translate="I18N_ERROR_DISABLED_EXPLORATION_MESSAGE"></span>\n        <span translate="I18N_ERROR_NEXT_STEPS" translate-values="{issueTrackerUrl: \'https://github.com/oppia/oppia/issues/new\', homeUrl: \'/\'}"></span>\n      </div>\n    </div>\n\n  </div>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  I18N_ERROR_DISABLED_EXPLORATION_PAGE_TITLE\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

blocks = {'content': block_content, 'maintitle': block_maintitle, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&10=17&6=24&3=31'