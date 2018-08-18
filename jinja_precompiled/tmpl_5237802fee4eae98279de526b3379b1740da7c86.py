from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/get_started/get_started.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/get_started/get_started.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/components/background/BackgroundBannerDirective.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/get_started/get_started.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-static-header">\n    <h1 translate="I18N_GET_STARTED_PAGE_HEADING"></h1>\n  </div>\n\n  <background-banner></background-banner>\n  <div class="oppia-page-card oppia-static-content oppia-static-content-below-banner">\n    <div class="oppia-static-card-content oppia-static-card-content-narrow oppia-get-started">\n\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_1">\n      </p>\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_2_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_2">\n      </p>\n\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_3_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_3">\n      </p>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_4">\n\n      </p>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_5">\n\n      </p>\n      <ul style="margin-left: 40px;">\n        <li><a href="https://www.oppia.org/explore/0" target="new">Welcome to Oppia</a></li>\n        <li><a href="https://www.oppia.org/collection/wqCTKpKA0LBe" target="new">Get Electrified!</a></li>\n        <li><a href="https://www.oppia.org/collection/inDXV0w8-p1C" target="new">Programming with Carla</a></li>\n      </ul>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_6">\n      </p>\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_7_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_7">\n      </p>\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_8_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_8">\n      </p>\n\n      <!-- todo: make it easy to get the right link to share, update this doc with that info -->\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_9_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_9">\n      </p>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_10">\n\n      </p>\n\n      <h2 translate="I18N_GET_STARTED_PAGE_PARAGRAPH_11_HEADING"></h2>\n      <p translate="I18N_GET_STARTED_PAGE_PARAGRAPH_11">\n      </p>\n    </div>\n  </div>\n  <div class="oppia-footer-padding-below-banner">\n  </div>\n  <style>\n    .oppia-get-started h2 {\n      font-size: 1.17em;\n      font-weight: bold;\n      text-align: left;\n    }\n  </style>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  I18N_GET_STARTED_PAGE_TITLE\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    pass
    yield u'\n  %s\n' % (
        escape(context.call(l_0_super)), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Get Started\n    </li>\n  </ul>\n'

blocks = {'footer_js': block_footer_js, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&87=17&88=24&92=27&93=33&20=38&3=45&7=52&8=59&11=62'