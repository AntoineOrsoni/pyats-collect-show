Get a list of `show commands` for a list of `ip addresses`, based on a `testbed` template.

`show commands` are listed in `./templates/list_show.yaml`
`ip addresses` are listed in `./templates/list_ip.yaml`
`testbed` template is described in `./templates/testbed.tpl`

# Installing the requirements
pyATS supports Python versions from 3.5 to 3.8 (i.e. 3.9 is not yet supported). You can check the latest information here:

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/install/installpyATS.html

```bash
pip install -r requirements.txt
```

# Running the script

To run the script, run the below command.

```bash
python get_show.py
```