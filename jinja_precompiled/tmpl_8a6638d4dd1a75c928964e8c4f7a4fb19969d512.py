from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/delete_audio_translation_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h4 class="modal-title">Confirmation Required</h4>\n</div>\n<div class="modal-body">\n  <p>Are you sure you want to delete this audio?</p>\n</div>\n<div class="modal-footer">\n  <button type="button" ng-click="cancel()" class="btn btn-default">Cancel</button>\n  <button type="button" ng-click="reallyDelete()" class="btn btn-danger protractor-test-confirm-discard-changes">Delete</button>\n</div>'

blocks = {}
debug_info = ''