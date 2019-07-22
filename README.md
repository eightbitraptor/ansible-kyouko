MVH Workstation Management
=========

This repository contains provisioning and config management playbooks required
to decorate and furnish a bare Fedora install into the kind of place I'm
comfortable living. It's opinionated, and always right.

Requirements
------------

The assumptions made are these:

  * You have installed Fedora Workstation
  * You have a non-root user, who's account you are logged in as
  * That user has a default ssh key configured, that is authorised to pull from Github
  * You have already installed git

Variables
---------

* `fedora_version`: The version of Fedora that is installed on the machine. Defaults to 30.


Running these Playbooks
--------------

* Clone the repo from Github somewhere sensible (I usually use `~/ansible`) and `cd` there.
* run `bash install.sh` which will install ansible and the required Galaxy roles.
* run `ansible-playbook -K main.yml`

Dependencies
------------

* [Jared Hocutt's Gnome Extensions](https://galaxy.ansible.com/jaredhocutt/gnome_extensions)

Author Information
------------------

Matt Valentine-House
matt@eightbitraptor.com
https://www.eightbitraptor.com

TODO
----

* Ubuntu support
* Alternative Window manager (i3?)
* better structure for developer role
* think about separate libvirt/kvm role
* override DNF so that it nags when used directly
