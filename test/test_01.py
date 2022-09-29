import pytest

def test_01():
  assert True

@pytest.mark.xfail(strict=True)
def test_02():
  assert False
