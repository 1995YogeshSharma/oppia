from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'mathjaxConfig.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u"window.MathJax = {\n  skipStartupTypeset: true,\n  messageStyle: 'none',\n  'HTML-CSS': {\n    linebreaks: {\n      automatic: true,\n      width: '500px'\n    },\n    scale: 91,\n    showMathMenu: false\n  }\n};"

blocks = {}
debug_info = ''