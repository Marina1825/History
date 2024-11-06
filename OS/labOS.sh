#!/bin/bash

mkdir OS
mkdir -p OS/{tab,qut,blender,bash}
touch OS/file{00..15}
chmod -R 504 OS
ls -l OS/
