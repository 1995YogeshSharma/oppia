from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/editor_tab/skill_editor_main_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-if="hasLoadedSkill()" class="col-lg-8 col-md-8 col-sm-8">\n  <skill-description-editor></skill-description-editor>\n  <skill-concept-card-editor></skill-concept-card-editor>\n  <skill-misconceptions-editor></skill-misconceptions-editor>\n</div>'

blocks = {}
debug_info = ''