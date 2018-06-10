from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/settings_tab/collection_settings_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<!-- Collection details -->\n<div class="oppia-page-cards-container">\n  <md-card class="oppia-page-card oppia-long-text">\n    <h2>Collection Settings</h2>\n    <collection-details-editor></collection-details-editor>\n  </md-card>\n</div>\n<div class="oppia-page-cards-container">\n  <collection-permissions-card></collection-permissions-card>\n</div>'

blocks = {}
debug_info = ''