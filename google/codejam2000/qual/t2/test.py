from lib.task import load_google_task
task = load_google_task(__file__)


def test(): task.run('test')


