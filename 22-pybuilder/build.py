# pip install -U --pre pybuilder

# https://pybuilder.github.io/documentation/tutorial.html
# https://github.com/pybuilder/pybuilder/blob/master/docs/customizing-the-build.rst
# https://gist.github.com/miebach/9752025

# pyb -t
# pyb -v
# pyb -E dev
# pyb install_dependencies

from pybuilder.core import init, task, depends, use_plugin, dependents
from pybuilder.plugins.core_plugin import prepare

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = "publish"


@task("foo", description="foo task")
@depends("bar")
@dependents(prepare)
def foo(logger, project):
    logger.warn("Executing: foo")
    logger.info("name: " + project.name)
    logger.info("basedir: " + project.basedir)


@task("bar", description="bar task")
def bar(logger):
    logger.warn("Executing: bar")


@init
def initialize1(logger, project):
    logger.warn("Executing: initialize 1")
    project.build_depends_on('mockito')


@init
def initialize2(logger):
    logger.warn("Executing: initialize 2")


@init(environments="dev")
def initialize3(logger):
    logger.warn("Executing: initialize 3 - dev only")
