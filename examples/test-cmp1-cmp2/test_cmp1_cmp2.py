import pytest

@pytest.mark.parametrize(
    'target', [
        'esp32',
    ], indirect=True
)
@pytest.mark.multiboard
def test_cmp1_cmp2(dut):
    dut.expect('func1')
    dut.expect('func2')
