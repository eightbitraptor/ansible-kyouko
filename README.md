MVH Workstation Management
=========

This repository contains provisioning and config management playbooks required
to decorate and furnish a bare Fedora install into the kind of place I'm
comfortable living. It's opinionated, and always right.

Requirements
------------

The assumptions made are these:

  * You have installed the latest Ubuntu Mate LTS (18.04 at time of writing)
  * You have a non-root user, who's account you are logged in as
  * That user has a default ssh key configured, that is authorised to pull from Github
  * You have already installed git


Running these Playbooks
--------------

* Clone the repo from Github somewhere sensible (I usually use `~/ansible`) and `cd` there.
* run `bash install.sh` which will install ansible and the required Galaxy roles.
* run `ansible-playbook -K main.yml`

Author Information
------------------

Matt Valentine-House
matt@eightbitraptor.com
https://www.eightbitraptor.com

TODO
----

* [X] Ubuntu support
* [ ] Add some checks so long tasks only run when they need to
* [ ] why is Emacs customisation file always "changed"
* [ ] Emacs 26 in Ubuntu 18.04
* [ ] fzf in Ubuntu 18.04
* [X] bitmap fonts aren't currently working
* [ ] better openbox theme
* [X] display backlight keys in Openbox
* [ ] Automatic i3lock on suspend
* [X] trackpad two finger scrolling with libinput
* [ ] mpd/mpv
* [X] Alternative Window manager (openbox)
* [ ] better structure for developer role
* [ ] think about separate libvirt/kvm role
* [ ] override APT so that it nags when used directly
