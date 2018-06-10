from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/error/error_iframed.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/error/error_iframed.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div role="main" style="margin: 0 auto; position: relative;">\n    <div class="oppia-page-container">\n      <md-card class="oppia-main-error-card">\n        <h3>Exploration Not Found</h3>\n        <p>\n          Uh-oh! The Oppia exploration you requested may have been removed or deleted.\n        </p>\n        <br>\n        <p>\n          To find similar explorations, visit the\n          <a href="https://www.oppia.org/library" target="_blank">Oppia.org library</a>.\n        </p>\n      </md-card>\n    </div>\n  </div>\n\n  <style>\n    html, body {\n      background: #afd2eb no-repeat center center fixed;\n      background-size: cover;\n      color: rgba(0,0,0,0.87);\n      font-family: \'Roboto\', Arial, sans-serif;\n      font-size: 1.0em;\n    }\n\n    .oppia-page-container {\n      align-items: flex-start;\n      display: flex;\n      justify-content: center;\n      margin: 0 auto;\n      max-width: 1400px;\n      padding: 40px 14px;\n      width: 100%;\n    }\n\n    .oppia-main-error-card {\n      background: #fff;\n      border-radius: 2px;\n      flex-shrink: 10000;\n      max-width: 560px;\n      min-width: 360px;\n      padding: 20px 20px 30px;\n      text-align: left;\n      width: 100%;\n      z-index: 1;\n    }\n  </style>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Exploration Not Found - Oppia\n'

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

blocks = {'content': block_content, 'maintitle': block_maintitle, 'local_top_nav_options': block_local_top_nav_options, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&13=17&3=24&10=31&7=38'