from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/library/search_results_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  search-results .oppia-search-results-no-match, search-results .oppia-search-results-no-match p {\n    font-size: 0.85em;\n    text-align: center;\n  }\n  search-results .oppia-search-results-intro {\n    font-size: 1.6em;\n    padding-bottom: 40px;\n    padding-top: 40px;\n  }\n  @media (max-width: 800px) {\n    search-results .oppia-search-results-intro {\n      margin-left: 20px;\n      margin-right: 20px;\n    }\n  }\n</style>\n\n<div>\n  <div class="visible-xs" style="margin: 0 auto; width: fit-content;">\n    <search-bar></search-bar>\n  </div>\n  <div ng-if="!someResultsExist" class="oppia-search-results-intro" ng-cloak>\n    <div class="oppia-search-results-no-match">\n      <img ng-src="<[noExplorationsImgUrl]>" alt="No explorations found">\n      <p style="text-align: center;">\n        <span translate="I18N_LIBRARY_NO_EXPLORATION_FOR_QUERY"></span><br><br>\n        <a ng-if="!userIsLoggedIn" href="" ng-click="onRedirectToLogin(\'/creator_dashboard?mode=create\')"\n           translate="I18N_LIBRARY_CREATE_EXPLORATION_QUESTION">\n        </a>\n        <a ng-if="userIsLoggedIn" href="/creator_dashboard?mode=create"\n           translate="I18N_LIBRARY_CREATE_EXPLORATION_QUESTION">\n        </a>\n      </p>\n    </div>\n  </div>\n\n  <activity-tiles-infinity-grid></activity-tiles-infinity-grid>\n</div>'

blocks = {}
debug_info = ''