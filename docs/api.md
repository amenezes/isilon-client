# Object Storage API

> reference: [openstack object storage API](https://docs.openstack.org/api-ref/object-store/)

Default values from `IsilonClient`.

```txt
# environment variables
ISILON_ADDRESS=http://localhost:8080
ISILON_ACCOUNT=test
ISILON_USER=tester
ISILON_PASSWORD=testing
```

This values can be override setting environment variable or incluing in the class constructor.

```python
import isilon

isilon.isilon_addr
# default: 'http://localhost:8080'

isilon.account
# default: 'test'

isilon.user
# default: 'tester'

isilon.password
# default: 'testing'
)
```

## Discoverability

```python
# List activated capabilities
await isilon.discoverability.info()
```

## Accounts

```python
# Show account details and list containers.
await isilon.accounts.show()

# Create, update, or delete account metadata.
await isilon.accounts.update()

# Show account metadata.
await isilon.accounts.metadata()
```

## Containers

```python
# create container
await isilon.containers.create("my_container")

# show container details and list objects
await isilon.containers.objects("my_container")

# create, update or delete container metadata
metadata = {'X-Container-Meta-Test': "My metadata"}
await isilon.containers.update_metadata("my_container", headers=metadata)

# show container metadata
await isilon.containers.show_metadata("my_container")

# delete container
await isilon.containers.delete("my_container")
```

## Objects

```python
# Get object content and metadata.
# Use this method only for small objects
await isilon.objects.get("my_container". "my_object")

# Get large object content and metadata.
await isilon.objects.get_large("my_container", "my_remote_object", "my_object")

# Create or replace object
await isilon.objects.create("my_container", "my_remote_object", "my_object")

# Create or replace large object.
await isilon.objects.create_large("my_container", "my_remote_object", "my_object")

# Copy object.
# This call will raise NotImplementedError
await isilon.objects.copy("my_container", "my_remote_object", "my_object")

# Delete object.
await isilon.objects.delete("my_container", "my_remote_object", "my_object")

# Show object metadata.
await isilon.objects.show_metadata("my_container", "my_remote_object", "my_object")

# Create or update object metadata.
await isilon.objects.update_metadata("my_container", "my_remote_object", "my_object")
```

## Endpoints

```python
# List endpoints.
await isilon.endpoints()
```
