testbed:
  name: XRDocs
  credentials:
    default:
      username: admin
      password: C1sco12345
      
devices:
{% for ip, id in list_ip_id %}
  Node_{{id}}:
    type: iosxr-devnet
    os: iosxr
    connections:
      vty:
        protocol: ssh
        ip: {{ip}}
        settings:
          GRACEFUL_DISCONNECT_WAIT_SEC: 0
          POST_DISCONNECT_WAIT_SEC: 0
        arguments:
          connection_timeout: 10
{% endfor %}
