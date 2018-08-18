from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/subtopics_editor/new_subtopic_title_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Enter Subtopic Title\n  </h3>\n</div>\n<div class="modal-body new-subtopic-title-editor"\n     ng-class="{\'has-error\': isSubtopicTitleEmpty(subtopicTitle)}">\n  <p>\n    Enter the title for the subtopic: &nbsp;\n    <input class="form-group" ng-model="subtopicTitle">\n    <span ng-if="isSubtopicTitleEmpty(subtopicTitle)"\n          class="help-block" style="font-size: smaller">\n      A title is required to create a subtopic.\n    </span>\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-disabled="isSubtopicTitleEmpty(subtopicTitle)"\n          ng-click="save(subtopicTitle)">\n    <span>Create Subtopic</span>\n  </button>\n</div>\n<style>\n  .new-subtopic-title-editor .help-block {\n    margin-left: 37.5%;\n    margin-top: -3%;\n  }\n</style>'

blocks = {}
debug_info = ''