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
    yield u'\n  <div class="oppia-dashboard-container" ng-controller="DashboardNotifications">\n    <h2 class="oppia-page-heading">Notifications</h2>\n    <div class="oppia-page-heading-subtext" ng-if="jobQueuedMsec">\n      Last updated: <[getLocaleAbbreviatedDatetimeString(jobQueuedMsec)]>\n    </div>\n\n    <div>\n      <md-card ng-if="recentNotifications.length === 0" class="oppia-page-card oppia-notifications-dashboard-card">\n        <em>No recent notifications.</em>\n      </md-card>\n\n      <div ng-if="recentNotifications.length > 0">\n        <a ng-href="<[getItemUrl(notification.activity_id, notification.type)]>"\n           ng-repeat="notification in recentNotifications">\n          <md-card class="oppia-dashboard-row"\n                   ng-class="{\'oppia-dashboard-row-recent\': lastSeenMsec && lastSeenMsec < notification.last_updated_ms && notification.author_username !== currentUsername}">\n            <div class="oppia-notification-content">\n              <span>\n                <span ng-if="notification.type === \'feedback_thread\'"\n                      title="Feedback thread">\n                  <i class="material-icons">&#xE0B9;</i>\n                </span>\n                <span ng-if="notification.type === \'exploration_commit\'"\n                      title="Exploration commit">\n                  <i class="material-icons">&#xE150;</i>\n                </span>\n              </span>\n              <span class="oppia-notification-author-username">\n                <strong>\n                  <span>\n                    <[notification.author_username]>\n                  </span>\n                  <span ng-if="!notification.author_username">\n                    Anonymous\n                  </span>\n                </strong>\n                <span ng-if="notification.type === \'exploration_commit\'">\n                  made a new commit to\n                </span>\n                <span ng-if="notification.type === \'feedback_thread\'">\n                  left a comment on\n                </span>\n                <span class="oppia-notification-activity-title">\n                  <[notification.activity_title]>\n                </span>\n              </span>\n            </div>\n            <div class="oppia-notification-last-updated">\n              <[getLocaleAbbreviatedDatetimeString(notification.last_updated_ms)]>\n            </div>\n          </md-card>\n        </a>\n      </div>\n    </div>\n  </div>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    pass
    yield u'\n  %s\n  <script src="%s/pages/notifications_dashboard/NotificationsDashboard.js"></script>\n' % (
        escape(context.call(l_0_super)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
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
debug_info = '1=11&16=17&74=24&75=32&76=33&3=36&7=43'