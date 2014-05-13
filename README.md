# Kickstart v.0.4.0

Kickstart is away to kickstart your web project by setting up your files for you.

This script will ask you some questions and create the folders and files you need according to your answers. This is to save time setting up simple website directories. 

What can Kickstart set up for you:

HTML template already set up for working with directories
JS folder with a script.js file and/or a data.json file
CSS folder witha style.css file already for use in your HTML doc

## How to get started

Get kickstart.py 

```
$ cd ~
$ mdkir bin
$ cd bin
$ git clone https://github.com/mattludwigs/kickstart.git
```

Next set up .bash_profile or .profile

```
$ nano ~/.bash_profile
```

In nano type:

```
export PATH="/Users/you-user-name/bin:$PATH"
```

Press ctrl-x and y to exit and save the file, then type:

```
source .bash_profile
```

## How to use

Navigate to the dicrectory where you want to start your new web project

```
$ cd Documents
```

Then type:

```
$ kickstart.py
```

Then run kickstart and ask you a few questions, follow the prompt and then you should have the new project started in your directory. Just have navigate to the project and you can get started.

## License
Kickstart is released under the MIT License.




