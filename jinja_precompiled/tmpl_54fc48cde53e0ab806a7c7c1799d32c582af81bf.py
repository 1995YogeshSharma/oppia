from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/learner_dashboard/learner_dashboard_icons_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<i class="oppia-learner-dashboard-icon fa fa-clock-o"\n   ng-if="isAddToPlaylistIconShown()"\n   ng-show="canActivityBeAddedToLearnerPlaylist(getActivityId()) && !isContainerNarrow()"\n   ng-click="addToLearnerPlaylist(getActivityId(), getActivityType())"\n   ng-mouseenter="setHoverState(true)" ng-mouseleave="setHoverState(false)"\n   aria-hidden="true"\n   uib-tooltip="<[\'I18N_LIBRARY_ADD_TO_LEARNER_PLAYLIST\' | translate]>"\n   tooltip-placement="left">\n</i>\n<div ng-show="canActivityBeAddedToLearnerPlaylist(getActivityId()) && isContainerNarrow()" class="btn-group dropdown oppia-learner-dashboard-icon" uib-dropdown>\n  <ul style="left:-150px;top:0" class="dropdown-menu" uib-dropdown-menu role="menu" aria-labelledby="single-button">\n    <li role="menuitem" ng-click="addToLearnerPlaylist(getActivityId(), getActivityType())">\n      <a><[\'I18N_LIBRARY_ADD_TO_LEARNER_PLAYLIST\' | translate]></a>\n    </li>\n  </ul>\n  <i class="fa fa-ellipsis-v dropdown-toggle" uib-dropdown-toggle></i>\n</div>\n<i class="oppia-learner-dashboard-icon fa fa-clock-o"\n   ng-if="belongsToLearnerPlaylist()"\n   ng-click="removeFromLearnerPlaylist(getActivityId(), getActivityTitle(), getActivityType())"\n   aria-hidden="true"\n   tooltip-enable="<[playlistTooltipIsEnabled]>"\n   ng-mouseleave="enablePlaylistTooltip()"\n   uib-tooltip="<[\'I18N_LIBRARY_ACTIVITY_IN_LEARNER_PLAYLIST\' | translate]>"\n   tooltip-placement="left">\n</i>\n<i class="oppia-learner-dashboard-icon fa fa-check-circle-o"\n   ng-if="belongsToCompletedActivities()"\n   aria-hidden="true"\n   uib-tooltip="<[\'I18N_LIBRARY_ACTIVITY_COMPLETED_ICON\' | translate]>"\n   tooltip-placement="left">\n</i>\n<i class="oppia-learner-dashboard-icon fa fa-spinner"\n   ng-if="belongsToIncompleteActivities()"\n   aria-hidden="true"\n   tooltip-append-to-body="true"\n   tooltip-class="library-incomplete-activity-tooltip"\n   uib-tooltip="<[\'I18N_LIBRARY_INCOMPLETE_ACTIVITY_ICON\' | translate]>"\n   tooltip-placement="left">\n</i>\n<style>\n  .library-incomplete-activity-tooltip .tooltip-inner {\n    max-width: none;\n    white-space: nowrap;\n  }\n</style>'

blocks = {}
debug_info = ''