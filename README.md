# VSPK Generator

## Installation


You can install vspk from our `devpypi`:

    $  pip install vspkgenerator

This generator relies on `monolithe` which should be previously installed in your virtualenv.


## Usage

Specify which branches you'd like to generate the VSPK for. For instance:

    $ generate-vspk -b 3.2 master

will generate a `vspk` library for both master and 3.2 branches
