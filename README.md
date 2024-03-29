Kyouko: Ansible Config
=========

This repository contains provisioning and config management playbooks required
to decorate and furnish a bare Ubuntu install into the kind of place I'm
comfortable living. It's opinionated, and always right.

![kyouko](https://i.pinimg.com/originals/d6/71/43/d671437969650dd64e71e81a801174d4.jpg)

It contains configuration for 2 machines:

 * Kyouko is the hostname of my (old) personal computer, a Lenovo Thinkpad X251
   and one of the titular protagonists from [the manga
Horimiya](https://en.wikipedia.org/wiki/Hori-san_to_Miyamura-kun)).
 * Deunan is the hostname of my Ruby build server, a Ryzen based Mini ITX
   Desktop and the main protagonist of the Manga Appleseed.

Requirements
------------

The assumptions made are these:

  * You have installed a minimal install of the latest Ubuntu (most recently
    tested with 21.04)
  * You have a non-root user who's account you are logged in as
  * That user has a default ssh key configured, that is authorised to pull from
    Github
  * You have already installed git


Running these Playbooks
--------------

* Clone the repo from Github into somewhere sensible (I usually use `~/ansible`) and `cd` there.
* run `bash install.sh` to install Ansible and any dependancies.
* run Ansible for a host, eg. `ansible-playbook -K kyouko.yml`

Author Information
------------------

- Matt Valentine-House
- matt@eightbitraptor.com
- https://www.eightbitraptor.com

References
----------

There are some pre-built packages of software that I use contained within this
repo. Source can be found at the following links:

1. **light: [haikarainen/light](https://github.com/haikarainen/light)** A super
   useful little utility for controlling the display backlight of a Thinkpad,
   used when you don't want or need to run a full power-manager
2. **pywal: [dylanaraps/pywal](https://github.com/dylanaraps/pywal)** As a
   colourblind person, this utility is a lifeline :) It takes an image as input
   and manages your X application colour scheme automatically, works with `i3`,
   `urxvt` and loads more. I love it. The package in this repo is actually from
   the PPA
   [kgilmer/speed-ricer](https://launchpad.net/~kgilmer/+archive/ubuntu/speed-ricer),
   build scripts for which [you can find
   here](https://github.com/regolith-linux/speed-ricer)

