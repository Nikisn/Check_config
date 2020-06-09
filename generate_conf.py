from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.txt')

with open('vars.yaml') as f:
    routers = yaml.safe_load(f)

for router in routers:
    r1_conf = router['name']+'.txt'
    with open(r1_conf,'w') as f:
        f.write(template.render(router))
