from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/signup/licence_explanation_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3 translate="I18N_SIGNUP_WHY_LICENSE"></h3>\n</div>\n\n<div class="modal-body oppia-long-text">\n  <p style="line-height: 1.5;" translate="I18N_SIGNUP_SITE_OBJECTIVE" translate-values="{sitename: siteName}">\n  </p>\n\n  <p style="line-height: 1.5;" translate="I18N_SIGNUP_LICENSE_OBJECTIVE" translate-licenselink="<a href=&quot;https://creativecommons.org/licenses/by-sa/4.0/&quot; target=&quot;_blank&quot;>CC-BY-SA v4.0</a>">\n  </p>\n\n  <p style="line-height: 1.5;" translate="I18N_SIGNUP_WAIVER_OBJECTIVE"></p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="close()" translate="I18N_SIGNUP_CLOSE_BUTTON"></button>\n</div>'

blocks = {}
debug_info = ''