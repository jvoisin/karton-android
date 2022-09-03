import sys

import androguard
from karton.core import Karton, Task

from .__version__ import __version__

class Android(Karton):
    """
    Augment apk files with various information.
    """

    identity = "karton.android"
    version = __version__
    filters = [
        {"type": "sample", "extension": "apk"},
    ]

    def process(self, task: Task) -> None:
        sample = task.get_resource("sample")

        a = androguard.core.bytecodes.apk.APK(sample)
        if not a.is_valid_APK():
            self.log.info("Not a valid APK file.")
            return

        metadata = {
           'package': a.package,
           'sample': sample,
           'activities': a.get_activites(),
           'main_activity': a.get_main_activity(),
           'permissions': a.get_permissions(),
        }

        if a.is_signed() or a.is_signed_v3():
            metadata['certificate'] = a.get_certificates()[0].sha1_fingerprint.replace(" ", "")

        self.send_task(
            Task(
                headers={"type": "sample", "stage": "analyzed"},
                payload=metadata)
            )

if __name__ == "__main__":
    Android().loop()
