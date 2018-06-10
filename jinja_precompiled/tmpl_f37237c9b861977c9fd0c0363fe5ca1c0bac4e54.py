from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/feedback_tab/editor_create_feedback_thread_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Start New Feedback Thread</h3>\n</div>\n\n<div class="modal-body">\n  <p>Thread subject: <input type="text" ng-model="newThreadSubject"></p>\n  <p>Message text <textarea ng-model="newThreadText" rows="6"></textarea></p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-success" ng-click="create(newThreadSubject, newThreadText)" ng-disabled="!newThreadSubject || !newThreadText">Create Thread</button>\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n</div>'

blocks = {}
debug_info = ''