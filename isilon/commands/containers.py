import json

from cleo import Command

from isilon.commands.exec import Operator


class ContainersCommand(Command):
    """
    Containers.

    containers
        {container : Container name.}
        {--headers=* : HTTP headers.}
        {--o|objects : Show container details and list objects.}
        {--c|create : Create container.}
        {--m|metadata : Show container metadata.}
        {--u|update : Create, update or delete container metadata.}
        {--d|delete : Delete container.}
    """

    def handle(self):
        op = Operator()
        container_name = str(self.argument("container"))
        headers = dict()
        for header in self.option("headers"):
            headers.update(json.loads(header))
        if self.option("objects"):
            resp = op.execute(op.client.containers.objects, container_name, headers)
            for obj in resp:
                self.line(json.dumps(obj, indent=4, sort_keys=True))
        elif self.option("create"):
            op.execute(op.client.containers.create, container_name, headers)
            self.line(
                f"<options=bold>container <comment>{container_name}</comment> created.</>"
            )
        elif self.option("delete"):
            op.execute(op.client.containers.delete, container_name, headers)
            self.line(
                f"<options=bold>container <comment>{container_name}</comment> deleted.</>"
            )
        elif self.option("metadata"):
            resp = op.execute(
                op.client.containers.show_metadata, container_name, headers
            )
            for meta_key, meta_value in resp.items():
                self.line(f"<options=bold>{meta_key}</>: {meta_value}")
        elif self.option("update"):
            op.execute(op.client.containers.update_metadata, container_name, headers)
            self.line("<options=bold>container metadata updated.</>")
