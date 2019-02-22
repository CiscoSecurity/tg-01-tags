[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Grid "Gitter chat")

### Threat Grid Working with Tags:

These scripts demonstrate how to add, list, and delete tags from entities in Threat Grid. They are grouped by the entity they operate on:

01: Sample IDs  
02: IP Addresses  
03: Domains  
04: URLs  
05: File Paths  
06: Artifact SHA256s  
07: Registry Keys  

### Before using you must update the following:
- api_key

Entity names where present:
- sample_id
- ip_address
- domain
- url
- path
- artifact_sha256
- registry_key

When an entity is present in a script an example with the appropriate format is provided as a comment. These variables are noted with a < (less-than-sign) and > (greater-than-sign).
```
# EXAMPLE:
# ip_address = '193.70.19.218'
ip_address = '<IP_ADDRESS>'
``` 

### Usage:
```
python 01a_add_sample_tag.py
```

### Example script output:
```
{'api_version': 2, 'id': 1363296}
```
