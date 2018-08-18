from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/assign_skill_to_topic_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Select topic(s) to which the skill is to be assigned</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    Selected Topics Count: <[selectedTopicIds.length]>\n  </p>\n  <div class="topics-table">\n    <topics-list topic-summaries="topicSummaries"\n                 user-can-delete-topic="false"\n                 in-modal="true"\n                 selected-topic-ids="selectedTopicIds">\n    </topics-list>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-click="done()">Save</button>\n</div>\n\n<style>\n  .topics-table {\n    width: 100%;\n  }\n</style>'

blocks = {}
debug_info = ''