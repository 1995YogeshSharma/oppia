from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/teach_oppia_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Enter a Sample Answer</h3>\n</div>\n\n<div class="modal-body">\n  <div class="oppia-rule-details-header">\n    <test-interaction-panel state-content="stateContent" input-template="inputTemplate" on-submit-answer="submitAnswer(answer)">\n    </test-interaction-panel>\n\n    <div ng-if="trainingDataAnswer" style="padding-top: 10px; border-top: 1px solid #e5e5e5;">\n      <form name="testOppiaForm" class="form-inline">\n        <training-panel ng-if="classification.answerGroupIndex >= 0" answer="trainingDataAnswer" answer-feedback="trainingDataFeedback" answer-outcome-dest="trainingDataOutcomeDest" classification="classification" on-finish-training="finishTeaching(true)">\n        </training-panel>\n      </form>\n      <div ng-if="classification.answerGroupIndex === -1">\n        <div>\n          <span><strong>If Oppia encounters the answer:</strong></span>\n        </div>\n\n        <div>\n          <div angular-html-bind="answerTemplate">\n          </div>\n        </div>\n\n        <br>\n\n        <div>\n          <span><strong>it will reply with:</strong></span>\n        </div>\n\n        <div>\n          <div angular-html-bind="trainingDataFeedback">\n          </div>\n        </div>\n\n        <br>\n\n        <div>\n          <span><strong>and then direct the learner to: </strong></span>\n          <span angular-html-bind="trainingDataOutcomeDest"></span>\n        </div>\n\n        <br>\n\n        <div>\n          <span><strong>This is due to a specific rule and therefore cannot be trained. If you do not think this is right, you should change the rule directly referring to this answer.</strong></span>\n        </div>\n      </div>\n    </div>\n  <div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="finishTeaching(false)">Exit</button>\n</div>'

blocks = {}
debug_info = ''