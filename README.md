# VSPK Generator

## Installation

    $  pip install vspkgenerator


## Usage

`vspkgenerator` operates on a directory that contains specifications.

Then to generate a python vspk from a directory containing specifications:

    $ generate-vspk -f path/to/dir -L python

It also handles git repositories. To build a vspk from multiple branches of repository:

Then to generate the vsd api documentation:

    $ generate-vspk -b master 4.0 -f path/to/repo -L python
