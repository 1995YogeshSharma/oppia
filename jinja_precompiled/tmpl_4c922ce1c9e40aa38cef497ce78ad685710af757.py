from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/add_or_update_solution_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header protractor-test-add-or-update-solution-modal">\n  <h3><[StateSolutionService.savedMemento !== null ? \'Update Solution\' : \'Add Solution\']></h3>\n</div>\n\n<div class="modal-body">\n  <form name="addSolutionForm.answer"\n        class="form-inline">\n    <div class="oppia-rule-details-header">\n      <select class="protractor-test-answer-is-exclusive-select"\n              ng-model="data.answerIsExclusive"\n              ng-options="(item ? \'The only\' : \'One\') for item in [true, false]">\n      </select> <strong>solution is...</strong>\n      <br>\n      <br>\n      <div>\n        <angular-html-bind class="protractor-test-interaction-html"\n                           html-data="correctAnswerEditorHtml">\n        </angular-html-bind>\n      </div>\n      <br>\n      <md-button class="oppia-learner-confirm-button protractor-test-submit-answer-button"\n                 ng-click="onSubmitFromSubmitButton()"\n                 ng-if="data.correctAnswer === null && shouldAdditionalSubmitButtonBeShown()"\n                 ng-disabled="!answerIsValid">\n        Submit\n      </md-button>\n      <br>\n      <div ng-show="data.correctAnswer !== null">\n        <strong>Explanation:</strong>\n        <schema-based-editor class="protractor-test-explanation-textarea"\n                             schema="EXPLANATION_FORM_SCHEMA"\n                             local-value="data.explanationHtml">\n        </schema-based-editor>\n      </div>\n    </div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-submit-solution-button"\n          ng-click="saveSolution()"\n          ng-disabled="data.correctAnswer === null || !data.explanationHtml || !answerIsValid">\n    Check and Save Solution\n  </button>\n</div>'

blocks = {}
debug_info = ''