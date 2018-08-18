from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/exploration_save_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    <span ng-if="isExplorationPrivate">Save Draft</span>\n    <span ng-if="!isExplorationPrivate">Publish Changes</span>\n  </h3>\n</div>\n<div class="modal-body oppia-long-text">\n  <p>\n    <span ng-if="isExplorationPrivate">(Optional)</span>\n    Please enter a brief description of what you have changed:\n    <textarea rows="3" cols="50" ng-model="commitMessage" focus-on="saveChangesModalOpened" class="protractor-test-commit-message-input" autofocus></textarea>\n  </p>\n  <button class="btn btn-default" ng-click="onClickToggleDiffButton()">\n    <span ng-if="!showDiff">Show Changes</span>\n    <span ng-if="showDiff">Hide Changes</span>\n  </button>\n\n  <version-diff-visualization ng-if="showDiff" diff-data="diffData"\n                              earlier-version-header="earlierVersionHeader"\n                              later-version-header="laterVersionHeader">\n  </version-diff-visualization>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-save-draft-button" ng-disabled="!isExplorationPrivate && !commitMessage" ng-click="save(commitMessage)">\n    <span ng-if="isExplorationPrivate">Save Draft</span>\n    <span ng-if="!isExplorationPrivate">Publish Changes</span>\n  </button>\n</div>'

blocks = {}
debug_info = ''