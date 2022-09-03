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
    "payload": {
        "sample": <Resource>,
        "certificate": <string>,
        "package": <string>
    }
}
```

## Usage

First of all, make sure you have setup the core system: https://github.com/CERT-Polska/karton

Then install karton-android from PyPi, as well as androguard

```shell
$ pip install karton-android androguard

$ karton-android
```
