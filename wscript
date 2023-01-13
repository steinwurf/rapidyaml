#! /usr/bin/env python
# encoding: utf-8

APPNAME = "rapidyaml"
VERSION = "1.0.0"


def build(bld):
    directory = bld.dependency_node("rapidyaml-source")
    includes = directory.find_node("src")

    bld(name="rapidyaml", export_includes=[includes])
