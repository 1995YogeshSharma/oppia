from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/maintenance/maintenance.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    t_1 = environment.filters['js_string']
    pass
    yield u'<!DOCTYPE html>\n<html ng-app="oppia" lang="<[currentLang]>" ng-controller="Maintenance" itemscope itemtype="http://schema.org/Organization">\n  <head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">\n    <title itemprop="name" translate="Down for Maintenance - Oppia"></title>\n    '
    template = environment.get_template('pages/header_css_libs.html', 'pages/maintenance/maintenance.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u"\n\n    <script>\n      var GLOBALS = {\n        ADDITIONAL_ANGULAR_MODULES: [],\n        DEV_MODE: JSON.parse('%s')\n      };\n    </script>\n    " % (
        escape(t_1((undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE))), 
    )
    template = environment.get_template('pages/header_js_libs.html', 'pages/maintenance/maintenance.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </head>\n  <body>\n    <div class="oppia-base-container">\n      <div class="oppia-content-container">\n        <div id="wrapper">\n          <div class="oppia-main-body">\n            <nav class="navbar navbar-default oppia-navbar oppia-prevent-selection" role="navigation">\n              <div class="navbar-container">\n                <div class="navbar-header protractor-test-navbar-header pull-left">\n                  <a class="oppia-navbar-brand-name oppia-transition-200" href="/">\n                    <img ng-src="<[getStaticImageUrl(\'/logo/288x128_logo_white.png\')]>"\n                         class="oppia-logo oppia-logo-wide" alt="Oppia Home">\n                  </a>\n                </div>\n                <div ng-cloak class="navbar-header pull-right">\n                </div>\n              </div>\n            </nav>\n\n            <div class="oppia-top-of-page-padding"></div>\n            <div class="oppia-page-cards-container">\n              <md-card class="oppia-page-card oppia-long-text">\n                <h2>The Oppia site is temporarily unavailable.</h2>\n\n                <p>\n                  Oppia is currently being upgraded, and the site should be up\n                  and running again in a few hours. Thanks for your patience!\n                </p>\n              </md-card>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n\n    '
    template = environment.get_template('pages/footer_js_libs.html', 'pages/maintenance/maintenance.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    <script src="/templates/dev/head/app.js"></script>\n    <script src="/templates/dev/head/i18n.js"></script>\n    <script src="/templates/dev/head/services/AlertsService.js"></script>\n    <script src="/templates/dev/head/services/UtilsService.js"></script>\n    <script src="/templates/dev/head/services/ContextService.js"></script>\n    <script src="/templates/dev/head/services/IdGenerationService.js"></script>\n    <script src="/templates/dev/head/services/DebouncerService.js"></script>\n    <script src="/templates/dev/head/services/HtmlEscaperService.js"></script>\n    <script src="/templates/dev/head/services/RteHelperService.js"></script>\n    <script src="/templates/dev/head/services/contextual/UrlService.js"></script>\n    <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n    <script src="/templates/dev/head/components/forms/ObjectEditorDirective.js"></script>\n    <script src="/templates/dev/head/domain/utilities/UrlInterpolationService.js"></script>\n    <script src="/templates/dev/head/pages/maintenance/Maintenance.js"></script>\n\n    <!-- These three files need to be loaded here only because they are dependencies for $provide, and Angular will not load without them. -->\n    <script src="/templates/dev/head/services/contextual/DeviceInfoService.js"></script>\n    <script src="/templates/dev/head/services/stateful/FocusManagerService.js"></script>\n    <script src="/templates/dev/head/services/TranslationFileHashLoaderService.js"></script>\n  </body>\n</html>'

blocks = {}
debug_info = '7=13&12=17&15=19&51=23'