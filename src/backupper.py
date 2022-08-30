import docker as dr

class Backupper:
    def __init__(self):
        self.cl = dr.from_env()

    def list_containers(self):
        self.containers = []
        for container in self.cl.containers.list():
            self.containers.append((container.name, container.id))
        return self.containers
