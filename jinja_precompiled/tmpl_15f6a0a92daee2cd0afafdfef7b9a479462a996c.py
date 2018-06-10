from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/rich_text_components.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_ASSET_DIR_PREFIX = resolve('ASSET_DIR_PREFIX')
    pass
    yield u'<script src="%s/extensions/rich_text_components/Collapsible/directives/CollapsibleDirective.js"></script>\n<script src="%s/extensions/rich_text_components/Image/directives/ImageDirective.js"></script>\n<script src="%s/extensions/rich_text_components/Link/directives/LinkDirective.js"></script>\n<script src="%s/extensions/rich_text_components/Math/directives/MathDirective.js"></script>\n<script src="%s/extensions/rich_text_components/Tabs/directives/TabsDirective.js"></script>\n<script src="%s/extensions/rich_text_components/Video/directives/VideoDirective.js"></script>' % (
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
        escape((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX)), 
    )

blocks = {}
debug_info = '1=12&2=13&3=14&4=15&5=16&6=17'