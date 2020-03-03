import unittest
import bareosdir
import time


class TestBareosFd(unittest.TestCase):

    def test_GetValue(self):
        bareosdir.GetValue(1)

    def test_SetValue(self):
        bareosdir.SetValue()

    def test_DebugMessage(self):
        bareosdir.DebugMessage(0, "This is a debug message\n")

    def test_JobMessage(self):
        bareosdir.JobMessage(0, "This is a Job Message")

    def test_RegisterEvents(self):
        bareosdir.RegisterEvents()

    def test_UnRegisterEvents(self):
        bareosdir.UnRegisterEvents()

    def test_GetInstanceCount(self):
        bareosdir.GetInstanceCount()


if __name__ == "__main__":
    unittest.main()
