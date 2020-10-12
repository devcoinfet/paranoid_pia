import commands
fdisk_output = commands.getoutput("fdisk -l %s" % partition)
print(fdisk_output)

