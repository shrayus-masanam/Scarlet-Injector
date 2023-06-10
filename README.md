# Scarlet Injector
Normally, [Scarlet](https://usescarlet.com) only lets you inject one tweak into an app through the installation process. This program creates a simple Scarlet JSON repo that will let you inject as many tweaks as you want into an IPA with Scarlet. 

The repo houses the user-supplied IPA's download URL along with the URLs of all dylib/deb files that the user specifies. The JSON data is uploaded to [Ghostbin](https://paste.bingner.com) and will persist for 14 days. Once the app is installed onto the device, the repo can be safely removed and the app will stay installed & refresh/resign when needed.

To use, simply run `python3 main.py`, and input direct URLs to the target IPA and dylib/deb files when asked. Then, once the program gives you a Ghostbin URL, paste that URL into Scarlet as if it were a repo. You will then see a single app that you can install, and while installing it Scarlet will inject the tweaks into the app.
