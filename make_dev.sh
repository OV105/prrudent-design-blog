#!/bin/bash -x

rm -rf output/* ; pelican ; make devserver
