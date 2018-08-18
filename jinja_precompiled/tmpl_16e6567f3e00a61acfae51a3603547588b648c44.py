from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/questions/tag_misconception_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Select the misconception to tag to:\n  </h3>\n</div>\n<div class="modal-body new-subtopic-title-editor">\n  Selected Misconception: <[selectedMisconception.getName()]>\n  <div ng-repeat="misconception in misconceptions track by $index">\n    <button class="btn btn-default" style="width: 100%" ng-click="selectMisconception(misconception)">\n      <[misconception.getName()]>\n    </button>\n    <div ng-if="selectedMisconception.getId() === misconception.getId()">\n      <label class="misconception-label"> Note to creators: </label>\n      <angular-html-bind html-data="misconception.getNotes()">\n      </angular-html-bind>\n      <label class="misconception-label"> Misconception Feedback: </label>\n      <angular-html-bind html-data="misconception.getFeedback()">\n      </angular-html-bind>\n    </div>\n  </div>\n  <span ng-click="toggleMisconceptionFeedbackUsage()" aria-hidden="true">\n    <i ng-if="!misconceptionFeedbackIsUsed" class="material-icons md-18">&#xE835;</i>\n    <i ng-if="misconceptionFeedbackIsUsed" class="material-icons md-18">&#xE834;</i>\n    Use misconception feedback as answer group feedback.\n  </span>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()"> Cancel </button>\n  <button class="btn btn-success" ng-disabled="selectedMisconception === null" ng-click="done()"> Done </button>\n</div>\n\n<style>\n  .misconception-label {\n    margin-top: 2vh;\n  }\n</style>'

blocks = {}
debug_info = ''