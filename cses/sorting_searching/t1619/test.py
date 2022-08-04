from lib.task import load_cses_task
task = load_cses_task(__file__)


def test(): task.run('test')


