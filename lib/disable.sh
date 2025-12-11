#!/bin/bash

cd $(dirname $0)/..

name=$(basename $1 .h)
name=$(basename $name .c)

inc_h=inc/${name}.h
src_c=src/${name}.c

[ -f $inc_h ] && mv -v $inc_h lib
[ -f $src_c ] && mv -v $src_c lib
