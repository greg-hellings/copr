#!xonsh
# vim: set ft=python

import sys
pkgs = sys.argv[1:]

for pkg in pkgs:
    go2rpm @(pkg)
    spec = `.*\.spec`[0]
    pkgname = spec.split('.')[0]
    mkdir -p @(pkgname)
    mv @(spec) @(pkgname)
    cd @(pkgname)
    spectool -g ./@(spec)
    fedpkg --release f36 mockbuild
    cd ..
