from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/base.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_status_code = resolve('status_code')
    l_0_meta_name = resolve('meta_name')
    l_0_logout_url = resolve('logout_url')
    l_0_ACTIVITY_STATUS_PRIVATE = resolve('ACTIVITY_STATUS_PRIVATE')
    l_0_promo_bar_enabled = resolve('promo_bar_enabled')
    l_0_profile_picture_data_url = resolve('profile_picture_data_url')
    l_0_ACTIVITY_STATUS_PUBLIC = resolve('ACTIVITY_STATUS_PUBLIC')
    l_0_nav_mode = resolve('nav_mode')
    l_0_SITE_FEEDBACK_FORM_URL = resolve('SITE_FEEDBACK_FORM_URL')
    l_0_additional_angular_modules = resolve('additional_angular_modules')
    l_0_SITE_NAME = resolve('SITE_NAME')
    l_0_is_admin = resolve('is_admin')
    l_0_SYSTEM_USERNAMES = resolve('SYSTEM_USERNAMES')
    l_0_user_is_logged_in = resolve('user_is_logged_in')
    l_0_username = resolve('username')
    l_0_get_complete_static_resource_url = resolve('get_complete_static_resource_url')
    l_0_iframed = resolve('iframed')
    l_0_FULL_URL = resolve('FULL_URL')
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_csrf_token = resolve('csrf_token')
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    l_0_meta_description = resolve('meta_description')
    l_0_promo_bar_message = resolve('promo_bar_message')
    l_0_allow_yaml_file_upload = resolve('allow_yaml_file_upload')
    l_0_is_moderator = resolve('is_moderator')
    l_0_ASSET_DIR_PREFIX = resolve('ASSET_DIR_PREFIX')
    l_0_preferred_site_language_code = resolve('preferred_site_language_code')
    l_0_BEFORE_END_HEAD_TAG_HOOK = resolve('BEFORE_END_HEAD_TAG_HOOK')
    l_0_GCS_RESOURCE_BUCKET_NAME = resolve('GCS_RESOURCE_BUCKET_NAME')
    l_0_DOMAIN_URL = resolve('DOMAIN_URL')
    l_0_get_static_resource_url = resolve('get_static_resource_url')
    l_0_login_url = resolve('login_url')
    l_0_is_super_admin = resolve('is_super_admin')
    l_0_can_create_collections = resolve('can_create_collections')
    l_0_INVALID_NAME_CHARS = resolve('INVALID_NAME_CHARS')
    l_0_warnings_and_loader = missing
    t_1 = environment.filters['js_string']
    pass
    def macro():
        t_2 = []
        pass
        t_2.append(
            u'<div tabindex="0" aria-label="Oppia Main Content" id="oppia-main-content" class="protractor-test-main-content" ng-cloak>\n    <div class="oppia-toast-container toast-top-center">\n      <div ng-repeat="warning in (AlertsService.warnings | limitTo:5) track by $index" class="toast toast-warning oppia-toast">\n        <button type="button" class="toast-close-button" ng-click="AlertsService.deleteWarning(warning)" role="button">&times;</button>\n        <div class="toast-message">\n          <[warning.content]>\n        </div>\n      </div>\n    </div>\n\n    <div>\n      <div ng-repeat="message in AlertsService.messages track by $index">\n        <alert-message message-object="message" message-index="$index"></alert-message>\n      </div>\n    </div>\n\n    <div ng-show="loadingMessage" class="oppia-loading-fullpage">\n      <div class="oppia-align-center">\n        <span translate="<[loadingMessage]>"></span>\n        <span class="oppia-loading-dot-one">.</span>\n        <span class="oppia-loading-dot-two">.</span>\n        <span class="oppia-loading-dot-three">.</span>\n      </div>\n    </div>\n    <div ng-show="!loadingMessage">\n      ',
        )
        for event in context.blocks['content'][0](context):
            t_2.append(event)
        t_2.append(
            u'\n      ',
        )
        for event in context.blocks['footer'][0](context):
            t_2.append(event)
        t_2.append(
            u'\n    </div>\n  </div>',
        )
        return concat(t_2)
    context.exported_vars.add('warnings_and_loader')
    context.vars['warnings_and_loader'] = l_0_warnings_and_loader = Macro(environment, macro, 'warnings_and_loader', (), False, False, False, context.eval_ctx.autoescape)
    yield u'\n\n<!DOCTYPE html>\n<html ng-app="oppia" lang="<[currentLang]>" ng-controller="Base" itemscope itemtype="http://schema.org/Organization">\n  <head>\n    '
    for event in context.blocks['prerender'][0](context):
        yield event
    yield u'\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">\n\n    <!-- Tiles for Internet Explorer. -->\n    <meta name="application-name" content="%s">\n    <meta name="msapplication-TileColor" content="#ffffff">\n    <meta name="msapplication-square70x70logo" content="%s">\n    <meta name="msapplication-square150x150logo" content="%s">\n    <meta name="msapplication-wide310x150logo" content="%s">\n    <meta name="msapplication-square310x310logo" content="%s">\n\n    <!-- The itemprops are for G+ sharing. -->\n    <meta itemprop="name" content="%s">\n    <meta itemprop="description" content="%s">\n    <!-- The og tags are for Facebook sharing. -->\n    <meta property="og:title" content="%s">\n    <meta property="og:site_name" content="Oppia">\n    <meta property="og:url" content="%s">\n    <meta property="og:description" content="%s">\n    <meta property="og:type" content="article">\n    <meta property="og:image" content="%s">\n\n    <link rel="apple-touch-icon" href="%s">\n\n    <!-- The title is bound to the rootScope. The content of the block\n    maintitle can be a string or a translation id. If it is a translation it\n    will be replaced by its translation when the page is loading. If it is a\n    string it would be displayed as is. This is the only way to translate\n    the page title because the head of the file is outside the scope of\n    any other controller. -->\n    <title itemprop="name" translate="' % (
        escape((undefined(name='SITE_NAME') if l_0_SITE_NAME is missing else l_0_SITE_NAME)), 
        escape(context.call((undefined(name='get_complete_static_resource_url') if l_0_get_complete_static_resource_url is missing else l_0_get_complete_static_resource_url), (undefined(name='DOMAIN_URL') if l_0_DOMAIN_URL is missing else l_0_DOMAIN_URL), '/assets/images/logo/msapplication-tiny.png')), 
        escape(context.call((undefined(name='get_complete_static_resource_url') if l_0_get_complete_static_resource_url is missing else l_0_get_complete_static_resource_url), (undefined(name='DOMAIN_URL') if l_0_DOMAIN_URL is missing else l_0_DOMAIN_URL), '/assets/images/logo/msapplication-square.png')), 
        escape(context.call((undefined(name='get_complete_static_resource_url') if l_0_get_complete_static_resource_url is missing else l_0_get_complete_static_resource_url), (undefined(name='DOMAIN_URL') if l_0_DOMAIN_URL is missing else l_0_DOMAIN_URL), '/assets/images/logo/msapplication-wide.png')), 
        escape(context.call((undefined(name='get_complete_static_resource_url') if l_0_get_complete_static_resource_url is missing else l_0_get_complete_static_resource_url), (undefined(name='DOMAIN_URL') if l_0_DOMAIN_URL is missing else l_0_DOMAIN_URL), '/assets/images/logo/msapplication-large.png')), 
        escape((undefined(name='meta_name') if l_0_meta_name is missing else l_0_meta_name)), 
        escape((undefined(name='meta_description') if l_0_meta_description is missing else l_0_meta_description)), 
        escape((undefined(name='meta_name') if l_0_meta_name is missing else l_0_meta_name)), 
        escape((undefined(name='FULL_URL') if l_0_FULL_URL is missing else l_0_FULL_URL)), 
        escape((undefined(name='meta_description') if l_0_meta_description is missing else l_0_meta_description)), 
        escape(context.call((undefined(name='get_complete_static_resource_url') if l_0_get_complete_static_resource_url is missing else l_0_get_complete_static_resource_url), (undefined(name='DOMAIN_URL') if l_0_DOMAIN_URL is missing else l_0_DOMAIN_URL), '/assets/images/logo/288x288_logo_mint.png')), 
        escape(context.call((undefined(name='get_static_resource_url') if l_0_get_static_resource_url is missing else l_0_get_static_resource_url), '/assets/images/logo/favicon.png')), 
    )
    for event in context.blocks['maintitle'][0](context):
        yield event
    yield u'"></title>\n    '
    for event in context.blocks['base_url'][0](context):
        yield event
    yield u'\n\n    '
    for event in context.blocks['header_css'][0](context):
        yield event
    yield u"\n\n    <script>\n      var GLOBALS = {\n        ACTIVITY_STATUS_PRIVATE: JSON.parse(\n          '%s'),\n        ACTIVITY_STATUS_PUBLIC: JSON.parse(\n          '%s'),\n        ADDITIONAL_ANGULAR_MODULES: [],\n        ASSET_DIR_PREFIX: JSON.parse('%s'),\n        can_create_collections: JSON.parse(\n          '%s'),\n        csrf_token: JSON.parse('%s'),\n        DEV_MODE: JSON.parse('%s'),\n        status_code: JSON.parse('%s'),\n        GCS_RESOURCE_BUCKET_NAME: JSON.parse('%s'),\n        INVALID_NAME_CHARS: JSON.parse('%s'),\n        NAV_MODE: JSON.parse('%s'),\n        /* A list of functions to be called when an exploration is completed */\n        POST_COMPLETION_HOOKS: [],\n        preferredSiteLanguageCode: JSON.parse(\n          '%s'),\n        SITE_NAME: JSON.parse('%s'),\n        SYSTEM_USERNAMES: JSON.parse('%s'),\n        TEMPLATE_DIR_PREFIX: JSON.parse('%s'),\n        isAdmin: JSON.parse('%s'),\n        isModerator: JSON.parse('%s'),\n        isSuperAdmin: JSON.parse('%s'),\n        loginUrl: JSON.parse('%s'),\n        logoutUrl: JSON.parse('%s'),\n        profilePictureDataUrl: JSON.parse('%s'),\n        userIsLoggedIn: JSON.parse('%s'),\n        username: JSON.parse('%s'),\n        allowYamlFileUpload: JSON.parse('%s'),\n        PROMO_BAR_IS_ENABLED: JSON.parse('%s'),\n        PROMO_BAR_MESSAGE: JSON.parse('%s')\n      };\n\n      " % (
        escape(t_1((undefined(name='ACTIVITY_STATUS_PRIVATE') if l_0_ACTIVITY_STATUS_PRIVATE is missing else l_0_ACTIVITY_STATUS_PRIVATE))), 
        escape(t_1((undefined(name='ACTIVITY_STATUS_PUBLIC') if l_0_ACTIVITY_STATUS_PUBLIC is missing else l_0_ACTIVITY_STATUS_PUBLIC))), 
        escape(t_1((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX))), 
        escape(t_1((undefined(name='can_create_collections') if l_0_can_create_collections is missing else l_0_can_create_collections))), 
        escape(t_1((undefined(name='csrf_token') if l_0_csrf_token is missing else l_0_csrf_token))), 
        escape(t_1((undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE))), 
        escape((undefined(name='status_code') if l_0_status_code is missing else l_0_status_code)), 
        escape(t_1((undefined(name='GCS_RESOURCE_BUCKET_NAME') if l_0_GCS_RESOURCE_BUCKET_NAME is missing else l_0_GCS_RESOURCE_BUCKET_NAME))), 
        escape(t_1((undefined(name='INVALID_NAME_CHARS') if l_0_INVALID_NAME_CHARS is missing else l_0_INVALID_NAME_CHARS))), 
        escape(t_1((undefined(name='nav_mode') if l_0_nav_mode is missing else l_0_nav_mode))), 
        escape(t_1((undefined(name='preferred_site_language_code') if l_0_preferred_site_language_code is missing else l_0_preferred_site_language_code))), 
        escape(t_1((undefined(name='SITE_NAME') if l_0_SITE_NAME is missing else l_0_SITE_NAME))), 
        escape(t_1((undefined(name='SYSTEM_USERNAMES') if l_0_SYSTEM_USERNAMES is missing else l_0_SYSTEM_USERNAMES))), 
        escape(t_1((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX))), 
        escape(t_1((undefined(name='is_admin') if l_0_is_admin is missing else l_0_is_admin))), 
        escape(t_1((undefined(name='is_moderator') if l_0_is_moderator is missing else l_0_is_moderator))), 
        escape(t_1((undefined(name='is_super_admin') if l_0_is_super_admin is missing else l_0_is_super_admin))), 
        escape(t_1((undefined(name='login_url') if l_0_login_url is missing else l_0_login_url))), 
        escape(t_1((undefined(name='logout_url') if l_0_logout_url is missing else l_0_logout_url))), 
        escape(t_1((undefined(name='profile_picture_data_url') if l_0_profile_picture_data_url is missing else l_0_profile_picture_data_url))), 
        escape(t_1((undefined(name='user_is_logged_in') if l_0_user_is_logged_in is missing else l_0_user_is_logged_in))), 
        escape(t_1((undefined(name='username') if l_0_username is missing else l_0_username))), 
        escape(t_1((undefined(name='allow_yaml_file_upload') if l_0_allow_yaml_file_upload is missing else l_0_allow_yaml_file_upload))), 
        escape(t_1((undefined(name='promo_bar_enabled') if l_0_promo_bar_enabled is missing else l_0_promo_bar_enabled))), 
        escape(t_1((undefined(name='promo_bar_message') if l_0_promo_bar_message is missing else l_0_promo_bar_message))), 
    )
    if (undefined(name='additional_angular_modules') if l_0_additional_angular_modules is missing else l_0_additional_angular_modules):
        pass
        yield u"\n        GLOBALS.ADDITIONAL_ANGULAR_MODULES = JSON.parse(\n          '%s');\n      " % (
            escape(t_1((undefined(name='additional_angular_modules') if l_0_additional_angular_modules is missing else l_0_additional_angular_modules))), 
        )
    yield u'\n    </script>\n\n    '
    for event in context.blocks['header_js'][0](context):
        yield event
    yield u'\n\n    %s\n  </head>\n\n  <body>\n    ' % (
        escape((undefined(name='BEFORE_END_HEAD_TAG_HOOK') if l_0_BEFORE_END_HEAD_TAG_HOOK is missing else l_0_BEFORE_END_HEAD_TAG_HOOK)), 
    )
    if (undefined(name='iframed') if l_0_iframed is missing else l_0_iframed):
        pass
        yield u'\n      %s\n    ' % (
            escape(context.call((undefined(name='warnings_and_loader') if l_0_warnings_and_loader is missing else l_0_warnings_and_loader))), 
        )
    else:
        pass
        yield u'\n      <div role="button" tabindex="0" ng-click="skipToMainContent()" class="oppia-skip-to-content protractor-test-skip-link">Skip to Main Content</div>\n      <promo-bar ng-if="promoBarIsEnabled" promo-message="promoBarMessage">\n      </promo-bar>\n      <div ng-if="isBackgroundMaskActive()" class="ng-cloak oppia-background-mask">\n      </div>\n\n      <div class="oppia-base-container"\n           ng-class="{\'oppia-sidebar-menu-open\': isSidebarShown(), \'oppia-sidebar-menu-closed\': !isSidebarShown()}"\n           ng-swipe-left="closeSidebarOnSwipe()">\n        <div class="oppia-content-container">\n          <div id="wrapper">\n            <div class="oppia-main-body">\n              <nav class="navbar navbar-default oppia-navbar oppia-prevent-selection" role="navigation" headroom tolerance="0" offset="0">\n                <div class="navbar-container">\n                  <top-navigation-bar></top-navigation-bar>\n                  <div class="collapse navbar-collapse oppia-navbar-collapse ng-cloak">\n                    '
        for event in context.blocks['navbar_breadcrumb'][0](context):
            yield event
        yield u'\n\n                    '
        for event in context.blocks['local_top_nav_options'][0](context):
            yield event
        yield u'\n                  </div>\n                </div>\n              </nav>\n\n              <div class="oppia-top-of-page-padding">\n              </div>\n\n              %s\n            </div>\n\n            <noscript>\n              <div class="oppia-page-cards-container">\n                <div class="md-default-theme oppia-page-card oppia-long-text">\n                  <!-- Note to developers: We replicate the translated text inline because, without JavaScript enabled, the translation engine doesn\'t kick in.-->\n                  <h2>\n                    <span translate="I18N_SPLASH_JAVASCRIPT_ERROR_TITLE">We Need JavaScript in Your Browser</span>\n                    <i class="material-icons">&#xE811;</i>\n                  </h2>\n                  <p translate="I18N_SPLASH_JAVASCRIPT_ERROR_DESCRIPTION"\n                     translate-values="{hrefUrl: \'http://www.enable-javascript.com/\'}">Oppia is a free, open-source learning platform full of interactive activities called \'explorations\'.  Sadly, Oppia requires JavaScript to be enabled in your web browser in order to function properly and your web browser has JavaScript disabled.  If you need help enabling JavaScript, <a href="http://www.enable-javascript.com"/>click here.</a></p>\n                  <p translate="I18N_SPLASH_JAVASCRIPT_ERROR_THANKS">Thank you.</p>\n                </div>\n              </div>\n            </noscript>\n\n            <side-navigation-bar></side-navigation-bar>\n          </div>\n        </div>\n      </div>\n\n      ' % (
            escape(context.call((undefined(name='warnings_and_loader') if l_0_warnings_and_loader is missing else l_0_warnings_and_loader))), 
        )
        if (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE):
            pass
            yield u'\n        <div class="oppia-dev-mode">\n          Dev Mode\n        </div>\n      '
        yield u'\n\n      '
        if (undefined(name='SITE_FEEDBACK_FORM_URL') if l_0_SITE_FEEDBACK_FORM_URL is missing else l_0_SITE_FEEDBACK_FORM_URL):
            pass
            yield u'\n        <a href="%s" target="_blank"\n           class="oppia-site-feedback oppia-transition-200">\n          <i class="material-icons md-18">&#xE87F;</i>\n            <span translate="I18N_SPLASH_SITE_FEEDBACK"></span>\n          </i>\n        </a>\n      ' % (
                escape((undefined(name='SITE_FEEDBACK_FORM_URL') if l_0_SITE_FEEDBACK_FORM_URL is missing else l_0_SITE_FEEDBACK_FORM_URL)), 
            )
        yield u'\n    '
    yield u'\n\n    '
    template = environment.get_template('pages/footer_js_libs.html', 'pages/base.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'warnings_and_loader': l_0_warnings_and_loader})):
        yield event
    yield u'\n\n    <script src="%s/app.js"></script>\n    <script src="%s/directives.js"></script>\n    <script src="%s/filters.js"></script>\n    <script src="%s/i18n.js"></script>\n\n    <script src="%s/pages/Base.js"></script>\n\n    <script src="%s/services/AlertsService.js"></script>\n    <script src="%s/services/ExplorationContextService.js"></script>\n    <script src="%s/services/UtilsService.js"></script>\n    <script src="%s/services/DebouncerService.js"></script>\n    <script src="%s/services/DateTimeFormatService.js"></script>\n    <script src="%s/services/IdGenerationService.js"></script>\n    <script src="%s/services/ValidatorsService.js"></script>\n    <script src="%s/services/HtmlEscaperService.js"></script>\n    <script src="%s/services/TranslationFileHashLoaderService.js"></script>\n    <script src="%s/services/RteHelperService.js"></script>\n    <script src="%s/services/StateRulesStatsService.js"></script>\n    <script src="%s/services/ConstructTranslationIdsService.js"></script>\n    <script src="%s/services/contextual/DeviceInfoService.js"></script>\n    <script src="%s/services/contextual/UrlService.js"></script>\n    <script src="%s/services/contextual/WindowDimensionsService.js"></script>\n    <script src="%s/services/stateful/BackgroundMaskService.js"></script>\n    <script src="%s/services/stateful/FocusManagerService.js"></script>\n\n    <script src="%s/components/alerts/AlertMessageDirective.js"></script>\n    <script src="%s/components/create_button/CreateActivityButtonDirective.js"></script>\n\n    <script src="%s/components/forms/ObjectEditorDirective.js"></script>\n    <script src="%s/components/promo/PromoBarDirective.js"></script>\n    <script src="%s/components/side_navigation_bar/SideNavigationBarDirective.js"></script>\n    <script src="%s/components/social_buttons/SocialButtonsDirective.js"></script>\n    <script src="%s/components/top_navigation_bar/TopNavigationBarDirective.js"></script>\n\n    <script src="%s/components/CollectionCreationService.js"></script>\n    <script src="%s/components/ExplorationCreationService.js"></script>\n\n    <script src="%s/domain/sidebar/SidebarStatusService.js"></script>\n    <script src="%s/domain/utilities/UrlInterpolationService.js"></script>\n\n    ' % (
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
    )
    for event in context.blocks['footer_js'][0](context):
        yield event
    yield u'\n  </body>\n</html>'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n    '

def block_prerender(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n    '

def block_header_css(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n      '
    template = environment.get_template('pages/header_css_libs.html', 'pages/base.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    '

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass

def block_base_url(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'Oppia'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n      '
    template = environment.get_template('pages/header_js_libs.html', 'pages/base.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    '

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n                    '

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n                    '

blocks = {'footer_js': block_footer_js, 'prerender': block_prerender, 'header_css': block_header_css, 'footer': block_footer, 'base_url': block_base_url, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb, 'local_top_nav_options': block_local_top_nav_options}
debug_info = '1=47&27=53&28=58&36=67&42=70&44=71&45=72&46=73&47=74&50=75&51=76&53=77&55=78&56=79&58=80&60=81&68=83&69=86&71=89&78=92&80=93&82=94&84=95&85=96&86=97&87=98&88=99&89=100&90=101&94=102&95=103&96=104&97=105&98=106&99=107&100=108&101=109&102=110&103=111&104=112&105=113&106=114&107=115&108=116&111=118&113=121&117=124&121=127&125=129&126=132&144=137&147=140&156=143&179=145&185=149&186=152&195=156&197=160&198=161&199=162&200=163&202=164&204=165&205=166&206=167&207=168&208=169&209=170&210=171&211=172&212=173&213=174&214=175&215=176&216=177&217=178&218=179&219=180&220=181&222=182&223=183&225=184&226=185&227=186&228=187&229=188&231=189&232=190&234=191&235=192&237=194&36=205&71=212&72=218&28=223&69=229&27=235&68=241&117=248&118=254&144=259&147=266'