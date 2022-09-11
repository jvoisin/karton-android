# Android karton service

Extract various information from APK.

**Author**: Julien (jvoisin) Voisin


**Consumes:**
```
{
    "type":  "sample",
    "extension": "apk"
} 
```

**Produces:**
```
{
    "type": "sample",
    "kind": "analyzed",
    "sample": <Resource>,
    "payload": {
	"attributes": {
          "certificate": <string>,
          "main_activity": <string>,
          "package": <string>
          "activities": <list<string>>
          "permissions": <list<string>>
	  "certificate_not_after": <string>
	  "certificate_serial": <int>
	  "certificate_subject": <string>
	  "certificate_not_before": <string>
	  "certificate_issuer": <string>
	  "app_name": <string>
	}
    }
}
```

## Usage

First of all, make sure you have setup the core system: https://github.com/CERT-Polska/karton

Then install karton-android and run it:

```shell
$ pip install git+https://github.com/jvoisin/karton-android

$ karton-android
```
