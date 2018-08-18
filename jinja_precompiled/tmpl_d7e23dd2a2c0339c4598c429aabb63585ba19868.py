from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/skills_list_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card layout="row" class="list-view-item">\n  <table class="dashboard-table">\n    <colgroup>\n      <col style="width: 40%;">\n      <col style="width: 20%;">\n      <col style="width: 20%;">\n      <col style="width: 10%;">\n    </colgroup>\n    <tr>\n      <th ng-repeat="key in SKILL_HEADINGS"\n          class="dashboard-table-headings">\n        <p ng-if="key === \'description\'"> Skill Description </p>\n        <p ng-if="key === \'worked_examples_count\'"> Worked Examples </p>\n        <p ng-if="key === \'misconception_count\'"> Misconceptions </p>\n      </th>\n    </tr>\n    <tr ng-repeat="skill in getSkillSummaries()"\n        class="list-item">\n      <td>\n        <a ng-href="<[getSkillEditorUrl(skill.id)]>" class="list-summary">\n          <span> <[skill.description]> </span>\n        </a>\n      </td>\n      <td>\n        <a ng-href="<[getSkillEditorUrl(skill.id)]>" class="list-summary">\n          <span> <[skill.worked_examples_count]> </span>\n        </a>\n      </td>\n      <td>\n        <a ng-href="<[getSkillEditorUrl(skill.id)]>" class="list-summary">\n          <span> <[skill.misconception_count]> </span>\n        </a>\n      </td>\n      <td ng-if="getEditableTopicSummaries().length > 0">\n        <button class="btn btn-default" ng-click="assignSkillToTopic(skill.id)">\n          <span> Assign to Topic </span>\n        </button>\n      </td>\n    </tr>\n  </table>\n</md-card>\n\n<style>\n  skills-list .list-view-item {\n    background: #fff;\n    margin: 20px 7.5px 0 12.5%;\n    padding: 10px 20px;\n    width: 75%;\n  }\n\n  skills-list .dashboard-table {\n    font-size: 15px;\n    width: 100%;\n  }\n\n  skills-list .dashboard-table .dashboard-table-headings {\n    border-bottom: 2px solid #bbb;\n    padding-bottom: 0.7em;\n  }\n\n  skills-list .dashboard-table .dashboard-table-headings p {\n    display: inline;\n  }\n\n  skills-list .list-summary,\n  skills-list .list-summary:active,\n  skills-list .list-summary:visited {\n    color: inherit;\n    display: block;\n    height: 2em;\n    text-decoration: none;\n  }\n\n  skills-list .list-item:not(:last-child) {\n    border-bottom: 1px solid #bbb;\n  }\n\n  skills-list .list-item:hover {\n    background-color: #ededed;\n  }\n\n  skills-list .list-summary span {\n    display: inline-block;\n    line-height: normal;\n    vertical-align: middle;\n  }\n</style>'

blocks = {}
debug_info = ''