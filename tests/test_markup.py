import io
from operator import itemgetter

from clldutils.markup import Table


def test_Table():
    t = Table()
    assert t.render() == ''

    t = Table('a', 'b', rows=[[1, 2], [3, 4]])
    assert t.render() == \
        '| a | b |\n|----:|----:|\n| 1 | 2 |\n| 3 | 4 |'
    assert t.render(condensed=False) == \
        '|   a |   b |\n|----:|----:|\n|   1 |   2 |\n|   3 |   4 |'
    assert t.render(verbose=True) == \
        '| a | b |\n|----:|----:|\n| 1 | 2 |\n| 3 | 4 |\n\n(2 rows)\n\n'
    assert t.render(sortkey=itemgetter(1), reverse=True) == \
        '| a | b |\n|----:|----:|\n| 3 | 4 |\n| 1 | 2 |'


def test_Table_context(capsys):
    with Table('a', 'b', tablefmt='simple') as t:
        t.append([1, 2.345])
    out, _ = capsys.readouterr()
    assert out == '  a     b\n---  ----\n  1  2.35\n'

    f = io.StringIO()
    with Table('a', 'b', tablefmt='simple', file=f) as t:
        t.append([1, 2.345])
    assert f.getvalue() == '  a     b\n---  ----\n  1  2.35\n'
