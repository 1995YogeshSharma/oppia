from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/activities_tab/admin_prod_mode_activities_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card class="oppia-page-card oppia-long-text" style="max-width: 700px">\nThe \'Activities\' tab is not available in the production environment.\n</md-card>'

blocks = {}
debug_info = ''