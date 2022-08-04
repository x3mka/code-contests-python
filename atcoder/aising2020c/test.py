from lib.task import load_ac_task
task = load_ac_task(__file__)


def test(): task.run('test')


