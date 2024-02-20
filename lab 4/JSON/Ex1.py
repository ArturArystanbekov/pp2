import json

data = json.load(open("sample-data.json", "r"))

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU ')
print('-------------------------------------------------- --------------------  ------  ------')

i = data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]

for i in range(len(data["imdata"])):
    dn = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    speed = data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    mtu = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(f'{f"{dn}":<72}{f"{speed}":<11}{f"{mtu}":<10}')