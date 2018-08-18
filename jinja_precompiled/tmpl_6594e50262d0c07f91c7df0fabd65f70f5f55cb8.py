from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/creator_dashboard/create_question_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Select topic to create question in</h3>\n  <select ng-model="topicId" ng-options="topicSummary.id as topicSummary.name for topicSummary in topicSummaries"></select>\n  <h3>Create Question</h3>\n</div>\n\n<div class="modal-body">\n  <question-editor question-id="null" question-state-data="questionStateData" misconceptions="misconceptions" can-edit-question="true">\n  </question-editor>\n</div>\n<div class="modal-footer">\n  <span class="oppia-suggestion-review-error"><[errorMessage]></span>\n  <button class="btn btn-default" ng-click="dismissModal()">Cancel</button>\n  <button class="btn btn-success" ng-click="createQuestion()" ng-disabled="!isValidQuestion()">Submit</button>\n</div>'

blocks = {}
debug_info = ''