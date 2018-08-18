from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/new_topic_name_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Enter Topic Name\n  </h3>\n</div>\n<div class="modal-body new-topic-name-editor" ng-class="{\'has-error\': isTopicNameEmpty(topicName)}">\n  <p>\n    Enter the name for the topic: &nbsp;\n    <input class="form-group" ng-model="topicName">\n    <span ng-if="isTopicNameEmpty(topicName)" class="help-block" style="font-size: smaller">\n     A name is required to create a topic.\n    </span>\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-disabled="isTopicNameEmpty(topicName)" ng-click="save(topicName)">\n    <span>Create Topic</span>\n  </button>\n</div>\n<style>\n  .new-topic-name-editor .help-block {\n    margin-left: 37.5%;\n    margin-top: -3%;\n  }\n</style>'

blocks = {}
debug_info = ''