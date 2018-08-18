from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/translation_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-translation-tab">\n  <div class="oppia-translator-overview">\n    <translator-overview is-translation-tab-busy="isTranslationTabBusy"></translator-overview>\n  </div>\n  <div class="row">\n    <div class="col-lg-8 col-md-8 col-sm-8">\n      <state-translation is-translation-tab-busy="isTranslationTabBusy"></state-translation>\n    </div>\n    <div class="col-lg-4 col-md-4 col-sm-4">\n      <div class="oppia-editor-sidebar hidden-xs hidden-sm">\n        <state-translation-status-graph is-translation-tab-busy="isTranslationTabBusy"></state-translation-status-graph>\n      </div>\n    </div>\n    <attribution-guide></attribution-guide>\n  </div>\n</div>'

blocks = {}
debug_info = ''