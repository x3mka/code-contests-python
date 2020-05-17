from lib.compare_strategies import SetLinesCompareStrategy, ByLineCompareStrategy
from lib.task import load_cf_task
task = load_cf_task(__file__)


def test(): task.run('test', strategy=ByLineCompareStrategy(default_line_compare_strategy=SetLinesCompareStrategy()))


