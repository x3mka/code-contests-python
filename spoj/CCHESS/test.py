from lib.task import load_spoj_task
task = load_spoj_task(__file__)


def test(): task.run('test')


