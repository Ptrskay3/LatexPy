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

    same, end1, end2 = diff("almaalma", "almaalma", silent=False)
    assert same == "almaalma"
    assert end1 == ""
    assert end2 == ""

    same, end1, end2 = diff("almaalm", "almaalma", silent=False)
    assert same == "almaalm"
    assert end1 == ""
    assert end2 == "a"

    same, end1, end2 = diff("almaalmaa", "almaalm", silent=False)
    assert same == "almaalm"
    assert end1 == "aa"
    assert end2 == ""
