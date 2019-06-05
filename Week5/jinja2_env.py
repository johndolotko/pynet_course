# Python 2/3 glue code
from __future__ import unicode_literals, print_function

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Create a jinja2 environment
#env = Environment()
env = Environment(undefined=StrictUndefined)

# Load the jinja2 templates from the current working directory
#env.loader = FileSystemLoader('.')
env.loader = FileSystemLoader(['.', './templates/'])

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "10.20.30.1"
}

template_file = 'bgp_config.j2'

# We don’t use open filename we used get_template to read in the template file
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

