from lib.task import load_cf_task
task = load_cf_task(__file__)


def test1(): task.run('test1')


def test2(): task.run('test2')



