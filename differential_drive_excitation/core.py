import math
from .common import number,integer,identifier,unique_ids
def run(d):
 rows=d['segments'];track=number(d['track_width'],1e-9,1e6)
 if not 2<=len(rows)<=10000:raise ValueError('segments')
 aa=ab=bb=ay=by=0;equations=[]
 for r in rows:
  l=number(r['left_rotation']);rr=number(r['right_rotation']);s=number(r['distance']);yaw=number(r['yaw'])
  for a,b,y in [(l/2,rr/2,s),(-l/track,rr/track,yaw)]:aa+=a*a;ab+=a*b;bb+=b*b;ay+=a*y;by+=b*y;equations.append((a,b,y))
 det=aa*bb-ab*ab;trace=aa+bb
 if trace==0 or det<=1e-12*trace*trace:return dict(status='unidentifiable',gram=[[aa,ab],[ab,bb]],determinant=det)
 left=(ay*bb-by*ab)/det;right=(by*aa-ay*ab)/det;res=[a*left+b*right-y for a,b,y in equations];return dict(status='fitted',left_radius=left,right_radius=right,physical=left>0 and right>0,residual_sse=math.fsum(x*x for x in res),gram=[[aa,ab],[ab,bb]],determinant=det)
