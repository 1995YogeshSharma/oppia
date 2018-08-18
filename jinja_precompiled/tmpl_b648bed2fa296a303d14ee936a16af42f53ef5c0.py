from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_reloading_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-loading-modal-body">\n  <p>\n    Reloading last saved version<loading-dots></loading-dots>\n  </p>\n</div>\n\n<style>\n  .oppia-loading-modal {\n    left: 50%;\n    margin-left: -40%;\n    margin-top: -100px;\n    top: 50%;\n  }\n  .oppia-loading-modal .modal-content {\n    border-radius: 0;\n    height: 100%;\n    width: 80%;\n  }\n\n  .oppia-loading-modal-body,\n  .oppia-loading-modal-body p {\n    padding: 1%;\n    text-align: center;\n  }\n</style>'

blocks = {}
debug_info = ''