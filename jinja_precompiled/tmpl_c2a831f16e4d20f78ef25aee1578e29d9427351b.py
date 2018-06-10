from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/header_js_libs.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_ASSET_DIR_PREFIX = resolve('ASSET_DIR_PREFIX')
    pass
    yield u'<script src="%s/assets/rich_text_components_definitions.js"></script>\n<script src="%s/assets/constants.js"></script>\n' % (
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
    )
    if (not (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE)):
        pass
        yield u'\n  <script src="%s/assets/hashes.js"></script>\n' % (
            escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        )
    yield u'\n<!-- jquery.js, angular.js and jquery-ui.js are removed from bundled js because\nthey need to be at the header. Including bundled js at the header will block\nrendering.-->\n<script src="/third_party/static/jquery-3.2.1/jquery.min.js"></script>\n<script src="/third_party/static/jqueryui-1.12.1/jquery-ui.min.js"></script>\n<script src="/third_party/static/angularjs-1.5.8/angular.min.js"></script>\n<script src="/third_party/static/jquery-ui-touch-punch-0.3.1/jquery.ui.touch-punch-improved.js"></script>\n<script src="/third_party/static/headroom-js-0.9.4/headroom.min.js"></script>\n<script src="/third_party/static/headroom-js-0.9.4/angular.headroom.min.js"></script>'

blocks = {}
debug_info = '1=13&2=14&3=16&4=19'