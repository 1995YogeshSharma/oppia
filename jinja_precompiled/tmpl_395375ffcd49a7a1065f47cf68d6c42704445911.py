from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/admin.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_is_moderator = resolve('is_moderator')
    l_0_logout_url = resolve('logout_url')
    l_0_ASSET_DIR_PREFIX = resolve('ASSET_DIR_PREFIX')
    l_0_updatable_roles = resolve('updatable_roles')
    l_0_profile_picture_data_url = resolve('profile_picture_data_url')
    l_0_demo_collections = resolve('demo_collections')
    l_0_human_readable_current_time = resolve('human_readable_current_time')
    l_0_value_generators_js = resolve('value_generators_js')
    l_0_role_graph_data = resolve('role_graph_data')
    l_0_demo_explorations = resolve('demo_explorations')
    l_0_username = resolve('username')
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_csrf_token = resolve('csrf_token')
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    l_0_unfinished_job_data = resolve('unfinished_job_data')
    l_0_viewable_roles = resolve('viewable_roles')
    l_0_demo_exploration_ids = resolve('demo_exploration_ids')
    l_0_continuous_computations_data = resolve('continuous_computations_data')
    l_0_is_super_admin = resolve('is_super_admin')
    l_0_recent_job_data = resolve('recent_job_data')
    l_0_one_off_job_specs = resolve('one_off_job_specs')
    l_0_user_email = resolve('user_email')
    t_1 = environment.filters['js_string']
    pass
    yield u'<!DOCTYPE html>\n<html ng-app="oppia" ng-controller="Admin">\n  <head>\n    <title>Oppia Admin Panel</title>\n\n    '
    template = environment.get_template('pages/header_css_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u"\n\n    <script>\n      var GLOBALS = {\n        csrf_token: JSON.parse('%s'),\n        USERNAME: JSON.parse('%s'),\n        USER_EMAIL: JSON.parse('%s'),\n        PROFILE_PICTURE_DATA_URL: JSON.parse('%s'),\n        IS_MODERATOR: JSON.parse('%s'),\n        IS_SUPER_ADMIN: JSON.parse('%s'),\n        LOGOUT_URL: JSON.parse('%s'),\n        ASSET_DIR_PREFIX: JSON.parse('%s'),\n        TEMPLATE_DIR_PREFIX: JSON.parse('%s'),\n        DEMO_EXPLORATIONS: JSON.parse('%s'),\n        DEMO_EXPLORATION_IDS: JSON.parse('%s'),\n        DEMO_COLLECTIONS: JSON.parse('%s'),\n        HUMAN_READABLE_CURRENT_TIME: JSON.parse(\n          '%s'),\n        CONTINUOUS_COMPUTATIONS_DATA: JSON.parse(\n          '%s'),\n        ONE_OFF_JOB_SPECS: JSON.parse('%s'),\n        UNFINISHED_JOB_DATA: JSON.parse('%s'),\n        RECENT_JOB_DATA: JSON.parse('%s'),\n        UPDATABLE_ROLES: JSON.parse('%s'),\n        VIEWABLE_ROLES: JSON.parse('%s'),\n        ROLE_GRAPH_DATA: JSON.parse('%s'),\n        DEV_MODE: JSON.parse('%s')\n      }\n    </script>\n\n    " % (
        escape(t_1((undefined(name='csrf_token') if l_0_csrf_token is missing else l_0_csrf_token))), 
        escape(t_1((undefined(name='username') if l_0_username is missing else l_0_username))), 
        escape(t_1((undefined(name='user_email') if l_0_user_email is missing else l_0_user_email))), 
        escape(t_1((undefined(name='profile_picture_data_url') if l_0_profile_picture_data_url is missing else l_0_profile_picture_data_url))), 
        escape(t_1((undefined(name='is_moderator') if l_0_is_moderator is missing else l_0_is_moderator))), 
        escape(t_1((undefined(name='is_super_admin') if l_0_is_super_admin is missing else l_0_is_super_admin))), 
        escape(t_1((undefined(name='logout_url') if l_0_logout_url is missing else l_0_logout_url))), 
        escape(t_1((undefined(name='ASSET_DIR_PREFIX') if l_0_ASSET_DIR_PREFIX is missing else l_0_ASSET_DIR_PREFIX))), 
        escape(t_1((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX))), 
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
    )
    template = environment.get_template('pages/header_js_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </head>\n\n  <body>\n    <admin-navbar username="username" user-email="userEmail"\n                  profile-picture-data-url="profilePictureDataUrl"\n                  is-moderator="isModerator" is-super-admin="isSuperAdmin"\n                  logout-url="logoutUrl">\n    </admin-navbar>\n\n    <div align="center"\n         ng-if="statusMessage"\n         style="background-color: #ffffff; position: fixed; max-width: 30%; z-index: 3000; border: 1px solid #00376d; right: 30px; bottom: 30px">\n      <[statusMessage]>\n    </div>\n    <br>\n\n    <div style="padding-top: 16px;">\n      <admin-dev-mode-activities-tab ng-if="isActivitiesTabOpen() && inDevMode"\n                                     set-status-message="setStatusMessage">\n      </admin-dev-mode-activities-tab>\n      <admin-prod-mode-activities-tab ng-if="isActivitiesTabOpen() && !inDevMode">\n      </admin-prod-mode-activities-tab>\n\n      <admin-jobs-tab ng-if="isJobsTabOpen()"\n                      set-status-message="setStatusMessage">\n      </admin-jobs-tab>\n\n      <admin-config-tab ng-if="isConfigTabOpen()"\n                        set-status-message="setStatusMessage">\n      </admin-config-tab>\n\n      <admin-roles-tab ng-if="isRolesTabOpen()"\n                       set-status-message="setStatusMessage">\n      </admin-roles-tab>\n\n      <admin-misc-tab ng-if="isMiscTabOpen()"\n                      set-status-message="setStatusMessage">\n      </admin-misc-tab>\n    </div>\n\n    <div ng-if="inDevMode" class="oppia-dev-mode">\n      Dev Mode\n    </div>\n\n    '
    template = environment.get_template('pages/footer_js_libs.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n\n    <script src="%s/app.js"></script>\n\n    <script src="%s/pages/admin/Admin.js"></script>\n    <script src="%s/pages/admin/AdminNavbarDirective.js"></script>\n    <script src="%s/pages/admin/AdminRouterService.js"></script>\n    <script src="%s/pages/admin/AdminTaskManagerService.js"></script>\n    <script src="%s/pages/admin/activities_tab/AdminDevModeActivitiesTabDirective.js"></script>\n    <script src="%s/pages/admin/activities_tab/AdminProdModeActivitiesTabDirective.js"></script>\n    <script src="%s/pages/admin/config_tab/AdminConfigTabDirective.js"></script>\n    <script src="%s/pages/admin/jobs_tab/AdminJobsTabDirective.js"></script>\n\n    <script src="%s/pages/admin/roles_tab/RolesTabDirective.js"></script>\n    <script src="%s/pages/admin/roles_tab/RoleGraphDirective.js"></script>\n    <script src="%s/components/StateGraphLayoutService.js"></script>\n    <script src="%s/filters.js"></script>\n\n    <script src="%s/pages/admin/misc_tab/AdminMiscTabDirective.js"></script>\n    <script src="%s/directives.js"></script>\n    <script src="%s/services/AlertsService.js"></script>\n    <script src="%s/services/ExplorationContextService.js"></script>\n    <script src="%s/services/UtilsService.js"></script>\n    <script src="%s/services/IdGenerationService.js"></script>\n    <script src="%s/services/DebouncerService.js"></script>\n    <script src="%s/services/HtmlEscaperService.js"></script>\n    <script src="%s/services/RteHelperService.js"></script>\n    <script src="%s/services/SchemaDefaultValueService.js"></script>\n    <script src="%s/services/SchemaUndefinedLastElementService.js"></script>\n    <script src="%s/services/NestedDirectivesRecursionTimeoutPreventionService.js"></script>\n    <script src="%s/services/contextual/DeviceInfoService.js"></script>\n    <script src="%s/services/contextual/UrlService.js"></script>\n    <script src="%s/services/stateful/FocusManagerService.js"></script>\n\n    <script src="%s/components/forms/FormBuilder.js"></script>\n    <script src="%s/components/forms/ObjectEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedBoolEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedChoicesEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedCustomEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedExpressionEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedFloatEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedHtmlEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedIntEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n    <script src="%s/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n\n    <script src="%s/expressions/ExpressionSyntaxTreeService.js"></script>\n    <script src="%s/expressions/ExpressionEvaluatorService.js"></script>\n    <script src="%s/expressions/ExpressionParserService.js"></script>\n    <script src="%s/domain/utilities/UrlInterpolationService.js"></script>\n\n    ' % (
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
    )
    template = environment.get_template('components/rich_text_components.html', 'pages/admin/admin.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n\n    <script>\n      %s\n    </script>\n  </body>\n</html>' % (
        escape((undefined(name='value_generators_js') if l_0_value_generators_js is missing else l_0_value_generators_js)), 
    )

blocks = {}
debug_info = '6=34&10=38&11=39&12=40&13=41&14=42&15=43&16=44&17=45&18=46&19=47&20=48&21=49&23=50&25=51&26=52&27=53&28=54&29=55&30=56&31=57&32=58&36=60&81=64&83=68&85=69&86=70&87=71&88=72&89=73&90=74&91=75&92=76&94=77&95=78&96=79&97=80&99=81&100=82&101=83&102=84&103=85&104=86&105=87&106=88&107=89&108=90&109=91&110=92&111=93&112=94&113=95&115=96&116=97&117=98&118=99&119=100&120=101&121=102&122=103&123=104&124=105&125=106&126=107&127=108&129=109&130=110&131=111&132=112&134=114&137=118'