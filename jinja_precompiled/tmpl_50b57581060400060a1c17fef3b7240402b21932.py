from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/story_editor/save_pending_changes_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-body">\n  <p>\n    Please save all pending changes before returning to the topic.\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Ok</button>\n</div>'

blocks = {}
debug_info = ''