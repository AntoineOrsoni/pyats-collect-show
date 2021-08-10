testbed:
  name: XRDocs
  credentials:
    default:
      username: cisco
      password: cisco
    enable:
      password: cisco
      
devices:
{% for ip, id in list_ip_id %}
  Node_{{id}}:
    type: iosxr
    os: iosxr
    connections:
      vty:
        protocol: telnet
        ip: {{ip}}
        settings:
          GRACEFUL_DISCONNECT_WAIT_SEC: 0
          POST_DISCONNECT_WAIT_SEC: 0
        arguments:
          connection_timeout: 10
{% endfor %}

