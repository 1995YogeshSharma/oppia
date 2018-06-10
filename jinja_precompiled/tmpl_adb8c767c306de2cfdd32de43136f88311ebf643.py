from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/save_validation_fail_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Error Saving Exploration</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    Sorry, an unexpected error occurred. Please refresh the page to\n    return to the most recent draft of your exploration.\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="closeAndRefresh()">\n    Close and Refresh\n  </button>\n</div>'

blocks = {}
debug_info = ''