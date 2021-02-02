Get a list of `show commands` for a list of `ip addresses`, based on a `testbed` template.

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

# Editing the variable files

You can edit three files. They are in the `./templates` folder.

## Show commands

`show commands` are listed in `./templates/list_show.yaml`

You can add more show commands by adding a new line, starting with a `-` followed by a show command.

## IP addresses of the devices

`ip addresses` are listed in `./templates/list_ip.yaml`

You can add more ip addresses by adding a new line, starting with a `-` followed by an IP address.

## Testbed

`testbed` template is described in `./templates/testbed.tpl`

You can modify connections parameters such as the login or the passwords.