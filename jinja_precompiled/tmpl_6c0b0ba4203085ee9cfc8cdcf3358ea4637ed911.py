from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/skill_editor_save_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Save Draft\n  </h3>\n</div>\n<div class="modal-body oppia-long-text">\n  <p>\n    Please enter a brief description of what you have changed:\n    <textarea rows="3" cols="50" ng-model="commitMessage" focus-on="saveChangesModalOpened" class="protractor-test-commit-message-input" autofocus></textarea>\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-close-save-modal-button" ng-disabled="!commitMessage" ng-click="save(commitMessage)">\n    <span>Save Draft</span>\n  </button>\n</div>'

blocks = {}
debug_info = ''