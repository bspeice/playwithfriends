from os import path
from bottle import SimpleTemplate


def render_template(template_name, params=None):
    if params is None:
        params = {}

    package_dir = path.abspath(path.dirname(__file__))
    static_dir = path.join(package_dir, 'static')

    with open(path.join(static_dir, template_name), 'r') as handle:
        template = SimpleTemplate(handle.read())

    return template.render(**params)
