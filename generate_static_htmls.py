import os
import json

import utils  # pylint: disable=relative-import

import jinja2
from jinja2 import meta

def _js_string_filter(value):
    """Converts a value to a JSON string for use in JavaScript code."""
    # string = json.dumps(value)
    #
    # replacements = [('\\', '\\\\'), ('"', '\\"'), ("'", "\\'"),
    #                 ('\n', '\\n'), ('\r', '\\r'), ('\b', '\\b'),
    #                 ('<', '\\u003c'), ('>', '\\u003e'), ('&', '\\u0026')]
    #
    # for replacement in replacements:
    #     string = string.replace(replacement[0], replacement[1])
    # return jinja2.utils.Markup(string)
    return jinja2.utils.Markup('')


def _log2_floor_filter(value):
    """Returns the logarithm base 2 of the given value, rounded down."""
    return int(math.log(value, 2))


JINJA_FILTERS = {
    'is_list': lambda x: isinstance(x, list),
    'is_dict': lambda x: isinstance(x, dict),
    'js_string': _js_string_filter,
    'log2_floor': _log2_floor_filter,
}

def get_jinja_env(dir_path):
    # loader = jinja2.FileSystemLoader(os.path.join(
    #     os.path.dirname(__file__), dir_path))
    print '^^^^^^^^^^^^^^^^^^^^^^^^'
    print os.path.join(
            os.path.dirname(__file__), 'jinja_precompiled/')
    loader = jinja2.ChoiceLoader([
        jinja2.ModuleLoader(os.path.join(
            os.path.dirname(__file__), 'jinja_precompiled/')),
        jinja2.FileSystemLoader(os.path.join(
            os.path.dirname(__file__), dir_path))
        ])
    env = jinja2.Environment(autoescape=True, loader=loader)

    def get_static_resource_url(resource_suffix):
        """Returns the relative path for the resource, appending it to the
        corresponding cache slug. resource_suffix should have a leading
        slash.
        """
        return '%s%s' % (utils.get_asset_dir_prefix(), resource_suffix)

    def get_complete_static_resource_url(domain_url, resource_suffix):
        """Returns the relative path for the resource, appending it to the
        corresponding cache slug. resource_suffix should have a leading
        slash.
        """
        return '%s%s%s' % (
            domain_url, utils.get_asset_dir_prefix(), resource_suffix)

    print '\n\nFUNCTION CALLED\n\n'
    env.globals['get_static_resource_url'] = get_static_resource_url
    env.globals['get_complete_static_resource_url'] = (
        get_complete_static_resource_url)
    env.filters.update(JINJA_FILTERS)

    #env.compile_templates('jinja_precompiled/', zip=None)

    return env


def main():
    template_dir = os.path.join('core', 'templates', 'dev', 'head')
    env = get_jinja_env(template_dir)
    values = {}
    values['profile_picture_data_url'] = None
    values['DEV_MODE'] = False
    #print env.get_template('pages/error/error.html').render(values)
    print (env.get_template('pages/about/about.html').render(values)).encode('utf-8')

if __name__ == '__main__':
    env = get_jinja_env
    main()
