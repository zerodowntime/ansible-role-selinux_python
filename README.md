# selinux_python

Ansible role to install selinux python dependencies

## Installation

```yaml
   ansible-galaxy install zerodowntime.selinux_python
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
```

## Default role variables

| Variable name                  | Required? |  Type  | Description               |
|:------------------------------ |:---------:|:------:|:------------------------- |
| selinux_python__package_status |    no     | string | installed packages status |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Example Playbook

```yaml
  - hosts: all
    become: true
    roles:
    - role: zerodowntime.selinux_python
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
