#!/bin/sh

cd $HOME/Interval-Scheduling-Algorithm-with-Applied-Constraints/src/webserver

# If you want to use a different python interpreter, set your
# $PATH to something else.
for i in {1..8};
do
  python crawl.py
  sleep 60
done


