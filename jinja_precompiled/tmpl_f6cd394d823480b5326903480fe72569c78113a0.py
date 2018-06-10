from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/collection_editor_pre_publish_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Add Some Details</h3>\n</div>\n\n<div class="modal-body oppia-long-text">\n  <p>\n    Just a few more things before you publish:\n  </p>\n  <p ng-if="requireTitleToBeSpecified">\n    Add a title: what should your collection be called?\n    <input type="text" class="form-control protractor-collection-editor-title-input" ng-model="$parent.newTitle"\n           placeholder="Music in the 19th Century">\n  </p>\n  <p ng-if="requireObjectiveToBeSpecified">\n    Add a goal: what does the collection help people to do?\n    <input type="text" class="form-control protractor-collection-editor-objective-input" ng-model="$parent.newObjective"\n           placeholder="Learn how to ...">\n  </p>\n  <p ng-if="requireCategoryToBeSpecified">\n    Add a category: how would you categorize your collection?\n    <select2-dropdown item="$parent.newCategory"\n                      choices="CATEGORY_LIST_FOR_SELECT2"\n                      class="protractor-test-collection-editor-category-dropdown"\n                      placeholder="Choose or type new"\n                      new-choice-regex="^[A-Z a-z]+$"\n                      width="100%"\n                      invalid-search-term-message="Invalid category name">\n    </select2-dropdown>\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-collection-save-changes-button" ng-click="save()" ng-disabled="!isSavingAllowed()">Save Changes</button>\n</div>'

blocks = {}
debug_info = ''