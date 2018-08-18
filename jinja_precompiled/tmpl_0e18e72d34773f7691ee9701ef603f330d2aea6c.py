from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/email_dashboard/email_dashboard_result.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/email_dashboard/email_dashboard_result.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <style>\n    .oppia-email-form {\n      text-align: center;\n      margin-top: 2%;\n    }\n    .disable-form {\n      pointer-events: none;\n      opacity: 0.6;\n    }\n    textarea {\n      margin-bottom: 1%;\n      border-radius: 10px;\n    }\n    .invalid-input {\n      color: red;\n    }\n    .success {\n      color: green;\n    }\n    .warning {\n      color: #ccb418;\n    }\n  </style>\n  <div class="oppia-email-form" ng-controller="EmailDashboardResult">\n    <p ng-if="emailSubmitted" class="success">Emails sent successfully. Redirecting to the Email Dashboard...</p>\n    <p ng-if="testEmailSentSuccessfully" class="success">Test email sent successfully. Please check your inbox.</p>\n    <p ng-if="emailCancelled" class="warning">Emails cancelled. Redirecting to the Email Dashboard...</p>\n    <p ng-if="invalid.subject" class="invalid-input">Please enter a valid email subject</p>\n    <p ng-if="invalid.body" class="invalid-input">Please enter a valid email body</p>\n    <p ng-if="invalid.maxRecipients" class="invalid-input">Please enter valid number of recipients</p>\n    <p ng-if="errorHasOccurred" class="invalid-input">There was an error processing your request. Please report this bug.</p>\n    <form ng-class = "{\'disable-form\': submitIsInProgress}" ng-submit="submitEmail()">\n      Email subject: <textarea rows="2" cols="10" placeholder="Enter email subject here..." ng-model="emailSubject"></textarea>\n      <br>\n      Email body: <textarea rows="15" cols="20" placeholder="Enter email body here..." ng-model="emailBody"></textarea>\n      <br>\n      Email intent: <select ng-model="emailIntent" ng-options="intent for intent in POSSIBLE_EMAIL_INTENTS"></select><br><br>\n      Email option: <input type="radio" name="email" ng-model="emailOption" value="all" checked> Send to all\n      <input type="radio" name="email" ng-model="emailOption" value="custom"> Send to max N users:\n      <input type="number" ng-model="maxRecipients" min="0" placeholder="Enter number of users..." ng-disabled="emailOption == \'all\'"><br><br>\n      <input class="btn btn-default" type="button" ng-click="sendTestEmail()" value="Send yourself a test email">\n      <input class="btn btn-success" type="submit" value="Submit Email">\n      <input class="btn btn-default" type="reset" value="Reset" ng-click="resetForm()">\n      <input class="btn btn-danger" type="button" ng-click="cancelEmail()" value="Cancel">\n    </form>\n  </div>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/email_dashboard/EmailDashboardResult.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Email Dashboard Result - Oppia\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    pass
    yield u'\n  %s\n' % (
        escape(context.call(l_0_super)), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Email Dashboard Result\n    </li>\n  </ul>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&20=17&69=24&70=31&3=34&7=41&8=48&11=51'