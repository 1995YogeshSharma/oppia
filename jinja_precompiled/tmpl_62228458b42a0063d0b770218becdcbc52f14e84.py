from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/main_editor/stories_list_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<table class="dashboard-table">\n  <colgroup>\n    <col style="width: 50%;">\n    <col style="width: 50%;">\n  </colgroup>\n  <tr>\n    <th ng-repeat="key in STORY_TABLE_COLUMN_HEADINGS"\n        class="dashboard-table-headings">\n      <p ng-if="key === \'title\'"> Title </p>\n      <p ng-if="key === \'node_count\'"> Node Count </p>\n    </th>\n  </tr>\n  <tr ng-repeat="story in storySummaries"\n      class="list-item">\n    <td>\n      <a ng-click="openStoryEditor(story.id)" class="list-summary">\n        <span> <[story.title]> </span>\n      </a>\n    </td>\n    <td>\n      <a ng-click="openStoryEditor(story.id)" class="list-summary">\n        <span> <[story.node_count]> </span>\n      </a>\n    </td>\n    <td>\n      <span ng-click="deleteCanonicalStory(story.id)" class="fa fa-trash list-summary"> </span>\n    </td>\n  </tr>\n</table>\n\n<style>\n  stories-list .list-view-item {\n    background: #fff;\n    margin: 20px 7.5px 0 12.5%;\n    padding: 10px 20px;\n    width: 75%;\n  }\n\n  stories-list .dashboard-table {\n    font-size: 15px;\n    width: 100%;\n  }\n\n  stories-list .dashboard-table .dashboard-table-headings {\n    border-bottom: 2px solid #bbb;\n    padding-bottom: 0.7em;\n  }\n\n  stories-list .dashboard-table .dashboard-table-headings p {\n    display: inline;\n  }\n\n  stories-list .list-summary,\n  stories-list .list-summary:active,\n  stories-list .list-summary:visited {\n    color: inherit;\n    display: block;\n    height: 2em;\n    text-decoration: none;\n  }\n\n  stories-list .list-item:not(:last-child) {\n    border-bottom: 1px solid #bbb;\n  }\n\n  stories-list .list-item:hover {\n    background-color: #ededed;\n  }\n\n  stories-list .list-summary span {\n    display: inline-block;\n    line-height: normal;\n    vertical-align: middle;\n  }\n</style>'

blocks = {}
debug_info = ''