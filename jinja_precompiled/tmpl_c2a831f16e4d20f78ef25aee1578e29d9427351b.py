from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/header_js_libs.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    pass
    yield u'<script src="/assets/rich_text_components_definitions.js"></script>\n<script src="/assets/constants.js"></script>\n'
    if (not (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE)):
        pass
        yield u'\n  <script src="/assets/hashes.js"></script>\n'
    yield u'\n<!-- jquery.js, angular.js and jquery-ui.js are removed from bundled js because\nthey need to be at the header. Including bundled js at the header will block\nrendering.-->\n<script src="/third_party/static/jquery-3.2.1/jquery.min.js"></script>\n<script src="/third_party/static/jqueryui-1.12.1/jquery-ui.min.js"></script>\n<script src="/third_party/static/angularjs-1.5.8/angular.min.js"></script>\n<script src="/third_party/static/jquery-ui-touch-punch-0.3.1/jquery.ui.touch-punch-improved.js"></script>\n<script src="/third_party/static/headroom-js-0.9.4/headroom.min.js"></script>\n<script src="/third_party/static/headroom-js-0.9.4/angular.headroom.min.js"></script>\n<script src="/third_party/static/angular-drag-and-drop-lists-2.1.0/angular-drag-and-drop-lists.min.js"></script>\n<script src="/third_party/static/ckeditor-4.9.2/ckeditor.js"></script>\n<script src="/third_party/static/angular-recorder-1.4.1/dist/angular-audio-recorder.min.js"></script>'

blocks = {}
debug_info = '3=12'