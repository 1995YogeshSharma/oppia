from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topics_and_skills_dashboard/topics_and_skills_dashboard.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/topics_and_skills_dashboard/topics_and_skills_dashboard.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <background-banner></background-banner>\n  <div class="oppia-topics-and-skills-dashboard" ng-controller="TopicsAndSkillsDashboard" style="position: relative;">\n    <div>\n      <h2 class="dashboard-title" translate="I18N_DASHBOARD_TOPICS_AND_SKILLS_DASHBOARD"></h2>\n    </div>\n    <div ng-if="topicSummaries.length > 0 || untriagedSkillSummaries.length > 0 || unpublishedSkillSummaries.length > 0">\n      <ul class="dashboard-tabs">\n        <li ng-if="topicSummaries.length > 0"\n            ng-class="{\'dashboard-tabs-active\': activeTab === TAB_NAME_TOPICS}">\n          <a class="dashboard-tabs-text"\n             ng-click="setActiveTab(TAB_NAME_TOPICS)">\n             Topics\n          </a>\n        </li>\n        <li ng-if="untriagedSkillSummaries.length > 0"\n            ng-class="{\'dashboard-tabs-active\': activeTab === TAB_NAME_UNTRIAGED_SKILLS}">\n          <a class="dashboard-tabs-text"\n             ng-click="setActiveTab(TAB_NAME_UNTRIAGED_SKILLS)">\n             Untriaged Skills\n          </a>\n        </li>\n        <li ng-if="unpublishedSkillSummaries.length > 0"\n            ng-class="{\'dashboard-tabs-active\': activeTab === TAB_NAME_UNPUBLISHED_SKILLS}">\n          <a class="dashboard-tabs-text"\n             ng-click="setActiveTab(TAB_NAME_UNPUBLISHED_SKILLS)">\n             Unpublished Skills\n          </a>\n        </li>\n      </ul>\n\n      <div ng-if="activeTab === TAB_NAME_TOPICS">\n        <topics-list topic-summaries="topicSummaries"\n                     user-can-delete-topic="userCanDeleteTopic"\n                     in-modal="false">\n        </topics-list>\n      </div>\n\n      <div ng-if="activeTab === TAB_NAME_UNTRIAGED_SKILLS">\n        <skills-list skill-summaries="untriagedSkillSummaries"\n                     editable-topic-summaries="editableTopicSummaries">\n        </skills-list>\n      </div>\n\n      <div ng-if="activeTab === TAB_NAME_UNPUBLISHED_SKILLS">\n        <skills-list skill-summaries="unpublishedSkillSummaries"\n                     editable-topic-summaries="editableTopicSummaries">\n        </skills-list>\n      </div>\n    </div>\n\n    <div class="col-sm-8" ng-if="topicSummaries.length === 0 && untriagedSkillSummaries.length === 0 && unpublishedSkillSummaries.length === 0">\n      <blockquote class="intro-card">\n        <p class="intro-card-message" style="padding-top: 6px;">\n          No topics or skills have been created yet.\n        </p>\n        <button class="btn oppia-dashboard-intro-button oppia-transition-200"\n                style="color: white; text-decoration: none;"\n                ng-click="createTopic()"\n                ng-if="userCanCreateTopic">\n          Create Topic\n        </button>\n      </blockquote>\n    </div>\n  </div>\n  <style>\n    .oppia-topics-and-skills-dashboard .dashboard-tabs {\n      border-bottom: 1px solid #eee;\n      display: -webkit-flex;\n      display: flex;\n      flex-wrap: wrap;\n      margin-bottom: 0;\n      margin-left: 12.5%;\n      padding-left: 0;\n      padding-top: 6%;\n      text-align: center;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs li {\n      display: -webkit-flex;\n      display: flex;\n      margin-bottom: 0;\n      width: 200px;\n    }\n    .oppia-topics-and-skills-dashboard .dashboard-title {\n      color: #01645c;\n      font-family: \'Capriola\', \'Roboto\', Arial, sans-serif;\n      font-size: 3em;\n      margin-top: 0px;\n      margin-bottom: 25px;\n      padding-top: 78.5px;\n      text-align: center;\n    }\n\n    .oppia-topics-and-skills-dashboard .intro-card {\n      background: #fff;\n      border-left: none;\n      border-radius: 5px;\n      margin: 1em 0 0;\n      margin-left: 25%;\n      margin-right: 25%;\n      padding: 37px 30px;\n      text-align: center;\n      width: 100%;\n    }\n\n    .oppia-topics-and-skills-dashboard .intro-card:before {\n      background: #fff;\n      border-bottom-right-radius: 80px 50px;\n      bottom: -1.7em;\n      content: "";\n      display: block;\n      height: 30px;\n      position: absolute;\n      width: 50px;\n      z-index: 10;\n    }\n\n    .oppia-topics-and-skills-dashboard .intro-card:after {\n      background: #eee;\n      border-bottom-right-radius: 40px 50px;\n      bottom: -1.7em;\n      content: "";\n      display: block;\n      height: 30px;\n      position: absolute;\n      width: 20px;\n      z-index: 10;\n    }\n\n    .oppia-topics-and-skills-dashboard .intro-card-message {\n      font-family: \'Capriola\', \'Roboto\', Arial, sans-serif;\n      font-size: 18px;\n      text-align: center;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs .dashboard-tabs-text {\n      color: #009688;\n      font-size: 1em;\n      padding: 10px;\n      text-decoration: none;\n      text-transform: uppercase;\n      width: 100%;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs-active .dashboard-tabs-text,\n    .oppia-topics-and-skills-dashboard .dashboard-tabs-active .dashboard-tabs-text:hover {\n      border-bottom: 4px solid #009688;\n      color: #009688;\n      margin-left: 7.5px;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs .dashboard-tabs-text:hover {\n      color: #009688;\n      font-size: 1em;\n      padding: 10px;\n      text-decoration: none;\n      text-transform: uppercase;\n      width: 100%;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs .dashboard-tabs-text:hover,\n    .oppia-topics-and-skills-dashboard .dashboard-tabs .dashboard-tabs-text:focus {\n      text-decoration: none;\n    }\n\n    .oppia-topics-and-skills-dashboard .dashboard-tabs .list-card-view-toggle {\n      margin-left: auto;\n      margin-right: 7.5px;\n      width: auto;\n    }\n\n    @media(max-width: 815px) {\n      .oppia-topics-and-skills-dashboard .dashboard-tabs {\n        justify-content: center;\n      }\n\n      .oppia-topics-and-skills-dashboard .intro-card {\n        width: auto;\n      }\n\n      .oppia-topics-and-skills-dashboard .dashboard-tabs li {\n        width: auto;\n      }\n\n      .oppia-topics-and-skills-dashboard .oppia-dashboard-intro-button {\n        display: none;\n      }\n\n      .oppia-topics-and-skills-dashboard .dashboard-tabs .sort-explorations-select {\n        margin-top: 8px;\n        width: 100%;\n      }\n    }\n  </style>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/components/background/BackgroundBannerDirective.js"></script>\n\n  <script src="/templates/dev/head/pages/topics_and_skills_dashboard/SkillsListDirective.js"></script>\n  <script src="/templates/dev/head/pages/topics_and_skills_dashboard/TopicsAndSkillsDashboard.js"></script>\n  <script src="/templates/dev/head/pages/topics_and_skills_dashboard/TopicsAndSkillsDashboardNavbarBreadcrumbDirective.js"></script>\n  <script src="/templates/dev/head/pages/topics_and_skills_dashboard/TopicsAndSkillsDashboardNavbarDirective.js"></script>\n  <script src="/templates/dev/head/pages/topics_and_skills_dashboard/TopicsListDirective.js"></script>\n\n  <script src="/templates/dev/head/domain/topic/EditableTopicBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/topics_and_skills_dashboard/TopicsAndSkillsDashboardBackendApiService.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Topics and Skills Dashboard - Oppia\n'

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <topics-and-skills-dashboard-navbar>\n  </topics-and-skills-dashboard-navbar>\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <topics-and-skills-dashboard-navbar-breadcrumb>\n  </topics-and-skills-dashboard-navbar-breadcrumb>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'local_top_nav_options': block_local_top_nav_options, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&18=17&216=24&217=31&3=34&12=41&7=48'