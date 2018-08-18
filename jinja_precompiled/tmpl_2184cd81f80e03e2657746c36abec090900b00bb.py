from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/thanks/thanks.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/thanks/thanks.html')
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
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/thanks/Thanks.js"></script>\n  <script src="/templates/dev/head/components/background/BackgroundBannerDirective.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/thanks/thanks.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <background-banner></background-banner>\n  <div class="oppia-page-card oppia-static-content" ng-controller="Thanks">\n    <div class="oppia-static-card-content oppia-static-card-content-wide" style="height: 450px">\n      <h2>Thank you for donating to The Oppia Foundation!</h2>\n      <br>\n      <div style="float:left;">\n        <img ng-src="<[thanksImgUrl]>" alt="Otter holding a gift" style="height: 250px;">\n      </div>\n      <div style="float:right;">\n        <p>\n          Your contribution will be used towards:\n        </p>\n        <ul style="margin-left: 30px;">\n          <li>Maintaining our servers</li>\n          <li>Marketing</li>\n          <li>Distributing learning materials to students</li>\n        </ul>\n        <p>\n          Thank you for your support!\n        </p>\n      </div>\n    </div>\n  </div>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Thanks - Oppia\n'

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
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Thanks\n    </li>\n  </ul>\n'

blocks = {'footer_js': block_footer_js, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&46=17&47=24&52=27&53=33&20=38&3=45&7=52&8=59&11=62'