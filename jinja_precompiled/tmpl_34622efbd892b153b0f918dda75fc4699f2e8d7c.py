from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/moderator/moderator.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/moderator/moderator.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="Moderator">\n    <div class="oppia-content">\n      <br>\n      <uib-tabset>\n        <uib-tab heading="Recent Commits" active>\n          <h3>Recent Commits (all non-private explorations)</h3>\n          <div ng-show="allCommits.length">\n            <table class="oppia-padded-table">\n              <tr>\n                <th>Timestamp</th>\n                <th>Exploration</th>\n                <th>Category</th>\n                <th>Username</th>\n                <th>Commit message</th>\n                <th>Community-owned?</th>\n              </tr>\n              <tr ng-repeat="commit in allCommits track by $index">\n                <td><[getDatetimeAsString(commit.last_updated)]></td>\n                <td>\n                  <a ng-href="<[getExplorationCreateUrl(commit.exploration_id)]>">\n                    <[explorationData[commit.exploration_id].title]>\n                  </a>\n                </td>\n                <td>\n                  <[explorationData[commit.exploration_id].category]>\n                </td>\n                <td><[commit.username]></td>\n                <td><[commit.commit_message]></td>\n                <td><[commit.post_commit_community_owned]></td>\n              </tr>\n            </table>\n          </div>\n        </uib-tab>\n\n        <uib-tab heading="Recent Feedback Messages">\n          <h3>Recent Feedback Messages</h3>\n          (Note that some of these links may be to private explorations, and thus result in authorization errors.)\n          <br>\n          <br>\n          <div ng-show="allFeedbackMessages.length">\n            <table class="oppia-padded-table">\n              <tr>\n                <th>Timestamp</th>\n                <th>Exploration ID</th>\n                <th>Username</th>\n              </tr>\n              <tr ng-repeat="message in allFeedbackMessages track by $index">\n                <td><[getDatetimeAsString(message.created_on)]></td>\n                <td>\n                  <a ng-href="<[getExplorationCreateUrl(message.exploration_id)]>">\n                    <[message.exploration_id]>\n                  </a>\n                </td>\n                <td><[message.author_username]></td>\n              </tr>\n            </table>\n          </div>\n        </uib-tab>\n\n        <uib-tab heading="Featured Activities">\n          <h3>Activities to feature in the library</h3>\n          <br>\n          <br>\n\n          <schema-based-editor schema="FEATURED_ACTIVITY_REFERENCES_SCHEMA"\n                               local-value="displayedFeaturedActivityReferences">\n          </schema-based-editor>\n          <br>\n          <br>\n\n          <button class="btn btn-success" ng-click="saveFeaturedActivityReferences()"\n                  ng-disabled="isSaveFeaturedActivitiesButtonDisabled()">\n            Save Featured Activities\n          </button>\n        </uib-tab>\n      </uib-tabset>\n    </div>\n  </div>\n  <style>\n    table.oppia-padded-table {\n      border: 1px solid black;\n      padding: 5px;\n    }\n    table.oppia-padded-table th, table.oppia-padded-table td {\n      border: 1px solid black;\n      padding: 5px;\n    }\n  </style>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n  <script src="/templates/dev/head/services/SchemaDefaultValueService.js"></script>\n  <script src="/templates/dev/head/services/SchemaUndefinedLastElementService.js"></script>\n  <script src="/templates/dev/head/services/NestedDirectivesRecursionTimeoutPreventionService.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedChoicesEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n\n  <script src="/templates/dev/head/pages/moderator/Moderator.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Moderator Tools - Oppia\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Moderator Tools\n    </li>\n  </ul>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&16=17&107=24&108=31&3=34&7=41'