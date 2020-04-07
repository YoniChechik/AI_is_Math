#!/bin/bash

echo "here"

cd /home/yoni/dev/AI_is_Math/raw_docs
bundler exec jekyll build -d ../docs
