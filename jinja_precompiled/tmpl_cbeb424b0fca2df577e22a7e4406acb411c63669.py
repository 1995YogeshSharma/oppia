from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/settings_tab/moderator_unpublish_exploration_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Unpublish exploration (as moderator)</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    You are about to unpublish this exploration.\n  </p>\n\n  <div ng-if="willEmailBeSent">\n    <br>\n    <p>\n      Doing so will send the following email to all exploration owners;\n      please edit it as needed. (NB: do not include a salutation or a\n      signoff -- the text "Hi [username]" and "Thanks! [your username] (Oppia moderator)" will\n      be auto-added.)\n    </p>\n\n    <schema-based-editor schema="EMAIL_BODY_SCHEMA" local-value="$parent.emailBody">\n    </schema-based-editor>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-click="reallyTakeAction()">\n    <span>Unpublish Exploration</span>\n  </button>\n</div>'

blocks = {}
debug_info = ''