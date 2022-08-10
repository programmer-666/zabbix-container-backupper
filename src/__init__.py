import docker 

client = docker.from_env()

c1 = client.containers.get(client.containers.list()[1].id)

print(c1.attrs['Config']['Image']) # gives container name