from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/delete_topic_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Are you sure you want to delete this topic?\n  </h3>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-danger" ng-click="confirmDeletion()">\n    <span>Delete Topic</span>\n  </button>\n</div>'

blocks = {}
debug_info = ''