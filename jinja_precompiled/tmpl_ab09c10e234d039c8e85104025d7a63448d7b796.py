from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/learner_local_nav.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<ul class="nav navbar-nav oppia-navbar-nav navbar-right"\n    ng-controller="LearnerLocalNav" style="margin-right: 0px;">\n  <li popover-placement="bottom" uib-popover-template="\'popover/feedback\'" popover-trigger="click">\n    <a href="" class="protractor-test-exploration-feedback-popup-link" uib-tooltip="<[\'I18N_PLAYER_FEEDBACK_TOOLTIP\' | translate]>" tooltip-placement="bottom">\n      <i class="material-icons">&#xE87F;</i>\n      <span class="oppia-icon-accessibility-label"><[\'I18N_PLAYER_FEEDBACK_TOOLTIP\' | translate]></span>\n    </a>\n  </li>\n  <li>\n    <a ng-if="canEdit" ng-href="/create/<[explorationId]>" uib-tooltip="<[\'I18N_PLAYER_EDIT_TOOLTIP\' | translate]>" tooltip-placement="bottom" target="_blank">\n      <i class="material-icons">&#xE254;</i>\n      <span class="oppia-icon-accessibility-label"><[\'I18N_PLAYER_EDIT_TOOLTIP\' | translate]></span>\n    </a>\n    <a ng-if="!canEdit && username" class="protractor-test-exploration-suggestion-popup-link" ng-click="showLearnerSuggestionModal()" uib-tooltip="Suggest Changes" tooltip-placement="bottom" target="_blank">\n      <i class="material-icons">&#xE254;</i>\n      <span class="oppia-icon-accessibility-label">Suggest Changes</span>\n    </a>\n  </li>\n  <li>\n    <a ng-if="username" ng-click="showFlagExplorationModal()" uib-tooltip="<[\'I18N_PLAYER_REPORT_TOOLTIP\' | translate]>" tooltip-placement="bottom" tabindex="0">\n      <i class="material-icons">&#xE153;</i>\n      <span class="oppia-icon-accessibility-label"><[\'I18N_PLAYER_REPORT_TOOLTIP\' | translate]></span>\n    </a>\n  </li>\n</ul>'

blocks = {}
debug_info = ''