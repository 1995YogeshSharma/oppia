from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/state_statistics.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-controller="StateStatistics">\n  <div ng-if="SHOW_TRAINABLE_UNRESOLVED_ANSWERS && isInteractionTrainable && trainingDataButtonContentsList.length > 0">\n    <div class="oppia-editor-header">\n      <strong>Learner Answers to Teach Oppia</strong>\n    </div>\n\n    <button type="button" ng-repeat="trainingDataButtonContents in trainingDataButtonContentsList" class="btn btn-default protractor-test-train-unresolved-answer oppia-unresolved-answer-button" ng-click="openTrainUnresolvedAnswerModal($index)">\n      <angular-html-bind html-data="trainingDataButtonContents.answerHtml">\n      </angular-html-bind>\n      <span style="margin-left: 8px;">\n        <em><[trainingDataButtonContents.frequency]> time<span ng-if="trainingDataButtonContents.frequency != 1">s</span></em>\n      </span>\n    </button>\n  </div>\n</div>'

blocks = {}
debug_info = ''