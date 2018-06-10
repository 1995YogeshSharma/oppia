from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/outcome_feedback_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  outcome-feedback-editor .oppia-rule-edit-feedback {\n    position: relative;\n  }\n</style>\n<div class="oppia-rule-edit-feedback protractor-test-feedback-bubble">\n  <div class="oppia-rule-details-header">\n    <strong>Oppia tells the learner...</strong>\n  </div>\n  <span ng-if="!outcome.hasNonemptyFeedback()">\n    <em>No feedback specified.</em>\n  </span>\n\n  <!-- TODO(sll): Find a way to do this without resorting to private properties like _html -->\n  <schema-based-editor schema="OUTCOME_FEEDBACK_SCHEMA" local-value="outcome.feedback._html">\n  </schema-based-editor>\n</div>'

blocks = {}
debug_info = ''