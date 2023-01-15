import os

from jinja2 import Environment, loaders

print(os.path.dirname(os.path.realpath(__file__)))
environment = Environment(
        loader=loaders.FileSystemLoader(os.path.dirname(os.path.realpath(__file__))+"/templates"),
    )

environment.get_template('{% if True %}a{%endif%}.txt.jinja').render(var=True)
