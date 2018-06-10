from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/settings_tab/transfer_exploration_ownership_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Transfer Ownership to the Community</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    You are about to transfer ownership of this exploration to the\n    community! This will allow anyone to freely edit and improve\n    the exploration. Your previous contributions will still be visible\n    in the version history logs, and you will still be able to view and\n    edit the exploration.\n  </p>\n\n  <p>\n    Please note that after the ownership of an exploration is transferred\n    to the community, it will no longer have an explicit list of managers,\n    so this action is <strong>not reversible</strong>.\n  </p>\n\n  <p>\n    Would you like to transfer ownership of this exploration to the\n    community?\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-success" ng-click="transfer()">Transfer Ownership</button>\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n</div>'

blocks = {}
debug_info = ''