from lib.task import load_cf_task
task = load_cf_task(__file__)


def test(): task.run('test')


def test2(): task.run('test2')



