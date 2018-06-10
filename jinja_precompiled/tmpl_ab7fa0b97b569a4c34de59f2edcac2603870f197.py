from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/editor_tab/collection_node_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card class="collection-editor-node">\n  <div class="collection-editor-node-title">\n    <a ng-href="/create/<[getCollectionNode().getExplorationId()]>" target="_blank">\n      <[getCollectionNode().getExplorationTitle()]>\n    </a>\n  </div>\n  <span class="collection-editor-delete-node protractor-test-editor-delete-node">\n    <span ng-click="deleteNode()" aria-hidden="true">\n      <i class="material-icons md-18">&#xE14C;</i>\n    </span>\n  </span>\n  <span ng-click="shiftNodeLeft()"\n        ng-if="getLinearIndex() > 0"\n        class="collection-editor-shift-left-arrow protractor-test-editor-shift-left"\n        aria-hidden="true">\n    <i class="material-icons">&#xE5CB;</i>\n  </span>\n  <span ng-click="shiftNodeRight()"\n        ng-if="getLinearIndex() < collection.getCollectionNodeCount() - 1"\n        class="collection-editor-shift-right-arrow protractor-test-editor-shift-right"\n        aria-hidden="true">\n    <i class="material-icons">&#xE5CC;</i>\n  </span>\n</md-card>\n\n<style>\n  .collection-editor-node {\n    background-color: #F5F5F5;\n    color: #424242;\n    display: inline-block;\n    font-family: "Capriola", "Roboto", Arial, sans-serif;\n    font-size: 0.8em;\n    margin: 0;\n    padding-top: 5px;\n    padding-bottom: 5px;\n    position: relative;\n    text-align: center;\n  }\n\n  .collection-editor-delete-node {\n    color: #ef5350;\n    position: absolute;\n    right: 0;\n    top: 0;\n  }\n\n  .collection-editor-shift-left-arrow {\n    bottom: 0;\n    color: #000;\n    left: 0;\n    opacity: 0.7;\n    position: absolute;\n  }\n  .collection-editor-shift-right-arrow {\n    bottom: 0;\n    color: #000;\n    position: absolute;\n    opacity: 0.7;\n    right: 0;\n  }\n\n  .collection-editor-node-title {\n    padding: 16px 16px 20px 16px;\n  }\n</style>'

blocks = {}
debug_info = ''