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
from isilon import IsilonClient

client = IsilonClient(
    isilon_addr='http://localhost:8080' # default
    account='test' # default
    user='tester' # default
    password='testing' # default
)
```

## Discoverability

```
# List activated capabilities
response = await client.discoverability.info() # JSON
print(response)
```

## Accounts

```python
# Show account details and list containers.
await client.accounts.show()

# Create, update, or delete account metadata.
await client.accounts.update()

# Show account metadata.
await client.accounts.metadata()
```

## Containers

```python
# create container
resp = await client.containers.create("my_container")
print(resp)

# show container details and list objects
resp = await client.containers.objects("my_container")
print(resp)

# create, update or delete container metadata
metadata = {'X-Container-Meta-Test': "My metadata"}
resp = await client.containers.update_metadata("my_container", headers=metadata)
print(resp)

# show container metadata
resp = await client.containers.show_metadata("my_container")
print(resp)

# delete container
resp = await client.containers.delete("my_container")
print(resp)
```

## Objects

```python
# Get object content and metadata.
# Use this method only for small objects
await client.objects.get("my_container". "my_object")

# Get large object content and metadata.
await client.objects.get_large("my_container", "my_remote_object", "my_object")

# Create or replace object
await client.objects.create("my_container", "my_remote_object", "my_object")

# Create or replace large object.
await client.objects.create_large("my_container", "my_remote_object", "my_object")

# Copy object.
# This call will raise NotImplementedError
await client.objects.copy("my_container", "my_remote_object", "my_object")

# Delete object.
await client.objects.delete("my_container", "my_remote_object", "my_object")

# Show object metadata.
await client.objects.show_metadata("my_container", "my_remote_object", "my_object")

# Create or update object metadata.
await client.objects.update_metadata("my_container", "my_remote_object", "my_object")
```

## Endpoints

```python
# List endpoints.
await client.endpoints()
```
