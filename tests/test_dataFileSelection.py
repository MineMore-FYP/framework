import pytest

from gdelt.dataFileSelection import getMonthlyFiles


def test_dataFileSelection_getMonthlyFiles():
	getMonthlyFiles("JULY")
	assert selectMonth == "07","test passed"