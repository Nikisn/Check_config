from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('Jinja2_templates'), trim_blocks=True, 
                  lstrip_blocks=True)
template = env.get_template('template_route.txt')

with open('vars.yaml') as f:
    routers = yaml.safe_load(f)



for router in routers:
    r_conf = router['name']+'.txt'
    print(f'Генирруется конфигурационный файл {r_conf}')
    with open(r_conf,'w') as f:
        f.write(template.render(router))
    print(f'Файл сгенерирован')