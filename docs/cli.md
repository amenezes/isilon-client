# Command-line

## Instalation

```bash
pip install isilon-client[cli]
```

## Overview

```bash
python -m isilon -h

Isilon Client version 0.1.0a0

USAGE
  isilon-client [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]

ARGUMENTS
  <command>              The command to execute
  <arg>                  The arguments of the command

GLOBAL OPTIONS
  -h (--help)            Display this help message
  -q (--quiet)           Do not output any message
  -v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more verbose output and "-vvv" for debug
  -V (--version)         Display this application version
  --ansi                 Force ANSI output
  --no-ansi              Disable ANSI output
  -n (--no-interaction)  Do not ask any interactive question

AVAILABLE COMMANDS
  accounts               Accounts.
  containers             Containers.
  discoverability        Discoverability.
  endpoints              Endpoints.
  help                   Display the manual of a command
  objects                Objects.
```

## Discoverability

If configured, lists the activated capabilities for this version of the Object Storage API.

```bash
python -m isilon discovery
```

Sample Response
```txt
{
    "bulk_delete": {
        "max_deletes_per_request": 10000,
        "max_failed_deletes": 1000
    },
    "bulk_upload": {
        "max_containers_per_extraction": 10000,
        "max_failed_extractions": 1000
    },
    "s3api": {
        "allow_multipart_uploads": true,
        "max_bucket_listing": 1000,
        "max_multi_delete_objects": 1000,
        "max_parts_listing": 1000,
        "max_upload_part_num": 1000,
        "min_segment_size": 5242880,
        "s3_acl": false
    },
    "slo": {
        "max_manifest_segments": 1000,
        "max_manifest_size": 8388608,
        "min_segment_size": 1,
        "yield_frequency": 10
    },
    "swift": {
        "account_autocreate": true,
        "account_listing_limit": 10000,
        "allow_account_management": true,
        "container_listing_limit": 10000,
        "extra_header_count": 0,
        "max_account_name_length": 256,
        "max_container_name_length": 256,
        "max_file_size": 5368709122,
        "max_header_size": 8192,
        "max_meta_count": 90,
        "max_meta_name_length": 128,
        "max_meta_overall_size": 4096,
        "max_meta_value_length": 256,
        "max_object_name_length": 1024,
        "policies": [
            {
                "aliases": "Policy-0",
                "default": true,
                "name": "Policy-0"
            }
        ],
        "strict_cors_mode": true,
        "version": "2.20.0"
    },
    "symlink": {
        "symloop_max": 2
    },
    "tempauth": {
        "account_acls": true
    },
    "tempurl": {
        "allowed_digests": [
            "sha1",
            "sha256",
            "sha512"
        ],
        "incoming_allow_headers": [],
        "incoming_remove_headers": [
            "x-timestamp"
        ],
        "methods": [
            "GET",
            "HEAD",
            "PUT",
            "POST",
            "DELETE"
        ],
        "outgoing_allow_headers": [
            "x-object-meta-public-*"
        ],
        "outgoing_remove_headers": [
            "x-object-meta-*"
        ]
    },
    "versioned_writes": {
        "allowed_flags": [
            "x-versions-location",
            "x-history-location"
        ]
    }
}
```

## Accounts

Lists containers for an account.

```python
python -m isilon accounts 
```

### Show account details and list containers

```python
python -m isilon accounts -s test
```

Sample response

```bash
[
    {
        "bytes": 0,
        "count": 0,
        "last_modified": "2020-10-24T00:29:06.773620",
        "name": "digital"
    }
]
```

### Create, update, or delete account metadata

```python
python -m isilon accounts -u test --meta '{"department": "HR"}'
```

Sample response

```bash
metadata updated.
```

### Show account metadata

```python
python -m isilon accounts -m test
```

Sample response

```bash
Content-Length: 0
X-Account-Object-Count: 0
X-Account-Storage-Policy-Policy-0-Bytes-Used: 0
X-Account-Storage-Policy-Policy-0-Container-Count: 1
X-Timestamp: 1603499346.75625
X-Account-Storage-Policy-Policy-0-Object-Count: 0
X-Account-Meta-Department: HR
X-Account-Bytes-Used: 0
X-Account-Container-Count: 1
Content-Type: application/json; charset=utf-8
Accept-Ranges: bytes
X-Trans-Id: tx1fdd460a8c6e4f5da5a61-005f937e84
X-Openstack-Request-Id: tx1fdd460a8c6e4f5da5a61-005f937e84
Date: Sat, 24 Oct 2020 01:08:20 GMT
```

## Containers

Lists objects in a container.

### Show container details and list objects

```python
python -m isilon containers -o mycontainer
```

Sample response

```bash
{'bytes': 5, 'last_modified': '2020-09-28T03:01:46.874810', 'hash': '8e6f6f815b50f474cf0dc22d4f400725', 'name': 'test.txt', 'content_type': 'text/html;charset=UTF-8'}
```

### Create container

```python
python -m isilon containers -c my_new_container
```

Sample response

```bash
my_new_container created.
```

### Show container metadata

```python
python -m isilon containers -m my_new_container
```

Sample response

```bash
Content-Length: 0
X-Container-Object-Count: 0
Accept-Ranges: bytes
X-Storage-Policy: Policy-0
Last-Modified: Mon, 28 Sep 2020 03:08:46 GMT
X-Container-Bytes-Used: 0
X-Timestamp: 1601262525.60213
Content-Type: application/json; charset=utf-8
X-Trans-Id: tx2a91cf7eae25430b93108-005f7153ea
X-Openstack-Request-Id: tx2a91cf7eae25430b93108-005f7153ea
Date: Mon, 28 Sep 2020 03:09:30 GMT
```

### Create, update or delete container metadata

```python
python -m isilon containers -u my_new_container
```
Sample response

```bash
metadata updated.
```

### Delete container

```python
python -m isilon containers -d my_new_container
```

Sample response

```bash
my_new_container deleted.
```

## Objects

Creates, replaces, shows details for, and deletes objects.

### Create or replace object

```python
python -m isilon objects -c my_container my_object
```

### Show object metadata

```python
python -m isilon objects -m my_container my_object
```

### Create or update object metadata

```python
python -m isilon objects -u my_container my_object
```

### Delete object

```python
python -m isilon objects -d my_container my_object
```

## Endpoints

If configured, lists endpoints for an account.

```python
python -m isilon endpoints
```

