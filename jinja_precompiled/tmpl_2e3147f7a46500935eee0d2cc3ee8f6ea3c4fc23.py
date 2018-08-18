from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/questions/select_skill_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Select the skill to link the question to:\n  </h3>\n</div>\n<div class="modal-body new-subtopic-title-editor">\n  <div ng-repeat="skillSummary in skillSummaries track by $index">\n    <button class="btn btn-default" style="width: 100%" ng-click="selectSkill(skillSummary.getId())">\n      <[skillSummary.getDescription()]>\n    </button>\n  </div>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()"> Cancel </button>\n  <button class="btn btn-success" ng-disabled="selectedSkillId === null" ng-click="done()"> Done </button>\n</div>'

blocks = {}
debug_info = ''