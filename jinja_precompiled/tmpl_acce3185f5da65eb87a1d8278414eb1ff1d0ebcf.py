from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/lost_changes_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Error Loading Exploration</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    Sorry! The following changes will be lost. It appears that your\n    draft was overwritten by changes on another machine.\n  </p>\n\n  <p ng-show="hasLostChanges">\n    The lost changes are displayed below. You may want to copy and\n    paste these changes before discarding them.\n  </p>\n\n  <div class="oppia-lost-changes" ng-bind-html="lostChangesHtml">\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="close()">Close</button>\n</div>'

blocks = {}
debug_info = ''