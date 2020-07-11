from latexpy.util.string import diff


def test_diff():
    same, end1, end2 = diff("alma_körte vége", "alma körte\nvége", silent=True)
    assert same == "alma"
    assert end1 == "_körte vége"
    assert end2 == " körte"
    same, end1, end2 = diff("\nalma_körte vége", "alma körte\nvége", silent=True)
    assert same == ""
    assert end1 == ""
    assert end2 == "alma körte"
