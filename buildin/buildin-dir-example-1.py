import sys

def dump(valud):
    print valud,"=>",dir(valud)

dump(0)
dump(1.0)
dump(0.0j)

dump([])
dump({})

dump("string")
dump(len)
dump(sys)
