# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class Element(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsElement(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Element()
        x.Init(buf, n + offset)
        return x

    # Element
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Element
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Uint16Flags, o + self._tab.Pos
            )
        return 0

    # Element
    def ElementType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Element
    def Element(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None


def ElementStart(builder):
    builder.StartObject(3)


def ElementAddId(builder, id):
    builder.PrependUint16Slot(0, id, 0)


def ElementAddElementType(builder, elementType):
    builder.PrependUint8Slot(1, elementType, 0)


def ElementAddElement(builder, element):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(element), 0
    )


def ElementEnd(builder):
    return builder.EndObject()
