from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/exploration_publish_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Publish Exploration</h3>\n</div>\n\n<div class="modal-body oppia-long-text">\n  <p>\n    Congratulations, you\'re about to publish an exploration!\n  </p>\n  <p>\n    Before publishing, please ensure that your exploration fits the\n    <a href="/teach#playbook" target="_blank">site publication criteria</a>. In particular, it should:\n    <ul>\n      <li>help its intended audience learn something new</li>\n      <li>provide useful feedback/guidance to help them if they get stuck.</li>\n    </ul>\n  </p>\n  <p>\n    Once the exploration is published, it will be available in the Oppia library for anyone to learn from and provide feedback. You can also check out\n      its stats by clicking on the Stats tab in the top right of the editor.\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-confirm-publish" ng-click="publish()">Publish Exploration</button>\n</div>'

blocks = {}
debug_info = ''