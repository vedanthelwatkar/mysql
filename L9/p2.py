#wapp to demo dictionary
#declare
#add
#update
#remove

#declare ele
d1={"idli":30,"dosa":40,"wada":20}
print(d1)

#add ele
d1["samosa"]=30
print(d1)

#update ele
d1["wada"]=30
print(d1)

#add ele
d1["dhokla"]=25
print(d1)

#update one dict with another
d1.update({"upma":30,"poha":40})
print(d1)

#remove ele
d1.pop("dhokla")
print(d1)

#accessing the key to get values
print(d1.get("wada"))
print(d1.get("upma"))
print(d1.get("momo"))
#print(d1.get["momo"])
