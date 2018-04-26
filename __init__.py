from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('cmpl', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)