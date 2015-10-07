# VSPK Generator

## Installation

    $  pip install vspkgenerator


## Usage

Environment Variables

The following environment variables can be used to avoid having to enter command arguments

    export MONOLITHE_GITHUB_API_URL=https://api.github.com
    export MONOLITHE_GITHUB_TOKEN=<github-app-token> # username and password won't be used
    export MONOLITHE_GITHUB_USERNAME=<github-username>
    export MONOLITHE_GITHUB_ORGANIZATION=Documentation
    export MONOLITHE_GITHUB_REPOSITORY=vsd-api-specifications
    export MONOLITHE_GITHUB_REPOSITORY_PATH=/

Then to generate a vsdk:

    $ generate-vspk -b 3.2

Then to generate a vsdk and the documentation:

    $ generate-vspk -b 3.2 --doc

Then to generate the vsd api documentation:

    $ generate-vsd-apidoc -b 3.2
