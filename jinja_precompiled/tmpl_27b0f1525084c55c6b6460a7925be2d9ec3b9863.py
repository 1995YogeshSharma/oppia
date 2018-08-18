from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_html_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<!-- label-for-focus-target feature is removed since CKEditor has a\nfocusManager to manage the focus activity automatically. -->\n<ck-editor-rte ng-if="!isDisabled()" ng-model="$parent.localValue"\n               ui-config="uiConfig()">\n</ck-editor-rte>\n\n<span ng-if="isDisabled()"\n      ng-class="{\'oppia-disabled-contenteditable\': isDisabled()}"\n      ng-bind-html="localValue">\n</span>'

blocks = {}
debug_info = ''