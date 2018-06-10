from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/outcome_destination_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="form-inline protractor-test-dest-bubble" style="margin-bottom: 10px;">\n  <div class="oppia-rule-details-header">\n    <strong ng-if="outcomeHasFeedback">And afterwards, directs the learner to...</strong>\n    <strong ng-if="!outcomeHasFeedback">Oppia directs the learner to...</strong>\n  </div>\n  <div class="form-group" style="font-size: 1.1em;">\n    <span>\n      <select class="form-control" ng-model="outcome.dest" ng-options="choice.id as choice.text for choice in destChoices" style="width: 200px;" ng-change="onDestSelectorChange()">\n      </select>\n    </span>\n  </div>\n  <ng-form name="newStateNameForm">\n    <span ng-if="isCreatingNewState(outcome)">\n      <input type="text" focus-on="newStateNameInputField" name="newStateName" ng-model="outcome.newStateName" class="form-control protractor-test-add-state-input" tabindex="0" aria-invalid="false" ng-pattern="newStateNamePattern" required>\n    </span>\n    <p ng-show="newStateNameForm.newStateName.$error.pattern" class="help-block oppia-form-error" style="font-size: 0.85em;">Please pick a card name consisting of alphanumeric characters, spaces and/or hyphens.</p>\n  </ng-form>\n\n  <div ng-if="isSelfLoop() && canEditRefresherExplorationId" style="margin-top: 12px;">\n    <b>Refresher exploration ID (optional):</b>\n    <input type="text" name="refresherExplorationId" ng-model="outcome.refresherExplorationId" class="form-control protractor-test-add-refresher-exploration-id" tabindex="0" aria-invalid="false" ng-pattern="explorationIdPattern">\n  </div>\n</div>'

blocks = {}
debug_info = ''