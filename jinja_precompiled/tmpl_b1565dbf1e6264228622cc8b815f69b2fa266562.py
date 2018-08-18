from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_player/collection_node_list_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<exploration-summary-tile ng-repeat="collectionNode in getCollectionNodes()"\n                          collection-id="getCollectionId()"\n                          exploration-id="collectionNode.getExplorationId()"\n                          exploration-title="collectionNode.getExplorationSummaryObject().title"\n                          last-updated-msec="collectionNode.getExplorationSummaryObject().last_updated_msec"\n                          objective="collectionNode.getExplorationSummaryObject().objective"\n                          category="collectionNode.getExplorationSummaryObject().category"\n                          ratings="collectionNode.getExplorationSummaryObject().ratings"\n                          num-views="collectionNode.getExplorationSummaryObject().num_views"\n                          thumbnail-icon-url="collectionNode.getExplorationSummaryObject().thumbnail_icon_url"\n                          thumbnail-bg-color="collectionNode.getExplorationSummaryObject().thumbnail_bg_color"\n                          is-community-owned="collectionNode.getExplorationSummaryObject().community_owned">\n</exploration-summary-tile>'

blocks = {}
debug_info = ''