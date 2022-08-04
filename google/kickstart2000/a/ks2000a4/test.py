from lib.task import load_google_task
task = load_google_task(__file__)


def test1(): task.run('test1')


def test2(): task.run('test2')



