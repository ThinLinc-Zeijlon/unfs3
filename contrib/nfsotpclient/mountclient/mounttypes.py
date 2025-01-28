# Generated by rpcgen.py at Mon Mar  8 11:09:57 2004

from .mountconstants import *
from .mountpacker import *
import rpc

__all__ = ['BadDiscriminant', 'fhstatus', 'mountres3_ok', 'mountres3', 'mountbody', 'groupnode', 'exportnode']

def init_type_class(klass, ncl):
    # Initilize type class
    klass.ncl = ncl
    klass.packer = ncl.packer
    klass.unpacker = ncl.unpacker

def assert_not_none(klass, *args):
    for arg in args:
        if arg == None:
            raise TypeError(repr(klass) + " has uninitialized data")

def pack_objarray(ncl, list):
    # FIXME: Support for length assertion. 
    ncl.packer.pack_uint(len(list))
    for item in list:
        item.pack()

def unpack_objarray(ncl, klass):
    n = ncl.unpacker.unpack_uint()
    list = []
    for i in range(n):
        obj = klass(ncl)
        obj.unpack()
        list.append(obj)
    return list


class BadDiscriminant(rpc.RPCException):
    def __init__(self, value, klass):
        self.value = value
        self.klass = klass

    def __str__(self):
        return "Bad Discriminant %s in %s" % (self.value, self.klass)

class fhstatus:
    # XDR definition:
    # union fhstatus switch (unsigned fhs_status) {
    #     case 0:
    #         fhandle2    fhs_fhandle;
    #     default:
    #         void;
    # };
    def __init__(self, ncl, fhs_status=None, fhs_fhandle=None):
        init_type_class(self, ncl)
        self.fhs_status = fhs_status
        self.fhs_fhandle = fhs_fhandle
        # Shortcut to current arm
        self.arm = None

    def __repr__(self):
        s = " fhs_status=%s fhs_fhandle=%s" % (str(self.fhs_status), str(self.fhs_fhandle))
        if len(s) > 70: s = s[:70] + "..."
        return "<fhstatus:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.fhs_status)
        self.packer.pack_unsigned(self.fhs_status)
        if self.fhs_status == 0:
            assert_not_none(self, self.fhs_fhandle)
            self.packer.pack_fhandle2(self.fhs_fhandle)
            self.arm = self.fhs_fhandle
        else:
            pass
            

    def unpack(self):
        self.fhs_status = self.unpacker.unpack_unsigned()
        if self.fhs_status == 0:
            self.fhs_fhandle = self.unpacker.unpack_fhandle2()
            self.arm = self.fhs_fhandle
        else:
            pass
            

class mountres3_ok:
    # XDR definition:
    # struct mountres3_ok {
    #     fhandle3 fhandle;
    #     int auth_flavors<>;
    # };
    def __init__(self, ncl, fhandle=None, auth_flavors=None):
        init_type_class(self, ncl)
        self.fhandle = fhandle
        self.auth_flavors = auth_flavors

    def __repr__(self):
        s = " fhandle=%s auth_flavors=%s" % (str(self.fhandle), str(self.auth_flavors))
        if len(s) > 70: s = s[:70] + "..."
        return "<mountres3_ok:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.fhandle, self.auth_flavors)
        self.packer.pack_fhandle3(self.fhandle)
        self.packer.pack_int(self.auth_flavors)

    def unpack(self):
        self.fhandle = self.unpacker.unpack_fhandle3()
        self.auth_flavors = self.unpacker.unpack_array(self.unpacker.unpack_int)

class mountres3:
    # XDR definition:
    # union mountres3 switch (mountstat3 fhs_status) {
    #     case MNT3_OK:
    #         mountres3_ok    mountinfo;
    #     default:
    #         void;
    # };
    def __init__(self, ncl, fhs_status=None, mountinfo=None):
        init_type_class(self, ncl)
        self.fhs_status = fhs_status
        self.mountinfo = mountinfo
        # Shortcut to current arm
        self.arm = None

    def __repr__(self):
        s = " fhs_status=%s mountinfo=%s" % (str(self.fhs_status), str(self.mountinfo))
        if len(s) > 70: s = s[:70] + "..."
        return "<mountres3:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.fhs_status)
        self.packer.pack_mountstat3(self.fhs_status)
        if self.fhs_status == MNT3_OK:
            assert_not_none(self, self.mountinfo)
            self.mountinfo.pack()
            self.arm = self.mountinfo
        else:
            pass
            

    def unpack(self):
        self.fhs_status = self.unpacker.unpack_mountstat3()
        if self.fhs_status == MNT3_OK:
            self.mountinfo = mountres3_ok(self)
            self.mountinfo.unpack()
            self.arm = self.mountinfo
        else:
            pass
            

class mountbody:
    # XDR definition:
    # struct mountbody {
    #     name ml_hostname;
    #     dirpath ml_directory;
    #     mountlist ml_next;
    # };
    def __init__(self, ncl, ml_hostname=None, ml_directory=None, ml_next=None):
        init_type_class(self, ncl)
        self.ml_hostname = ml_hostname
        self.ml_directory = ml_directory
        self.ml_next = ml_next

    def __repr__(self):
        s = " ml_hostname=%s ml_directory=%s ml_next=%s" % (str(self.ml_hostname), str(self.ml_directory), str(self.ml_next))
        if len(s) > 70: s = s[:70] + "..."
        return "<mountbody:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.ml_hostname, self.ml_directory, self.ml_next)
        self.packer.pack_name(self.ml_hostname)
        self.packer.pack_dirpath(self.ml_directory)
        self.packer.pack_mountlist(self.ml_next)

    def unpack(self):
        self.ml_hostname = self.unpacker.unpack_name()
        self.ml_directory = self.unpacker.unpack_dirpath()
        self.ml_next = self.unpacker.unpack_mountlist()

class groupnode:
    # XDR definition:
    # struct groupnode {
    #     name gr_name;
    #     groups gr_next;
    # };
    def __init__(self, ncl, gr_name=None, gr_next=None):
        init_type_class(self, ncl)
        self.gr_name = gr_name
        self.gr_next = gr_next

    def __repr__(self):
        s = " gr_name=%s gr_next=%s" % (str(self.gr_name), str(self.gr_next))
        if len(s) > 70: s = s[:70] + "..."
        return "<groupnode:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.gr_name, self.gr_next)
        self.packer.pack_name(self.gr_name)
        self.packer.pack_groups(self.gr_next)

    def unpack(self):
        self.gr_name = self.unpacker.unpack_name()
        self.gr_next = self.unpacker.unpack_groups()

class exportnode:
    # XDR definition:
    # struct exportnode {
    #     dirpath ex_dir;
    #     groups ex_groups;
    #     exports ex_next;
    # };
    def __init__(self, ncl, ex_dir=None, ex_groups=None, ex_next=None):
        init_type_class(self, ncl)
        self.ex_dir = ex_dir
        self.ex_groups = ex_groups
        self.ex_next = ex_next

    def __repr__(self):
        s = " ex_dir=%s ex_groups=%s ex_next=%s" % (str(self.ex_dir), str(self.ex_groups), str(self.ex_next))
        if len(s) > 70: s = s[:70] + "..."
        return "<exportnode:%s>" % s

    def pack(self, dummy=None):
        assert_not_none(self, self.ex_dir, self.ex_groups, self.ex_next)
        self.packer.pack_dirpath(self.ex_dir)
        self.packer.pack_groups(self.ex_groups)
        self.packer.pack_exports(self.ex_next)

    def unpack(self):
        self.ex_dir = self.unpacker.unpack_dirpath()
        self.ex_groups = self.unpacker.unpack_groups()
        self.ex_next = self.unpacker.unpack_exports()

