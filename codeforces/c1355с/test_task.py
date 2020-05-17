from lib.utils import run_problem
import importlib
import os

dir_name = os.path.dirname(os.path.realpath(__file__)).split(os.sep)[-1]
task = importlib.import_module("codeforces.{}.task".format(dir_name))


def test1():
    run_problem(task.main, 'test1')


# def test2():
#     run_problem(task.main, 'test2')


# def test3():
#     run_problem(task.main, 'test3')


# def test4():
#     run_problem(task.main, 'test4')

