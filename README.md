# Update interfaces NAT Zones

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Setup authentication as listed below
* run the script using: ``pyhton3  cgxSetNATZone.py --zone <nat zone> --interface <interface> [--interface <more interfaces>] --element <element name> [--element <more elements>]``
* You can also supply a list of elements (ION) names in a text file (one ION/Element name per line, use # for comment) and reference it with ``--elements``
* `--interface` and `--element` can repeat itself for many times to add more elements or interfaces
* `--list_elements` will list all the elements. use it to create elements text file

cgxSetNATZone.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)


Example of a run:
```
(cgx) ~/proj/cgxSetNATZone$ python3 cgxSetNATZone.py --zone internet --interface "1" --interface "2" --element "Dmitry-ION2K" --element "Alireza Test"
INFO:cgxSetNATZone:Working on Dmitry-ION2K
INFO:cgxSetNATZone:----- Updating interface 2
INFO:cgxSetNATZone:---------- Success
INFO:cgxSetNATZone:----- Updating interface 1
INFO:cgxSetNATZone:---------- Success
INFO:cgxSetNATZone:Working on Alireza Test
INFO:cgxSetNATZone:----- Updating interface 1
INFO:cgxSetNATZone:---------- Success
INFO:cgxSetNATZone:----- Updating interface 2
INFO:cgxSetNATZone:---------- Success
```
