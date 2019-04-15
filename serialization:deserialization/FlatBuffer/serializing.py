import sys
sys.path.insert(0, '/Users/onion8/learning/serialization:deserialization/FlatBuffer')
sys.path.insert(0, '/Users/onion8/learning/serialization:deserialization/fla')
import flatbuffers
import message
#from . import *



builder = flatbuffers.Builder(1024)
print(builder)
Mesage=builder.CreateString("Orc")
print(Mesage)
message.messageStart(builder)
message.messageAddMesage(builder, Mesage)
msgs=message.messageEnd(builder)
builder.Finish(msgs)
buf = builder.Output()
newFileByteArray = bytearray(buf)
newFile = open("abc.bin", "wb")
newFile.write(newFileByteArray)