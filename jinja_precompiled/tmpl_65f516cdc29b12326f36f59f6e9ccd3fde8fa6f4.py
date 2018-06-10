from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/take_break_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Time for a break?\n  </h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    You seem to be submitting answers very quickly. Are you starting to get tired?\n  </p>\n  <br>\n  <p>\n    If so, consider taking a break! You can come back later.\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-success" ng-click="okay()">I\'m ready to continue the lesson</button>\n</div>'

blocks = {}
debug_info = ''