from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/mark_all_audio_as_needing_update_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Update Audio Translations</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    Would you like to flag all existing audio translations as \'may not match content\'?\n    <br>\n    This informs audio translators to record new audio that reflects any changes in text.\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">No</button>\n  <button class="btn btn-default" ng-click="flagAll()">Yes</button>\n</div>'

blocks = {}
debug_info = ''