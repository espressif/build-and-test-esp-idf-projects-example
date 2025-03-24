import pytest

@pytest.mark.parametrize(
    'target', [
        'esp32',
    ], indirect=True
)
@pytest.mark.arm64
def test_cmp2(dut):
    dut.expect('func2')
