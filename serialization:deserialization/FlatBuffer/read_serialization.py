
import sys
sys.path.insert(0, '/Users/onion8/learning/serialization:deserialization/FlatBuffer')

# import pkg.sdkdata as pkg
# from pkg.sdkdata import *;
import message


with open("/Users/onion8/learning/serialization:deserialization/FlatBuffer/abc.bin", "rb") as f:
    buff = bytearray(f.read())
    #print(buff)
#print(buff)
monster = message.message.GetRootAsmessage(buff, 0)

#sender = monster.Id();
msg = monster.Mesage();

#print(monster)
#print(sender)
print(msg)


