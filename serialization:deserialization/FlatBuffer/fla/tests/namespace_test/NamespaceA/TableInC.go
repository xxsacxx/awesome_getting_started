// automatically generated by the FlatBuffers compiler, do not modify

package NamespaceA

import (
	flatbuffers "github.com/google/flatbuffers/go"
)
type TableInC struct {
	_tab flatbuffers.Table
}

func (rcv *TableInC) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *TableInC) ReferToA1(obj *TableInFirstNS) *TableInFirstNS {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		x := rcv._tab.Indirect(o + rcv._tab.Pos)
		if obj == nil {
			obj = new(TableInFirstNS)
		}
		obj.Init(rcv._tab.Bytes, x)
		return obj
	}
	return nil
}

func (rcv *TableInC) ReferToA2(obj *SecondTableInA) *SecondTableInA {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		x := rcv._tab.Indirect(o + rcv._tab.Pos)
		if obj == nil {
			obj = new(SecondTableInA)
		}
		obj.Init(rcv._tab.Bytes, x)
		return obj
	}
	return nil
}

func TableInCStart(builder *flatbuffers.Builder) { builder.StartObject(2) }
func TableInCAddReferToA1(builder *flatbuffers.Builder, referToA1 flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(referToA1), 0) }
func TableInCAddReferToA2(builder *flatbuffers.Builder, referToA2 flatbuffers.UOffsetT) { builder.PrependUOffsetTSlot(1, flatbuffers.UOffsetT(referToA2), 0) }
func TableInCEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT { return builder.EndObject() }
