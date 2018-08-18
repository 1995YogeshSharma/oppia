from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/editor_tab/delete_worked_example_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Delete Worked Example</h3>\n</div>\n\n<div class="modal-body">\n  <span>Are you sure you want to delete this worked example?</span>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-danger" ng-click="confirm()">Delete Worked Example</button>\n</div>'

blocks = {}
debug_info = ''