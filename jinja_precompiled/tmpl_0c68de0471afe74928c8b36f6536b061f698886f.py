from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/editor_tab/collection_node_creator_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<h2>Add Exploration</h2>\n<form class="form-inline" ng-submit="createNewExploration()">\n  <input class="form-control" ng-model="newExplorationTitle" type="text" placeholder="New exploration title">\n  <button class="btn btn-success" type="submit" ng-disabled="!newExplorationTitle">Create New Exploration</button>\n</form>\nor\n<form class="form-inline" ng-class="{\'has-error\': searchQueryHasError}" ng-submit="addExploration()">\n  <input class="form-control protractor-test-add-exploration-input" style="width: 430px" ng-model="newExplorationId" type="text" placeholder="Enter exploration id to be added, or search explorations by name" uib-typeahead="exploration for exploration in fetchTypeaheadResults($viewValue)" ng-model-options="{ debounce: 300 }">\n  <button class="btn btn-success protractor-test-add-exploration-button" type="submit" ng-disabled="!newExplorationId">Add Existing Exploration</button>\n  <span class="help-block" style="font-size: smaller" ng-if="isMalformedId(newExplorationId)">\n    <em>The trailing \'#\' is not part of the ID.</em>\n  </span>\n</form>'

blocks = {}
debug_info = ''