Site_name = "Saxony"
PCI = 28
RSRP = -117.5
SINR = 25
ENDC = True

print(type(Site_name))
print(type(PCI))
print(type(RSRP))
print(type(SINR))
print(type(ENDC))

if RSRP <= -110:
	print("ALARM")
elif RSRP >= -110 and RSRP <=-105:
	print("WARNING")
else:
	print("OK")


pci_list = [ 211 , 138 , 139, 205, 206, 292, 211, 139, 388]

print(pci_list[0])
print(pci_list[-1])

pci_list.append(12)

