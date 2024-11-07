import pyrosetta
from pyrosetta.rosetta import core
import pybind11
import inspect

class MyClass:
    def __init__(self):
        pass

def extract_class_signature_from_overload_line( l ):
    #     1. (pose: pyrosetta.rosetta.core.pose.Pose, residue_positions: pyrosetta.rosetta.utility.vector1_bool) -> None
    l = l.split("->")[0]
    #    1. (pose: pyrosetta.rosetta.core.pose.Pose, residue_positions: pyrosetta.rosetta.utility.vector1_bool)
    s1 = l.find("(")+1
    s2 = l.rfind(")")
    if s1==s2: return []
    l = l[s1:s2]
    #pose: pyrosetta.rosetta.core.pose.Pose, residue_positions: pyrosetta.rosetta.utility.vector1_bool
    ls = [a.strip().rstrip() for a in l.split( "," )]
    #['pose: pyrosetta.rosetta.core.pose.Pose', 'residue_positions: pyrosetta.rosetta.utility.vector1_bool']
    ls = [ a[a.find(":")+1:].strip() for a in ls ]
    #['pyrosetta.rosetta.core.pose.Pose', 'pyrosetta.rosetta.utility.vector1_bool']
    ls = [ eval(a) for a in ls ]
    #[<class 'pyrosetta.rosetta.core.pose.Pose'>, <class 'pyrosetta.rosetta.utility.vector1_bool'>]
    # returns a list of classes
    return ls
    
def signatures_conflict( sig1, sig2, only_enforce_distinct_parents=True ):
    # if only_enforce_distinct_parents=True, we will not complain if foo(<class B>) shadows foo(<class B>), we will only complain if foo(<class B>) shadows foo(<class A>) where A is a parent of B
    if len(sig1) != len(sig2): return False
    
    if (sig1 == sig2) and only_enforce_distinct_parents: return False

    for i in range(len(sig1)):
        class1 = sig1[i]
        class2 = sig2[i]
        check12 = issubclass( class1, class2 )
        check21 = issubclass( class2, class1 )
        if not (check12 or check21):
            # if neither class clashes with the other one, these two signatures are safe
            return False

    return True
    

def test_function( F ):
    failed = True
    try:
        F( MyClass() )
        failed = False
    except Exception as E:
        exception_str = str(E)

    assert failed, F
    assert "The following argument types are supported" in exception_str, exception_str

    signatures = []
    for l in exception_str.split("\n"):
        if l[0:4] != "    " or l[5] != ".": continue
        #if "->" not in l: continue

        if "*" in l:
            print( "Skipping weird signature", l )
            # like     2. pyrosetta.rosetta.core.chemical.MutableChiRecord(atm_vec: pyrosetta.rosetta.utility.vector1_void_*)
            continue

        if "::" in l:
            print( "Skipping incompletely bound signature", l )
            continue

        if "Tuple[" in l or "Callable[" in l:
            print( "Skipping complicated signature (for now?)", l )
            continue

        try:
            sig = extract_class_signature_from_overload_line( l )
        except Exception as e:
            if str(e).startswith("name '") and str(e).endswith("' is not defined"):
                print( "Skipping incompletely bound signature", l, ":", str(e) )
                continue
            print( "ERROR" )
            print( l )
            print( "-----" )
            print( e )
            exit( 0 )
        signatures.append( sig )

    for i in range(len(signatures)):
        for j in range(i+1,len(signatures)):
            if signatures_conflict( signatures[i], signatures[j] ):
                print( f"CONFLICT {F} {signatures[i]} {signatures[j]}" )

def test_class( C ):
    # 1. test __init__
    try:
        test_function( C )
    except AssertionError as E:
        if "No constructor defined" in str(E):
            print( "No constructor defined for", C )
            pass
        else:
            raise E

    # 2. test functions
    for cname in dir(C):
        if cname.startswith("__"): continue
        #if cname == "__init__": continue

        cattr = getattr(C,cname)
        type_str = str( type( cattr ) )
        if type_str == "<class 'instancemethod'>":
            try:
                test_function( cattr )
            except AssertionError as e:
                if "takes no arguments" in str(e):
                    pass
                else:
                    raise e
        elif type_str == "<class 'module'>":
            print( cattr )
            exit( 0 )
            test_module( cattr )
        else:
            print( "skipping type", type_str, "for", cname, "in", C )

def test_module( D ):
    for dname in dir(D):
        dattr = getattr(D,dname)
        type_str = str( type( dattr ) )
        if type_str == "<class 'pybind11_builtins.pybind11_type'>":
            if dname.endswith( "Creator" ):
                print( "skipping creator type", dname )
            else:
                test_class( dattr )
        elif type_str == "<class 'builtin_function_or_method'>":
            test_function( dattr )
        elif type_str == "<class 'module'>":
            test_module( dattr )
        else:
            print( "skipping type", type_str, "for", dname )

if __name__ == '__main__':
    #test_class( core.select.residue_selector.NotResidueSelector )
    test_module( core )
