# To build the docker image:
    P=proxy.com:8000
    docker build \
        --build-arg HTTP_PROXY=$P \
        --build-arg http_proxy=http://$P \
        --build-arg HTTPS_PROXY=$P \    
        -t vspkgenerator . 


# To run:
    P=proxy.com:8000
    docker run -ti --rm \
        -e HTTPS_PROXY=$P \
        -e HTTP_PROXY=$P \
        -e MONOLITHE_REPO=https://github.com/nuagenetworks/monolithe.git \
        -e MONOLITHE_BRANCH=master \
        -e SPEC_REPO=https://github.com/nuagenetworks/vsd-api-specifications.git \
        -v `git rev-parse --show-toplevel`:/build/git/vspkgenerator \
        vspkgenerator <version> <spec branch> <lang>

    Any of the env varialbles in the docker command is optional.

    The version parameter can be anything. The resulting VSPK will be
    versioned with that string. The spec branch would usually be "master"

    "lang" can be any of the languages supported by vspkgenerator. i.e: "java" or "csharp" or "python" ...

* Note that all the proxy stuff is optional and can be left out if working
  with direct internet access


# Example:
    docker build -t vspkgenerator .
    docker run -ti --rm -v `git rev-parse --show-toplevel`:/build/git/vspkgenerator vspkgenerator 6.0.1 master java
