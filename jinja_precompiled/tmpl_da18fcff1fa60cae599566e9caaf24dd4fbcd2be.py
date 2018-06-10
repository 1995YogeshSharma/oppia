from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/embed_modal/embed_exploration_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  .oppia-embed-exploration-modal .oppia-embed-modal-code {\n    background-color: #fcfcfc;\n    border: 1px solid #d9d9d9;\n    border-radius: 4px;\n    display: inline-block;\n    padding: 10px;\n  }\n\n  .oppia-embed-exploration-modal .oppia-embed-modal-code:hover {\n    background-color: #f9f9f9;\n  }\n</style>\n\n<div class="oppia-embed-exploration-modal">\n  <div class="modal-header">\n    <h3>Embed this exploration</h3>\n  </div>\n\n  <div class="modal-body">\n    <p>\n      To embed this exploration in another webpage, copy the following HTML into the source code of the webpage:\n    </p>\n\n    <div class="oppia-embed-modal-code" ng-click="selectText($event)">&lt;iframe src="<[serverName]>/embed/exploration/<[explorationId]>" width="700" height="1000"&gt;</div>\n\n    <p>\n      For more details, as well as instructions on how to embed a particular version of an exploration, please see the <a href="https://oppia.github.io/#/EmbeddingAnExploration" target="_blank">documentation</a>.\n    </p>\n  </div>\n\n  <div class="modal-footer">\n    <button class="btn btn-default" ng-click="close()">Close</button>\n  </div>\n</div>'

blocks = {}
debug_info = ''