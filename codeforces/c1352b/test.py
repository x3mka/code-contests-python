from lib.compare_strategies import ByLineCompareStrategy, EqualSumLinesCompareStrategy
from lib.task import load_cf_task
task = load_cf_task(__file__)


class CustomByLineCompareStrategy(ByLineCompareStrategy):

    def pick_line_compare_strategy(self, index, expected_lines, actual_lines):
        if index > 0 and expected_lines[index-1] == 'YES':
            return EqualSumLinesCompareStrategy()
        return self.default_line_compare_strategy


def test(): task.run('test', strategy=CustomByLineCompareStrategy())

