import sys
prog_name = sys.argv[0]
args = sys.argv[1:]
count = len(args)
print(prog_name) # -- Cmd1
print(args) # -- Cmd2
print(count) # -- Cmd3
for x in sys.argv:
 print(f"Argument:, {x}")