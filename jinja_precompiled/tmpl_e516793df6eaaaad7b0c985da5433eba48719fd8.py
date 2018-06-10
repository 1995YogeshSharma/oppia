from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/settings_tab/preview_summary_tile_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Preview Summary Card</h3>\n</div>\n\n<div class="modal-body text-center">\n  This is how your activity will appear to learners in search results\n  or the library.\n  <exploration-summary-tile exploration-title="getExplorationTitle()"\n                            objective="getExplorationObjective()"\n                            category="getExplorationCategory()"\n                            thumbnail-icon-url="getThumbnailIconUrl()"\n                            thumbnail-bg-color="getThumbnailBgColor()"\n                            class="protractor-test-exploration-summary-tile">\n  </exploration-summary-tile>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default protractor-test-close-preview-summary-modal" ng-click="close()">Return to editor</button>\n</div>'

blocks = {}
debug_info = ''