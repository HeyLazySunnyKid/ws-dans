ws-dans
=========

The main idea is that user's workstation in conrast of servers has just one
role: to be a user's workstation! ws-dans which means workstation-dance with
anSible tries to help manage user's workstations by using ansible configure
system. You should just fill several dictionaries in your playbook vars which
describe all changes and configurations from default system installation and get
ability to deploy workstation wherever you want and dance at appearing free time
in result.

Supprted Systems
----------------

Fedora 30

Role Variables
--------------

```
dans_repos: dict with all repositories
  file: list of paths to files with custom .repo files
  copr: list of copr repositories
  dnf: list of repositories installed by packages

dans_tools: list of all tools
  - name: name of package in `type` package manager
    type(default: dnf): dnf, pip2, pip3, npm, none
    desc: text fild for decription
    include_tasks: path to tool specific tasks
    conf: list of configuration files. if extention of file is `.j2` template
            module used.
```

Example Playbook
----------------

Simple example of this role usage.
More examples in molecule tests: molecule/default/playbook.yml

```yaml
- hosts: servers
  vars:
    dans_repos:
      file: []
      copr: []
      dnf:
        - "https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-{{ ansible_distribution_version }}.noarch.rpm"  # noqa 204

    dans_tools:
      - name: zsh
        desc: 'Interactive shell'
        deps: [fontconfig, util-linux-user, ruby, gawk, git, xclip, fzf]
        include_tasks: tools_tasks/zsh.yml
        conf:
        - src: config/zsh
          dest: ~/.zshrc
        - src: config/zshalias
          dest: ~/.zshalias
  roles:
    - ws-dans
```

License
-------

MIT

Author Information
------------------

HeyLazySunnyKid
