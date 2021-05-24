#!/bin/sh

if [ -d build ]; then
  rm -dr build
fi
if [ -d dist ]; then
  rm -dr dist
fi
if [ -d src/hervenue.egg-info ]; then
  rm -dr src/hervenue.egg-info
fi
