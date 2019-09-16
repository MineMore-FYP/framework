import pytest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from gdelt.dataFileSelection import getMonthlyFiles

def test_dataFileSelection_getMonthlyFiles():
	assert getMonthlyFiles("JANUARY") == "01", "JANUARY test failed"
	assert getMonthlyFiles("JULY") == "07", "JULY test failed"
	assert getMonthlyFiles("NOVEMBER") == "11", "NOVEMBER test failed"

