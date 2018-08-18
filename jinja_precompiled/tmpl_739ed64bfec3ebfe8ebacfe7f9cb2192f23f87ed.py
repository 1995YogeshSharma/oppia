from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/unresolved_answers_overview_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  unresolved-answers-overview .answer-container {\n    vertical-align: text-bottom;\n  }\n  unresolved-answers-overview .refresh-container {\n    font-size: 0.8em;\n    text-align: right;\n  }\n  unresolved-answers-overview .refresh-container a {\n    font-weight: bold;\n  }\n</style>\n\n<div ng-if="isUnresolvedAnswersOverviewShown()">\n  <span style="font-size: 16px;">\n    <strong>Issues Overview</strong>\n  </span>\n  <md-card style="background-color: white; margin: 20px 0; padding: 8px;">\n    <strong>Unresolved Student Answers</strong>\n    <ul>\n      <li ng-repeat="data in getUnresolvedStateStats()" class="answer-container">\n        <strong>(<[data.frequency]> times)</strong>: <span ng-bind-html="data.answerHtml"></span>\n      </li>\n      <li ng-if="getUnresolvedStateStats().length === 0">\n        <em>No outstanding answers require attention.</em>\n      </li>\n    </ul>\n  </md-card>\n\n  <md-card style="margin: 20px 0px; padding: 0px;" ng-if="SHOW_TRAINABLE_UNRESOLVED_ANSWERS && isCurrentInteractionTrainable()">\n    <div ng-if="isEditableOutsideTutorialMode() && !isCurrentInteractionLinear()">\n      <button type="button" class="btn btn-default btn-lg oppia-add-response-button protractor-test-open-teach-modal" ng-click="openTeachOppiaModal()">\n        Train Oppia\n      </button>\n    </div>\n  </md-card>\n</div>'

blocks = {}
debug_info = ''