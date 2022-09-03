import os

from karton.android import Android

from karton.core import Task
from karton.core.test import KartonTestCase, TestResource


class AndroidMagicTestCase(KartonTestCase):
    karton_class = Android

    def test_android(self):
        testcase = os.path.join(os.path.dirname(__file__), "testsdata", "example.apk")
        with self.subTest(testcase):
            with open(testcase, "rb") as f:
                content = f.read()
            sample = TestResource(testcase, content)
            expected = Task(
                {
                    "type": "sample",
                    "stage": "analyzed",
                    "origin": "karton.android",
                },
                payload={
                    'attributes': {
                      "certificate": ["61ED377E85D386A8DFEE6B864BD85B0BFAA5AF81"],
                      "main_activity": ["com.example.android.contactmanager..ContactManager"],
                      "package": ["com.example.android.contactmanager"],
                      "activities": ["com.example.android.contactmanager..ContactManager", "com.example.android.contactmanager.ContactAdder"],
                      "permissions": ["android.permission.GET_ACCOUNTS", "android.permission.READ_CONTACTS", "android.permission.WRITE_CONTACTS"],
                    }
                },
            )
            task = Task(
                {
                    "type": "sample",
                    "extension": "apk",
                },
                payload={"sample": sample},
            )
            results = self.run_task(task)

            self.assertTasksEqual(results, [expected])
