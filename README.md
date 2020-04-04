ws-dans
=========

The main idea is that user's workstation in conrast of servers has just one
role: be a user workstation! ws-dans ,which means workstation-dansing, try to
help manage user workstation's using configure system anSible. User just should
fill several dicts in their playbook's which would describe every changes and
configurations files from default system installation.  And in result get
ability to deploy workstation wherever he want and danSing in new free time.

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
    type(default: dnf): dnf, pip2, pip3, npm, role, none 
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

public

Author Information
------------------

HeyLazySunnyKid
