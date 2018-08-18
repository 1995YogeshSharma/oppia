from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'css/.stylelintrc'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'{ \n  "extends": "stylelint-config-recommended",\n  "rules": {\n    "indentation": 2,\n    "no-descending-specificity": true,\n    "no-duplicate-selectors": true,\n    "selector-type-no-unknown": [\n      true,\n      {\n        ignore: ["custom-elements"]\n      }\n    ],\n  }\n}'

blocks = {}
debug_info = ''