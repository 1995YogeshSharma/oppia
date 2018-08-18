from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/misc_tab/admin_misc_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card class="oppia-page-card oppia-long-text" style="max-width: 700px">\n  <h3>Topic Similarities</h3>\n  <div>\n    Upload a csv file:<br>\n    The first line of data should be a list of topic names. The next lines should be a symmetric adjacency matrix of similarities, which are values between 0 and 1.<br>\n    <input type="file" id="topicSimilaritiesFile">\n    <button ng-click="uploadTopicSimilaritiesFile()">Upload</button><br>\n    <button ng-click="downloadTopicSimilaritiesFile()">Download current topic similarities</button>\n  </div>\n</md-card>\n\n<md-card class="oppia-page-card oppia-long-text" style="max-width: 700px">\n  <h3>Search Index</h3>\n  <button ng-click="clearSearchIndex()">Clear Search Index</button>\n</md-card>\n\n<md-card class="oppia-page-card oppia-long-text" style="max-width: 700px">\n  <h3>Extract Data</h3>\n  <div class="oppia-query-form">\n    <form class="form" ng-submit="submitQuery()">\n      Exploration ID: <input type="text" ng-model="expId" required="true">\n      <br>\n      Exploration version: <input type="number" min="0" ng-model="expVersion" required="true">\n      <br>\n      State name: <input type="text" ng-model="stateName" required="true">\n      <br>\n      Number of answers: <input type="number" min="0" ng-model="numAnswers" required="true">\n      <br>\n      <input type="submit" value="submit query">\n      <input type="reset" value="reset">\n    </form>\n    <br>\n    <p> (To get all answers set number of answers to 0) </p>\n    <p ng-if="showDataExtractionQueryStatus">Status: <[dataExtractionQueryStatusMessage]></p>\n  </div>\n</md-card>'

blocks = {}
debug_info = ''