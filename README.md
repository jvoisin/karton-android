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
