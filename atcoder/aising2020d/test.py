from lib.task import load_ac_task
task = load_ac_task(__file__)


def test1(): task.run('test1')


def test2(): task.run('test2')


def test3(): task.run('test3')

