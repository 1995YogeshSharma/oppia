from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/editor_tab/collection_editor_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-if="hasLoadedCollection()">\n  <div class="collection-editor-cards-container">\n    <md-card class="oppia-page-card oppia-long-text">\n      <!-- Collection node list graph -->\n      <div class="collection-editor-node-list-container">\n        <div ng-if="collection.getCollectionNodeCount() === 0">\n          No explorations have been added to this collection yet.\n        </div>\n        <div ng-if="collection.getCollectionNodeCount() > 0">\n          <div class="collection-editor-node-container"\n               ng-repeat="node in getLinearlySortedNodes() track by $index">\n            <collection-node-editor collection-node="node"\n                                    linear-index="$index"\n                                    ng-class="{true: \'collection-editor-last-node\'} [$last]">\n            </collection-node-editor>\n\n            <div ng-if="!$last"\n                 class="collection-editor-node-connector-container">\n              <svg class="collection-editor-node-connector">\n                <defs>\n                  <marker id="arrow" markerWidth="10" markerHeight="10"\n                          refx="0" refy="3" orient="auto"\n                          markerUnits="strokeWidth" viewBox="0 0 20 20">\n                    <path d="M0,0 L0,6 L9,3 z" stroke="#88888A"/>\n                  </marker>\n                </defs>\n\n                <line x1="0" y1="25" x2="35" y2="25" stroke="#88888A"\n                      stroke-width="2" marker-end="url(#arrow)" />\n              </svg>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <collection-node-creator></collection-node-creator>\n    </md-card>\n  </div>\n</div>\n\n<style>\n  .collection-editor-cards-container {\n    margin: auto;\n    max-width: 898px;\n    position: relative;\n  }\n\n  .collection-editor-last-node {\n    margin-right: 20px;\n  }\n\n  .collection-editor-node-list-container {\n    background-color: white;\n    border: 1px solid #BDBDBD;\n    display: block;\n    margin: 30px auto;\n    min-width: 98%;\n    overflow-x: auto;\n    padding: 70px 20px;\n    text-align: center;\n    white-space: nowrap;\n    width: 98%;\n  }\n\n  .collection-editor-node-container, .collection-editor-node-connector-container{\n    display: inline-block;\n  }\n\n  .collection-editor-node-connector-container {\n    margin-left: -4px;\n    width: 45px;\n  }\n\n  .collection-editor-node-connector {\n    width: 50px;\n    height: 30px;\n  }\n\n  svg {\n    color: #88888A;\n  }\n</style>'

blocks = {}
debug_info = ''