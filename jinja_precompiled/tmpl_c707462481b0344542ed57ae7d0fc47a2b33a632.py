from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/top_navigation_bar/top_navigation_bar_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="navbar-header protractor-test-navbar-header pull-left">\n  <a ng-if="windowIsNarrow" ng-click="toggleSidebar()"\n     class="navbar-brand oppia-navbar-menu oppia-transition-200 protractor-mobile-test-navbar-button"\n     tabindex="0">\n    <i class="material-icons oppia-navbar-menu-icon" ng-if="!isSidebarShown()" >&#xE5D2;</i>\n    <i class="material-icons oppia-navbar-close-icon" ng-if="isSidebarShown()" >&#10005;</i>\n  </a>\n\n  <a class="oppia-navbar-brand-name oppia-transition-200 protractor-test-oppia-main-logo" href="/"\n     focus-on="<[::LABEL_FOR_CLEARING_FOCUS]>">\n    <img ng-src="<[getStaticImageUrl(\'/logo/288x128_logo_white.png\')]>" class="oppia-logo"\n         ng-class="windowIsNarrow ? \'oppia-logo-small\' : \'oppia-logo-wide\'" alt="Oppia Home">\n  </a>\n  <!-- This is needed for the correct image to appear when an exploration is shared using G+. -->\n  <a style="display: none;">\n    <img ng-src="<[getStaticImageUrl(\'/logo/288x128_logo_mint.png\')]>" itemprop="image" alt="Oppia Home">\n  </a>\n</div>\n\n<div ng-cloak class="navbar-header pull-right" ng-if="userMenuIsShown">\n  <ul class="nav oppia-navbar-nav" ng-if="standardNavIsShown">\n    <ul ng-if="windowIsNarrow" class="nav oppia-navbar-tabs-narrow">\n      <create-activity-button></create-activity-button>\n    </ul>\n    <ul ng-if="!windowIsNarrow" class="nav oppia-navbar-tabs">\n      <li ng-show="navElementsVisibilityStatus.I18N_TOPNAV_LIBRARY" class="oppia-clickable-navbar-element">\n        <a ng-mouseover="blurNavigationLinks($event)" class="oppia-navbar-tab oppia-navbar-tab-content" href="/library" translate="I18N_TOPNAV_LIBRARY"></a>\n      </li>\n      <li ng-class="{\'open\' : activeMenuName === \'aboutMenu\'}" uib-dropdown ng-show="navElementsVisibilityStatus.I18N_TOPNAV_ABOUT" class="oppia-navbar-clickable-dropdown protractor-test-about-oppia-list-item">\n        <a ng-keydown="onMenuKeypress($event, \'aboutMenu\', {shiftTab: ACTION_CLOSE, enter: ACTION_OPEN})" class="oppia-navbar-tab"\n           role="menuitem"\n           aria-haspopup="true"\n           aria-expanded="false"\n           tabindex="0"\n           ng-mouseover="openSubmenu($event, \'aboutMenu\')"\n           ng-mouseleave="closeSubmenuIfNotMobile($event)">\n          <span class="oppia-navbar-tab-content" translate="I18N_TOPNAV_ABOUT"></span>\n          <span class="caret"></span>\n        </a>\n        <ul uib-dropdown-menu class="uib-dropdown-menu oppia-navbar-dropdown"\n            ng-mouseover="openSubmenu($event, \'aboutMenu\')"\n            ng-mouseleave="closeSubmenuIfNotMobile($event)"\n            role="menu">\n          <li><a ng-keydown="onMenuKeypress($event, \'aboutMenu\', {shiftTab: ACTION_CLOSE})" class="oppia-navbar-tab-content protractor-test-about-link" href="/about" translate="I18N_TOPNAV_ABOUT_OPPIA"></a></li>\n          <li><a class="oppia-navbar-tab-content protractor-test-get-started-link " href="/get_started" translate="I18N_TOPNAV_GET_STARTED"></a></li>\n          <li><a class="oppia-navbar-tab-content protractor-test-playbook-link " href="/teach#playbook" translate="I18N_TOPNAV_PARTICIPATION_PLAYBOOK"></a></li>\n          <li><a class="oppia-navbar-tab-content" href="https://medium.com/oppia-org" target="_blank"  translate="I18N_TOPNAV_BLOG">Blog</a></li>\n          <li><a class="oppia-navbar-tab-content" href="http://oppiafoundation.org"  target="_blank" translate="I18N_TOPNAV_OPPIA_FOUNDATION"></a></li>\n          <li><a ng-keydown="onMenuKeypress($event, \'aboutMenu\', {tab: ACTION_CLOSE})" class="oppia-navbar-tab-content" href="http://oppiafoundation.org/get-involved" target="_blank" translate="I18N_TOPNAV_GET_INVOLVED"></a></li>\n        </ul>\n      </li>\n      <li ng-mouseover="blurNavigationLinks($event)" ng-show="navElementsVisibilityStatus.I18N_TOPNAV_DONATE">\n        <div class="oppia-navbar-button-container">\n          <a href="/donate"\n             class="btn oppia-navbar-button oppia-navbar-hide-on-small-width oppia-transition-200">\n            <span class="oppia-navbar-tab-content" translate="I18N_TOPNAV_DONATE"></span>\n          </a>\n        </div>\n      </li>\n      <create-activity-button ng-mouseover="blurNavigationLinks($event)" ng-show="navElementsVisibilityStatus.I18N_CREATE_EXPLORATION_CREATE"></create-activity-button>\n    </ul>\n  </ul>\n  <ul class="nav oppia-navbar-nav oppia-navbar-profile">\n    <li ng-class="{\'open\' : activeMenuName === \'profileMenu\'}" uib-dropdown ng-if="username" class="protractor-test-profile-dropdown">\n      <a uib-dropdown-toggle class="oppia-navbar-dropdown-toggle"\n         ng-mouseover="openSubmenu($event, \'profileMenu\')"\n         ng-mouseleave="closeSubmenuIfNotMobile($event)"\n         ng-keydown="onMenuKeypress($event, \'profileMenu\', {shiftTab: ACTION_CLOSE, enter: ACTION_OPEN})"\n         role="menuitem"\n         aria-haspopup="true"\n         aria-expanded="false"\n         aria-label="User Menu"\n         tabindex="0">\n        <div class="oppia-navbar-profile-picture-container">\n          <span ng-if="profilePictureDataUrl">\n            <img ng-src="<[profilePictureDataUrl]>" class="oppia-navbar-profile-picture img-circle" alt="User Avatar">\n            <span class="caret"></span>\n          </span>\n          <span ng-if="!profilePictureDataUrl">\n            <i class="material-icons md-40" style="margin-top: -1px;">&#xE853;</i>\n            <span class="oppia-icon-accessibility-label">User Avatar</span>\n            <span class="caret" style="margin-top: -26px;"></span>\n          </span>\n\n          <div class="oppia-navbar-dashboard-indicator ng-cloak" ng-if="numUnseenNotifications > 0">\n            <span class="oppia-navbar-dashboard-indicator-text">\n              <[numUnseenNotifications]>\n            </span>\n          </div>\n\n          <div class="oppia-navbar-role-indicator" ng-if="isAdmin || isModerator">\n            <!--\n             "right: 4px;" is necessary here but not in moderator to prevent \'A\'\n             from appearing off-center because \'A\' is slightly thinner than \'M\' in\n             this font.\n            -->\n            <span ng-if="isAdmin" class="oppia-navbar-role-text" style="right: 4px;">A</span>\n            <span ng-if="isModerator && !isAdmin" class="oppia-navbar-role-text">M</span>\n          </div>\n        </div>\n      </a>\n\n      <ul uib-dropdown-menu class="uib-dropdown-menu ng-cloak oppia-navbar-dropdown" role="menu"\n          ng-mouseover="openSubmenu($event, \'profileMenu\')"\n          ng-mouseleave="closeSubmenuIfNotMobile($event)">\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event)" ng-href="<[profilePageUrl]>"\n             class="protractor-test-profile-link"\n             ng-keydown="onMenuKeypress($event, \'profileMenu\', {shiftTab: ACTION_CLOSE})">\n            <strong><[username]></strong>\n          </a>\n        </li>\n        <hr class="oppia-top-right-menu-item-separator">\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event)" href="/creator_dashboard"\n             class="protractor-test-dashboard-link protractor-test-creator-dashboard-link">\n            <span translate="I18N_TOPNAV_CREATOR_DASHBOARD"></span>\n          </a>\n        </li>\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event)" href="/learner_dashboard"\n             class="protractor-test-dashboard-link protractor-test-learner-dashboard-link">\n            <span translate="I18N_TOPNAV_LEARNER_DASHBOARD"></span>\n          </a>\n        </li>\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event)" href="/notifications_dashboard"\n             class="protractor-test-notifications-link">\n            <span translate="I18N_TOPNAV_NOTIFICATIONS"></span>\n            <span ng-if="numUnseenNotifications > 0">\n              (<[numUnseenNotifications]>)\n            </span>\n          </a>\n        </li>\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event)" href="/preferences"\n             class="protractor-test-preferences-link">\n            <span translate="I18N_TOPNAV_PREFERENCES"></span>\n          </a>\n        </li>\n        <li ng-if="isModerator">\n          <a ng-click="closeSubmenuIfNotMobile($event)" href="/moderator" target="_blank">\n            <span translate="I18N_TOPNAV_MODERATOR_PAGE"></span>\n          </a>\n        </li>\n        <li ng-if="isSuperAdmin">\n          <a class="protractor-test-admin-link" ng-click="closeSubmenuIfNotMobile($event)" href="/admin" target="_blank">\n            <span translate="I18N_TOPNAV_ADMIN_PAGE"></span>\n          </a>\n        </li>\n\n        <hr class="oppia-top-right-menu-item-separator">\n\n        <li>\n          <a ng-click="closeSubmenuIfNotMobile($event);onLogoutButtonClicked()" ng-href="<[logoutUrl]>"\n             ng-keydown="onMenuKeypress($event, \'profileMenu\', {tab: ACTION_CLOSE})">\n            <span translate="I18N_TOPNAV_LOGOUT"></span>\n          </a>\n        </li>\n      </ul>\n    </li>\n\n    <li uib-dropdown ng-if="!username" class="oppia-navbar-clickable-dropdown">\n      <div class="oppia-navbar-button-container" style="margin-right: 10px;">\n        <button class="btn oppia-navbar-button protractor-mobile-test-login"\n                ng-click="onLoginButtonClicked()">\n          <span translate="I18N_TOPNAV_SIGN_IN"></span>\n          <span class="caret"></span>\n        </button>\n      </div>\n      <ul uib-dropdown-menu class="uib-dropdown-menu oppia-navbar-dropdown" role="menu"\n          style="margin-right: 15px; padding: 0;">\n        <li>\n          <a href="" style="padding: 0; width: 190px;" ng-click="onLoginButtonClicked()">\n            <div class="oppia-signin-google">\n              <div class="oppia-signin-g-icon">\n                <img ng-src="<[googleSignInIconUrl]>">\n              </div>\n              <span class="oppia-signin-text" translate="I18N_TOPNAV_SIGN_IN_WITH_GOOGLE"></span>\n            </div>\n          </a>\n        </li>\n      </ul>\n    </li>\n  </ul>\n</div>\n<style>\n  .oppia-navbar-brand-name:focus {\n    outline: 1px dotted #fff;\n    outline: auto 5px -webkit-focus-ring-color;\n  }\n  top-navigation-bar .oppia-signin-google {\n    background-color: #FFFFFF;\n    border-radius: 5px;\n    border-width: 0;\n    box-shadow: 1px 1px 0px 1px rgba(0,0,0,0.05);\n    color: #737373;\n    font-family: Roboto, arial, sans-serif;\n    font-size: 14px;\n    font-weight: bold;\n    height: 40px;\n    padding-left: 8px;\n    padding-right: 8px;\n    vertical-align: middle;\n    white-space: nowrap;\n  }\n  top-navigation-bar .oppia-signin-google:focus,\n  top-navigation-bar .oppia-signin-google:hover {\n    box-shadow: 1px 4px 5px 1px rgba(0,0,0,0.1);\n  }\n  top-navigation-bar .oppia-signin-google:active {\n    background-color: #e5e5e5;\n    box-shadow: none;\n    transition-duration: 10ms;\n  }\n  top-navigation-bar .oppia-signin-g-icon {\n    float: left;\n    padding: 10px 24px 10px 0;\n  }\n  top-navigation-bar .oppia-navbar-menu-icon {\n    color: #fff;\n    margin-top: -5px;\n  }\n  top-navigation-bar .oppia-navbar-dashboard-indicator-text {\n    bottom: 0;\n    color: white;\n    font-size: 1.12rem;\n    font-weight: bold;\n    position: absolute;\n    right: 4px;\n  }\n  top-navigation-bar .oppia-navbar-clickable-dropdown:hover ul.uib-dropdown-menu {\n    display: block;\n  }\n  top-navigation-bar .oppia-navbar-role-text {\n    bottom: 0;\n    color: white;\n    font-size: 11px;\n    font-weight: bold;\n    position: absolute;\n    right: 3px;\n  }\n  top-navigation-bar .oppia-navbar-dashboard-indicator {\n    background-color: #f7a541;\n    border-radius: 20px;\n    height: 15px;\n    position: absolute;\n    right: 25px;\n    top: 8px;\n    width: 15px;\n  }\n  top-navigation-bar .oppia-navbar-menu {\n    margin-left: 10px;\n    opacity: 0.9;\n    outline-color: transparent;\n    padding-top: 20px;\n  }\n  top-navigation-bar .oppia-navbar-menu:hover {\n    opacity: 1;\n  }\n  top-navigation-bar .oppia-navbar-menu:focus {\n    outline: 1px dotted #212121;\n    outline: auto 5px -webkit-focus-ring-color;\n  }\n  top-navigation-bar .oppia-navbar-profile {\n    float: right;\n  }\n  top-navigation-bar .oppia-navbar-role-indicator {\n    background-color: #f7a541;\n    border-radius: 20px;\n    bottom: 10px;\n    height: 15px;\n    position: absolute;\n    right: 25px;\n    width: 15px;\n  }\n  top-navigation-bar .oppia-navbar-close-icon {\n    color: #fff;\n    margin-right: 4px;\n    margin-top: -10px;\n  }\n  top-navigation-bar .oppia-signin-text {\n    font-family: Roboto, arial, sans-serif;\n    font-size: 14px;\n    font-weight: 500;\n    letter-spacing: .21px;\n    line-height: 38px;\n  }\n</style>'

blocks = {}
debug_info = ''