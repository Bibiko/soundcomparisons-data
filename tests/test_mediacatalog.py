from pathlib import Path

import pytest

from pysoundcomparisons.mediacatalog import *


@pytest.fixture
def catalog():
    return MediaCatalog(Path(__file__).parent / 'fixtures' / 'catalog.json')


def test_SoundfileName():
    with pytest.raises(ValueError):
        SoundfileName('abc')
    sfn = SoundfileName('abc_123_def')
    assert not sfn.extension
    assert sfn.variety == 'abc'


def test_MediaCatalog(catalog):
    assert "EAEA0-0000-3A1B-047F-0" in catalog
    assert len(catalog["Oce_Van_Mal_Nth_WNth_MaluaBay_Marasup_Dl_626_leaf_lif"].bitstreams) == 3
    assert len(
        catalog.matching_bitstreams("Oce_Van_Mal_Nth_WNth_MaluaBay_Marasup_Dl_626_leaf_lif")) == 3
