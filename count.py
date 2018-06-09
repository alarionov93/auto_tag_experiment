from json import load, dump

ob = load(open("rez.json"))

sum_at = 0
sum_ha = 0
sum_yt = 0

for i in [ str(_) for _ in ob.keys() ]:
    try:
        n_at = len(ob[i]["AT"]["tags"])
        n_ha = len(ob[i]["HA"]["tags"])
        n_ct = len(ob[i]["CT"])
        n_yt = len(ob[i]["YT"]["tags"])
        sum_at += ob[i]["AT"]["dasha"]/max(n_at, n_ct) 
        sum_ha += ob[i]["HA"]["dasha"]/max(n_ha, n_ct)
        sum_yt += ob[i]["YT"]["dasha"]/max(n_yt, n_ct)
    except TypeError as e:
        print(e)
    
ob.update({"dasha_at":sum_at})
ob.update({"dasha_ha":sum_ha})
ob.update({"dasha_yt":sum_yt})

dump(ob,open("rez1.json","w"),ensure_ascii = 0,indent = 4)
