
import sys
sys.path.insert(0, '/Users/onion8/learning/serialization:deserialization/FlatBuffer')

# import pkg.sdkdata as pkg
# from pkg.sdkdata import *;
import message


with open("/Users/onion8/learning/serialization:deserialization/FlatBuffer/flatmain.bin", "rb") as f:
    buff = f.read()

monster = message.message.GetRootAsmessage(buff, 1)

sender = monster.Name();
msg = monster.Mesage();

print(monster)
print(sender)
print(msg)


