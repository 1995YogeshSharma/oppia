from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/error/error.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/error/error.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-content oppia-error-page-main-content" ng-controller="Error">\n    <br>\n\n    <div class="oppia-wide-panel oppia-error-wide-container">\n      <div class="oppia-wide-panel-content protractor-test-error-container">\n        <h1 class="oppia-error-h1">\n          <div ng-if="statusCode === 400">\n            <span translate="I18N_ERROR_HEADER_400"></span>\n            - Bad Request\n          </div>\n          <div ng-if="statusCode === 401">\n            <span translate="I18N_ERROR_HEADER_401"></span>\n            - Unauthorized\n          </div>\n          <div ng-if="statusCode === 404">\n            <span translate="I18N_ERROR_HEADER_404"></span>\n            - Page Not Found\n          </div>\n          <div ng-if="statusCode === 500">\n            <span translate="I18N_ERROR_HEADER_500"></span>\n            - System Error\n          </div>\n        </h1>\n\n        <br>\n\n        <img ng-src="<[oopsMintImgUrl]>" alt="Oops!" width="299" height="142">\n        <p>\n          <h2 ng-if="statusCode === 400" class="oppia-error-h2" translate="I18N_ERROR_MESSAGE_400"></h2>\n          <h2 ng-if="statusCode === 401" class="oppia-error-h2" translate="I18N_ERROR_MESSAGE_401"></h2>\n          <h2 ng-if="statusCode === 404" class="oppia-error-h2" translate="I18N_ERROR_MESSAGE_404"></h2>\n          <h2 ng-if="statusCode === 500" class="oppia-error-h2" translate="I18N_ERROR_MESSAGE_500"></h2>\n        </p>\n        <p><span translate="I18N_ERROR_NEXT_STEPS" translate-values="{issueTrackerUrl: \'https://github.com/oppia/oppia/issues/new\', homeUrl: \'/\'}"></span></p>\n      </div>\n    </div>\n  </div>\n  <style>\n    .oppia-error-h1 {\n      font-size: 1em;\n      margin: 1.33em 0;\n    }\n    .oppia-error-h2 {\n      font-size: 1.17em;\n      font-weight: 700;\n    }\n    @media screen and (min-width: 768px) {\n      .oppia-footer {\n        position: relative;\n      }\n    }\n  </style>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/error/Error.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_status_code = resolve('status_code')
    pass
    yield u'\n  '
    if (undefined(name='status_code') if l_0_status_code is missing else l_0_status_code) == 400:
        pass
        yield u'\n    I18N_ERROR_PAGE_TITLE_400\n  '
    elif (undefined(name='status_code') if l_0_status_code is missing else l_0_status_code) == 401:
        pass
        yield u'\n    I18N_ERROR_PAGE_TITLE_401\n  '
    elif (undefined(name='status_code') if l_0_status_code is missing else l_0_status_code) == 404:
        pass
        yield u'\n    I18N_ERROR_PAGE_TITLE_404\n  '
    elif (undefined(name='status_code') if l_0_status_code is missing else l_0_status_code) == 500:
        pass
        yield u'\n    I18N_ERROR_PAGE_TITLE_500\n  '
    yield u'\n'

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/error/error.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'footer': block_footer, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&19=17&74=24&75=31&6=34&7=41&9=44&11=47&13=50&79=55&80=61&3=66'