from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/state_param_changes_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div style="margin-top: -5px;">\n  <md-card class="oppia-editor-card-with-avatar">\n    <div class="oppia-editor-card-body">\n      <div class="oppia-editor-card-section protractor-test-state-edit-param-changes">\n        <param-changes-editor param-changes-service="StateParamChangesService"\n                              currently-in-settings-tab="false">\n        </param-changes-editor>\n      </div>\n    </div>\n  </md-card>\n</div>'

blocks = {}
debug_info = ''