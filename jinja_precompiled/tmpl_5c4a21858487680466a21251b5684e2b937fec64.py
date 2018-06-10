from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/create_button/create_activity_button_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-navbar-button-container">\n  <!-- User must complete the registration process. -->\n  <button class="btn oppia-navbar-button oppia-navbar-hide-on-small-width protractor-test-create-activity oppia-transition-200"\n          ng-click="onRedirectToLogin(\'/creator_dashboard?mode=create\')" ng-if="!userIsLoggedIn">\n    <span class="oppia-navbar-tab-content" translate="I18N_CREATE_EXPLORATION_CREATE"></span>\n  </button>\n  <button class="btn oppia-navbar-button oppia-navbar-hide-on-small-width protractor-test-create-activity oppia-transition-200"\n          ng-click="initCreationProcess()" ng-disabled="creationInProgress" ng-if="userIsLoggedIn">\n    <span class="oppia-navbar-tab-content" translate="I18N_CREATE_EXPLORATION_CREATE"></span>\n  </button>\n  <button class="btn oppia-navbar-button oppia-navbar-hide-on-small-width oppia-transition-200"\n          ng-click="showUploadExplorationModal()" ng-disabled="creationInProgress" ng-if="allowYamlFileUpload && userIsLoggedIn">\n    <span class="oppia-navbar-tab-content" translate="I18N_CREATE_EXPLORATION_UPLOAD"></span>\n  </button>\n</div>'

blocks = {}
debug_info = ''