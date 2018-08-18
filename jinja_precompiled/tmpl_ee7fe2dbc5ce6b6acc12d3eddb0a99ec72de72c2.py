from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/response_header_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  response-header .oppia-delete-response-button {\n    cursor: pointer;\n    opacity: 0.5;\n    position: absolute;\n    right: 8px;\n    top: 8px;\n    width: 20px;\n  }\n\n  response-header .oppia-delete-response-button:hover {\n    opacity: 1;\n  }\n\n  response-header .oppia-response-header-block {\n    overflow: hidden;\n    padding-left: 24px;\n    white-space: nowrap;\n  }\n\n  response-header .oppia-nested-link {\n    color: #0844aa;\n    cursor: pointer;\n  }\n  response-header .oppia-nested-link:hover {\n    color: #3f2c76;\n    text-decoration: underline;\n  }\n\n  response-header .oppia-response-header {\n    float: left;\n    overflow: hidden;\n    text-overflow: ellipsis;\n    white-space: nowrap;\n    width: 80%;\n  }\n\n  response-header .oppia-response-tick-cross {\n    margin-bottom: 7px;\n  }\n\n  /* This is to break the line only when screen is too narrow to have both divs\n     in same line.*/\n  @media screen and (min-width: 370px) {\n    response-header .break-in-mobile {\n      display: none;\n    }\n  }\n</style>\n<div class="oppia-response-header-block">\n  <div class="oppia-response-header">\n    <span ng-if="showWarning()">\u26a0</span>\n    <i class="material-icons md-18 oppia-response-tick-cross" ng-if="!isCorrect() && isCorrectnessFeedbackEnabled() && isResponse() && !isCurrentInteractionLinear()">&#x2718;</i>\n    <i class="material-icons md-18 oppia-response-tick-cross" ng-if="isCorrect() && isCorrectnessFeedbackEnabled() && isResponse() && !isCurrentInteractionLinear()">&#10004;</i>\n    <span ng-if="!isActive()" ng-attr-title="<[getSummary()]>">\n      <[getShortSummary()]>\n      <span ng-if="getNumRules() > 1" class="label label-primary" style="position: relative; bottom: 4px;">\n        +<[getNumRules() - 1]>\n      </span>\n    </span>\n    <span ng-if="isActive()">&nbsp;</span>\n  </div>\n\n  <br class="break-in-mobile">\n  <span ng-if="getOutcome()">\u2192</span>\n  <span ng-if="isCorrect() && isInQuestionMode()">\n    Continue\n  </span>\n  <span ng-if="getOutcome() && !isOutcomeLooping() && !isCreatingNewState() && !isInQuestionMode()"\n        ng-click="navigateToState(getOutcome().dest)" class="oppia-nested-link">\n    <[getOutcome().dest]>\n  </span>\n  <span ng-if="getOutcome() && !isOutcomeLooping() && isCreatingNewState()">\n    <em ng-if="getOutcome().newStateName">(<[getOutcome().newStateName]>)</em>\n    <em ng-if="!getOutcome().newStateName">Nowhere yet...</em>\n  </span>\n  <span ng-if="getOutcome() && (isOutcomeLooping() || (!isCorrect() && !getOutcome().dest && isInQuestionMode()))">\n    <em>(try again)</em>\n  </span>\n</div>\n\n<span class="oppia-delete-response-button oppia-transition-200 protractor-test-delete-response"\n      ng-if="EditabilityService.isEditable() && getOnDeleteFn()"\n      ng-click="deleteResponse($event)">\n  <i class="material-icons md-18">&#xE5CD;</i>\n</span>'

blocks = {}
debug_info = ''