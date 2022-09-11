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
            "activities": sorted(a.get_activities()),
            "main_activity": [a.get_main_activity()],
            "package": [a.package.strip()],
            "permissions": sorted(a.get_permissions()),
        }

        app_name = a.get_app_name().strip()
        if app_name:
            metadata["app_name"] = [app_name]

        if a.is_signed() or a.is_signed_v3():
            certs = a.get_certificates()
            if len(certs):
                cert = certs[0]
                sha1_cert = cert.sha1_fingerprint.replace(" ", "")
                cert_validity = cert["tbs_certificate"]["validity"]
                not_before_raw = cert_validity["not_before"]
                not_before = not_before_raw.native.strftime("%b %-d %X %Y %Z")
                not_after_raw = cert_validity["not_after"]
                not_after = not_after_raw.native.strftime("%b %-d %X %Y %Z")
                metadata.update(
                    {
                        "certificate": [sha1_cert],
                        "certificate_issuer": [cert.issuer.human_friendly],
                        "certificate_not_after": [not_after],
                        "certificate_not_before": [not_before],
                        "certificate_serial": [cert.serial_number],
                        "certificate_subject": [cert.subject.human_friendly],
                    }
                )

        self.send_task(
            Task(
                headers={
                    "type": "sample",
                    "stage": "analyzed",
                },
                payload={"sample": sample, "attributes": metadata},
            )
        )
