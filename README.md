[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Threat Grid Working with Tags

These scripts demonstrate how to add, list, and delete tags from entities in Threat Grid. They are grouped by the entity they operate on:

01: Sample IDs  
02: IP Addresses  
03: Domains  
04: URLs  
05: File Paths  
06: Artifact SHA256s  
07: Registry Keys  

### Before using you must update the following:
- Line 3/4: api_key

Entity names used in the different scripts are found on line 7 or 11 depending on the script:
- sample_id
- ip_address
- domain
- url
- path
- artifact_sha256
- registry_key

Using domain as an example you will need to update it from:
```
domain = '<DOMAIN>'
``` 
to
```
domain = 'cisco.com'
```

### Usage

```
python 01a_add_sample_tag.py
```
