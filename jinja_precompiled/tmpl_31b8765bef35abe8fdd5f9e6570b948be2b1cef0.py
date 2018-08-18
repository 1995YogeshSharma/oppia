from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/state_editor/state_interaction_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div id="tutorialStateInteraction">\n  <md-card style="margin: 20px 0px; padding: 0px;" ng-if="!interactionId">\n    <div class="oppia-add-interaction-button-container">\n      <button type="button" class="btn btn-default btn-lg oppia-add-interaction-button protractor-test-open-add-interaction-modal" ng-click="openInteractionCustomizerModal()">\n        + Add Interaction / End Exploration\n      </button>\n    </div>\n  </md-card>\n\n  <div ng-if="interactionId">\n    <md-card class="oppia-editor-card-with-avatar">\n      <div class="oppia-editor-card-body" title="<[getCurrentInteractionName()]>">\n        <img ng-src="<[userBlueImgUrl]>" alt="" class="oppia-editor-card-avatar">\n        <div class="oppia-editor-card-section-container">\n          <div class="oppia-editor-card-section" style="height: 100%;">\n            <button type="button" class="protractor-test-delete-interaction oppia-delete-interaction-button oppia-transition-200" ng-click="deleteInteraction()" ng-if="EditabilityService.isEditable()">\n              <i class="material-icons md-18">&#xE5CD;</i>\n            </button>\n\n            <div ng-if="hasLoaded" class="protractor-test-interaction" ng-class="{\'oppia-editable-section\': EditabilityService.isEditable()}">\n              <div class="oppia-interaction-preview oppia-transition-200" style="position: absolute; width: 100%; height: 100%;" ng-click="openInteractionCustomizerModal()">\n              </div>\n              <div>\n                <angular-html-bind html-data="interactionPreviewHtml" style="padding: 5px; pointer-events: none;">\n                </angular-html-bind>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </md-card>\n  </div>\n</div>'

blocks = {}
debug_info = ''