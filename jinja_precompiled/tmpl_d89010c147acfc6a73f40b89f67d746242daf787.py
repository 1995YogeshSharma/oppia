from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/notifications_dashboard/notifications_dashboard.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/notifications_dashboard/notifications_dashboard.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-dashboard-container" ng-controller="DashboardNotifications">\n    <h2 class="oppia-page-heading">Notifications</h2>\n    <div class="oppia-page-heading-subtext" ng-if="jobQueuedMsec">\n      Last updated: <[getLocaleAbbreviatedDatetimeString(jobQueuedMsec)]>\n    </div>\n\n    <div>\n      <md-card ng-if="recentNotifications.length === 0" class="oppia-page-card oppia-notifications-dashboard-card">\n        <em>No recent notifications.</em>\n      </md-card>\n\n      <div ng-if="recentNotifications.length > 0">\n        <a ng-href="<[getItemUrl(notification.activity_id, notification.type)]>"\n           ng-repeat="notification in recentNotifications">\n          <md-card class="oppia-dashboard-row"\n                   ng-class="{\'oppia-dashboard-row-recent\': lastSeenMsec && lastSeenMsec < notification.last_updated_ms && notification.author_username !== currentUsername}">\n            <div class="oppia-notification-content">\n              <span>\n                <span ng-if="notification.type === \'feedback_thread\'"\n                      title="Feedback thread">\n                  <i class="material-icons">&#xE0B9;</i>\n                </span>\n                <span ng-if="notification.type === \'exploration_commit\'"\n                      title="Exploration commit">\n                  <i class="material-icons">&#xE150;</i>\n                </span>\n              </span>\n              <span class="oppia-notification-author-username">\n                <strong>\n                  <span>\n                    <[notification.author_username]>\n                  </span>\n                  <span ng-if="!notification.author_username">\n                    Anonymous\n                  </span>\n                </strong>\n                <span ng-if="notification.type === \'exploration_commit\'">\n                  made a new commit to\n                </span>\n                <span ng-if="notification.type === \'feedback_thread\'">\n                  left a comment on\n                </span>\n                <span class="oppia-notification-activity-title">\n                  <[notification.activity_title]>\n                </span>\n              </span>\n            </div>\n            <div class="oppia-notification-last-updated">\n              <[getLocaleAbbreviatedDatetimeString(notification.last_updated_ms)]>\n            </div>\n          </md-card>\n        </a>\n      </div>\n    </div>\n  </div>\n  <style>\n    .oppia-page-heading-subtext {\n      font-size: smaller;\n      opacity: 0.7;\n    }\n    .oppia-notifications-dashboard-card {\n      padding: 15px 40px;\n    }\n    .oppia-dashboard-row {\n      background-color: #fff;\n      cursor: pointer;\n      margin-bottom: -5px;\n      overflow: auto;\n      position: relative;\n    }\n    .oppia-dashboard-row:hover {\n      background: #eee;\n    }\n    .oppia-dashboard-row-recent {\n      background: #fff4ca;\n    }\n    .oppia-dashboard-row-recent:hover {\n      background: #ffe279;\n    }\n    .oppia-notification-content {\n      color: black;\n      display: inline-block;\n      float: left;\n    }\n    .oppia-notification-last-updated {\n      float: right;\n    }\n    @media (max-width: 500px) {\n      .oppia-notification-content,\n      .oppia-notification-last-updated {\n        display: inline;\n      }\n    }\n  </style>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/notifications_dashboard/NotificationsDashboard.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Notifications - Oppia\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Notifications\n    </li>\n  </ul>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&16=17&113=24&114=31&3=34&7=41'