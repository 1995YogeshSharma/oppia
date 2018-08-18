from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/add_answer_group_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header protractor-test-add-response-modal-header">\n  <h3>Add Response</h3>\n</div>\n\n<div class="modal-body">\n  <form name="addAnswerGroupForm.outcomeDetailsForm" class="form-inline protractor-test-add-response-details">\n    <div class="oppia-rule-details-header">\n      <strong>If the learner\'s answer...</strong>\n    </div>\n\n    <rule-editor rule="tmpRule" is-editable="EditabilityService.isEditable()" is-editing-rule-inline="false">\n    </rule-editor>\n\n    <br>\n\n    <div ng-if="!feedbackEditorIsOpen && !isLinearWithNoFeedback(tmpOutcome)"\n         title="Edit feedback"\n         style="height: 100%; margin-right: 22px;">\n      <div class="oppia-rule-details-header oppia-editable-section">\n        <div class="oppia-rule-preview oppia-transition-200">\n          <div class="oppia-click-to-start-editing protractor-test-open-feedback-editor" ng-click="openFeedbackEditor()">\n            <i class="material-icons oppia-editor-edit-icon pull-right" title="Edit Feedback">&#xE254;</i>\n          </div>\n          <strong>Oppia tells the learner...</strong>\n          <div style="position: relative;">\n            <span style="color: #888">\n              <em>Nothing</em>\n            </span>\n          </div>\n        </div>\n      </div>\n    </div>\n\n    <div ng-if="feedbackEditorIsOpen">\n      <outcome-feedback-editor outcome="tmpOutcome">\n      </outcome-feedback-editor>\n    </div>\n    <br>\n\n    <outcome-destination-editor outcome="tmpOutcome"\n                                ng-if="!questionModeEnabled"\n                                outcome-has-feedback="!isLinearWithNoFeedback(tmpOutcome)"\n                                add-state="addState">\n    </outcome-destination-editor>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default protractor-test-close-add-response-modal" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-add-new-response" ng-click="saveResponse(false)" ng-disabled="addAnswerGroupForm.outcomeDetailsForm.$invalid || isSelfLoopWithNoFeedback(tmpOutcome)">Save Response</button>\n  <button class="btn btn-success" ng-click="saveResponse(true)" ng-disabled="addAnswerGroupForm.outcomeDetailsForm.$invalid || isSelfLoopWithNoFeedback(tmpOutcome)">Save and Add Another</button>\n</div>'

blocks = {}
debug_info = ''