import yaml
import jinja2
from genie.testbed import load

with open("./templates/list_ip.yaml", "r") as file:
    list_ip = yaml.load(file, Loader=yaml.FullLoader)

with open("./templates/list_show.yaml", "r") as file:
    list_show = yaml.load(file, Loader=yaml.FullLoader)

# Where's the folder with my templates (or my folders, if multiple)
template_loader = jinja2.FileSystemLoader(searchpath="./templates")

# Instance of the Environment class. Gives the loader (above), optionally parameters like
# block strings, variable strings etc.
template_env = jinja2.Environment(loader=template_loader)

# Which file is my template
template = template_env.get_template("testbed.tpl")

# We give the template two lists:
# - list_ip: the IP of our devices
# - range(len(list_ip)), the id (from 0 to the max device) that will be used in device.name to make it unique
testbed = load(template.render(list_ip_id = zip(list_ip, range(len(list_ip)))))

# Writting each file
for device in testbed:
    
    device.connect(learn_hostname=True,
                   init_exec_commands=[],
                   init_config_commands=[],
                   log_stdout=False)

    print(f'-- {device.hostname} --')

    with open(f'./outputs/{device.hostname}.txt', 'w') as file:

        # Collect and write each output
        for show in list_show:
            file.write(f'--- {show} ---\n')
            file.write(device.execute(show))
            file.write('\n\n')

    print('  done')

    device.disconnect()

