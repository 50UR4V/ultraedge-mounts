"""3MF (core spec) -> binary STL in millimetres. Handles multiple build items, item transforms and components."""
import sys, zipfile, struct, xml.etree.ElementTree as ET
NS = {'c': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
SCALE = {'micron': 0.001, 'millimeter': 1, 'centimeter': 10, 'inch': 25.4, 'foot': 304.8, 'meter': 1000}
def mat(t):
    if not t: return [1,0,0,0,1,0,0,0,1,0,0,0]
    return [float(v) for v in t.split()]
def mul(a, b):  # 3MF 4x3 row-vector matrices: p' = p*A*B
    A = [a[0:3]+[0], a[3:6]+[0], a[6:9]+[0], a[9:12]+[1]]
    B = [b[0:3]+[0], b[3:6]+[0], b[6:9]+[0], b[9:12]+[1]]
    C = [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    return C[0][:3]+C[1][:3]+C[2][:3]+C[3][:3]
def app(m, p):
    x, y, z = p
    return (x*m[0]+y*m[3]+z*m[6]+m[9], x*m[1]+y*m[4]+z*m[7]+m[10], x*m[2]+y*m[5]+z*m[8]+m[11])
def main(src, dst):
    root = ET.fromstring(zipfile.ZipFile(src).read('3D/3dmodel.model'))
    k = SCALE[root.get('unit', 'millimeter')]
    objs = {o.get('id'): o for o in root.find('c:resources', NS).findall('c:object', NS)}
    tris = []
    def emit(oid, m):
        o = objs[oid]; mesh = o.find('c:mesh', NS)
        if mesh is not None:
            v = [tuple(float(e.get(a)) for a in 'xyz') for e in mesh.find('c:vertices', NS)]
            for t in mesh.find('c:triangles', NS):
                tris.append([app(m, v[int(t.get(a))]) for a in ('v1', 'v2', 'v3')])
        comps = o.find('c:components', NS)
        if comps is not None:
            for c in comps: emit(c.get('objectid'), mul(mat(c.get('transform')), m))
    for it in root.find('c:build', NS): emit(it.get('objectid'), mat(it.get('transform')))
    with open(dst, 'wb') as f:
        f.write(b'UltraEdge mounts - converted from 3MF, units mm'.ljust(80, b' '))
        f.write(struct.pack('<I', len(tris)))
        lo = [1e9]*3; hi = [-1e9]*3
        for t in tris:
            p = [tuple(c*k for c in q) for q in t]
            for q in p:
                for i in range(3): lo[i] = min(lo[i], q[i]); hi[i] = max(hi[i], q[i])
            u = [p[1][i]-p[0][i] for i in range(3)]; w = [p[2][i]-p[0][i] for i in range(3)]
            n = (u[1]*w[2]-u[2]*w[1], u[2]*w[0]-u[0]*w[2], u[0]*w[1]-u[1]*w[0]); l = (n[0]**2+n[1]**2+n[2]**2) ** .5 or 1
            f.write(struct.pack('<12fH', n[0]/l, n[1]/l, n[2]/l, *p[0], *p[1], *p[2], 0))
    print(f'{dst}: {len(tris)} triangles, size mm {[round(hi[i]-lo[i],1) for i in range(3)]}')
if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
