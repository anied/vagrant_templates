# Vagrant Project Templates

## What and Why
This repo exists to house various Vagrant project templates that can be copied and pasted as the basis for your own projects.  Starting a single page app from scratch and just need a basic environment provisioned?  Looking for a fuller stack with an MV*, dependency loader and some basic Grunt tasks?  This exists to house those kind of barebones skeletons to grab and build your projects on top of.  There is only a single entry at the moment, but I will add more as they are useful for my own purposes.  Collaboration is encouraged!  If you have a basic setup you would like to share here, feel free to make a pull request.

## How
To use Vagrant, you need to have it installed on your system-- you can grab it from [VagrantUp.com](https://www.vagrantup.com/).  Also, you will need a system to run the VM's-- while Vagrant runs with many providers, [VirtualBox](https://www.virtualbox.org/) is free and easy to use.

Once you have those installed, copy the template you want to use.  Now would be a good time to rename it to your project.  Navigate to the directory in the terminal or command prompt and run the command `vagrant up`.  Then sit back and watch the magic happen.

[**NOTE**: All these templates, unless otherwise noted, use the **ubuntu/trusty64** box.  If you do not already have this on your system, the first time you attempt to run one of these boxes there will be a considerable amount of time spent downloading the VM.  However, once it is on your system any subsequent setup will go _much_ faster, as the same initial ubuntu/trusty64 box will be reused for subsequent Vagrant projects configured to use it.]

Once the vagrant installation and provisioning process completes, you can check to see your index served up in your hosted environment.  **ALL TEMPLATES IN THIS REPO SERVE FILES ON PORT 4567 UNLESS OTHERWISE NOTED.**

### Vagrant Commands Basics Cheatsheet
While it would not hurt to read up a little bit at the [Vagrant Documentation Page](https://docs.vagrantup.com/v2/), here are a few basic terminal commands to get you started:
+ `vagrant up` -- Used to start up your vagrant box.  If it is the first time you are starting this particular box, it will also provision it.
+ `vagrant ssh` -- SSH into your Vagrant box and run commands on its internal terminal interface.
+ `vagrant halt` -- Shut down your vagrant box-- it can be turned back on with `vagrant up` -- the box will not reprovision when being brought back up from a halted state.
+ `vagrant provision` -- Used to re-run any provisioning scripts on the box.
+ `vagrant destroy` -- Shut down Vagrant box and remove it completely (the original box will remain on your system, and will not need to be re-downloaded should you decide you want to run `vagrant up` on the project again-- however, re-provisioning will occur.)

You can learn more at the [Vagrant Command Line](https://docs.vagrantup.com/v2/cli/index.html) documentation page.

### A Note About System Resources
Vagrant is a great tool, but comes with a price in system resources.  Every Vagrant box that is currently "up" is a virtualized OS hosted on your machine, eating up RAM and CPU.  Additionally, every installed and provisioned box, up or halted/suspended, takes up a decent chunk of disk space.  For this reason, make sure to `vagrant halt` boxes that you are not actively using, and `vagrant destroy` boxes for projects you do not expect to be working on for a while.

## Current Templates

### Single Page App Basic
Barebones project template that sets up a Vagrant box and apache configuration to redirect all unmatched requests back to `index.html` -- this becomes the entry point of your single page app, where you could use a MV* library like [Backbone.JS](http://backbonejs.org/) to route those requests.

The provisioning script:
+ Installs Apache
+ Configures Apache to allow configuration overrides
+ Points Apache towards the `/src` directory in the project.

Additionally, an `.htaccess` file is included in the project `/src` directory that redirects requests back to index.html-- make sure to include this file when moving the project to a webserver.

Finally, this template achieves some of its configuration changes by overwriting the `apache2.conf` file on the Vagrant box with the contents of the `apache_edited.txt` file in the project directory.  This means that if you would like to make further tweaks to the apache2.conf configuration you can make it in `apache_edited.txt` and then provision the machine to push in the change!

### More To Come!
I intend to add more templates as time goes on-- if you have one you would like to add to the project, fork the repo, spin it up and send me a pull request!  Thanks!

## Quick Resources
[Vagrant Documentation](https://www.vagrantup.com/)
[Vagrant - Getting Started](https://docs.vagrantup.com/v2/getting-started/index.html)
[Vagrant - Command Line Interface](https://docs.vagrantup.com/v2/cli/index.html)

## License
You are welcome to use any of the templates in this repo for your own projects.  Attribution is appreciated but not necessary.