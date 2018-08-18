from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/admin.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_username = resolve('username')
    l_0_is_moderator = resolve('is_moderator')
    l_0_human_readable_current_time = resolve('human_readable_current_time')
    l_0_logout_url = resolve('logout_url')
    l_0_value_generators_js = resolve('value_generators_js')
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_csrf_token = resolve('csrf_token')
    l_0_demo_collections = resolve('demo_collections')
    l_0_demo_exploration_ids = resolve('demo_exploration_ids')
    l_0_recent_job_data = resolve('recent_job_data')
    l_0_continuous_computations_data = resolve('continuous_computations_data')
    l_0_user_is_logged_in = resolve('user_is_logged_in')
    l_0_unfinished_job_data = resolve('unfinished_job_data')
    l_0_is_super_admin = resolve('is_super_admin')
    l_0_demo_explorations = resolve('demo_explorations')
    l_0_role_graph_data = resolve('role_graph_data')
    l_0_one_off_job_specs = resolve('one_off_job_specs')
    l_0_updatable_roles = resolve('updatable_roles')
    l_0_viewable_roles = resolve('viewable_roles')
    l_0_user_email = resolve('user_email')
    t_1 = environment.filters['js_string']
    pass
    yield u'<!DOCTYPE html>\n<html ng-app="oppia" ng-controller="Admin">\n  <head>\n    <title>Oppia Admin Panel</title>\n\n    '
    template = environment.get_template('pages/header_css_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u"\n\n    <script>\n      var GLOBALS = {\n        csrf_token: JSON.parse('%s'),\n        USERNAME: JSON.parse('%s'),\n        USER_EMAIL: JSON.parse('%s'),\n        IS_MODERATOR: JSON.parse('%s'),\n        IS_SUPER_ADMIN: JSON.parse('%s'),\n        LOGOUT_URL: JSON.parse('%s'),\n        DEMO_EXPLORATIONS: JSON.parse('%s'),\n        DEMO_EXPLORATION_IDS: JSON.parse('%s'),\n        DEMO_COLLECTIONS: JSON.parse('%s'),\n        HUMAN_READABLE_CURRENT_TIME: JSON.parse(\n          '%s'),\n        CONTINUOUS_COMPUTATIONS_DATA: JSON.parse(\n          '%s'),\n        ONE_OFF_JOB_SPECS: JSON.parse('%s'),\n        UNFINISHED_JOB_DATA: JSON.parse('%s'),\n        RECENT_JOB_DATA: JSON.parse('%s'),\n        UPDATABLE_ROLES: JSON.parse('%s'),\n        VIEWABLE_ROLES: JSON.parse('%s'),\n        ROLE_GRAPH_DATA: JSON.parse('%s'),\n        DEV_MODE: JSON.parse('%s'),\n        userIsLoggedIn: JSON.parse('%s'),\n      }\n    </script>\n\n    " % (
        escape(t_1((undefined(name='csrf_token') if l_0_csrf_token is missing else l_0_csrf_token))), 
        escape(t_1((undefined(name='username') if l_0_username is missing else l_0_username))), 
        escape(t_1((undefined(name='user_email') if l_0_user_email is missing else l_0_user_email))), 
        escape(t_1((undefined(name='is_moderator') if l_0_is_moderator is missing else l_0_is_moderator))), 
        escape(t_1((undefined(name='is_super_admin') if l_0_is_super_admin is missing else l_0_is_super_admin))), 
        escape(t_1((undefined(name='logout_url') if l_0_logout_url is missing else l_0_logout_url))), 
        escape(t_1((undefined(name='demo_explorations') if l_0_demo_explorations is missing else l_0_demo_explorations))), 
        escape(t_1((undefined(name='demo_exploration_ids') if l_0_demo_exploration_ids is missing else l_0_demo_exploration_ids))), 
        escape(t_1((undefined(name='demo_collections') if l_0_demo_collections is missing else l_0_demo_collections))), 
        escape(t_1((undefined(name='human_readable_current_time') if l_0_human_readable_current_time is missing else l_0_human_readable_current_time))), 
        escape(t_1((undefined(name='continuous_computations_data') if l_0_continuous_computations_data is missing else l_0_continuous_computations_data))), 
        escape(t_1((undefined(name='one_off_job_specs') if l_0_one_off_job_specs is missing else l_0_one_off_job_specs))), 
        escape(t_1((undefined(name='unfinished_job_data') if l_0_unfinished_job_data is missing else l_0_unfinished_job_data))), 
        escape(t_1((undefined(name='recent_job_data') if l_0_recent_job_data is missing else l_0_recent_job_data))), 
        escape(t_1((undefined(name='updatable_roles') if l_0_updatable_roles is missing else l_0_updatable_roles))), 
        escape(t_1((undefined(name='viewable_roles') if l_0_viewable_roles is missing else l_0_viewable_roles))), 
        escape(t_1((undefined(name='role_graph_data') if l_0_role_graph_data is missing else l_0_role_graph_data))), 
        escape(t_1((undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE))), 
        escape(t_1((undefined(name='user_is_logged_in') if l_0_user_is_logged_in is missing else l_0_user_is_logged_in))), 
    )
    template = environment.get_template('pages/header_js_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </head>\n\n  <body>\n    <admin-navbar username="username" user-email="userEmail"\n                  is-moderator="isModerator" is-super-admin="isSuperAdmin"\n                  logout-url="logoutUrl">\n    </admin-navbar>\n\n    <div align="center"\n         ng-if="statusMessage"\n         style="background-color: #ffffff; position: fixed; max-width: 30%; z-index: 3000; border: 1px solid #00376d; right: 30px; bottom: 30px">\n      <[statusMessage]>\n    </div>\n    <br>\n\n    <div style="padding-top: 16px;">\n      <admin-dev-mode-activities-tab ng-if="isActivitiesTabOpen() && inDevMode"\n                                     set-status-message="setStatusMessage">\n      </admin-dev-mode-activities-tab>\n      <admin-prod-mode-activities-tab ng-if="isActivitiesTabOpen() && !inDevMode">\n      </admin-prod-mode-activities-tab>\n\n      <admin-jobs-tab ng-if="isJobsTabOpen()"\n                      set-status-message="setStatusMessage">\n      </admin-jobs-tab>\n\n      <admin-config-tab ng-if="isConfigTabOpen()"\n                        set-status-message="setStatusMessage">\n      </admin-config-tab>\n\n      <admin-roles-tab ng-if="isRolesTabOpen()"\n                       set-status-message="setStatusMessage">\n      </admin-roles-tab>\n\n      <admin-misc-tab ng-if="isMiscTabOpen()"\n                      set-status-message="setStatusMessage">\n      </admin-misc-tab>\n    </div>\n\n    <div ng-if="inDevMode" class="oppia-dev-mode">\n      Dev Mode\n    </div>\n\n    '
    template = environment.get_template('pages/footer_js_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n\n    <script src="/templates/dev/head/app.js"></script>\n\n    <script src="/templates/dev/head/pages/admin/Admin.js"></script>\n    <script src="/templates/dev/head/pages/admin/AdminNavbarDirective.js"></script>\n    <script src="/templates/dev/head/pages/admin/AdminRouterService.js"></script>\n    <script src="/templates/dev/head/pages/admin/AdminTaskManagerService.js"></script>\n    <script src="/templates/dev/head/pages/admin/activities_tab/AdminDevModeActivitiesTabDirective.js"></script>\n    <script src="/templates/dev/head/pages/admin/activities_tab/AdminProdModeActivitiesTabDirective.js"></script>\n    <script src="/templates/dev/head/pages/admin/config_tab/AdminConfigTabDirective.js"></script>\n    <script src="/templates/dev/head/pages/admin/jobs_tab/AdminJobsTabDirective.js"></script>\n\n    <script src="/templates/dev/head/pages/admin/roles_tab/RolesTabDirective.js"></script>\n    <script src="/templates/dev/head/pages/admin/roles_tab/RoleGraphDirective.js"></script>\n    <script src="/templates/dev/head/components/StateGraphLayoutService.js"></script>\n    <script src="/templates/dev/head/filters.js"></script>\n\n    <script src="/templates/dev/head/pages/admin/misc_tab/AdminMiscTabDirective.js"></script>\n    <script src="/templates/dev/head/directives.js"></script>\n    <script src="/templates/dev/head/services/AlertsService.js"></script>\n    <script src="/templates/dev/head/services/ContextService.js"></script>\n    <script src="/templates/dev/head/services/UtilsService.js"></script>\n    <script src="/templates/dev/head/services/IdGenerationService.js"></script>\n    <script src="/templates/dev/head/services/DebouncerService.js"></script>\n    <script src="/templates/dev/head/services/HtmlEscaperService.js"></script>\n    <script src="/templates/dev/head/services/RteHelperService.js"></script>\n    <script src="/templates/dev/head/services/SchemaDefaultValueService.js"></script>\n    <script src="/templates/dev/head/services/SchemaUndefinedLastElementService.js"></script>\n    <script src="/templates/dev/head/services/NestedDirectivesRecursionTimeoutPreventionService.js"></script>\n    <script src="/templates/dev/head/services/UserService.js"></script>\n    <script src="/templates/dev/head/services/contextual/DeviceInfoService.js"></script>\n    <script src="/templates/dev/head/services/contextual/UrlService.js"></script>\n    <script src="/templates/dev/head/services/stateful/FocusManagerService.js"></script>\n\n    <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n    <script src="/templates/dev/head/components/forms/ObjectEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedBoolEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedChoicesEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedCustomEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedExpressionEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedFloatEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedHtmlEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedIntEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n    <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n\n    <script src="/templates/dev/head/expressions/ExpressionSyntaxTreeService.js"></script>\n    <script src="/templates/dev/head/expressions/ExpressionEvaluatorService.js"></script>\n    <script src="/templates/dev/head/expressions/ExpressionParserService.js"></script>\n    <script src="/templates/dev/head/domain/utilities/UrlInterpolationService.js"></script>\n\n    '
    template = environment.get_template('components/rich_text_components.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n\n    <script>\n      %s\n    </script>\n  </body>\n</html>' % (
        escape((undefined(name='value_generators_js') if l_0_value_generators_js is missing else l_0_value_generators_js)), 
    )

blocks = {}
debug_info = '6=32&10=36&11=37&12=38&13=39&14=40&15=41&16=42&17=43&18=44&20=45&22=46&23=47&24=48&25=49&26=50&27=51&28=52&29=53&30=54&34=56&78=60&132=64&135=68'