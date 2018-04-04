/etc/security/limits.conf
weblogic  soft  nofile  8192
weblogic  hard  nofile  8192

/etc/sysctl.conf
fs.file-max =

hdfs-site.xml data.dir

/etc/fstab
/data noatime,noadirtime

SELINUX off

ntp

최신버전 바로 업그레이드하지 말 것

/etc/ssh/sshd_config
GSSAPIAuthentication no
UseDNS no

~/.ssh/config
Host nn01
  StrictHostkeyChecking nop
  UseKnownHostsFile /dev/null
Host dn01
  StrictHostkeyChecking nop
  UseKnownHostsFile /dev/null
