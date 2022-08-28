import docker

client = docker.from_env()

"""
print(client.containers.list())

c1 = client.containers.get(client.containers.list()[1].id)

print(c1.attrs['Config']['Image']) # gives container name
#print(c1.logs()[:10]) # shows logs

#print(client.networks.get(client.networks.list()[1].id).name) # network names
#print(client.networks.list()[1].name) # first networks name

#pd.DataFrame(c1.stats(stream=False)).to_csv('out.csv', index=False) # returns multiple stats
"""

#print(client.containers.list()[1].commit(tag="V1B1", repository="test")) # repository -> images name, tag = tag


#print([(x.name,x.id) for x in client.containers.list()])

#print(client.images.get('test:V1B1').tags) # gives name:tag

""" SAVING IMAGE
image = client.images.get('test:V1B1')
f = open('test.tar', "wb")
for chunk in image.save():
    f.write(chunk)
f.close()
"""

#print(client.images.remove('test:V1B1')) # deletes image