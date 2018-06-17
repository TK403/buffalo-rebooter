# Buffalo-rebooter
Buffalo-rebooter is automation script about reboot for Buffalo router using selenium.

---

## Tested on the following models and firmware version
* WXR-1750DHP2  Version 2.52

---

## Quickstart
1. Edit your access URL, username and possword in src/settings.yaml.
2. Build container.
```bash
$ docker build tk403/buffalo-rebooter:latest .
```
3. Run container and REBOOT your router.
```bash
$ docker run -it --name buffalo-rebooter tk403/buffalo-rebooter
```

---

## License
MIT License
