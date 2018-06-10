from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_html_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<text-angular-rte ng-if="!isDisabled()" html-content="$parent.localValue"\n                ui-config="uiConfig()" label-for-focus-target="labelForFocusTarget()">\n</text-angular-rte>\n<span ng-if="isDisabled()"\n    ng-class="{\'oppia-disabled-contenteditable\': isDisabled()}"\n    ng-bind-html="localValue">\n</span>'

blocks = {}
debug_info = ''