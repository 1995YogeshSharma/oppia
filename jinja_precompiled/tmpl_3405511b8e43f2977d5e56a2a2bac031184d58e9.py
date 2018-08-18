from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/forum/forum.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/forum/forum.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_full_google_group_url = resolve('full_google_group_url')
    pass
    yield u'\n  <style>\n    html, body {\n      background: #fff;\n    }\n    .oppia-forum {\n      font-size: large;\n      margin: 5px auto;\n      margin-top: 0;\n      min-height: 400px;\n      padding: 20px;\n    }\n    .oppia-forum-warning {\n      background: #F9EDBE;\n      max-width: 700px;\n      width: 80%%;\n    }\n  </style>\n\n  <div class="container">\n    <div class="oppia-forum" ng-controller="Forum">\n      <div ng-if="DEV_MODE" class="oppia-forum-warning">\n        <strong>Warning:</strong> This page may not display correctly on localhost. To view it, change \'localhost\' to \'127.0.0.1\' in the URL bar.\n      </div>\n\n      <iframe src="%s" frameborder="0" height="1300" style="width: 100%%;">\n      </iframe>\n    </div>\n  </div>\n' % (
        escape((undefined(name='full_google_group_url') if l_0_full_google_group_url is missing else l_0_full_google_group_url)), 
    )

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/forum/Forum.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Community Forum - Oppia\n'

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/forum/forum.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Forum\n    </li>\n  </ul>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'footer': block_footer, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&16=17&41=24&51=27&52=34&3=37&47=44&48=50&7=55'