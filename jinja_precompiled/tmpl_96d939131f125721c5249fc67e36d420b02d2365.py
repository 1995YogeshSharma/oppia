from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/training_unresolved_answer_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Teach Oppia</h3>\n</div>\n\n<div class="modal-body">\n  <form name="teachOppiaForm" class="form-inline">\n    <div class="oppia-rule-details-header">\n      <div>\n        <training-panel answer="trainingDataAnswer" answer-feedback="trainingDataFeedback" answer-outcome-dest="trainingDataOutcomeDest" classification="classification" on-finish-training="finishTraining()">\n        </training-panel>\n      </div>\n    <div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-success" ng-click="finishTraining()">Exit</button>\n</div>'

blocks = {}
debug_info = ''