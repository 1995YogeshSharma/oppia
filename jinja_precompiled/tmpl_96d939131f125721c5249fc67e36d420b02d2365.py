from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/training_unresolved_answer_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Select Oppia\'s Response</h3>\n</div>\n\n<div class="modal-body">\n  <form name="teachOppiaForm" class="form-inline">\n    <div class="oppia-rule-details-header">\n      <div>\n        <training-panel answer="trainingDataAnswer"  classification="classification" on-finish-training="finishTraining()" adding-new-response="addingNewResponse">\n        </training-panel>\n      </div>\n    </div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="exitTrainer()">Cancel</button>\n  <button class="btn btn-default btn-success" ng-if="classification.answerGroupIndex >= 0 && !addingNewResponse" ng-click="onConfirm()">Confirm Response</button>\n</div>'

blocks = {}
debug_info = ''