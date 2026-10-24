import json, random
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def budget(b, mins):
    t = sum(mins); k = len(mins)
    tail = f"{pl(b-t,' minute',' minutes')} left." if t <= b else f"{pl(t-b,' minute',' minutes')} over."
    return f"The {pl(k,' app',' apps')} {v(k,'takes','take')} {pl(t,' minute',' minutes')} of the {b}-minute budget, {tail}"
def share(name, m, t):
    p = (200*m + t)//(2*t)
    return f"{name} takes {pl(m,' minute',' minutes')}, {p}% of the total."
def week(mins):
    w = sum(mins)*7; h, r = divmod(w, 60)
    return f"At this pace the week takes {pl(w,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
def split(b, k):
    q, r = divmod(b, k)
    return f"An even split of the {b}-minute budget over the {pl(k,' app',' apps')} gives {pl(q,' minute',' minutes')} each, {pl(r,' minute',' minutes')} spare."
random.seed(797)
R = random.randint
cases = [
 dict(fn="budget", args=["90",["25","40","15"]], expect=budget(90,[25,40,15])),
 dict(fn="share", args=["Messages","25","80"], expect=share("Messages",25,80)),
 dict(fn="share", args=["Shorts","40","80"], expect=share("Shorts",40,80)),
 dict(fn="share", args=["Maps","15","80"], expect=share("Maps",15,80)),
 dict(fn="week", args=[["25","40","15"]], expect=week([25,40,15])),
 dict(fn="split", args=["90","3"], expect=split(90,3)),
 dict(fn="budget", args=["1",["1"]], expect=budget(1,[1])),
 dict(fn="share", args=["Solo","1","1"], expect=share("Solo",1,1)),
 dict(fn="week", args=[["1"]], expect=week([1])),
 dict(fn="split", args=["1","1"], expect=split(1,1)),
 dict(fn="budget", args=["60",["30","30"]], expect=budget(60,[30,30])),
 dict(fn="budget", args=["30",["31"]], expect=budget(30,[31])),
 dict(fn="split", args=["90","7"], expect=split(90,7)),
 dict(fn="split", args=["1440","12"], expect=split(1440,12)),
 dict(fn="week", args=[["1440"]*12], expect=week([1440]*12)),
]
for _ in range(18):
    k = R(1,6); mins = [R(1,1440) for _ in range(k)]; b = R(1,1440)
    cases.append(dict(fn="budget", args=[str(b),[str(m) for m in mins]], expect=budget(b,mins)))
for _ in range(22):
    k = R(1,12); mins = [R(1,1440) for _ in range(k)]; t = sum(mins); m = mins[R(0,k-1)]; nm = f"App{R(1,999)}"
    cases.append(dict(fn="share", args=[nm,str(m),str(t)], expect=share(nm,m,t)))
for _ in range(20):
    k = R(1,12); mins = [R(1,1440) for _ in range(k)]
    cases.append(dict(fn="week", args=[[str(m) for m in mins]], expect=week(mins)))
for _ in range(24):
    b = R(1,1440); k = R(1,12)
    cases.append(dict(fn="split", args=[str(b),str(k)], expect=split(b,k)))
errs=[["budget",["0",["30"]]],["budget",["1441",["30"]]],["budget",["2.5",["30"]]],["budget",["90",["0"]]],["budget",["90",["1441"]]],
 ["budget",["90",["1.5"]]],["budget",["90",[]]],["share",["","25","80"]],["share",["X"*25,"25","80"]],["share",["App","0","80"]],
 ["share",["App","25","0"]],["week",[["0"]]],["week",[["1441"]]],["week",[[]]],["split",["0","3"]],["split",["90","0"]],
 ["split",["90","13"]],["split",["2.5","3"]],["budget",["90",["10"]*13]],["share",["App","1441","2000"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
