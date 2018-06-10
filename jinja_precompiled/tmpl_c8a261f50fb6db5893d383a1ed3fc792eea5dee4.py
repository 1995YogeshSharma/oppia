from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/settings_tab/delete_exploration_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Delete Exploration</h3>\n</div>\n\n<div class="modal-body">\n  <p>Really delete this exploration? <strong>This action cannot be reversed.</strong></p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-danger protractor-test-really-delete-exploration-button" ng-click="reallyDelete()">Delete Exploration</button>\n</div>'

blocks = {}
debug_info = ''