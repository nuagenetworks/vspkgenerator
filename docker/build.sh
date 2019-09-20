#!/bin/bash
set -e
set -x

VSPK_VERSION=$1
SPEC_BRANCH=$2
LANGUAGE_PLUGIN=$3

[[ -z "$MONOLITHE_REPO" ]] && MONOLITHE_REPO="https://github.com/nuagenetworks/monolithe.git"
[[ -z "$MONOLITHE_BRANCH" ]] && MONOLITHE_BRANCH="master"
[[ -z "$SPEC_REPO" ]] && SPEC_REPO="https://github.com/nuagenetworks/vsd-api-specifications.git"

export GIT_REPOS_ROOT=/build/git
export VSPK_GENERATOR_HOME=$GIT_REPOS_ROOT/vspkgenerator
export SPECIFICATION_DIR=$GIT_REPOS_ROOT/api-specifications
export GENERATION_VERSION=$VSPK_VERSION
export PYTHONPATH=$GIT_REPOS_ROOT/monolithe

mkdir -p "$GIT_REPOS_ROOT"

# Pull monolithe
cd "$GIT_REPOS_ROOT"
git clone $MONOLITHE_REPO
cd monolithe && git checkout $MONOLITHE_BRANCH
 
# Pull the specs
cd "$GIT_REPOS_ROOT"
git clone $SPEC_REPO "$SPECIFICATION_DIR"
cd "$SPECIFICATION_DIR" && git checkout $SPEC_BRANCH

cd $VSPK_GENERATOR_HOME
python -m monolithe.cli --config vspkgenerator/conf/config.ini --vanilla-prefix vspkgenerator --folder $SPECIFICATION_DIR --generation-version=$GENERATION_VERSION --language $LANGUAGE_PLUGIN

