
import pycas as pc

metric_prefixes = [('Y',1e+24),('Z',1e+21),('E',1e+18),('P',1e+15),('T',1e+12),('G',1e+09),('M',1e+06),('k',1e+03),('h',1e+02),('da',1e+01),('d',1e-01),('c',1e-02),('m',1e-03),('u',1e-06),('n',1e-09),('p',1e-12),('f',1e-15),('a ',1e-18),('z',1e-21),('y',1e-24)]

base_units = set()

def add_metric_prefixes(name):
    s = globals()[name]
    for p,v in metric_prefixes:
        globals()[p+name] = v*s

def create_unit(name):
    u = pc.Symbol("__si_base_unit_"+name,type=pc.Types.Real,positive=True,latex=r'\text{%s}' % name)
    globals()[name] = u
    base_units.add(u)
    add_metric_prefixes(name)

create_unit('m')
create_unit('kg')
create_unit('s')
create_unit('A')
create_unit('K')
create_unit('mol')
create_unit('cd')

C = s*A
add_metric_prefixes('C')

N = kg*m/s**2
add_metric_prefixes('N')

Hz = 1/s
add_metric_prefixes('Hz')

Pa = N/m**2
add_metric_prefixes('Pa')

V = kg*m**2*s**-3*A**-1
add_metric_prefixes('V')

J = C*V
add_metric_prefixes('J')

W = J/s
add_metric_prefixes('W')

F = kg**-1*m**-2*s**4*A**2
add_metric_prefixes('F')

ohm = kg*m**2*s**-3*A**-2
add_metric_prefixes('ohm')

eV = 1.6021766208 * pc.S(10)**-19 * J
add_metric_prefixes('eV')

h = 6.626070040*pc.S(10)**-34*J*s
hbar = h/(2*pc.pi)

c = 299792458 * m / s

def contains_unit(expr):
    for e in pc.postorder_traversal(expr):
        if e in base_units:
            return True
    return False