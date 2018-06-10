from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/tests/jinja_escaping.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/tests/jinja_escaping.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_SITE_FEEDBACK_FORM_URL = resolve('SITE_FEEDBACK_FORM_URL')
    pass
    yield u'\n  <div class="oppia-page-card oppia-static-content">\n    <div class="oppia-static-card-content-wide">\n      <h2>Get involved!</h2>\n      <p>\n        Oppia is an open commons for education. And, true to this ethos,\n        it is an open-source website created through the hard work and\n        creativity of people like you! To get involved in the Oppia\n        project and help us bring about our mission of free, high-quality\n        universal education, reach out via our\n        <a href="https://groups.google.com/forum/#!forum/oppia-dev">oppia-dev@</a> Google Group, or contact us at\n        <a href="mailto:admin@oppia.org" class="inline-links">admin@oppia.org</a>.\n        We\'re excited to hear from you!\n      </p>\n\n      <p>\n        Also, if you have any feedback for us, please don\'t hesitate to let us know via our <a href="%s">feedback form</a> &mdash; we read all the feedback we receive. Thanks in advance!\n      </p>\n    </div>\n  </div>\n' % (
        escape((undefined(name='SITE_FEEDBACK_FORM_URL') if l_0_SITE_FEEDBACK_FORM_URL is missing else l_0_SITE_FEEDBACK_FORM_URL)), 
    )

blocks = {'content': block_content}
debug_info = '1=11&3=17&19=24'