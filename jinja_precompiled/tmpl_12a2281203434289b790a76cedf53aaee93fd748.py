from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/delete_hint_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Delete Hint</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    Are you sure you want to delete this hint?\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-danger protractor-test-confirm-delete-hint"\n          ng-click="reallyDelete()">\n    Delete Hint\n  </button>\n</div>'

blocks = {}
debug_info = ''