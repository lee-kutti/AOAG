"""
@author: Aisha Ali-Gombe
@contact: aaligombe@towson.edu, apphackuno@gmail.com
"""
import artParse as art
import sys, os, subprocess, struct, binascii
from collections import OrderedDict

unpack_int = struct.Struct('<I').unpack
unpack_dec = struct.Struct('<i').unpack
unpack_b = struct.Struct('<B').unpack  #Byte or Bool
unpack_char = struct.Struct('<c').unpack
unpack_short = struct.Struct('<H').unpack
unpack_float = struct.Struct('<f').unpack
unpack_long = struct.Struct('<Q').unpack
unpack_double = struct.Struct('<d').unpack


def getDex(dexCache, mapList):
    [g, offset] = art.fromPointer(dexCache, mapList)
    dexFileIdx = art.getIndex("DexCache", "dex_file_")
    g.seek(offset + dexFileIdx)
    dexFile = hex(struct.unpack("<Q", g.read(8))[0])
    #print "dexFile "+dexFile
    loc_ = art.getIndex("DexCache", "location_")
    g.seek(offset + loc_)
    loc = hex(unpack_int(g.read(4))[0])
    g.close()
    [g, offset] = art.fromPointer(loc, mapList)
    #print "DexFile Location "+art.getStringClass(offset, g)
    g.close()
    return dexFile


def getIdx(Idxs, idx, dexFile, memList):
    idsOff = hex(int(dexFile, 16) + Idxs)
    [g, offset] = art.fromPointer(idsOff, memList)
    g.seek(offset + idx)
    id = hex(idx + int(idsOff, 16))
    g.close()
    return id


def getIds(g, offset):
    strIds = art.getIndex("DexFile", "string_ids_")
    g.seek(offset + strIds)
    sIdsOff = hex(unpack_int(g.read(4))[0])
    fieldIds = art.getIndex("DexFile", "field_ids_")
    g.seek(offset + fieldIds)
    fIdsOff = hex(unpack_int(g.read(4))[0])
    methodIds = art.getIndex("DexFile", "method_ids_")
    g.seek(offset + methodIds)
    mIdsOff = hex(unpack_int(g.read(4))[0])
    typeIds = art.getIndex("DexFile", "type_ids_")
    g.seek(offset + typeIds)
    tIdsOff = hex(unpack_int(g.read(4))[0])
    begin = art.getIndex("DexFile", "begin_")
    g.seek(offset + begin)
    beginOff = hex(unpack_int(g.read(4))[0])
    #fieldId = getIdx(fieldIds, fieldIdx, dexFile, memList)
    return [beginOff, sIdsOff, fIdsOff, mIdsOff, tIdsOff]


def getFieldIdx(fIdsOff, dex_field_index_, mapList):
    [g, offset] = art.fromPointer(fIdsOff, mapList)
    g.seek(offset + (8 * dex_field_index_))
    clsIdx = unpack_short(g.read(2))[0]
    typeIdx = unpack_short(g.read(2))[0]
    nameIdx = unpack_dec(g.read(4))[0]
    #typeAddr = hex(int(fIdsOff,16)+dex_field_index_+ art.getIndex("FieldId","type_idx_"))
    #nameAddr = hex(int(fIdsOff,16)+dex_field_index_+ art.getIndex("FieldId","name_idx_"))
    g.close()
    return [clsIdx, typeIdx, nameIdx]


def uleb128_decode(dataIndex, g):
    g.seek(dataIndex)
    result = struct.unpack("<B", g.read(1))[0]
    if (result > 0x7f):
        cur = struct.unpack("<B", g.read(1))[0]
        result = (result & 0x7f) | ((cur & 0x7f) << 7)
        if (cur > 0x7f):
            cur = struct.unpack("<B", g.read(1))[0]
            result |= (cur & 0x7f) << 14
            if (cur > 0x7f):
                cur = struct.unpack("<B", g.read(1))[0]
                result |= (cur & 0x7f) << 21
                if (cur > 0x7f):
                    cur = struct.unpack("<B", g.read(1))[0]
                    result |= cur << 28
    g.seek(g.tell())
    data = g.read(result)
    g.close()
    return data


def getName(sIdsOff, mapList, nameIdx, beginOff):
    [strHandle, strIdxOdd] = art.fromPointer(sIdsOff, mapList)
    strHandle.seek(strIdxOdd + 4 * nameIdx)
    strDataItemOff = unpack_dec(strHandle.read(4))[0]
    [bHandle, bOdd] = art.fromPointer(beginOff, mapList)
    strHandle.close()
    return uleb128_decode(bOdd + strDataItemOff, bHandle)


def getType(tIdsOff, mapList, typeIdx, beginOff, sIdsOff, clsIdx):
    [tHandle, tIdxOdd] = art.fromPointer(tIdsOff, mapList)
    tHandle.seek(tIdxOdd + (4 * typeIdx))
    descIdx_T = unpack_dec(tHandle.read(4))[0]
    type = getName(sIdsOff, mapList, descIdx_T, beginOff)
    tHandle.seek(tIdxOdd + (4 * clsIdx))
    descIdx_C = unpack_dec(tHandle.read(4))[0]
    cls = getName(sIdsOff, mapList, descIdx_C, beginOff)
    tHandle.close()
    return [type, cls]


def getMeta(dexCache, dex_field_index_, mapList, memList):
    dexFile = getDex(dexCache, mapList)
    [dexHandle, dexOffset] = art.fromPointer(dexFile, memList)
    [beginOff, sIdsOff, fIdsOff, mIdsOff,
     tIdsOff] = getIds(dexHandle, dexOffset)
    dexHandle.close()
    [clsIdx, typeIdx, nameIdx] = getFieldIdx(fIdsOff, dex_field_index_,
                                             mapList)
    name = getName(sIdsOff, mapList, nameIdx, beginOff)
    [type, cls] = getType(tIdsOff, mapList, typeIdx, beginOff, sIdsOff, clsIdx)
    return [cls, type, name]
