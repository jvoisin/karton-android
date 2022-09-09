import androguard.core.bytecodes.apk  # type: ignore
from karton.core import Karton, Task  # type: ignore

from .__version__ import __version__


class Android(Karton):
    """
    Augment apk files with various metadata.
    """

    identity = "karton.android"
    version = __version__
    filters = [
        {"type": "sample", "extension": "apk"},
    ]

    def process(self, task: Task) -> None:
        sample = task.get_resource("sample")

        a = androguard.core.bytecodes.apk.APK(sample.content, raw=True)
        if not a.is_valid_APK():
            self.log.info("Not a valid APK file.")
            return

        metadata = {
            "package": [a.package],
            "activities": sorted(a.get_activities()),
            "main_activity": [a.get_main_activity()],
            "permissions": sorted(a.get_permissions()),
        }

        if a.is_signed() or a.is_signed_v3():
            certs = a.get_certificates()
            if len(certs):
                cert = certs[0]
                sha1_cert = cert.sha1_fingerprint.replace(" ", "")
                metadata["certificate"] = [sha1_cert]

        self.send_task(
            Task(
                headers={
                    "type": "sample",
                    "stage": "analyzed",
                },
                payload={"sample": sample, "attributes": metadata},
            )
        )
