from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/feedback_tab/thread_table_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  thread-table .oppia-feedback-tab-row {\n    cursor: pointer;\n  }\n  thread-table .oppia-feedback-tab-row:hover {\n    background: #eee;\n  }\n</style>\n<table class="table">\n  <tr ng-if="getThreads().length > 0">\n    <th class="col-lg-1 col-md-1 col-sm-1">Status</th>\n    <th class="col-lg-6 col-md-6 col-sm-6">Subject</th>\n    <th class="col-lg-3 col-md-3 col-sm-3">Original author</th>\n    <th class="col-lg-2 col-md-2 col-sm-2">Last updated</th>\n  </tr>\n  <tr ng-repeat="thread in getThreads()|orderBy:\'-last_updated\'" ng-click="onClickRow(thread.threadId)" class="oppia-feedback-tab-row protractor-test-oppia-feedback-tab-row">\n    <td class="col-lg-1 col-md-1 col-sm-1">\n      <span ng-class="getLabelClass(thread.status)"><[getHumanReadableStatus(thread.status)]></span>\n    </td>\n    <td class="col-lg-6 col-md-6 col-sm-6">\n      <div class="protractor-test-exploration-feedback-subject"><[thread.subject | truncate:40]></div>\n    </td>\n    <td class="col-lg-3 col-md-3 col-sm-3">\n      <span ng-if="thread.originalAuthorName"><[thread.originalAuthorName]></span>\n    </td>\n    <td class="col-lg-2 col-md-2 col-sm-2">\n      <span><[getLocaleAbbreviatedDatetimeString(thread.lastUpdated)]></span>\n    </td>\n    <td class="col-lg-2 col-md-2 col-sm-2">\n    </td>\n  </tr>\n</table>'

blocks = {}
debug_info = ''