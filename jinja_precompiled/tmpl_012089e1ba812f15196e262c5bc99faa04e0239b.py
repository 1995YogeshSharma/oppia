from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/signup/signup.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/signup/signup.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <!-- NOTE: This page should not contain any direct anchors to internal links. If the user visits an internal\n  link before completing the signup process, they will be logged out.\n  -->\n\n  <div class="oppia-page-cards-container" ng-controller="Signup">\n    <md-card class="oppia-page-card">\n      <h2 class="oppia-signup-page-title" translate="I18N_SIGNUP_COMPLETE_REGISTRATION"></h2>\n\n      <form>\n        <div ng-show="!hasUsername" role="form" class="form-horizontal">\n          <div class="form-group">\n            <label for="username" class="col-lg-3 col-md-3 col-sm-3" translate="I18N_SIGNUP_USERNAME"></label>\n\n            <div class="col-lg-9 col-md-9 col-sm-9">\n              <input type="text" ng-model="username" id="username" class="form-control protractor-test-username-input" ng-blur="onUsernameInputFormBlur(username)" ng-change="updateWarningText(username)" ng-trim="false" focus-on="usernameInputField" style="width: 260px;" autofocus="true">\n              <span class="help-block" style="font-size: 0.8em;" translate="I18N_SIGNUP_USERNAME_EXPLANATION"></span>\n              <div style="height: 18px; width: 550px;">\n                <span style="color: red; font-size: 0.8em;" aria-live="assertive" ng-show="blurredAtLeastOnce">\n                  <[warningI18nCode | translate]>\n                </span>\n              </div>\n            </div>\n          </div>\n\n          <div ng-show="showEmailPreferencesForm" class="form-group">\n            <label for="canReceiveEmailUpdates" class="col-lg-3 col-md-3 col-sm-3" translate="I18N_SIGNUP_EMAIL_PREFERENCES"></label>\n            <div class="col-lg-9 col-md-9 col-sm-9">\n              <div class="radio">\n                <label>\n                  <input type="radio" ng-model="canReceiveEmailUpdates" value="yes" name="canReceiveEmailUpdates" ng-change="onSelectEmailPreference()">\n                  <span translate="I18N_SIGNUP_SEND_ME_NEWS"></span>\n                </label>\n                <label>\n                  <input type="radio" ng-model="canReceiveEmailUpdates" value="no" name="canReceiveEmailUpdates" ng-change="onSelectEmailPreference()">\n                  <span translate="I18N_SIGNUP_DO_NOT_SEND_EMAILS"></span>\n                </label>\n                <span class="help-block" style="font-size: smaller" translate="I18N_SIGNUP_EMAIL_PREFERENCES_EXPLAIN">\n                </span>\n              </div>\n              <div style="height: 18px; width: 550px;">\n                <span style="color: red; font-size: 0.8em;" aria-live="assertive" ng-show="blurredAtLeastOnce" translate="<[emailPreferencesWarningText]>">\n                </span>\n              </div>\n            </div>\n          </div>\n          <hr>\n        </div>\n\n        <div class="oppia-long-text" ng-if="hasEverRegistered">\n          <p>\n            <em translate="I18N_SIGNUP_UPDATE_WARNING"></em>\n          </p>\n        </div>\n        <div class="oppia-long-text" ng-if="!hasEverRegistered">\n          <p style="font-size: 1em;" translate="I18N_SIGNUP_SITE_DESCRIPTION" translate-values="{sitename: siteName}">\n\n          </p>\n        </div>\n\n        <div>\n          <strong translate="I18N_SIGNUP_CC_TITLE"></strong>\n          <br>\n          <span translate="I18N_SIGNUP_LICENSE_NOTE" translate-compile></span>\n        </div>\n\n        <hr>\n\n        <div class="checkbox oppia-long-text">\n          <label>\n            <input type="checkbox" ng-model="hasAgreedToLatestTerms"\n                   class="protractor-test-agree-to-terms-checkbox">\n            <span translate="I18N_SIGNUP_AGREE_LICENSE_DESCRIPTION" translate-value-sitename="<[siteName]>">\n            </span>\n          </label>\n        </div>\n\n        <br>\n\n        <button type="submit" class="btn btn-success protractor-test-register-user"\n                ng-disabled="warningI18nCode || !hasAgreedToLatestTerms || submissionInProcess"\n                ng-click="submitPrerequisitesForm(hasAgreedToLatestTerms, username, canReceiveEmailUpdates)"\n                translate="I18N_SIGNUP_BUTTON_SUBMIT">\n        </button>\n      </form>\n    </md-card>\n  </div>\n\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/signup/Signup.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  I18N_SIGNUP_PAGE_TITLE\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    l_0_CAN_SEND_EMAILS = resolve('CAN_SEND_EMAILS')
    t_1 = environment.filters['js_string']
    pass
    yield u'\n  %s\n  <script type="text/javascript">\n    GLOBALS.CAN_SEND_EMAILS = JSON.parse(\n      \'%s\');\n  </script>\n' % (
        escape(context.call(l_0_super)), 
        escape(t_1((undefined(name='CAN_SEND_EMAILS') if l_0_CAN_SEND_EMAILS is missing else l_0_CAN_SEND_EMAILS))), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      <span translate="I18N_SIGNUP_REGISTRATION"></span>\n    </li>\n  </ul>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&24=17&114=24&115=31&3=34&16=41&17=50&20=51&7=54'