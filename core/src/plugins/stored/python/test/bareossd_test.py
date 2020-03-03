import unittest
import bareossd
import time


class TestBareosFd(unittest.TestCase):

    def test_GetValue(self):
        bareossd.GetValue(1)

    def test_SetValue(self):
        bareossd.SetValue(2)

    def test_DebugMessage(self):
        bareossd.DebugMessage(1, "This is a debug message")

    def test_JobMessage(self):
        bareossd.JobMessage(1, "This is a Job message")

    def test_RegisterEvents(self):
        bareossd.RegisterEvents()

    def test_UnRegisterEvents(self):
        bareossd.UnRegisterEvents()

    def test_GetInstanceCount(self):
        bareossd.GetInstanceCount()


if __name__ == "__main__":
    unittest.main()
