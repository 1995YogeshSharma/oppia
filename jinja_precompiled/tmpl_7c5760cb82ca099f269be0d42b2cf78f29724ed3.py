from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/email_dashboard/email_dashboard.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/email_dashboard/email_dashboard.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/email_dashboard/EmailDashboard.js"></script>\n  <script src="/templates/dev/head/pages/email_dashboard/EmailDashboardDataService.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-query-form" ng-controller="EmailDashboard">\n    <form class="form" ng-submit="submitQuery()">\n      Has not logged in for n days: <input type="number" min="0" ng-model="has_not_logged_in_for_n_days">\n      <br>\n      Inactive in last n days: <input type="number" min="0" ng-model="inactive_in_last_n_days">\n      <br>\n      Has created at least n exps: <input type="number" min="0" ng-model="created_at_least_n_exps">\n      <br>\n      Has created fewer than n exps: <input type="number" min="0" ng-model="created_fewer_than_n_exps">\n      <br>\n      Has edited at least n exps: <input type="number" min="0" ng-model="edited_at_least_n_exps">\n      <br>\n      Has edited fewer than n exps: <input type="number" min="0" ng-model="edited_fewer_than_n_exps">\n      <br>\n      <input type="submit" value="submit query">\n      <input type="reset" value="reset" ng-click="resetForm()">\n    </form>\n    <p class="success" ng-if="showSuccessMessage">Query has been submitted successfully. Check recent queries below.</p>\n    <div class="oppia-recent-queries">\n      <p>Recent queries:</p>\n      <table class="table" ng-if="currentPageOfQueries.length > 0">\n        <thead>\n          <tr>\n            <td>Query id</td>\n            <td>Submitted on</td>\n            <td>Submitted by</td>\n            <td>Status</td>\n            <td>No. of qualified users</td>\n          </tr>\n        </thead>\n        <tbody>\n          <tr ng-repeat="q in currentPageOfQueries track by $index">\n            <td><[q.id]></td>\n            <td><[q.created_on]></td>\n            <td><[q.submitter_username]></td>\n            <td><[q.status]></td>\n            <td><[q.num_qualified_users]></td>\n            <td><button ng-click="recheckStatus($index)">Re-check status</button></td>\n            <td ng-if="showLinkToResultPage(q.submitter_username, q.status)">\n              <a ng-href="/emaildashboardresult/<[q.id]>">\n                <button class="btn btn-link">Result</button>\n              </a>\n            </td>\n          </tr>\n        </tbody>\n      </table>\n      <button ng-if="showPreviousButton()" ng-click="getPreviousPageOfQueries()">Previous</button>\n      <button ng-if="showNextButton()" ng-click="getNextPageOfQueries()">Next</button>\n    </div>\n  </div>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Email Dashboard - Oppia\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    pass
    yield u'\n  %s\n  <style>\n    .success {\n      color: #0000ff;\n    }\n    .oppia-query-form {\n      text-align: center;\n    }\n  </style>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Email Dashboard\n    </li>\n  </ul>\n'

blocks = {'footer_js': block_footer_js, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&84=17&85=24&81=27&28=34&3=41&7=48&8=55&19=58'