## Redis 설치하기
  
https://www.lesstif.com/pages/viewpage.action?pageId=6979743
  
~~~
[root@localhost yum.repos.d]# rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
Retrieving https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
Preparing...                          ################################# [100%]
        package epel-release-7-11.noarch is already installed
~~~
  
~~~
[root@localhost yum.repos.d]# rpm -Uvh http://mirror.premi.st/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
Retrieving http://mirror.premi.st/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
curl: (22) The requested URL returned error: 404 Not Found
error: skipping http://mirror.premi.st/epel/7/x86_64/e/epel-release-7-5.noarch.rpm - transfer failed
[root@localhost yum.repos.d]# rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
Retrieving http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
warning: /var/tmp/rpm-tmp.VgNNmY: Header V4 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
Preparing...                          ################################# [100%]
        package remi-release-7.4-2.el7.remi.noarch is already installed
~~~
  
~~~
[root@localhost yum.repos.d]# rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm
Retrieving https://mirror.webtatic.com/yum/el7/epel-release.rpm
warning: /var/tmp/rpm-tmp.TPfla9: Header V4 RSA/SHA1 Signature, key ID 62e74ca5: NOKEY
Preparing...                          ################################# [100%]
        package epel-release-7-11.noarch (which is newer than epel-release-7-5.noarch) is already installed
[root@localhost yum.repos.d]# rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
Retrieving https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
warning: /var/tmp/rpm-tmp.gJrHYH: Header V4 RSA/SHA1 Signature, key ID 62e74ca5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:webtatic-release-7-3             ################################# [100%]
~~~

~~~

[root@localhost yum.repos.d]# yum update
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi-safe: mirror.uta.edu.ec
 * webtatic: sp.repo.webtatic.com
Resolving Dependencies
--> Running transaction check
---> Package ModemManager.x86_64 0:1.6.0-2.el7 will be updated
---> Package ModemManager.x86_64 0:1.6.10-1.el7 will be an update
---> Package ModemManager-glib.x86_64 0:1.6.0-2.el7 will be updated
---> Package ModemManager-glib.x86_64 0:1.6.10-1.el7 will be an update
---> Package NetworkManager.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-adsl.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-adsl.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-glib.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-glib.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-libnm.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-libnm.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-ppp.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-ppp.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-team.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-team.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-tui.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-tui.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package NetworkManager-wifi.x86_64 1:1.8.0-9.el7 will be updated
---> Package NetworkManager-wifi.x86_64 1:1.10.2-14.el7_5 will be an update
---> Package PackageKit.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package PackageKit-command-not-found.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit-command-not-found.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package PackageKit-glib.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit-glib.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package PackageKit-gstreamer-plugin.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit-gstreamer-plugin.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package PackageKit-gtk3-module.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit-gtk3-module.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package PackageKit-yum.x86_64 0:1.1.5-1.el7.centos will be updated
---> Package PackageKit-yum.x86_64 0:1.1.5-2.el7.centos will be an update
---> Package abrt.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-ccpp.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-ccpp.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-kerneloops.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-kerneloops.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-pstoreoops.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-pstoreoops.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-python.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-python.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-vmcore.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-vmcore.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-addon-xorg.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-addon-xorg.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-cli.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-cli.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-console-notification.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-console-notification.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-dbus.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-dbus.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-desktop.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-desktop.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-gui.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-gui.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-gui-libs.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-gui-libs.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-libs.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-libs.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-python.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-python.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-retrace-client.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-retrace-client.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package abrt-tui.x86_64 0:2.1.11-48.el7.centos will be updated
---> Package abrt-tui.x86_64 0:2.1.11-50.el7.centos will be an update
---> Package accountsservice.x86_64 0:0.6.45-2.el7 will be updated
---> Package accountsservice.x86_64 0:0.6.45-7.el7 will be an update
---> Package accountsservice-libs.x86_64 0:0.6.45-2.el7 will be updated
---> Package accountsservice-libs.x86_64 0:0.6.45-7.el7 will be an update
---> Package acl.x86_64 0:2.2.51-12.el7 will be updated
---> Package acl.x86_64 0:2.2.51-14.el7 will be an update
---> Package adwaita-cursor-theme.noarch 0:3.22.0-1.el7 will be updated
---> Package adwaita-cursor-theme.noarch 0:3.26.0-1.el7 will be an update
---> Package adwaita-gtk2-theme.x86_64 0:3.22.2-1.el7 will be updated
---> Package adwaita-gtk2-theme.x86_64 0:3.22.2-2.el7_5 will be an update
---> Package adwaita-icon-theme.noarch 0:3.22.0-1.el7 will be updated
---> Package adwaita-icon-theme.noarch 0:3.26.0-1.el7 will be an update
---> Package alsa-lib.x86_64 0:1.1.3-3.el7 will be updated
---> Package alsa-lib.x86_64 0:1.1.4.1-2.el7 will be an update
---> Package anaconda-core.x86_64 0:21.48.22.121-1.el7.centos will be updated
---> Package anaconda-core.x86_64 0:21.48.22.134-1.el7.centos will be an update
---> Package anaconda-gui.x86_64 0:21.48.22.121-1.el7.centos will be updated
---> Package anaconda-gui.x86_64 0:21.48.22.134-1.el7.centos will be an update
---> Package anaconda-tui.x86_64 0:21.48.22.121-1.el7.centos will be updated
---> Package anaconda-tui.x86_64 0:21.48.22.134-1.el7.centos will be an update
---> Package anaconda-widgets.x86_64 0:21.48.22.121-1.el7.centos will be updated
---> Package anaconda-widgets.x86_64 0:21.48.22.134-1.el7.centos will be an update
---> Package at.x86_64 0:3.1.13-22.el7 will be updated
---> Package at.x86_64 0:3.1.13-23.el7 will be an update
---> Package attr.x86_64 0:2.4.46-12.el7 will be updated
---> Package attr.x86_64 0:2.4.46-13.el7 will be an update
---> Package audit.x86_64 0:2.7.6-3.el7 will be updated
---> Package audit.x86_64 0:2.8.1-3.el7 will be an update
---> Package audit-libs.x86_64 0:2.7.6-3.el7 will be updated
---> Package audit-libs.x86_64 0:2.8.1-3.el7 will be an update
---> Package audit-libs-python.x86_64 0:2.7.6-3.el7 will be updated
---> Package audit-libs-python.x86_64 0:2.8.1-3.el7 will be an update
---> Package augeas-libs.x86_64 0:1.4.0-2.el7 will be updated
---> Package augeas-libs.x86_64 0:1.4.0-5.el7_5.1 will be an update
---> Package avahi.x86_64 0:0.6.31-17.el7 will be updated
---> Package avahi.x86_64 0:0.6.31-19.el7 will be an update
---> Package avahi-glib.x86_64 0:0.6.31-17.el7 will be updated
---> Package avahi-glib.x86_64 0:0.6.31-19.el7 will be an update
---> Package avahi-gobject.x86_64 0:0.6.31-17.el7 will be updated
---> Package avahi-gobject.x86_64 0:0.6.31-19.el7 will be an update
---> Package avahi-libs.x86_64 0:0.6.31-17.el7 will be updated
---> Package avahi-libs.x86_64 0:0.6.31-19.el7 will be an update
---> Package avahi-ui-gtk3.x86_64 0:0.6.31-17.el7 will be updated
---> Package avahi-ui-gtk3.x86_64 0:0.6.31-19.el7 will be an update
---> Package bash.x86_64 0:4.2.46-28.el7 will be updated
---> Package bash.x86_64 0:4.2.46-30.el7 will be an update
---> Package bind-libs.x86_64 32:9.9.4-50.el7 will be updated
---> Package bind-libs.x86_64 32:9.9.4-61.el7 will be an update
---> Package bind-libs-lite.x86_64 32:9.9.4-50.el7 will be updated
---> Package bind-libs-lite.x86_64 32:9.9.4-61.el7 will be an update
---> Package bind-license.noarch 32:9.9.4-50.el7 will be updated
---> Package bind-license.noarch 32:9.9.4-61.el7 will be an update
---> Package bind-utils.x86_64 32:9.9.4-50.el7 will be updated
---> Package bind-utils.x86_64 32:9.9.4-61.el7 will be an update
---> Package binutils.x86_64 0:2.25.1-31.base.el7 will be updated
---> Package binutils.x86_64 0:2.27-27.base.el7 will be an update
---> Package biosdevname.x86_64 0:0.7.2-2.el7 will be updated
---> Package biosdevname.x86_64 0:0.7.3-1.el7 will be an update
---> Package bluez.x86_64 0:5.44-2.el7 will be updated
---> Package bluez.x86_64 0:5.44-4.el7_4 will be an update
---> Package brlapi.x86_64 0:0.6.0-15.el7 will be updated
---> Package brlapi.x86_64 0:0.6.0-16.el7 will be an update
---> Package brltty.x86_64 0:4.5-15.el7 will be updated
---> Package brltty.x86_64 0:4.5-16.el7 will be an update
---> Package ca-certificates.noarch 0:2017.2.14-71.el7 will be updated
---> Package ca-certificates.noarch 0:2018.2.22-70.0.el7_5 will be an update
---> Package centos-release.x86_64 0:7-4.1708.el7.centos will be updated
---> Package centos-release.x86_64 0:7-5.1804.el7.centos.2 will be an update
---> Package checkpolicy.x86_64 0:2.5-4.el7 will be updated
---> Package checkpolicy.x86_64 0:2.5-6.el7 will be an update
---> Package cheese.x86_64 2:3.22.1-1.el7 will be updated
---> Package cheese.x86_64 2:3.22.1-2.el7 will be an update
---> Package cheese-libs.x86_64 2:3.22.1-1.el7 will be updated
---> Package cheese-libs.x86_64 2:3.22.1-2.el7 will be an update
---> Package chrony.x86_64 0:3.1-2.el7.centos will be updated
---> Package chrony.x86_64 0:3.2-2.el7 will be an update
---> Package clutter.x86_64 0:1.26.0-1.el7 will be updated
---> Package clutter.x86_64 0:1.26.2-2.el7 will be an update
--> Processing Dependency: libinput(x86-64) >= 0.19.0 for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libinput.so.10(LIBINPUT_0.21.0)(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libinput.so.10(LIBINPUT_0.20.0)(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libinput.so.10(LIBINPUT_0.12.0)(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libwayland-server.so.0()(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libwayland-egl.so.1()(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libwayland-cursor.so.0()(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libwayland-client.so.0()(64bit) for package: clutter-1.26.2-2.el7.x86_64
--> Processing Dependency: libinput.so.10()(64bit) for package: clutter-1.26.2-2.el7.x86_64
---> Package clutter-gtk.x86_64 0:1.8.2-1.el7 will be updated
---> Package clutter-gtk.x86_64 0:1.8.4-1.el7 will be an update
---> Package cogl.x86_64 0:1.22.2-1.el7 will be updated
---> Package cogl.x86_64 0:1.22.2-2.el7 will be an update
---> Package control-center.x86_64 1:3.22.2-5.el7 will be updated
---> Package control-center.x86_64 1:3.26.2-8.el7 will be an update
---> Package control-center-filesystem.x86_64 1:3.22.2-5.el7 will be updated
---> Package control-center-filesystem.x86_64 1:3.26.2-8.el7 will be an update
---> Package copy-jdk-configs.noarch 0:2.2-3.el7 will be updated
---> Package copy-jdk-configs.noarch 0:3.3-10.el7_5 will be an update
---> Package coreutils.x86_64 0:8.22-18.el7 will be updated
---> Package coreutils.x86_64 0:8.22-21.el7 will be an update
---> Package cpio.x86_64 0:2.11-24.el7 will be updated
---> Package cpio.x86_64 0:2.11-27.el7 will be an update
---> Package crash.x86_64 0:7.1.9-2.el7 will be updated
---> Package crash.x86_64 0:7.2.0-6.el7 will be an update
---> Package cronie.x86_64 0:1.4.11-17.el7 will be updated
---> Package cronie.x86_64 0:1.4.11-19.el7 will be an update
---> Package cronie-anacron.x86_64 0:1.4.11-17.el7 will be updated
---> Package cronie-anacron.x86_64 0:1.4.11-19.el7 will be an update
---> Package cryptsetup.x86_64 0:1.7.4-3.el7 will be updated
---> Package cryptsetup.x86_64 0:1.7.4-4.el7 will be an update
---> Package cryptsetup-libs.x86_64 0:1.7.4-3.el7 will be updated
---> Package cryptsetup-libs.x86_64 0:1.7.4-4.el7 will be an update
---> Package cryptsetup-python.x86_64 0:1.7.4-3.el7 will be updated
---> Package cryptsetup-python.x86_64 0:1.7.4-4.el7 will be an update
---> Package cups.x86_64 1:1.6.3-29.el7 will be updated
---> Package cups.x86_64 1:1.6.3-35.el7 will be an update
---> Package cups-client.x86_64 1:1.6.3-29.el7 will be updated
---> Package cups-client.x86_64 1:1.6.3-35.el7 will be an update
---> Package cups-filesystem.noarch 1:1.6.3-29.el7 will be updated
---> Package cups-filesystem.noarch 1:1.6.3-35.el7 will be an update
---> Package cups-libs.x86_64 1:1.6.3-29.el7 will be updated
---> Package cups-libs.x86_64 1:1.6.3-35.el7 will be an update
---> Package curl.x86_64 0:7.29.0-42.el7 will be updated
---> Package curl.x86_64 0:7.29.0-46.el7 will be an update
---> Package cyrus-sasl.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl.x86_64 0:2.1.26-23.el7 will be an update
---> Package cyrus-sasl-gssapi.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl-gssapi.x86_64 0:2.1.26-23.el7 will be an update
---> Package cyrus-sasl-lib.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl-lib.x86_64 0:2.1.26-23.el7 will be an update
---> Package cyrus-sasl-md5.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl-md5.x86_64 0:2.1.26-23.el7 will be an update
---> Package cyrus-sasl-plain.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl-plain.x86_64 0:2.1.26-23.el7 will be an update
---> Package cyrus-sasl-scram.x86_64 0:2.1.26-21.el7 will be updated
---> Package cyrus-sasl-scram.x86_64 0:2.1.26-23.el7 will be an update
---> Package dbus.x86_64 1:1.6.12-17.el7 will be updated
---> Package dbus.x86_64 1:1.10.24-7.el7 will be an update
---> Package dbus-libs.x86_64 1:1.6.12-17.el7 will be updated
---> Package dbus-libs.x86_64 1:1.10.24-7.el7 will be an update
---> Package dbus-x11.x86_64 1:1.6.12-17.el7 will be updated
---> Package dbus-x11.x86_64 1:1.10.24-7.el7 will be an update
---> Package device-mapper.x86_64 7:1.02.140-8.el7 will be updated
---> Package device-mapper.x86_64 7:1.02.146-4.el7 will be an update
---> Package device-mapper-event.x86_64 7:1.02.140-8.el7 will be updated
---> Package device-mapper-event.x86_64 7:1.02.146-4.el7 will be an update
---> Package device-mapper-event-libs.x86_64 7:1.02.140-8.el7 will be updated
---> Package device-mapper-event-libs.x86_64 7:1.02.146-4.el7 will be an update
---> Package device-mapper-libs.x86_64 7:1.02.140-8.el7 will be updated
---> Package device-mapper-libs.x86_64 7:1.02.146-4.el7 will be an update
---> Package device-mapper-multipath.x86_64 0:0.4.9-111.el7 will be updated
---> Package device-mapper-multipath.x86_64 0:0.4.9-119.el7 will be an update
---> Package device-mapper-multipath-libs.x86_64 0:0.4.9-111.el7 will be updated
---> Package device-mapper-multipath-libs.x86_64 0:0.4.9-119.el7 will be an update
---> Package device-mapper-persistent-data.x86_64 0:0.7.0-0.1.rc6.el7 will be updated
---> Package device-mapper-persistent-data.x86_64 0:0.7.3-3.el7 will be an update
---> Package dhclient.x86_64 12:4.2.5-58.el7.centos will be updated
---> Package dhclient.x86_64 12:4.2.5-68.el7.centos.1 will be an update
---> Package dhcp-common.x86_64 12:4.2.5-58.el7.centos will be updated
---> Package dhcp-common.x86_64 12:4.2.5-68.el7.centos.1 will be an update
---> Package dhcp-libs.x86_64 12:4.2.5-58.el7.centos will be updated
---> Package dhcp-libs.x86_64 12:4.2.5-68.el7.centos.1 will be an update
---> Package dleyna-server.x86_64 0:0.5.0-1.el7 will be updated
---> Package dleyna-server.x86_64 0:0.5.0-3.el7 will be an update
---> Package dnsmasq.x86_64 0:2.76-2.el7 will be updated
---> Package dnsmasq.x86_64 0:2.76-5.el7 will be an update
---> Package dracut.x86_64 0:033-502.el7 will be updated
---> Package dracut.x86_64 0:033-535.el7 will be an update
---> Package dracut-config-rescue.x86_64 0:033-502.el7 will be updated
---> Package dracut-config-rescue.x86_64 0:033-535.el7 will be an update
---> Package dracut-network.x86_64 0:033-502.el7 will be updated
---> Package dracut-network.x86_64 0:033-535.el7 will be an update
---> Package e2fsprogs.x86_64 0:1.42.9-10.el7 will be updated
---> Package e2fsprogs.x86_64 0:1.42.9-12.el7_5 will be an update
---> Package e2fsprogs-libs.x86_64 0:1.42.9-10.el7 will be updated
---> Package e2fsprogs-libs.x86_64 0:1.42.9-12.el7_5 will be an update
---> Package ebtables.x86_64 0:2.0.10-15.el7 will be updated
---> Package ebtables.x86_64 0:2.0.10-16.el7 will be an update
---> Package elfutils.x86_64 0:0.168-8.el7 will be updated
---> Package elfutils.x86_64 0:0.170-4.el7 will be an update
---> Package elfutils-default-yama-scope.noarch 0:0.168-8.el7 will be updated
---> Package elfutils-default-yama-scope.noarch 0:0.170-4.el7 will be an update
---> Package elfutils-libelf.x86_64 0:0.168-8.el7 will be updated
---> Package elfutils-libelf.x86_64 0:0.170-4.el7 will be an update
---> Package elfutils-libs.x86_64 0:0.168-8.el7 will be updated
---> Package elfutils-libs.x86_64 0:0.170-4.el7 will be an update
---> Package emacs-filesystem.noarch 1:24.3-19.el7_3 will be updated
---> Package emacs-filesystem.noarch 1:24.3-20.el7_4 will be an update
---> Package ethtool.x86_64 2:4.8-1.el7 will be updated
---> Package ethtool.x86_64 2:4.8-7.el7 will be an update
---> Package evince.x86_64 0:3.22.1-5.el7 will be updated
---> Package evince.x86_64 0:3.22.1-7.el7 will be an update
---> Package evince-libs.x86_64 0:3.22.1-5.el7 will be updated
---> Package evince-libs.x86_64 0:3.22.1-7.el7 will be an update
---> Package evince-nautilus.x86_64 0:3.22.1-5.el7 will be updated
---> Package evince-nautilus.x86_64 0:3.22.1-7.el7 will be an update
---> Package evolution-data-server.x86_64 0:3.22.7-6.el7 will be updated
---> Package evolution-data-server.x86_64 0:3.22.7-8.el7 will be an update
---> Package exiv2-libs.x86_64 0:0.23-6.el7 will be updated
---> Package exiv2-libs.x86_64 0:0.26-3.el7 will be an update
---> Package filesystem.x86_64 0:3.2-21.el7 will be updated
---> Package filesystem.x86_64 0:3.2-25.el7 will be an update
---> Package firefox.x86_64 0:52.2.0-2.el7.centos will be updated
---> Package firefox.x86_64 0:52.8.0-1.el7.centos will be an update
---> Package firewall-config.noarch 0:0.4.4.4-6.el7 will be updated
---> Package firewall-config.noarch 0:0.4.4.4-14.el7 will be an update
---> Package firewalld.noarch 0:0.4.4.4-6.el7 will be updated
---> Package firewalld.noarch 0:0.4.4.4-14.el7 will be an update
---> Package firewalld-filesystem.noarch 0:0.4.4.4-6.el7 will be updated
---> Package firewalld-filesystem.noarch 0:0.4.4.4-14.el7 will be an update
---> Package flatpak.x86_64 0:0.8.7-1.el7 will be updated
---> Package flatpak.x86_64 0:0.8.8-3.el7 will be an update
---> Package flatpak-libs.x86_64 0:0.8.7-1.el7 will be updated
---> Package flatpak-libs.x86_64 0:0.8.8-3.el7 will be an update
---> Package freerdp-libs.x86_64 0:1.0.2-10.el7 will be updated
---> Package freerdp-libs.x86_64 0:1.0.2-15.el7 will be an update
---> Package fuse.x86_64 0:2.9.2-8.el7 will be updated
---> Package fuse.x86_64 0:2.9.2-10.el7 will be an update
---> Package fuse-libs.x86_64 0:2.9.2-8.el7 will be updated
---> Package fuse-libs.x86_64 0:2.9.2-10.el7 will be an update
---> Package gdb.x86_64 0:7.6.1-100.el7 will be updated
---> Package gdb.x86_64 0:7.6.1-110.el7 will be an update
---> Package gdm.x86_64 1:3.22.3-11.el7 will be updated
---> Package gdm.x86_64 1:3.26.2.1-5.el7 will be an update
---> Package ghostscript.x86_64 0:9.07-28.el7 will be updated
---> Package ghostscript.x86_64 0:9.07-28.el7_4.2 will be an update
---> Package ghostscript-cups.x86_64 0:9.07-28.el7 will be updated
---> Package ghostscript-cups.x86_64 0:9.07-28.el7_4.2 will be an update
---> Package gjs.x86_64 0:1.46.0-1.el7 will be updated
---> Package gjs.x86_64 0:1.50.4-4.el7 will be an update
---> Package glib2.x86_64 0:2.50.3-3.el7 will be updated
---> Package glib2.x86_64 0:2.54.2-2.el7 will be an update
---> Package glibc.x86_64 0:2.17-196.el7 will be updated
---> Package glibc.x86_64 0:2.17-222.el7 will be an update
---> Package glibc-common.x86_64 0:2.17-196.el7 will be updated
---> Package glibc-common.x86_64 0:2.17-222.el7 will be an update
---> Package glusterfs.x86_64 0:3.8.4-18.4.el7.centos will be updated
---> Package glusterfs.x86_64 0:3.8.4-53.el7.centos will be an update
---> Package glusterfs-api.x86_64 0:3.8.4-18.4.el7.centos will be updated
---> Package glusterfs-api.x86_64 0:3.8.4-53.el7.centos will be an update
---> Package glusterfs-cli.x86_64 0:3.8.4-18.4.el7.centos will be updated
---> Package glusterfs-cli.x86_64 0:3.8.4-53.el7.centos will be an update
---> Package glusterfs-client-xlators.x86_64 0:3.8.4-18.4.el7.centos will be updated
---> Package glusterfs-client-xlators.x86_64 0:3.8.4-53.el7.centos will be an update
---> Package glusterfs-libs.x86_64 0:3.8.4-18.4.el7.centos will be updated
---> Package glusterfs-libs.x86_64 0:3.8.4-53.el7.centos will be an update
---> Package gnome-classic-session.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-classic-session.noarch 0:3.26.2-3.el7 will be an update
--> Processing Dependency: gnome-shell-extension-top-icons = 3.26.2-3.el7 for package: gnome-classic-session-3.26.2-3.el7.noarch
---> Package gnome-color-manager.x86_64 0:3.22.2-1.el7 will be updated
---> Package gnome-color-manager.x86_64 0:3.22.2-2.el7 will be an update
---> Package gnome-initial-setup.x86_64 0:3.22.1-4.el7 will be updated
---> Package gnome-initial-setup.x86_64 0:3.22.1-5.el7 will be an update
---> Package gnome-online-accounts.x86_64 0:3.22.5-1.el7 will be updated
---> Package gnome-online-accounts.x86_64 0:3.26.2-1.el7 will be an update
---> Package gnome-session.x86_64 0:3.22.3-4.el7 will be updated
---> Package gnome-session.x86_64 0:3.26.1-11.el7 will be an update
---> Package gnome-session-xsession.x86_64 0:3.22.3-4.el7 will be updated
---> Package gnome-session-xsession.x86_64 0:3.26.1-11.el7 will be an update
---> Package gnome-settings-daemon.x86_64 0:3.22.2-5.el7 will be updated
---> Package gnome-settings-daemon.x86_64 0:3.26.2-9.el7 will be an update
---> Package gnome-shell.x86_64 0:3.22.3-17.el7 will be updated
---> Package gnome-shell.x86_64 0:3.26.2-5.el7 will be an update
---> Package gnome-shell-extension-alternate-tab.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-alternate-tab.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-apps-menu.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-apps-menu.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-common.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-common.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-launch-new-instance.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-launch-new-instance.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-places-menu.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-places-menu.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-user-theme.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-user-theme.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-shell-extension-window-list.noarch 0:3.22.2-10.el7 will be updated
---> Package gnome-shell-extension-window-list.noarch 0:3.26.2-3.el7 will be an update
---> Package gnome-software.x86_64 0:3.22.7-1.el7 will be updated
---> Package gnome-software.x86_64 0:3.22.7-5.el7 will be an update
---> Package gnome-system-monitor.x86_64 0:3.22.2-2.el7 will be updated
---> Package gnome-system-monitor.x86_64 0:3.22.2-3.el7 will be an update
---> Package gnome-themes-standard.x86_64 0:3.22.2-1.el7 will be updated
---> Package gnome-themes-standard.x86_64 0:3.22.2-2.el7_5 will be an update
---> Package gnome-tweak-tool.noarch 0:3.22.0-1.el7 will be updated
---> Package gnome-tweak-tool.noarch 0:3.22.0-2.el7_5 will be an update
---> Package gnome-weather.noarch 0:3.20.2-1.el7 will be updated
---> Package gnome-weather.noarch 0:3.26.0-1.el7 will be an update
---> Package gperftools-libs.x86_64 0:2.4-8.el7 will be updated
---> Package gperftools-libs.x86_64 0:2.6.1-1.el7 will be an update
---> Package graphite2.x86_64 0:1.3.6-1.el7_2 will be updated
---> Package graphite2.x86_64 0:1.3.10-1.el7_3 will be an update
---> Package grilo-plugins.x86_64 0:0.3.4-1.el7 will be updated
---> Package grilo-plugins.x86_64 0:0.3.4-3.el7 will be an update
---> Package grub2.x86_64 1:2.02-0.64.el7.centos will be obsoleted
---> Package grub2.x86_64 1:2.02-0.65.el7.centos.2 will be obsoleting
---> Package grub2-common.noarch 1:2.02-0.64.el7.centos will be updated
---> Package grub2-common.noarch 1:2.02-0.65.el7.centos.2 will be an update
---> Package grub2-pc.x86_64 1:2.02-0.64.el7.centos will be updated
---> Package grub2-pc.x86_64 1:2.02-0.65.el7.centos.2 will be an update
---> Package grub2-pc-modules.noarch 1:2.02-0.64.el7.centos will be updated
---> Package grub2-pc-modules.noarch 1:2.02-0.65.el7.centos.2 will be an update
---> Package grub2-tools.x86_64 1:2.02-0.64.el7.centos will be obsoleted
---> Package grub2-tools.x86_64 1:2.02-0.65.el7.centos.2 will be obsoleting
---> Package grub2-tools-extra.x86_64 1:2.02-0.64.el7.centos will be updated
---> Package grub2-tools-extra.x86_64 1:2.02-0.65.el7.centos.2 will be obsoleting
---> Package grub2-tools-minimal.x86_64 1:2.02-0.64.el7.centos will be updated
---> Package grub2-tools-minimal.x86_64 1:2.02-0.65.el7.centos.2 will be obsoleting
---> Package gsettings-desktop-schemas.x86_64 0:3.22.0-1.el7 will be updated
---> Package gsettings-desktop-schemas.x86_64 0:3.24.1-1.el7 will be an update
---> Package gssproxy.x86_64 0:0.7.0-4.el7 will be updated
---> Package gssproxy.x86_64 0:0.7.0-17.el7 will be an update
---> Package gstreamer1-plugins-bad-free.x86_64 0:1.10.4-2.el7 will be updated
---> Package gstreamer1-plugins-bad-free.x86_64 0:1.10.4-3.el7 will be an update
---> Package gtk-update-icon-cache.x86_64 0:3.22.10-4.el7 will be updated
---> Package gtk-update-icon-cache.x86_64 0:3.22.26-4.el7_5 will be an update
---> Package gtk-vnc2.x86_64 0:0.7.0-2.el7 will be updated
---> Package gtk-vnc2.x86_64 0:0.7.0-3.el7 will be an update
---> Package gtk3.x86_64 0:3.22.10-4.el7 will be updated
---> Package gtk3.x86_64 0:3.22.26-4.el7_5 will be an update
---> Package gtk3-immodule-xim.x86_64 0:3.22.10-4.el7 will be updated
---> Package gtk3-immodule-xim.x86_64 0:3.22.26-4.el7_5 will be an update
---> Package gtkmm30.x86_64 0:3.22.0-1.el7 will be updated
---> Package gtkmm30.x86_64 0:3.22.2-1.el7 will be an update
---> Package gvfs.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-afc.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-afc.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-afp.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-afp.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-archive.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-archive.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-client.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-client.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-fuse.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-fuse.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-goa.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-goa.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-gphoto2.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-gphoto2.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-mtp.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-mtp.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvfs-smb.x86_64 0:1.30.4-3.el7 will be updated
---> Package gvfs-smb.x86_64 0:1.30.4-5.el7 will be an update
---> Package gvnc.x86_64 0:0.7.0-2.el7 will be updated
---> Package gvnc.x86_64 0:0.7.0-3.el7 will be an update
---> Package gzip.x86_64 0:1.5-9.el7 will be updated
---> Package gzip.x86_64 0:1.5-10.el7 will be an update
---> Package hwdata.x86_64 0:0.252-8.6.el7 will be updated
---> Package hwdata.x86_64 0:0.252-8.8.el7 will be an update
---> Package hyperv-daemons.x86_64 0:0-0.30.20161211git.el7 will be updated
---> Package hyperv-daemons.x86_64 0:0-0.32.20161211git.el7 will be an update
---> Package hyperv-daemons-license.noarch 0:0-0.30.20161211git.el7 will be updated
---> Package hyperv-daemons-license.noarch 0:0-0.32.20161211git.el7 will be an update
---> Package hypervfcopyd.x86_64 0:0-0.30.20161211git.el7 will be updated
---> Package hypervfcopyd.x86_64 0:0-0.32.20161211git.el7 will be an update
---> Package hypervkvpd.x86_64 0:0-0.30.20161211git.el7 will be updated
---> Package hypervkvpd.x86_64 0:0-0.32.20161211git.el7 will be an update
---> Package hypervvssd.x86_64 0:0-0.30.20161211git.el7 will be updated
---> Package hypervvssd.x86_64 0:0-0.32.20161211git.el7 will be an update
---> Package ibus.x86_64 0:1.5.3-13.el7 will be updated
---> Package ibus.x86_64 0:1.5.17-2.el7 will be an update
---> Package ibus-gtk2.x86_64 0:1.5.3-13.el7 will be updated
---> Package ibus-gtk2.x86_64 0:1.5.17-2.el7 will be an update
---> Package ibus-gtk3.x86_64 0:1.5.3-13.el7 will be updated
---> Package ibus-gtk3.x86_64 0:1.5.17-2.el7 will be an update
---> Package ibus-libs.x86_64 0:1.5.3-13.el7 will be updated
---> Package ibus-libs.x86_64 0:1.5.17-2.el7 will be an update
---> Package ibus-setup.noarch 0:1.5.3-13.el7 will be updated
---> Package ibus-setup.noarch 0:1.5.17-2.el7 will be an update
---> Package icedtea-web.x86_64 0:1.6.2-4.el7 will be updated
---> Package icedtea-web.x86_64 0:1.7.1-1.el7 will be an update
---> Package info.x86_64 0:5.1-4.el7 will be updated
---> Package info.x86_64 0:5.1-5.el7 will be an update
---> Package initial-setup.x86_64 0:0.3.9.40-1.el7.centos will be updated
---> Package initial-setup.x86_64 0:0.3.9.43-1.el7.centos will be an update
---> Package initial-setup-gui.x86_64 0:0.3.9.40-1.el7.centos will be updated
---> Package initial-setup-gui.x86_64 0:0.3.9.43-1.el7.centos will be an update
---> Package initscripts.x86_64 0:9.49.39-1.el7 will be updated
---> Package initscripts.x86_64 0:9.49.41-1.el7 will be an update
---> Package iproute.x86_64 0:3.10.0-87.el7 will be updated
---> Package iproute.x86_64 0:4.11.0-14.el7 will be an update
---> Package iprutils.x86_64 0:2.4.14.1-1.el7 will be updated
---> Package iprutils.x86_64 0:2.4.15.1-1.el7 will be an update
---> Package iptables.x86_64 0:1.4.21-18.0.1.el7.centos will be updated
---> Package iptables.x86_64 0:1.4.21-24.1.el7_5 will be an update
---> Package ipxe-roms-qemu.noarch 0:20170123-1.git4e85b27.el7 will be updated
---> Package ipxe-roms-qemu.noarch 0:20170123-1.git4e85b27.el7_4.1 will be an update
---> Package irqbalance.x86_64 3:1.0.7-10.el7 will be updated
---> Package irqbalance.x86_64 3:1.0.7-11.el7 will be an update
---> Package iscsi-initiator-utils.x86_64 0:6.2.0.874-4.el7 will be updated
---> Package iscsi-initiator-utils.x86_64 0:6.2.0.874-7.el7 will be an update
---> Package iscsi-initiator-utils-iscsiuio.x86_64 0:6.2.0.874-4.el7 will be updated
---> Package iscsi-initiator-utils-iscsiuio.x86_64 0:6.2.0.874-7.el7 will be an update
---> Package iwl100-firmware.noarch 0:39.31.5.1-56.el7 will be updated
---> Package iwl100-firmware.noarch 0:39.31.5.1-62.el7 will be an update
---> Package iwl1000-firmware.noarch 1:39.31.5.1-56.el7 will be updated
---> Package iwl1000-firmware.noarch 1:39.31.5.1-62.el7 will be an update
---> Package iwl105-firmware.noarch 0:18.168.6.1-56.el7 will be updated
---> Package iwl105-firmware.noarch 0:18.168.6.1-62.el7 will be an update
---> Package iwl135-firmware.noarch 0:18.168.6.1-56.el7 will be updated
---> Package iwl135-firmware.noarch 0:18.168.6.1-62.el7 will be an update
---> Package iwl2000-firmware.noarch 0:18.168.6.1-56.el7 will be updated
---> Package iwl2000-firmware.noarch 0:18.168.6.1-62.el7 will be an update
---> Package iwl2030-firmware.noarch 0:18.168.6.1-56.el7 will be updated
---> Package iwl2030-firmware.noarch 0:18.168.6.1-62.el7 will be an update
---> Package iwl3160-firmware.noarch 0:22.0.7.0-56.el7 will be updated
---> Package iwl3160-firmware.noarch 0:22.0.7.0-62.el7 will be an update
---> Package iwl3945-firmware.noarch 0:15.32.2.9-56.el7 will be updated
---> Package iwl3945-firmware.noarch 0:15.32.2.9-62.el7 will be an update
---> Package iwl4965-firmware.noarch 0:228.61.2.24-56.el7 will be updated
---> Package iwl4965-firmware.noarch 0:228.61.2.24-62.el7 will be an update
---> Package iwl5000-firmware.noarch 0:8.83.5.1_1-56.el7 will be updated
---> Package iwl5000-firmware.noarch 0:8.83.5.1_1-62.el7 will be an update
---> Package iwl5150-firmware.noarch 0:8.24.2.2-56.el7 will be updated
---> Package iwl5150-firmware.noarch 0:8.24.2.2-62.el7 will be an update
---> Package iwl6000-firmware.noarch 0:9.221.4.1-56.el7 will be updated
---> Package iwl6000-firmware.noarch 0:9.221.4.1-62.el7 will be an update
---> Package iwl6000g2a-firmware.noarch 0:17.168.5.3-56.el7 will be updated
---> Package iwl6000g2a-firmware.noarch 0:17.168.5.3-62.el7 will be an update
---> Package iwl6000g2b-firmware.noarch 0:17.168.5.2-56.el7 will be updated
---> Package iwl6000g2b-firmware.noarch 0:17.168.5.2-62.el7 will be an update
---> Package iwl6050-firmware.noarch 0:41.28.5.1-56.el7 will be updated
---> Package iwl6050-firmware.noarch 0:41.28.5.1-62.el7 will be an update
---> Package iwl7260-firmware.noarch 0:22.0.7.0-56.el7 will be updated
---> Package iwl7260-firmware.noarch 0:22.0.7.0-62.el7 will be an update
---> Package iwl7265-firmware.noarch 0:22.0.7.0-56.el7 will be updated
---> Package iwl7265-firmware.noarch 0:22.0.7.0-62.el7 will be an update
---> Package java-1.8.0-openjdk.x86_64 1:1.8.0.131-11.b12.el7 will be updated
---> Package java-1.8.0-openjdk.x86_64 1:1.8.0.171-8.b10.el7_5 will be an update
---> Package java-1.8.0-openjdk-headless.x86_64 1:1.8.0.131-11.b12.el7 will be updated
---> Package java-1.8.0-openjdk-headless.x86_64 1:1.8.0.171-8.b10.el7_5 will be an update
---> Package kernel.x86_64 0:3.10.0-862.3.2.el7 will be installed
---> Package kernel-tools.x86_64 0:3.10.0-693.el7 will be updated
---> Package kernel-tools.x86_64 0:3.10.0-862.3.2.el7 will be an update
---> Package kernel-tools-libs.x86_64 0:3.10.0-693.el7 will be updated
---> Package kernel-tools-libs.x86_64 0:3.10.0-862.3.2.el7 will be an update
---> Package kexec-tools.x86_64 0:2.0.14-17.el7 will be updated
---> Package kexec-tools.x86_64 0:2.0.15-13.el7 will be an update
---> Package kmod.x86_64 0:20-15.el7 will be updated
---> Package kmod.x86_64 0:20-21.el7 will be an update
---> Package kmod-libs.x86_64 0:20-15.el7 will be updated
---> Package kmod-libs.x86_64 0:20-21.el7 will be an update
---> Package kpartx.x86_64 0:0.4.9-111.el7 will be updated
---> Package kpartx.x86_64 0:0.4.9-119.el7 will be an update
---> Package kpatch.noarch 0:0.4.0-1.el7 will be updated
---> Package kpatch.noarch 0:0.4.0-3.el7 will be an update
---> Package krb5-libs.x86_64 0:1.15.1-8.el7 will be updated
---> Package krb5-libs.x86_64 0:1.15.1-19.el7 will be an update
---> Package libacl.x86_64 0:2.2.51-12.el7 will be updated
---> Package libacl.x86_64 0:2.2.51-14.el7 will be an update
---> Package libattr.x86_64 0:2.4.46-12.el7 will be updated
---> Package libattr.x86_64 0:2.4.46-13.el7 will be an update
---> Package libbasicobjects.x86_64 0:0.1.1-27.el7 will be updated
---> Package libbasicobjects.x86_64 0:0.1.1-29.el7 will be an update
---> Package libblkid.x86_64 0:2.23.2-43.el7 will be updated
---> Package libblkid.x86_64 0:2.23.2-52.el7 will be an update
---> Package libcgroup.x86_64 0:0.41-13.el7 will be updated
---> Package libcgroup.x86_64 0:0.41-15.el7 will be an update
---> Package libcollection.x86_64 0:0.6.2-27.el7 will be updated
---> Package libcollection.x86_64 0:0.7.0-29.el7 will be an update
---> Package libcom_err.x86_64 0:1.42.9-10.el7 will be updated
---> Package libcom_err.x86_64 0:1.42.9-12.el7_5 will be an update
---> Package libcurl.x86_64 0:7.29.0-42.el7 will be updated
---> Package libcurl.x86_64 0:7.29.0-46.el7 will be an update
---> Package libdb.x86_64 0:5.3.21-20.el7 will be updated
---> Package libdb.x86_64 0:5.3.21-24.el7 will be an update
---> Package libdb-utils.x86_64 0:5.3.21-20.el7 will be updated
---> Package libdb-utils.x86_64 0:5.3.21-24.el7 will be an update
---> Package libdrm.x86_64 0:2.4.74-1.el7 will be updated
---> Package libdrm.x86_64 0:2.4.83-2.el7 will be an update
---> Package libepoxy.x86_64 0:1.3.1-1.el7 will be updated
---> Package libepoxy.x86_64 0:1.3.1-2.el7_5 will be an update
---> Package liberation-fonts-common.noarch 1:1.07.2-15.el7 will be updated
---> Package liberation-fonts-common.noarch 1:1.07.2-16.el7 will be an update
---> Package liberation-mono-fonts.noarch 1:1.07.2-15.el7 will be updated
---> Package liberation-mono-fonts.noarch 1:1.07.2-16.el7 will be an update
---> Package liberation-sans-fonts.noarch 1:1.07.2-15.el7 will be updated
---> Package liberation-sans-fonts.noarch 1:1.07.2-16.el7 will be an update
---> Package liberation-serif-fonts.noarch 1:1.07.2-15.el7 will be updated
---> Package liberation-serif-fonts.noarch 1:1.07.2-16.el7 will be an update
---> Package libgcab1.x86_64 0:0.7-3.el7 will be updated
---> Package libgcab1.x86_64 0:0.7-4.el7_4 will be an update
---> Package libgcc.x86_64 0:4.8.5-16.el7 will be updated
---> Package libgcc.x86_64 0:4.8.5-28.el7_5.1 will be an update
---> Package libgomp.x86_64 0:4.8.5-16.el7 will be updated
---> Package libgomp.x86_64 0:4.8.5-28.el7_5.1 will be an update
---> Package libgovirt.x86_64 0:0.3.3-5.el7 will be updated
---> Package libgovirt.x86_64 0:0.3.3-6.el7 will be an update
---> Package libgphoto2.x86_64 0:2.5.2-5.el7 will be updated
---> Package libgphoto2.x86_64 0:2.5.15-1.el7 will be an update
---> Package libgtop2.x86_64 0:2.34.2-1.el7 will be updated
---> Package libgtop2.x86_64 0:2.34.2-2.el7 will be an update
---> Package libgudev1.x86_64 0:219-42.el7 will be updated
---> Package libgudev1.x86_64 0:219-57.el7 will be an update
---> Package libgweather.x86_64 0:3.20.4-1.el7 will be updated
---> Package libgweather.x86_64 0:3.26.0-1.el7 will be an update
---> Package libibverbs.x86_64 0:13-7.el7 will be updated
---> Package libibverbs.x86_64 0:15-7.el7_5 will be an update
---> Package libini_config.x86_64 0:1.3.0-27.el7 will be updated
---> Package libini_config.x86_64 0:1.3.1-29.el7 will be an update
---> Package libldb.x86_64 0:1.1.29-1.el7 will be updated
---> Package libldb.x86_64 0:1.2.2-1.el7 will be an update
---> Package liblouis.x86_64 0:2.5.2-10.el7 will be updated
---> Package liblouis.x86_64 0:2.5.2-12.el7_4 will be an update
---> Package liblouis-python.noarch 0:2.5.2-10.el7 will be updated
---> Package liblouis-python.noarch 0:2.5.2-12.el7_4 will be an update
---> Package libmbim.x86_64 0:1.14.0-2.el7 will be updated
---> Package libmbim.x86_64 0:1.14.2-1.el7 will be an update
---> Package libmbim-utils.x86_64 0:1.14.0-2.el7 will be updated
---> Package libmbim-utils.x86_64 0:1.14.2-1.el7 will be an update
---> Package libmount.x86_64 0:2.23.2-43.el7 will be updated
---> Package libmount.x86_64 0:2.23.2-52.el7 will be an update
---> Package libmtp.x86_64 0:1.1.6-5.el7 will be updated
---> Package libmtp.x86_64 0:1.1.14-1.el7 will be an update
---> Package libnfsidmap.x86_64 0:0.25-17.el7 will be updated
---> Package libnfsidmap.x86_64 0:0.25-19.el7 will be an update
---> Package libnm-gtk.x86_64 0:1.8.0-3.el7 will be updated
---> Package libnm-gtk.x86_64 0:1.8.6-2.el7 will be an update
---> Package libnma.x86_64 0:1.8.0-3.el7 will be updated
---> Package libnma.x86_64 0:1.8.6-2.el7 will be an update
---> Package libpath_utils.x86_64 0:0.2.1-27.el7 will be updated
---> Package libpath_utils.x86_64 0:0.2.1-29.el7 will be an update
---> Package libpcap.x86_64 14:1.5.3-9.el7 will be updated
---> Package libpcap.x86_64 14:1.5.3-11.el7 will be an update
---> Package libpciaccess.x86_64 0:0.13.4-3.el7_3 will be updated
---> Package libpciaccess.x86_64 0:0.14-1.el7 will be an update
---> Package libproxy.x86_64 0:0.4.11-10.el7 will be updated
---> Package libproxy.x86_64 0:0.4.11-11.el7 will be an update
---> Package libproxy-mozjs.x86_64 0:0.4.11-10.el7 will be updated
---> Package libproxy-mozjs.x86_64 0:0.4.11-11.el7 will be an update
---> Package libpurple.x86_64 0:2.10.11-5.el7 will be updated
---> Package libpurple.x86_64 0:2.10.11-7.el7 will be an update
---> Package libpwquality.x86_64 0:1.2.3-4.el7 will be updated
---> Package libpwquality.x86_64 0:1.2.3-5.el7 will be an update
---> Package libqmi.x86_64 0:1.16.0-1.el7 will be updated
---> Package libqmi.x86_64 0:1.18.0-2.el7 will be an update
---> Package libqmi-utils.x86_64 0:1.16.0-1.el7 will be updated
---> Package libqmi-utils.x86_64 0:1.18.0-2.el7 will be an update
---> Package librdmacm.x86_64 0:13-7.el7 will be updated
---> Package librdmacm.x86_64 0:15-7.el7_5 will be an update
---> Package libref_array.x86_64 0:0.1.5-27.el7 will be updated
---> Package libref_array.x86_64 0:0.1.5-29.el7 will be an update
---> Package libreport.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-anaconda.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-anaconda.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-centos.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-centos.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-cli.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-cli.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-filesystem.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-filesystem.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-gtk.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-gtk.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-bugzilla.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-bugzilla.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-mailx.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-mailx.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-mantisbt.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-mantisbt.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-reportuploader.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-reportuploader.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-rhtsupport.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-rhtsupport.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-plugin-ureport.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-plugin-ureport.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-python.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-python.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-rhel-anaconda-bugzilla.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-rhel-anaconda-bugzilla.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreport-web.x86_64 0:2.1.11-38.el7.centos will be updated
---> Package libreport-web.x86_64 0:2.1.11-40.el7.centos will be an update
---> Package libreswan.x86_64 0:3.20-3.el7 will be updated
---> Package libreswan.x86_64 0:3.23-3.el7 will be an update
--> Processing Dependency: libunbound.so.2()(64bit) for package: libreswan-3.23-3.el7.x86_64
--> Processing Dependency: libldns.so.1()(64bit) for package: libreswan-3.23-3.el7.x86_64
---> Package libselinux.x86_64 0:2.5-11.el7 will be updated
---> Package libselinux.x86_64 0:2.5-12.el7 will be an update
---> Package libselinux-python.x86_64 0:2.5-11.el7 will be updated
---> Package libselinux-python.x86_64 0:2.5-12.el7 will be an update
---> Package libselinux-utils.x86_64 0:2.5-11.el7 will be updated
---> Package libselinux-utils.x86_64 0:2.5-12.el7 will be an update
---> Package libsemanage.x86_64 0:2.5-8.el7 will be updated
---> Package libsemanage.x86_64 0:2.5-11.el7 will be an update
---> Package libsemanage-python.x86_64 0:2.5-8.el7 will be updated
---> Package libsemanage-python.x86_64 0:2.5-11.el7 will be an update
---> Package libsepol.x86_64 0:2.5-6.el7 will be updated
---> Package libsepol.x86_64 0:2.5-8.1.el7 will be an update
---> Package libsmbclient.x86_64 0:4.6.2-8.el7 will be updated
---> Package libsmbclient.x86_64 0:4.7.1-6.el7 will be an update
---> Package libsoup.x86_64 0:2.56.0-3.el7 will be updated
---> Package libsoup.x86_64 0:2.56.0-6.el7 will be an update
---> Package libss.x86_64 0:1.42.9-10.el7 will be updated
---> Package libss.x86_64 0:1.42.9-12.el7_5 will be an update
---> Package libsss_idmap.x86_64 0:1.15.2-50.el7 will be updated
---> Package libsss_idmap.x86_64 0:1.16.0-19.el7 will be an update
---> Package libsss_nss_idmap.x86_64 0:1.15.2-50.el7 will be updated
---> Package libsss_nss_idmap.x86_64 0:1.16.0-19.el7 will be an update
---> Package libstdc++.x86_64 0:4.8.5-16.el7 will be updated
---> Package libstdc++.x86_64 0:4.8.5-28.el7_5.1 will be an update
---> Package libstoragemgmt.x86_64 0:1.4.0-3.el7 will be updated
---> Package libstoragemgmt.x86_64 0:1.6.1-2.el7 will be an update
---> Package libstoragemgmt-python.noarch 0:1.4.0-3.el7 will be updated
---> Package libstoragemgmt-python.noarch 0:1.6.1-2.el7 will be an update
---> Package libstoragemgmt-python-clibs.x86_64 0:1.4.0-3.el7 will be updated
---> Package libstoragemgmt-python-clibs.x86_64 0:1.6.1-2.el7 will be an update
---> Package libtalloc.x86_64 0:2.1.9-1.el7 will be updated
---> Package libtalloc.x86_64 0:2.1.10-1.el7 will be an update
---> Package libtdb.x86_64 0:1.3.12-2.el7 will be updated
---> Package libtdb.x86_64 0:1.3.15-1.el7 will be an update
---> Package libteam.x86_64 0:1.25-5.el7 will be updated
---> Package libteam.x86_64 0:1.27-4.el7 will be an update
---> Package libtevent.x86_64 0:0.9.31-1.el7 will be updated
---> Package libtevent.x86_64 0:0.9.33-2.el7 will be an update
---> Package libudisks2.x86_64 0:2.1.2-6.el7 will be updated
---> Package libudisks2.x86_64 0:2.7.3-6.el7 will be an update
---> Package libusbx.x86_64 0:1.0.20-1.el7 will be updated
---> Package libusbx.x86_64 0:1.0.21-1.el7 will be an update
---> Package libuser.x86_64 0:0.60-7.el7_1 will be updated
---> Package libuser.x86_64 0:0.60-9.el7 will be an update
---> Package libuser-python.x86_64 0:0.60-7.el7_1 will be updated
---> Package libuser-python.x86_64 0:0.60-9.el7 will be an update
---> Package libuuid.x86_64 0:2.23.2-43.el7 will be updated
---> Package libuuid.x86_64 0:2.23.2-52.el7 will be an update
---> Package libvirt-daemon.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-config-network.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-config-network.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-interface.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-interface.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-network.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-network.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-nodedev.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-nodedev.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-nwfilter.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-nwfilter.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-qemu.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-qemu.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-secret.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-secret.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-core.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-core.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-disk.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-disk.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-gluster.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-gluster.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-iscsi.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-iscsi.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-logical.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-logical.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-mpath.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-mpath.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-rbd.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-rbd.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-driver-storage-scsi.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-driver-storage-scsi.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-daemon-kvm.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-daemon-kvm.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvirt-libs.x86_64 0:3.2.0-14.el7 will be updated
---> Package libvirt-libs.x86_64 0:3.9.0-14.el7_5.5 will be an update
---> Package libvorbis.x86_64 1:1.3.3-8.el7 will be updated
---> Package libvorbis.x86_64 1:1.3.3-8.el7.1 will be an update
---> Package libwacom.x86_64 0:0.24-1.el7 will be updated
---> Package libwacom.x86_64 0:0.24-3.el7 will be an update
---> Package libwacom-data.noarch 0:0.24-1.el7 will be updated
---> Package libwacom-data.noarch 0:0.24-3.el7 will be an update
---> Package libwbclient.x86_64 0:4.6.2-8.el7 will be updated
---> Package libwbclient.x86_64 0:4.7.1-6.el7 will be an update
---> Package linux-firmware.noarch 0:20170606-56.gitc990aae.el7 will be updated
---> Package linux-firmware.noarch 0:20180220-62.git6d51311.el7 will be an update
---> Package logrotate.x86_64 0:3.8.6-14.el7 will be updated
---> Package logrotate.x86_64 0:3.8.6-15.el7 will be an update
---> Package lsof.x86_64 0:4.87-4.el7 will be updated
---> Package lsof.x86_64 0:4.87-5.el7 will be an update
---> Package lvm2.x86_64 7:2.02.171-8.el7 will be updated
---> Package lvm2.x86_64 7:2.02.177-4.el7 will be an update
---> Package lvm2-libs.x86_64 7:2.02.171-8.el7 will be updated
---> Package lvm2-libs.x86_64 7:2.02.177-4.el7 will be an update
---> Package m17n-db.noarch 0:1.6.4-3.el7 will be updated
---> Package m17n-db.noarch 0:1.6.4-4.el7 will be an update
---> Package mailx.x86_64 0:12.5-16.el7 will be updated
---> Package mailx.x86_64 0:12.5-19.el7 will be an update
---> Package man-pages-overrides.x86_64 0:7.4.3-1.el7 will be updated
---> Package man-pages-overrides.x86_64 0:7.5.2-1.el7 will be an update
---> Package mcelog.x86_64 3:144-3.94d853b2ea81.el7 will be updated
---> Package mcelog.x86_64 3:144-8.94d853b2ea81.el7 will be an update
---> Package mdadm.x86_64 0:4.0-5.el7 will be updated
---> Package mdadm.x86_64 0:4.0-13.el7 will be an update
---> Package mesa-dri-drivers.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-dri-drivers.x86_64 0:17.2.3-8.20171019.el7 will be an update
--> Processing Dependency: libLLVM-5.0-rhel.so(LLVM_5.0)(64bit) for package: mesa-dri-drivers-17.2.3-8.20171019.el7.x86_64
--> Processing Dependency: libLLVM-5.0-rhel.so()(64bit) for package: mesa-dri-drivers-17.2.3-8.20171019.el7.x86_64
---> Package mesa-filesystem.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-filesystem.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libEGL.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libEGL.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libGL.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libGL.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libGLES.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libGLES.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libgbm.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libgbm.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libglapi.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libglapi.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package mesa-libxatracker.x86_64 0:17.0.1-6.20170307.el7 will be updated
---> Package mesa-libxatracker.x86_64 0:17.2.3-8.20171019.el7 will be an update
---> Package microcode_ctl.x86_64 2:2.1-22.el7 will be updated
---> Package microcode_ctl.x86_64 2:2.1-29.2.el7_5 will be an update
---> Package mlocate.x86_64 0:0.26-6.el7 will be updated
---> Package mlocate.x86_64 0:0.26-8.el7 will be an update
---> Package mozjs17.x86_64 0:17.0.0-19.el7 will be updated
---> Package mozjs17.x86_64 0:17.0.0-20.el7 will be an update
---> Package mutter.x86_64 0:3.22.3-11.el7 will be updated
---> Package mutter.x86_64 0:3.26.2-13.el7 will be an update
---> Package nautilus.x86_64 0:3.22.3-3.el7 will be updated
---> Package nautilus.x86_64 0:3.22.3-5.el7 will be an update
---> Package nautilus-extensions.x86_64 0:3.22.3-3.el7 will be updated
---> Package nautilus-extensions.x86_64 0:3.22.3-5.el7 will be an update
---> Package ncurses.x86_64 0:5.9-13.20130511.el7 will be updated
---> Package ncurses.x86_64 0:5.9-14.20130511.el7_4 will be an update
---> Package ncurses-base.noarch 0:5.9-13.20130511.el7 will be updated
---> Package ncurses-base.noarch 0:5.9-14.20130511.el7_4 will be an update
---> Package ncurses-libs.x86_64 0:5.9-13.20130511.el7 will be updated
---> Package ncurses-libs.x86_64 0:5.9-14.20130511.el7_4 will be an update
---> Package net-snmp-libs.x86_64 1:5.7.2-28.el7 will be updated
---> Package net-snmp-libs.x86_64 1:5.7.2-33.el7_5.2 will be an update
---> Package nfs-utils.x86_64 1:1.3.0-0.48.el7 will be updated
---> Package nfs-utils.x86_64 1:1.3.0-0.54.el7 will be an update
---> Package nm-connection-editor.x86_64 0:1.8.0-3.el7 will be updated
---> Package nm-connection-editor.x86_64 0:1.8.6-2.el7 will be an update
---> Package nmap-ncat.x86_64 2:6.40-7.el7 will be updated
---> Package nmap-ncat.x86_64 2:6.40-13.el7 will be an update
---> Package nspr.x86_64 0:4.13.1-1.0.el7_3 will be updated
---> Package nspr.x86_64 0:4.19.0-1.el7_5 will be an update
---> Package nss.x86_64 0:3.28.4-8.el7 will be updated
---> Package nss.x86_64 0:3.36.0-5.el7_5 will be an update
---> Package nss-softokn.x86_64 0:3.28.3-6.el7 will be updated
---> Package nss-softokn.x86_64 0:3.36.0-5.el7_5 will be an update
---> Package nss-softokn-freebl.x86_64 0:3.28.3-6.el7 will be updated
---> Package nss-softokn-freebl.x86_64 0:3.36.0-5.el7_5 will be an update
---> Package nss-sysinit.x86_64 0:3.28.4-8.el7 will be updated
---> Package nss-sysinit.x86_64 0:3.36.0-5.el7_5 will be an update
---> Package nss-tools.x86_64 0:3.28.4-8.el7 will be updated
---> Package nss-tools.x86_64 0:3.36.0-5.el7_5 will be an update
---> Package nss-util.x86_64 0:3.28.4-3.el7 will be updated
---> Package nss-util.x86_64 0:3.36.0-1.el7_5 will be an update
---> Package ntpdate.x86_64 0:4.2.6p5-25.el7.centos.2 will be updated
---> Package ntpdate.x86_64 0:4.2.6p5-28.el7.centos will be an update
---> Package numactl-libs.x86_64 0:2.0.9-6.el7_2 will be updated
---> Package numactl-libs.x86_64 0:2.0.9-7.el7 will be an update
---> Package numad.x86_64 0:0.5-17.20150602git.el7 will be updated
---> Package numad.x86_64 0:0.5-18.20150602git.el7 will be an update
---> Package open-vm-tools.x86_64 0:10.1.5-3.el7 will be updated
---> Package open-vm-tools.x86_64 0:10.1.10-3.el7 will be an update
---> Package open-vm-tools-desktop.x86_64 0:10.1.5-3.el7 will be updated
---> Package open-vm-tools-desktop.x86_64 0:10.1.10-3.el7 will be an update
---> Package openldap.x86_64 0:2.4.44-5.el7 will be updated
---> Package openldap.x86_64 0:2.4.44-15.el7_5 will be an update
---> Package openssh.x86_64 0:7.4p1-11.el7 will be updated
---> Package openssh.x86_64 0:7.4p1-16.el7 will be an update
---> Package openssh-clients.x86_64 0:7.4p1-11.el7 will be updated
---> Package openssh-clients.x86_64 0:7.4p1-16.el7 will be an update
---> Package openssh-server.x86_64 0:7.4p1-11.el7 will be updated
---> Package openssh-server.x86_64 0:7.4p1-16.el7 will be an update
---> Package openssl.x86_64 1:1.0.2k-8.el7 will be updated
---> Package openssl.x86_64 1:1.0.2k-12.el7 will be an update
---> Package openssl-libs.x86_64 1:1.0.2k-8.el7 will be updated
---> Package openssl-libs.x86_64 1:1.0.2k-12.el7 will be an update
---> Package osinfo-db.noarch 0:20170423-2.el7 will be updated
---> Package osinfo-db.noarch 0:20170813-6.el7 will be an update
---> Package pam.x86_64 0:1.1.8-18.el7 will be updated
---> Package pam.x86_64 0:1.1.8-22.el7 will be an update
---> Package parted.x86_64 0:3.1-28.el7 will be updated
---> Package parted.x86_64 0:3.1-29.el7 will be an update
---> Package pciutils.x86_64 0:3.5.1-2.el7 will be updated
---> Package pciutils.x86_64 0:3.5.1-3.el7 will be an update
---> Package pciutils-libs.x86_64 0:3.5.1-2.el7 will be updated
---> Package pciutils-libs.x86_64 0:3.5.1-3.el7 will be an update
---> Package perl-Getopt-Long.noarch 0:2.40-2.el7 will be updated
---> Package perl-Getopt-Long.noarch 0:2.40-3.el7 will be an update
---> Package plymouth.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-core-libs.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-core-libs.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-graphics-libs.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-graphics-libs.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-plugin-label.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-plugin-label.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-plugin-two-step.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-plugin-two-step.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-scripts.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-scripts.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-system-theme.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-system-theme.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package plymouth-theme-charge.x86_64 0:0.8.9-0.28.20140113.el7.centos will be updated
---> Package plymouth-theme-charge.x86_64 0:0.8.9-0.31.20140113.el7.centos will be an update
---> Package policycoreutils.x86_64 0:2.5-17.1.el7 will be updated
---> Package policycoreutils.x86_64 0:2.5-22.el7 will be an update
---> Package policycoreutils-python.x86_64 0:2.5-17.1.el7 will be updated
---> Package policycoreutils-python.x86_64 0:2.5-22.el7 will be an update
---> Package polkit.x86_64 0:0.112-12.el7_3 will be updated
---> Package polkit.x86_64 0:0.112-14.el7 will be an update
---> Package poppler.x86_64 0:0.26.5-16.el7 will be updated
---> Package poppler.x86_64 0:0.26.5-17.el7_4 will be an update
---> Package poppler-glib.x86_64 0:0.26.5-16.el7 will be updated
---> Package poppler-glib.x86_64 0:0.26.5-17.el7_4 will be an update
---> Package poppler-utils.x86_64 0:0.26.5-16.el7 will be updated
---> Package poppler-utils.x86_64 0:0.26.5-17.el7_4 will be an update
---> Package procps-ng.x86_64 0:3.3.10-16.el7 will be updated
---> Package procps-ng.x86_64 0:3.3.10-17.el7_5.2 will be an update
---> Package pulseaudio.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-gdm-hooks.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-gdm-hooks.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-libs.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-libs.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-libs-glib2.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-libs-glib2.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-module-bluetooth.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-module-bluetooth.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-module-x11.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-module-x11.x86_64 0:10.0-5.el7 will be an update
---> Package pulseaudio-utils.x86_64 0:10.0-3.el7 will be updated
---> Package pulseaudio-utils.x86_64 0:10.0-5.el7 will be an update
---> Package pykickstart.noarch 0:1.99.66.12-1.el7 will be updated
---> Package pykickstart.noarch 0:1.99.66.18-1.el7 will be an update
---> Package pyparted.x86_64 1:3.9-13.el7 will be updated
---> Package pyparted.x86_64 1:3.9-15.el7 will be an update
---> Package python.x86_64 0:2.7.5-58.el7 will be updated
---> Package python.x86_64 0:2.7.5-68.el7 will be an update
---> Package python-backports-ssl_match_hostname.noarch 0:3.4.0.2-4.el7 will be updated
---> Package python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7 will be an update
--> Processing Dependency: python-ipaddress for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
---> Package python-blivet.noarch 1:0.61.15.65-1.el7 will be updated
---> Package python-blivet.noarch 1:0.61.15.69-1.el7 will be an update
---> Package python-brlapi.x86_64 0:0.6.0-15.el7 will be updated
---> Package python-brlapi.x86_64 0:0.6.0-16.el7 will be an update
---> Package python-dmidecode.x86_64 0:3.12.2-1.el7 will be updated
---> Package python-dmidecode.x86_64 0:3.12.2-2.el7 will be an update
---> Package python-firewall.noarch 0:0.4.4.4-6.el7 will be updated
---> Package python-firewall.noarch 0:0.4.4.4-14.el7 will be an update
---> Package python-gobject.x86_64 0:3.22.0-1.el7 will be updated
---> Package python-gobject.x86_64 0:3.22.0-1.el7_4.1 will be an update
---> Package python-gobject-base.x86_64 0:3.22.0-1.el7 will be updated
---> Package python-gobject-base.x86_64 0:3.22.0-1.el7_4.1 will be an update
---> Package python-libs.x86_64 0:2.7.5-58.el7 will be updated
---> Package python-libs.x86_64 0:2.7.5-68.el7 will be an update
---> Package python-perf.x86_64 0:3.10.0-693.el7 will be updated
---> Package python-perf.x86_64 0:3.10.0-862.3.2.el7 will be an update
---> Package python-pwquality.x86_64 0:1.2.3-4.el7 will be updated
---> Package python-pwquality.x86_64 0:1.2.3-5.el7 will be an update
---> Package python-slip.noarch 0:0.4.0-2.el7 will be updated
---> Package python-slip.noarch 0:0.4.0-4.el7 will be an update
---> Package python-slip-dbus.noarch 0:0.4.0-2.el7 will be updated
---> Package python-slip-dbus.noarch 0:0.4.0-4.el7 will be an update
---> Package python-smbc.x86_64 0:1.0.13-7.el7 will be updated
---> Package python-smbc.x86_64 0:1.0.13-8.el7 will be an update
---> Package qemu-img.x86_64 10:1.5.3-141.el7 will be updated
---> Package qemu-img.x86_64 10:1.5.3-156.el7_5.2 will be an update
---> Package qemu-kvm.x86_64 10:1.5.3-141.el7 will be updated
---> Package qemu-kvm.x86_64 10:1.5.3-156.el7_5.2 will be an update
---> Package qemu-kvm-common.x86_64 10:1.5.3-141.el7 will be updated
---> Package qemu-kvm-common.x86_64 10:1.5.3-156.el7_5.2 will be an update
---> Package quota.x86_64 1:4.01-14.el7 will be updated
---> Package quota.x86_64 1:4.01-17.el7 will be an update
---> Package quota-nls.noarch 1:4.01-14.el7 will be updated
---> Package quota-nls.noarch 1:4.01-17.el7 will be an update
---> Package radvd.x86_64 0:1.9.2-9.el7 will be updated
---> Package radvd.x86_64 0:1.9.2-9.el7_5.4 will be an update
---> Package rasdaemon.x86_64 0:0.4.1-28.el7 will be updated
---> Package rasdaemon.x86_64 0:0.4.1-33.1.el7_5 will be an update
---> Package rdma-core.x86_64 0:13-7.el7 will be updated
---> Package rdma-core.x86_64 0:15-7.el7_5 will be an update
---> Package rest.x86_64 0:0.8.0-1.el7 will be updated
---> Package rest.x86_64 0:0.8.0-2.el7 will be an update
---> Package rng-tools.x86_64 0:5-11.el7 will be updated
---> Package rng-tools.x86_64 0:5-13.el7 will be an update
---> Package rpcbind.x86_64 0:0.2.0-42.el7 will be updated
---> Package rpcbind.x86_64 0:0.2.0-44.el7 will be an update
---> Package rpm.x86_64 0:4.11.3-25.el7 will be updated
---> Package rpm.x86_64 0:4.11.3-32.el7 will be an update
---> Package rpm-build-libs.x86_64 0:4.11.3-25.el7 will be updated
---> Package rpm-build-libs.x86_64 0:4.11.3-32.el7 will be an update
---> Package rpm-libs.x86_64 0:4.11.3-25.el7 will be updated
---> Package rpm-libs.x86_64 0:4.11.3-32.el7 will be an update
---> Package rpm-python.x86_64 0:4.11.3-25.el7 will be updated
---> Package rpm-python.x86_64 0:4.11.3-32.el7 will be an update
---> Package rsync.x86_64 0:3.0.9-18.el7 will be updated
---> Package rsync.x86_64 0:3.1.2-4.el7 will be an update
---> Package rsyslog.x86_64 0:8.24.0-12.el7 will be updated
---> Package rsyslog.x86_64 0:8.24.0-16.el7_5.4 will be an update
---> Package samba-client-libs.x86_64 0:4.6.2-8.el7 will be updated
---> Package samba-client-libs.x86_64 0:4.7.1-6.el7 will be an update
--> Processing Dependency: libaesni-intel-samba4.so(SAMBA_4.7.1)(64bit) for package: samba-client-libs-4.7.1-6.el7.x86_64
--> Processing Dependency: libaesni-intel-samba4.so()(64bit) for package: samba-client-libs-4.7.1-6.el7.x86_64
---> Package samba-common.noarch 0:4.6.2-8.el7 will be updated
---> Package samba-common.noarch 0:4.7.1-6.el7 will be an update
---> Package sane-backends.x86_64 0:1.0.24-9.el7 will be updated
---> Package sane-backends.x86_64 0:1.0.24-11.el7 will be an update
---> Package sane-backends-drivers-scanners.x86_64 0:1.0.24-9.el7 will be updated
---> Package sane-backends-drivers-scanners.x86_64 0:1.0.24-11.el7 will be an update
---> Package sane-backends-libs.x86_64 0:1.0.24-9.el7 will be updated
---> Package sane-backends-libs.x86_64 0:1.0.24-11.el7 will be an update
---> Package scl-utils.x86_64 0:20130529-17.el7_1 will be updated
---> Package scl-utils.x86_64 0:20130529-18.el7_4 will be an update
---> Package seabios-bin.noarch 0:1.10.2-3.el7 will be updated
---> Package seabios-bin.noarch 0:1.11.0-2.el7 will be an update
---> Package seavgabios-bin.noarch 0:1.10.2-3.el7 will be updated
---> Package seavgabios-bin.noarch 0:1.11.0-2.el7 will be an update
---> Package selinux-policy.noarch 0:3.13.1-166.el7 will be updated
---> Package selinux-policy.noarch 0:3.13.1-192.el7_5.3 will be an update
---> Package selinux-policy-targeted.noarch 0:3.13.1-166.el7 will be updated
---> Package selinux-policy-targeted.noarch 0:3.13.1-192.el7_5.3 will be an update
---> Package setools-libs.x86_64 0:3.3.8-1.1.el7 will be updated
---> Package setools-libs.x86_64 0:3.3.8-2.el7 will be an update
---> Package setroubleshoot.x86_64 0:3.2.28-3.el7 will be updated
---> Package setroubleshoot.x86_64 0:3.2.29-3.el7 will be an update
---> Package setroubleshoot-plugins.noarch 0:3.0.65-1.el7 will be updated
---> Package setroubleshoot-plugins.noarch 0:3.0.66-2.1.el7 will be an update
---> Package setroubleshoot-server.x86_64 0:3.2.28-3.el7 will be updated
---> Package setroubleshoot-server.x86_64 0:3.2.29-3.el7 will be an update
---> Package setup.noarch 0:2.8.71-7.el7 will be updated
---> Package setup.noarch 0:2.8.71-9.el7 will be an update
---> Package shared-mime-info.x86_64 0:1.8-3.el7 will be updated
---> Package shared-mime-info.x86_64 0:1.8-4.el7 will be an update
---> Package smartmontools.x86_64 1:6.2-8.el7 will be updated
---> Package smartmontools.x86_64 1:6.5-1.el7 will be an update
---> Package sos.noarch 0:3.4-6.el7.centos will be updated
---> Package sos.noarch 0:3.5-7.el7.centos will be an update
---> Package spice-glib.x86_64 0:0.33-6.el7 will be updated
---> Package spice-glib.x86_64 0:0.34-3.el7 will be an update
--> Processing Dependency: liblz4.so.1()(64bit) for package: spice-glib-0.34-3.el7.x86_64
---> Package spice-gtk3.x86_64 0:0.33-6.el7 will be updated
---> Package spice-gtk3.x86_64 0:0.34-3.el7 will be an update
---> Package spice-server.x86_64 0:0.12.8-2.el7 will be updated
---> Package spice-server.x86_64 0:0.14.0-2.el7_5.3 will be an update
---> Package spice-vdagent.x86_64 0:0.14.0-14.el7 will be updated
---> Package spice-vdagent.x86_64 0:0.14.0-15.el7 will be an update
---> Package sssd-client.x86_64 0:1.15.2-50.el7 will be updated
---> Package sssd-client.x86_64 0:1.16.0-19.el7 will be an update
---> Package strace.x86_64 0:4.12-4.el7 will be updated
---> Package strace.x86_64 0:4.12-6.el7 will be an update
---> Package sudo.x86_64 0:1.8.19p2-10.el7 will be updated
---> Package sudo.x86_64 0:1.8.19p2-13.el7 will be an update
---> Package sysstat.x86_64 0:10.1.5-12.el7 will be updated
---> Package sysstat.x86_64 0:10.1.5-13.el7 will be an update
---> Package system-config-printer.x86_64 0:1.4.1-19.el7 will be updated
---> Package system-config-printer.x86_64 0:1.4.1-21.el7 will be an update
---> Package system-config-printer-libs.noarch 0:1.4.1-19.el7 will be updated
---> Package system-config-printer-libs.noarch 0:1.4.1-21.el7 will be an update
---> Package system-config-printer-udev.x86_64 0:1.4.1-19.el7 will be updated
---> Package system-config-printer-udev.x86_64 0:1.4.1-21.el7 will be an update
---> Package systemd.x86_64 0:219-42.el7 will be updated
---> Package systemd.x86_64 0:219-57.el7 will be an update
---> Package systemd-libs.x86_64 0:219-42.el7 will be updated
---> Package systemd-libs.x86_64 0:219-57.el7 will be an update
---> Package systemd-python.x86_64 0:219-42.el7 will be updated
---> Package systemd-python.x86_64 0:219-57.el7 will be an update
---> Package systemd-sysv.x86_64 0:219-42.el7 will be updated
---> Package systemd-sysv.x86_64 0:219-57.el7 will be an update
---> Package systemtap-runtime.x86_64 0:3.1-3.el7 will be updated
---> Package systemtap-runtime.x86_64 0:3.2-4.el7 will be an update
---> Package tar.x86_64 2:1.26-32.el7 will be updated
---> Package tar.x86_64 2:1.26-34.el7 will be an update
---> Package tcpdump.x86_64 14:4.9.0-5.el7 will be updated
---> Package tcpdump.x86_64 14:4.9.2-3.el7 will be an update
---> Package teamd.x86_64 0:1.25-5.el7 will be updated
---> Package teamd.x86_64 0:1.27-4.el7 will be an update
---> Package telepathy-glib.x86_64 0:0.24.0-1.el7 will be updated
---> Package telepathy-glib.x86_64 0:0.24.1-1.el7 will be an update
---> Package tigervnc-license.noarch 0:1.8.0-1.el7 will be updated
---> Package tigervnc-license.noarch 0:1.8.0-5.el7 will be an update
---> Package tigervnc-server-minimal.x86_64 0:1.8.0-1.el7 will be updated
---> Package tigervnc-server-minimal.x86_64 0:1.8.0-5.el7 will be an update
---> Package tracker.x86_64 0:1.10.5-4.el7 will be updated
---> Package tracker.x86_64 0:1.10.5-6.el7 will be an update
---> Package tuned.noarch 0:2.8.0-5.el7 will be updated
---> Package tuned.noarch 0:2.9.0-1.el7 will be an update
---> Package tzdata.noarch 0:2017b-1.el7 will be updated
---> Package tzdata.noarch 0:2018e-3.el7 will be an update
---> Package tzdata-java.noarch 0:2017b-1.el7 will be updated
---> Package tzdata-java.noarch 0:2018e-3.el7 will be an update
---> Package udisks2.x86_64 0:2.1.2-6.el7 will be updated
---> Package udisks2.x86_64 0:2.7.3-6.el7 will be an update
--> Processing Dependency: libblockdev-swap >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev-part >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev-mdraid >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev-loop >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev-fs >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev-crypto >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev >= 2.10 for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libblockdev.so.2()(64bit) for package: udisks2-2.7.3-6.el7.x86_64
--> Processing Dependency: libbd_utils.so.2()(64bit) for package: udisks2-2.7.3-6.el7.x86_64
---> Package unzip.x86_64 0:6.0-16.el7 will be updated
---> Package unzip.x86_64 0:6.0-19.el7 will be an update
---> Package usb_modeswitch.x86_64 0:2.4.0-5.el7 will be updated
---> Package usb_modeswitch.x86_64 0:2.5.1-1.el7 will be an update
---> Package usb_modeswitch-data.noarch 0:20160612-2.el7 will be updated
---> Package usb_modeswitch-data.noarch 0:20170806-1.el7 will be an update
---> Package usbredir.x86_64 0:0.7.1-2.el7 will be updated
---> Package usbredir.x86_64 0:0.7.1-3.el7 will be an update
---> Package util-linux.x86_64 0:2.23.2-43.el7 will be updated
---> Package util-linux.x86_64 0:2.23.2-52.el7 will be an update
---> Package vim-common.x86_64 2:7.4.160-2.el7 will be updated
---> Package vim-common.x86_64 2:7.4.160-4.el7 will be an update
---> Package vim-enhanced.x86_64 2:7.4.160-2.el7 will be updated
---> Package vim-enhanced.x86_64 2:7.4.160-4.el7 will be an update
---> Package vim-filesystem.x86_64 2:7.4.160-2.el7 will be updated
---> Package vim-filesystem.x86_64 2:7.4.160-4.el7 will be an update
---> Package vim-minimal.x86_64 2:7.4.160-2.el7 will be updated
---> Package vim-minimal.x86_64 2:7.4.160-4.el7 will be an update
---> Package vinagre.x86_64 0:3.22.0-8.el7 will be updated
---> Package vinagre.x86_64 0:3.22.0-9.el7 will be an update
---> Package virt-what.x86_64 0:1.13-10.el7 will be updated
---> Package virt-what.x86_64 0:1.18-4.el7 will be an update
---> Package webkitgtk4.x86_64 0:2.14.7-2.el7 will be updated
---> Package webkitgtk4.x86_64 0:2.16.6-6.el7 will be an update
---> Package webkitgtk4-jsc.x86_64 0:2.14.7-2.el7 will be updated
---> Package webkitgtk4-jsc.x86_64 0:2.16.6-6.el7 will be an update
---> Package webkitgtk4-plugin-process-gtk2.x86_64 0:2.14.7-2.el7 will be updated
---> Package webkitgtk4-plugin-process-gtk2.x86_64 0:2.16.6-6.el7 will be an update
---> Package wget.x86_64 0:1.14-15.el7 will be updated
---> Package wget.x86_64 0:1.14-15.el7_4.1 will be an update
---> Package wpa_supplicant.x86_64 1:2.6-5.el7 will be updated
---> Package wpa_supplicant.x86_64 1:2.6-9.el7 will be an update
---> Package xdg-user-dirs.x86_64 0:0.15-4.el7 will be updated
---> Package xdg-user-dirs.x86_64 0:0.15-5.el7 will be an update
---> Package xfsdump.x86_64 0:3.1.4-1.el7 will be updated
---> Package xfsdump.x86_64 0:3.1.7-1.el7 will be an update
---> Package xfsprogs.x86_64 0:4.5.0-12.el7 will be updated
---> Package xfsprogs.x86_64 0:4.5.0-15.el7 will be an update
---> Package xmlsec1.x86_64 0:1.2.20-5.el7 will be updated
---> Package xmlsec1.x86_64 0:1.2.20-7.el7_4 will be an update
---> Package xmlsec1-openssl.x86_64 0:1.2.20-5.el7 will be updated
---> Package xmlsec1-openssl.x86_64 0:1.2.20-7.el7_4 will be an update
---> Package xorg-x11-drv-ati.x86_64 0:7.7.1-3.20160928git3fc839ff.el7 will be updated
---> Package xorg-x11-drv-ati.x86_64 0:7.10.0-1.el7 will be an update
---> Package xorg-x11-drv-intel.x86_64 0:2.99.917-26.20160929.el7 will be updated
---> Package xorg-x11-drv-intel.x86_64 0:2.99.917-27.20160929.el7 will be an update
---> Package xorg-x11-drv-wacom.x86_64 0:0.34.2-2.el7 will be updated
---> Package xorg-x11-drv-wacom.x86_64 0:0.34.2-4.el7 will be an update
---> Package xorg-x11-server-Xorg.x86_64 0:1.19.3-11.el7 will be updated
---> Package xorg-x11-server-Xorg.x86_64 0:1.19.5-5.el7 will be an update
---> Package xorg-x11-server-common.x86_64 0:1.19.3-11.el7 will be updated
---> Package xorg-x11-server-common.x86_64 0:1.19.5-5.el7 will be an update
---> Package xorg-x11-xinit.x86_64 0:1.3.4-1.el7 will be updated
---> Package xorg-x11-xinit.x86_64 0:1.3.4-2.el7 will be an update
--> Running transaction check
---> Package gnome-shell-extension-top-icons.noarch 0:3.26.2-3.el7 will be installed
---> Package ldns.x86_64 0:1.6.16-10.el7 will be installed
---> Package libblockdev.x86_64 0:2.12-3.el7 will be installed
---> Package libblockdev-crypto.x86_64 0:2.12-3.el7 will be installed
--> Processing Dependency: libvolume_key.so.1()(64bit) for package: libblockdev-crypto-2.12-3.el7.x86_64
---> Package libblockdev-fs.x86_64 0:2.12-3.el7 will be installed
---> Package libblockdev-loop.x86_64 0:2.12-3.el7 will be installed
---> Package libblockdev-mdraid.x86_64 0:2.12-3.el7 will be installed
--> Processing Dependency: libbytesize.so.1()(64bit) for package: libblockdev-mdraid-2.12-3.el7.x86_64
---> Package libblockdev-part.x86_64 0:2.12-3.el7 will be installed
---> Package libblockdev-swap.x86_64 0:2.12-3.el7 will be installed
---> Package libblockdev-utils.x86_64 0:2.12-3.el7 will be installed
---> Package libinput.x86_64 0:1.8.4-2.el7 will be installed
---> Package libwayland-client.x86_64 0:1.14.0-2.el7 will be installed
---> Package libwayland-cursor.x86_64 0:1.14.0-2.el7 will be installed
---> Package libwayland-server.x86_64 0:1.14.0-2.el7 will be installed
---> Package llvm-private.x86_64 0:5.0.0-3.el7 will be installed
---> Package lz4.x86_64 0:1.7.5-2.el7 will be installed
---> Package mesa-libwayland-egl.x86_64 0:17.2.3-8.20171019.el7 will be installed
---> Package python-ipaddress.noarch 0:1.0.16-2.el7 will be installed
---> Package samba-common-libs.x86_64 0:4.7.1-6.el7 will be installed
---> Package unbound-libs.x86_64 0:1.6.6-1.el7 will be installed
--> Running transaction check
---> Package libbytesize.x86_64 0:1.2-1.el7 will be installed
---> Package volume_key-libs.x86_64 0:0.3.9-8.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved
======================================================================================
 Package                               Arch   Version                   Repository
                                                                                 Size
======================================================================================
Installing:
 grub2                                 x86_64 1:2.02-0.65.el7.centos.2  base     29 k
     replacing  grub2.x86_64 1:2.02-0.64.el7.centos
 grub2-tools                           x86_64 1:2.02-0.65.el7.centos.2  base    1.8 M
     replacing  grub2-tools.x86_64 1:2.02-0.64.el7.centos
 grub2-tools-extra                     x86_64 1:2.02-0.65.el7.centos.2  base    993 k
     replacing  grub2-tools.x86_64 1:2.02-0.64.el7.centos
 grub2-tools-minimal                   x86_64 1:2.02-0.65.el7.centos.2  base    170 k
     replacing  grub2-tools.x86_64 1:2.02-0.64.el7.centos
 kernel                                x86_64 3.10.0-862.3.2.el7        updates  46 M
Updating:
 ModemManager                          x86_64 1.6.10-1.el7              base    735 k
 ModemManager-glib                     x86_64 1.6.10-1.el7              base    231 k
 NetworkManager                        x86_64 1:1.10.2-14.el7_5         updates 1.7 M
 NetworkManager-adsl                   x86_64 1:1.10.2-14.el7_5         updates 158 k
 NetworkManager-glib                   x86_64 1:1.10.2-14.el7_5         updates 1.2 M
 NetworkManager-libnm                  x86_64 1:1.10.2-14.el7_5         updates 1.3 M
 NetworkManager-ppp                    x86_64 1:1.10.2-14.el7_5         updates 163 k
 NetworkManager-team                   x86_64 1:1.10.2-14.el7_5         updates 161 k
 NetworkManager-tui                    x86_64 1:1.10.2-14.el7_5         updates 235 k
 NetworkManager-wifi                   x86_64 1:1.10.2-14.el7_5         updates 191 k
 PackageKit                            x86_64 1.1.5-2.el7.centos        updates 583 k
 PackageKit-command-not-found          x86_64 1.1.5-2.el7.centos        updates  21 k
 PackageKit-glib                       x86_64 1.1.5-2.el7.centos        updates 127 k
 PackageKit-gstreamer-plugin           x86_64 1.1.5-2.el7.centos        updates  12 k
 PackageKit-gtk3-module                x86_64 1.1.5-2.el7.centos        updates  12 k
 PackageKit-yum                        x86_64 1.1.5-2.el7.centos        updates  75 k
 abrt                                  x86_64 2.1.11-50.el7.centos      base    536 k
 abrt-addon-ccpp                       x86_64 2.1.11-50.el7.centos      base    192 k
 abrt-addon-kerneloops                 x86_64 2.1.11-50.el7.centos      base    105 k
 abrt-addon-pstoreoops                 x86_64 2.1.11-50.el7.centos      base     96 k
 abrt-addon-python                     x86_64 2.1.11-50.el7.centos      base    102 k
 abrt-addon-vmcore                     x86_64 2.1.11-50.el7.centos      base    106 k
 abrt-addon-xorg                       x86_64 2.1.11-50.el7.centos      base     97 k
 abrt-cli                              x86_64 2.1.11-50.el7.centos      base     87 k
 abrt-console-notification             x86_64 2.1.11-50.el7.centos      base     88 k
 abrt-dbus                             x86_64 2.1.11-50.el7.centos      base    121 k
 abrt-desktop                          x86_64 2.1.11-50.el7.centos      base     87 k
 abrt-gui                              x86_64 2.1.11-50.el7.centos      base    190 k
 abrt-gui-libs                         x86_64 2.1.11-50.el7.centos      base     95 k
 abrt-libs                             x86_64 2.1.11-50.el7.centos      base    109 k
 abrt-python                           x86_64 2.1.11-50.el7.centos      base    109 k
 abrt-retrace-client                   x86_64 2.1.11-50.el7.centos      base    122 k
 abrt-tui                              x86_64 2.1.11-50.el7.centos      base     99 k
 accountsservice                       x86_64 0.6.45-7.el7              base     95 k
 accountsservice-libs                  x86_64 0.6.45-7.el7              base     78 k
 acl                                   x86_64 2.2.51-14.el7             base     81 k
 adwaita-cursor-theme                  noarch 3.26.0-1.el7              base    641 k
 adwaita-gtk2-theme                    x86_64 3.22.2-2.el7_5            updates 128 k
 adwaita-icon-theme                    noarch 3.26.0-1.el7              base     12 M
 alsa-lib                              x86_64 1.1.4.1-2.el7             base    422 k
 anaconda-core                         x86_64 21.48.22.134-1.el7.centos base    1.6 M
 anaconda-gui                          x86_64 21.48.22.134-1.el7.centos base    500 k
 anaconda-tui                          x86_64 21.48.22.134-1.el7.centos base    283 k
 anaconda-widgets                      x86_64 21.48.22.134-1.el7.centos base    215 k
 at                                    x86_64 3.1.13-23.el7             base     51 k
 attr                                  x86_64 2.4.46-13.el7             base     66 k
 audit                                 x86_64 2.8.1-3.el7               base    247 k
 audit-libs                            x86_64 2.8.1-3.el7               base     99 k
 audit-libs-python                     x86_64 2.8.1-3.el7               base     75 k
 augeas-libs                           x86_64 1.4.0-5.el7_5.1           updates 355 k
 avahi                                 x86_64 0.6.31-19.el7             base    264 k
 avahi-glib                            x86_64 0.6.31-19.el7             base     25 k
 avahi-gobject                         x86_64 0.6.31-19.el7             base     35 k
 avahi-libs                            x86_64 0.6.31-19.el7             base     61 k
 avahi-ui-gtk3                         x86_64 0.6.31-19.el7             base     37 k
 bash                                  x86_64 4.2.46-30.el7             base    1.0 M
 bind-libs                             x86_64 32:9.9.4-61.el7           base    1.0 M
 bind-libs-lite                        x86_64 32:9.9.4-61.el7           base    734 k
 bind-license                          noarch 32:9.9.4-61.el7           base     85 k
 bind-utils                            x86_64 32:9.9.4-61.el7           base    204 k
 binutils                              x86_64 2.27-27.base.el7          base    5.9 M
 biosdevname                           x86_64 0.7.3-1.el7               base     38 k
 bluez                                 x86_64 5.44-4.el7_4              base    1.2 M
 brlapi                                x86_64 0.6.0-16.el7              base    114 k
 brltty                                x86_64 4.5-16.el7                base    933 k
 ca-certificates                       noarch 2018.2.22-70.0.el7_5      updates 392 k
 centos-release                        x86_64 7-5.1804.el7.centos.2     updates  24 k
 checkpolicy                           x86_64 2.5-6.el7                 base    294 k
 cheese                                x86_64 2:3.22.1-2.el7            base    160 k
 cheese-libs                           x86_64 2:3.22.1-2.el7            base    1.1 M
 chrony                                x86_64 3.2-2.el7                 base    243 k
 clutter                               x86_64 1.26.2-2.el7              base    1.1 M
 clutter-gtk                           x86_64 1.8.4-1.el7               base     44 k
 cogl                                  x86_64 1.22.2-2.el7              base    462 k
 control-center                        x86_64 1:3.26.2-8.el7            base    4.5 M
 control-center-filesystem             x86_64 1:3.26.2-8.el7            base     24 k
 copy-jdk-configs                      noarch 3.3-10.el7_5              updates  21 k
 coreutils                             x86_64 8.22-21.el7               base    3.3 M
 cpio                                  x86_64 2.11-27.el7               base    211 k
 crash                                 x86_64 7.2.0-6.el7               base    2.6 M
 cronie                                x86_64 1.4.11-19.el7             base     91 k
 cronie-anacron                        x86_64 1.4.11-19.el7             base     35 k
 cryptsetup                            x86_64 1.7.4-4.el7               base    128 k
 cryptsetup-libs                       x86_64 1.7.4-4.el7               base    223 k
 cryptsetup-python                     x86_64 1.7.4-4.el7               base     35 k
 cups                                  x86_64 1:1.6.3-35.el7            base    1.3 M
 cups-client                           x86_64 1:1.6.3-35.el7            base    151 k
 cups-filesystem                       noarch 1:1.6.3-35.el7            base     96 k
 cups-libs                             x86_64 1:1.6.3-35.el7            base    357 k
 curl                                  x86_64 7.29.0-46.el7             base    268 k
 cyrus-sasl                            x86_64 2.1.26-23.el7             base     88 k
 cyrus-sasl-gssapi                     x86_64 2.1.26-23.el7             base     41 k
 cyrus-sasl-lib                        x86_64 2.1.26-23.el7             base    155 k
 cyrus-sasl-md5                        x86_64 2.1.26-23.el7             base     57 k
 cyrus-sasl-plain                      x86_64 2.1.26-23.el7             base     39 k
 cyrus-sasl-scram                      x86_64 2.1.26-23.el7             base     43 k
 dbus                                  x86_64 1:1.10.24-7.el7           base    245 k
 dbus-libs                             x86_64 1:1.10.24-7.el7           base    169 k
 dbus-x11                              x86_64 1:1.10.24-7.el7           base     47 k
 device-mapper                         x86_64 7:1.02.146-4.el7          base    289 k
 device-mapper-event                   x86_64 7:1.02.146-4.el7          base    185 k
 device-mapper-event-libs              x86_64 7:1.02.146-4.el7          base    184 k
 device-mapper-libs                    x86_64 7:1.02.146-4.el7          base    316 k
 device-mapper-multipath               x86_64 0.4.9-119.el7             base    137 k
 device-mapper-multipath-libs          x86_64 0.4.9-119.el7             base    257 k
 device-mapper-persistent-data         x86_64 0.7.3-3.el7               base    405 k
 dhclient                              x86_64 12:4.2.5-68.el7.centos.1  updates 284 k
 dhcp-common                           x86_64 12:4.2.5-68.el7.centos.1  updates 175 k
 dhcp-libs                             x86_64 12:4.2.5-68.el7.centos.1  updates 131 k
 dleyna-server                         x86_64 0.5.0-3.el7               base     72 k
 dnsmasq                               x86_64 2.76-5.el7                base    277 k
 dracut                                x86_64 033-535.el7               base    325 k
 dracut-config-rescue                  x86_64 033-535.el7               base     58 k
 dracut-network                        x86_64 033-535.el7               base    100 k
 e2fsprogs                             x86_64 1.42.9-12.el7_5           updates 699 k
 e2fsprogs-libs                        x86_64 1.42.9-12.el7_5           updates 167 k
 ebtables                              x86_64 2.0.10-16.el7             base    123 k
 elfutils                              x86_64 0.170-4.el7               base    282 k
 elfutils-default-yama-scope           noarch 0.170-4.el7               base     31 k
 elfutils-libelf                       x86_64 0.170-4.el7               base    195 k
 elfutils-libs                         x86_64 0.170-4.el7               base    267 k
 emacs-filesystem                      noarch 1:24.3-20.el7_4           base     58 k
 ethtool                               x86_64 2:4.8-7.el7               base    125 k
 evince                                x86_64 3.22.1-7.el7              base    2.5 M
 evince-libs                           x86_64 3.22.1-7.el7              base    358 k
 evince-nautilus                       x86_64 3.22.1-7.el7              base     40 k
 evolution-data-server                 x86_64 3.22.7-8.el7              base    3.1 M
 exiv2-libs                            x86_64 0.26-3.el7                base    823 k
 filesystem                            x86_64 3.2-25.el7                base    1.0 M
 firefox                               x86_64 52.8.0-1.el7.centos       updates  83 M
 firewall-config                       noarch 0.4.4.4-14.el7            base    135 k
 firewalld                             noarch 0.4.4.4-14.el7            base    418 k
 firewalld-filesystem                  noarch 0.4.4.4-14.el7            base     49 k
 flatpak                               x86_64 0.8.8-3.el7               base    712 k
 flatpak-libs                          x86_64 0.8.8-3.el7               base    424 k
 freerdp-libs                          x86_64 1.0.2-15.el7              base    224 k
 fuse                                  x86_64 2.9.2-10.el7              base     86 k
 fuse-libs                             x86_64 2.9.2-10.el7              base     93 k
 gdb                                   x86_64 7.6.1-110.el7             base    2.4 M
 gdm                                   x86_64 1:3.26.2.1-5.el7          base    518 k
 ghostscript                           x86_64 9.07-28.el7_4.2           base    4.3 M
 ghostscript-cups                      x86_64 9.07-28.el7_4.2           base     56 k
 gjs                                   x86_64 1.50.4-4.el7              base    6.9 M
 glib2                                 x86_64 2.54.2-2.el7              base    2.4 M
 glibc                                 x86_64 2.17-222.el7              base    3.6 M
 glibc-common                          x86_64 2.17-222.el7              base     11 M
 glusterfs                             x86_64 3.8.4-53.el7.centos       base    529 k
 glusterfs-api                         x86_64 3.8.4-53.el7.centos       base     75 k
 glusterfs-cli                         x86_64 3.8.4-53.el7.centos       base    176 k
 glusterfs-client-xlators              x86_64 3.8.4-53.el7.centos       base    789 k
 glusterfs-libs                        x86_64 3.8.4-53.el7.centos       base    370 k
 gnome-classic-session                 noarch 3.26.2-3.el7              base     39 k
 gnome-color-manager                   x86_64 3.22.2-2.el7              base    1.5 M
 gnome-initial-setup                   x86_64 3.22.1-5.el7              base    1.3 M
 gnome-online-accounts                 x86_64 3.26.2-1.el7              base    1.0 M
 gnome-session                         x86_64 3.26.1-11.el7             base    403 k
 gnome-session-xsession                x86_64 3.26.1-11.el7             base     11 k
 gnome-settings-daemon                 x86_64 3.26.2-9.el7              base    1.0 M
 gnome-shell                           x86_64 3.26.2-5.el7              base    2.0 M
 gnome-shell-extension-alternate-tab   noarch 3.26.2-3.el7              base     19 k
 gnome-shell-extension-apps-menu       noarch 3.26.2-3.el7              base     24 k
 gnome-shell-extension-common          noarch 3.26.2-3.el7              base    146 k
 gnome-shell-extension-launch-new-instance
                                       noarch 3.26.2-3.el7              base     18 k
 gnome-shell-extension-places-menu     noarch 3.26.2-3.el7              base     22 k
 gnome-shell-extension-user-theme      noarch 3.26.2-3.el7              base     19 k
 gnome-shell-extension-window-list     noarch 3.26.2-3.el7              base     28 k
 gnome-software                        x86_64 3.22.7-5.el7              base    3.4 M
 gnome-system-monitor                  x86_64 3.22.2-3.el7              base    650 k
 gnome-themes-standard                 x86_64 3.22.2-2.el7_5            updates 2.8 M
 gnome-tweak-tool                      noarch 3.22.0-2.el7_5            updates 274 k
 gnome-weather                         noarch 3.26.0-1.el7              base    5.0 M
 gperftools-libs                       x86_64 2.6.1-1.el7               base    272 k
 graphite2                             x86_64 1.3.10-1.el7_3            base    115 k
 grilo-plugins                         x86_64 0.3.4-3.el7               base    952 k
 grub2-common                          noarch 1:2.02-0.65.el7.centos.2  base    726 k
 grub2-pc                              x86_64 1:2.02-0.65.el7.centos.2  base     29 k
 grub2-pc-modules                      noarch 1:2.02-0.65.el7.centos.2  base    845 k
 gsettings-desktop-schemas             x86_64 3.24.1-1.el7              base    586 k
 gssproxy                              x86_64 0.7.0-17.el7              base    108 k
 gstreamer1-plugins-bad-free           x86_64 1.10.4-3.el7              base    1.7 M
 gtk-update-icon-cache                 x86_64 3.22.26-4.el7_5           updates  27 k
 gtk-vnc2                              x86_64 0.7.0-3.el7               base     41 k
 gtk3                                  x86_64 3.22.26-4.el7_5           updates 4.4 M
 gtk3-immodule-xim                     x86_64 3.22.26-4.el7_5           updates  16 k
 gtkmm30                               x86_64 3.22.2-1.el7              base    925 k
 gvfs                                  x86_64 1.30.4-5.el7              base    352 k
 gvfs-afc                              x86_64 1.30.4-5.el7              base     73 k
 gvfs-afp                              x86_64 1.30.4-5.el7              base     87 k
 gvfs-archive                          x86_64 1.30.4-5.el7              base     41 k
 gvfs-client                           x86_64 1.30.4-5.el7              base    909 k
 gvfs-fuse                             x86_64 1.30.4-5.el7              base     45 k
 gvfs-goa                              x86_64 1.30.4-5.el7              base     77 k
 gvfs-gphoto2                          x86_64 1.30.4-5.el7              base     77 k
 gvfs-mtp                              x86_64 1.30.4-5.el7              base     77 k
 gvfs-smb                              x86_64 1.30.4-5.el7              base     60 k
 gvnc                                  x86_64 0.7.0-3.el7               base     94 k
 gzip                                  x86_64 1.5-10.el7                base    130 k
 hwdata                                x86_64 0.252-8.8.el7             base    2.3 M
 hyperv-daemons                        x86_64 0-0.32.20161211git.el7    base    5.0 k
 hyperv-daemons-license                noarch 0-0.32.20161211git.el7    base     12 k
 hypervfcopyd                          x86_64 0-0.32.20161211git.el7    base     11 k
 hypervkvpd                            x86_64 0-0.32.20161211git.el7    base     19 k
 hypervvssd                            x86_64 0-0.32.20161211git.el7    base     12 k
 ibus                                  x86_64 1.5.17-2.el7              base    4.8 M
 ibus-gtk2                             x86_64 1.5.17-2.el7              base     43 k
 ibus-gtk3                             x86_64 1.5.17-2.el7              base     44 k
 ibus-libs                             x86_64 1.5.17-2.el7              base    227 k
 ibus-setup                            noarch 1.5.17-2.el7              base     79 k
 icedtea-web                           x86_64 1.7.1-1.el7               base    1.7 M
 info                                  x86_64 5.1-5.el7                 base    233 k
 initial-setup                         x86_64 0.3.9.43-1.el7.centos     base     90 k
 initial-setup-gui                     x86_64 0.3.9.43-1.el7.centos     base     28 k
 initscripts                           x86_64 9.49.41-1.el7             base    437 k
 iproute                               x86_64 4.11.0-14.el7             base    763 k
 iprutils                              x86_64 2.4.15.1-1.el7            base    243 k
 iptables                              x86_64 1.4.21-24.1.el7_5         updates 432 k
 ipxe-roms-qemu                        noarch 20170123-1.git4e85b27.el7_4.1
                                                                        base    759 k
 irqbalance                            x86_64 3:1.0.7-11.el7            base     45 k
 iscsi-initiator-utils                 x86_64 6.2.0.874-7.el7           base    422 k
 iscsi-initiator-utils-iscsiuio        x86_64 6.2.0.874-7.el7           base     90 k
 iwl100-firmware                       noarch 39.31.5.1-62.el7          base    155 k
 iwl1000-firmware                      noarch 1:39.31.5.1-62.el7        base    218 k
 iwl105-firmware                       noarch 18.168.6.1-62.el7         base    239 k
 iwl135-firmware                       noarch 18.168.6.1-62.el7         base    248 k
 iwl2000-firmware                      noarch 18.168.6.1-62.el7         base    241 k
 iwl2030-firmware                      noarch 18.168.6.1-62.el7         base    250 k
 iwl3160-firmware                      noarch 22.0.7.0-62.el7           base    1.6 M
 iwl3945-firmware                      noarch 15.32.2.9-62.el7          base     93 k
 iwl4965-firmware                      noarch 228.61.2.24-62.el7        base    106 k
 iwl5000-firmware                      noarch 8.83.5.1_1-62.el7         base    299 k
 iwl5150-firmware                      noarch 8.24.2.2-62.el7           base    151 k
 iwl6000-firmware                      noarch 9.221.4.1-62.el7          base    172 k
 iwl6000g2a-firmware                   noarch 17.168.5.3-62.el7         base    314 k
 iwl6000g2b-firmware                   noarch 17.168.5.2-62.el7         base    315 k
 iwl6050-firmware                      noarch 41.28.5.1-62.el7          base    247 k
 iwl7260-firmware                      noarch 22.0.7.0-62.el7           base    1.1 M
 iwl7265-firmware                      noarch 22.0.7.0-62.el7           base    5.5 M
 java-1.8.0-openjdk                    x86_64 1:1.8.0.171-8.b10.el7_5   updates 246 k
 java-1.8.0-openjdk-headless           x86_64 1:1.8.0.171-8.b10.el7_5   updates  32 M
 kernel-tools                          x86_64 3.10.0-862.3.2.el7        updates 6.2 M
 kernel-tools-libs                     x86_64 3.10.0-862.3.2.el7        updates 6.2 M
 kexec-tools                           x86_64 2.0.15-13.el7             base    341 k
 kmod                                  x86_64 20-21.el7                 base    121 k
 kmod-libs                             x86_64 20-21.el7                 base     50 k
 kpartx                                x86_64 0.4.9-119.el7             base     75 k
 kpatch                                noarch 0.4.0-3.el7               base     10 k
 krb5-libs                             x86_64 1.15.1-19.el7             updates 747 k
 libacl                                x86_64 2.2.51-14.el7             base     27 k
 libattr                               x86_64 2.4.46-13.el7             base     18 k
 libbasicobjects                       x86_64 0.1.1-29.el7              base     25 k
 libblkid                              x86_64 2.23.2-52.el7             base    178 k
 libcgroup                             x86_64 0.41-15.el7               base     65 k
 libcollection                         x86_64 0.7.0-29.el7              base     41 k
 libcom_err                            x86_64 1.42.9-12.el7_5           updates  41 k
 libcurl                               x86_64 7.29.0-46.el7             base    220 k
 libdb                                 x86_64 5.3.21-24.el7             base    720 k
 libdb-utils                           x86_64 5.3.21-24.el7             base    132 k
 libdrm                                x86_64 2.4.83-2.el7              base    151 k
 libepoxy                              x86_64 1.3.1-2.el7_5             updates 196 k
 liberation-fonts-common               noarch 1:1.07.2-16.el7           base     27 k
 liberation-mono-fonts                 noarch 1:1.07.2-16.el7           base    227 k
 liberation-sans-fonts                 noarch 1:1.07.2-16.el7           base    279 k
 liberation-serif-fonts                noarch 1:1.07.2-16.el7           base    298 k
 libgcab1                              x86_64 0.7-4.el7_4               base     66 k
 libgcc                                x86_64 4.8.5-28.el7_5.1          updates 101 k
 libgomp                               x86_64 4.8.5-28.el7_5.1          updates 156 k
 libgovirt                             x86_64 0.3.3-6.el7               base     70 k
 libgphoto2                            x86_64 2.5.15-1.el7              base    1.4 M
 libgtop2                              x86_64 2.34.2-2.el7              base    133 k
 libgudev1                             x86_64 219-57.el7                base     92 k
 libgweather                           x86_64 3.26.0-1.el7              base    3.0 M
 libibverbs                            x86_64 15-7.el7_5                updates 224 k
 libini_config                         x86_64 1.3.1-29.el7              base     63 k
 libldb                                x86_64 1.2.2-1.el7               base    131 k
 liblouis                              x86_64 2.5.2-12.el7_4            base    1.2 M
 liblouis-python                       noarch 2.5.2-12.el7_4            base     12 k
 libmbim                               x86_64 1.14.2-1.el7              base    101 k
 libmbim-utils                         x86_64 1.14.2-1.el7              base     35 k
 libmount                              x86_64 2.23.2-52.el7             base    180 k
 libmtp                                x86_64 1.1.14-1.el7              base    174 k
 libnfsidmap                           x86_64 0.25-19.el7               base     50 k
 libnm-gtk                             x86_64 1.8.6-2.el7               base     91 k
 libnma                                x86_64 1.8.6-2.el7               base     98 k
 libpath_utils                         x86_64 0.2.1-29.el7              base     28 k
 libpcap                               x86_64 14:1.5.3-11.el7           base    138 k
 libpciaccess                          x86_64 0.14-1.el7                base     26 k
 libproxy                              x86_64 0.4.11-11.el7             base     64 k
 libproxy-mozjs                        x86_64 0.4.11-11.el7             base     17 k
 libpurple                             x86_64 2.10.11-7.el7             base    5.4 M
 libpwquality                          x86_64 1.2.3-5.el7               base     85 k
 libqmi                                x86_64 1.18.0-2.el7              base    928 k
 libqmi-utils                          x86_64 1.18.0-2.el7              base     96 k
 librdmacm                             x86_64 15-7.el7_5                updates  61 k
 libref_array                          x86_64 0.1.5-29.el7              base     26 k
 libreport                             x86_64 2.1.11-40.el7.centos      base    451 k
 libreport-anaconda                    x86_64 2.1.11-40.el7.centos      base     49 k
 libreport-centos                      x86_64 2.1.11-40.el7.centos      base     50 k
 libreport-cli                         x86_64 2.1.11-40.el7.centos      base     51 k
 libreport-filesystem                  x86_64 2.1.11-40.el7.centos      base     39 k
 libreport-gtk                         x86_64 2.1.11-40.el7.centos      base    100 k
 libreport-plugin-bugzilla             x86_64 2.1.11-40.el7.centos      base     88 k
 libreport-plugin-mailx                x86_64 2.1.11-40.el7.centos      base     65 k
 libreport-plugin-mantisbt             x86_64 2.1.11-40.el7.centos      base     71 k
 libreport-plugin-reportuploader       x86_64 2.1.11-40.el7.centos      base     63 k
 libreport-plugin-rhtsupport           x86_64 2.1.11-40.el7.centos      base     77 k
 libreport-plugin-ureport              x86_64 2.1.11-40.el7.centos      base     57 k
 libreport-python                      x86_64 2.1.11-40.el7.centos      base     69 k
 libreport-rhel-anaconda-bugzilla      x86_64 2.1.11-40.el7.centos      base     41 k
 libreport-web                         x86_64 2.1.11-40.el7.centos      base     56 k
 libreswan                             x86_64 3.23-3.el7                base    1.3 M
 libselinux                            x86_64 2.5-12.el7                base    162 k
 libselinux-python                     x86_64 2.5-12.el7                base    235 k
 libselinux-utils                      x86_64 2.5-12.el7                base    151 k
 libsemanage                           x86_64 2.5-11.el7                base    150 k
 libsemanage-python                    x86_64 2.5-11.el7                base    112 k
 libsepol                              x86_64 2.5-8.1.el7               base    297 k
 libsmbclient                          x86_64 4.7.1-6.el7               base    132 k
 libsoup                               x86_64 2.56.0-6.el7              base    398 k
 libss                                 x86_64 1.42.9-12.el7_5           updates  45 k
 libsss_idmap                          x86_64 1.16.0-19.el7             base    141 k
 libsss_nss_idmap                      x86_64 1.16.0-19.el7             base    147 k
 libstdc++                             x86_64 4.8.5-28.el7_5.1          updates 303 k
 libstoragemgmt                        x86_64 1.6.1-2.el7               base    240 k
 libstoragemgmt-python                 noarch 1.6.1-2.el7               base    155 k
 libstoragemgmt-python-clibs           x86_64 1.6.1-2.el7               base     18 k
 libtalloc                             x86_64 2.1.10-1.el7              base     33 k
 libtdb                                x86_64 1.3.15-1.el7              base     48 k
 libteam                               x86_64 1.27-4.el7                base     47 k
 libtevent                             x86_64 0.9.33-2.el7              base     37 k
 libudisks2                            x86_64 2.7.3-6.el7               base    126 k
 libusbx                               x86_64 1.0.21-1.el7              base     61 k
 libuser                               x86_64 0.60-9.el7                base    400 k
 libuser-python                        x86_64 0.60-9.el7                base     52 k
 libuuid                               x86_64 2.23.2-52.el7             base     81 k
 libvirt-daemon                        x86_64 3.9.0-14.el7_5.5          updates 851 k
 libvirt-daemon-config-network         x86_64 3.9.0-14.el7_5.5          updates 175 k
 libvirt-daemon-driver-interface       x86_64 3.9.0-14.el7_5.5          updates 220 k
 libvirt-daemon-driver-network         x86_64 3.9.0-14.el7_5.5          updates 389 k
 libvirt-daemon-driver-nodedev         x86_64 3.9.0-14.el7_5.5          updates 221 k
 libvirt-daemon-driver-nwfilter        x86_64 3.9.0-14.el7_5.5          updates 243 k
 libvirt-daemon-driver-qemu            x86_64 3.9.0-14.el7_5.5          updates 714 k
 libvirt-daemon-driver-secret          x86_64 3.9.0-14.el7_5.5          updates 210 k
 libvirt-daemon-driver-storage         x86_64 3.9.0-14.el7_5.5          updates 173 k
 libvirt-daemon-driver-storage-core    x86_64 3.9.0-14.el7_5.5          updates 404 k
 libvirt-daemon-driver-storage-disk    x86_64 3.9.0-14.el7_5.5          updates 182 k
 libvirt-daemon-driver-storage-gluster x86_64 3.9.0-14.el7_5.5          updates 182 k
 libvirt-daemon-driver-storage-iscsi   x86_64 3.9.0-14.el7_5.5          updates 179 k
 libvirt-daemon-driver-storage-logical x86_64 3.9.0-14.el7_5.5          updates 183 k
 libvirt-daemon-driver-storage-mpath   x86_64 3.9.0-14.el7_5.5          updates 177 k
 libvirt-daemon-driver-storage-rbd     x86_64 3.9.0-14.el7_5.5          updates 184 k
 libvirt-daemon-driver-storage-scsi    x86_64 3.9.0-14.el7_5.5          updates 179 k
 libvirt-daemon-kvm                    x86_64 3.9.0-14.el7_5.5          updates 173 k
 libvirt-libs                          x86_64 3.9.0-14.el7_5.5          updates 4.1 M
 libvorbis                             x86_64 1:1.3.3-8.el7.1           updates 204 k
 libwacom                              x86_64 0.24-3.el7                base     30 k
 libwacom-data                         noarch 0.24-3.el7                base     63 k
 libwbclient                           x86_64 4.7.1-6.el7               base    107 k
 linux-firmware                        noarch 20180220-62.git6d51311.el7
                                                                        base     57 M
 logrotate                             x86_64 3.8.6-15.el7              base     69 k
 lsof                                  x86_64 4.87-5.el7                base    331 k
 lvm2                                  x86_64 7:2.02.177-4.el7          base    1.3 M
 lvm2-libs                             x86_64 7:2.02.177-4.el7          base    1.0 M
 m17n-db                               noarch 1.6.4-4.el7               base    225 k
 mailx                                 x86_64 12.5-19.el7               base    245 k
 man-pages-overrides                   x86_64 7.5.2-1.el7               base    1.3 M
 mcelog                                x86_64 3:144-8.94d853b2ea81.el7  base     78 k
 mdadm                                 x86_64 4.0-13.el7                base    431 k
 mesa-dri-drivers                      x86_64 17.2.3-8.20171019.el7     base    6.2 M
 mesa-filesystem                       x86_64 17.2.3-8.20171019.el7     base     16 k
 mesa-libEGL                           x86_64 17.2.3-8.20171019.el7     base     96 k
 mesa-libGL                            x86_64 17.2.3-8.20171019.el7     base    156 k
 mesa-libGLES                          x86_64 17.2.3-8.20171019.el7     base     25 k
 mesa-libgbm                           x86_64 17.2.3-8.20171019.el7     base     38 k
 mesa-libglapi                         x86_64 17.2.3-8.20171019.el7     base     43 k
 mesa-libxatracker                     x86_64 17.2.3-8.20171019.el7     base    1.2 M
 microcode_ctl                         x86_64 2:2.1-29.2.el7_5          updates 1.2 M
 mlocate                               x86_64 0.26-8.el7                base    113 k
 mozjs17                               x86_64 17.0.0-20.el7             base    1.4 M
 mutter                                x86_64 3.26.2-13.el7             base    2.3 M
 nautilus                              x86_64 3.22.3-5.el7              base    2.8 M
 nautilus-extensions                   x86_64 3.22.3-5.el7              base     76 k
 ncurses                               x86_64 5.9-14.20130511.el7_4     base    304 k
 ncurses-base                          noarch 5.9-14.20130511.el7_4     base     68 k
 ncurses-libs                          x86_64 5.9-14.20130511.el7_4     base    316 k
 net-snmp-libs                         x86_64 1:5.7.2-33.el7_5.2        updates 749 k
 nfs-utils                             x86_64 1:1.3.0-0.54.el7          base    407 k
 nm-connection-editor                  x86_64 1.8.6-2.el7               base    919 k
 nmap-ncat                             x86_64 2:6.40-13.el7             base    205 k
 nspr                                  x86_64 4.19.0-1.el7_5            updates 127 k
 nss                                   x86_64 3.36.0-5.el7_5            updates 835 k
 nss-softokn                           x86_64 3.36.0-5.el7_5            updates 315 k
 nss-softokn-freebl                    x86_64 3.36.0-5.el7_5            updates 222 k
 nss-sysinit                           x86_64 3.36.0-5.el7_5            updates  62 k
 nss-tools                             x86_64 3.36.0-5.el7_5            updates 514 k
 nss-util                              x86_64 3.36.0-1.el7_5            updates  78 k
 ntpdate                               x86_64 4.2.6p5-28.el7.centos     base     86 k
 numactl-libs                          x86_64 2.0.9-7.el7               base     29 k
 numad                                 x86_64 0.5-18.20150602git.el7    base     35 k
 open-vm-tools                         x86_64 10.1.10-3.el7             base    671 k
 open-vm-tools-desktop                 x86_64 10.1.10-3.el7             base    160 k
 openldap                              x86_64 2.4.44-15.el7_5           updates 355 k
 openssh                               x86_64 7.4p1-16.el7              base    510 k
 openssh-clients                       x86_64 7.4p1-16.el7              base    655 k
 openssh-server                        x86_64 7.4p1-16.el7              base    458 k
 openssl                               x86_64 1:1.0.2k-12.el7           base    492 k
 openssl-libs                          x86_64 1:1.0.2k-12.el7           base    1.2 M
 osinfo-db                             noarch 20170813-6.el7            base    142 k
 pam                                   x86_64 1.1.8-22.el7              base    720 k
 parted                                x86_64 3.1-29.el7                base    608 k
 pciutils                              x86_64 3.5.1-3.el7               base     93 k
 pciutils-libs                         x86_64 3.5.1-3.el7               base     46 k
 perl-Getopt-Long                      noarch 2.40-3.el7                base     56 k
 plymouth                              x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base    116 k
 plymouth-core-libs                    x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base    107 k
 plymouth-graphics-libs                x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     47 k
 plymouth-plugin-label                 x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     37 k
 plymouth-plugin-two-step              x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     45 k
 plymouth-scripts                      x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     39 k
 plymouth-system-theme                 x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     32 k
 plymouth-theme-charge                 x86_64 0.8.9-0.31.20140113.el7.centos
                                                                        base     37 k
 policycoreutils                       x86_64 2.5-22.el7                base    867 k
 policycoreutils-python                x86_64 2.5-22.el7                base    454 k
 polkit                                x86_64 0.112-14.el7              base    167 k
 poppler                               x86_64 0.26.5-17.el7_4           base    783 k
 poppler-glib                          x86_64 0.26.5-17.el7_4           base    137 k
 poppler-utils                         x86_64 0.26.5-17.el7_4           base    168 k
 procps-ng                             x86_64 3.3.10-17.el7_5.2         updates 290 k
 pulseaudio                            x86_64 10.0-5.el7                base    924 k
 pulseaudio-gdm-hooks                  x86_64 10.0-5.el7                base     20 k
 pulseaudio-libs                       x86_64 10.0-5.el7                base    651 k
 pulseaudio-libs-glib2                 x86_64 10.0-5.el7                base     27 k
 pulseaudio-module-bluetooth           x86_64 10.0-5.el7                base     75 k
 pulseaudio-module-x11                 x86_64 10.0-5.el7                base     38 k
 pulseaudio-utils                      x86_64 10.0-5.el7                base     77 k
 pykickstart                           noarch 1.99.66.18-1.el7          base    359 k
 pyparted                              x86_64 1:3.9-15.el7              base    195 k
 python                                x86_64 2.7.5-68.el7              base     93 k
 python-backports-ssl_match_hostname   noarch 3.5.0.1-1.el7             base     13 k
 python-blivet                         noarch 1:0.61.15.69-1.el7        base    815 k
 python-brlapi                         x86_64 0.6.0-16.el7              base     59 k
 python-dmidecode                      x86_64 3.12.2-2.el7              base     83 k
 python-firewall                       noarch 0.4.4.4-14.el7            base    328 k
 python-gobject                        x86_64 3.22.0-1.el7_4.1          base     16 k
 python-gobject-base                   x86_64 3.22.0-1.el7_4.1          base    294 k
 python-libs                           x86_64 2.7.5-68.el7              base    5.6 M
 python-perf                           x86_64 3.10.0-862.3.2.el7        updates 6.2 M
 python-pwquality                      x86_64 1.2.3-5.el7               base     12 k
 python-slip                           noarch 0.4.0-4.el7               base     31 k
 python-slip-dbus                      noarch 0.4.0-4.el7               base     32 k
 python-smbc                           x86_64 1.0.13-8.el7              base     26 k
 qemu-img                              x86_64 10:1.5.3-156.el7_5.2      updates 691 k
 qemu-kvm                              x86_64 10:1.5.3-156.el7_5.2      updates 1.9 M
 qemu-kvm-common                       x86_64 10:1.5.3-156.el7_5.2      updates 428 k
 quota                                 x86_64 1:4.01-17.el7             base    179 k
 quota-nls                             noarch 1:4.01-17.el7             base     90 k
 radvd                                 x86_64 1.9.2-9.el7_5.4           updates  85 k
 rasdaemon                             x86_64 0.4.1-33.1.el7_5          updates  93 k
 rdma-core                             x86_64 15-7.el7_5                updates  48 k
 rest                                  x86_64 0.8.0-2.el7               base     63 k
 rng-tools                             x86_64 5-13.el7                  base     36 k
 rpcbind                               x86_64 0.2.0-44.el7              base     59 k
 rpm                                   x86_64 4.11.3-32.el7             base    1.2 M
 rpm-build-libs                        x86_64 4.11.3-32.el7             base    105 k
 rpm-libs                              x86_64 4.11.3-32.el7             base    276 k
 rpm-python                            x86_64 4.11.3-32.el7             base     82 k
 rsync                                 x86_64 3.1.2-4.el7               base    403 k
 rsyslog                               x86_64 8.24.0-16.el7_5.4         updates 607 k
 samba-client-libs                     x86_64 4.7.1-6.el7               base    4.8 M
 samba-common                          noarch 4.7.1-6.el7               base    205 k
 sane-backends                         x86_64 1.0.24-11.el7             base    668 k
 sane-backends-drivers-scanners        x86_64 1.0.24-11.el7             base    2.3 M
 sane-backends-libs                    x86_64 1.0.24-11.el7             base     95 k
 scl-utils                             x86_64 20130529-18.el7_4         base     24 k
 seabios-bin                           noarch 1.11.0-2.el7              base    112 k
 seavgabios-bin                        noarch 1.11.0-2.el7              base     38 k
 selinux-policy                        noarch 3.13.1-192.el7_5.3        updates 453 k
 selinux-policy-targeted               noarch 3.13.1-192.el7_5.3        updates 6.6 M
 setools-libs                          x86_64 3.3.8-2.el7               base    619 k
 setroubleshoot                        x86_64 3.2.29-3.el7              base    130 k
 setroubleshoot-plugins                noarch 3.0.66-2.1.el7            base    345 k
 setroubleshoot-server                 x86_64 3.2.29-3.el7              base    388 k
 setup                                 noarch 2.8.71-9.el7              base    166 k
 shared-mime-info                      x86_64 1.8-4.el7                 base    312 k
 smartmontools                         x86_64 1:6.5-1.el7               base    460 k
 sos                                   noarch 3.5-7.el7.centos          updates 410 k
 spice-glib                            x86_64 0.34-3.el7                base    381 k
 spice-gtk3                            x86_64 0.34-3.el7                base     86 k
 spice-server                          x86_64 0.14.0-2.el7_5.3          updates 402 k
 spice-vdagent                         x86_64 0.14.0-15.el7             base     70 k
 sssd-client                           x86_64 1.16.0-19.el7             base    195 k
 strace                                x86_64 4.12-6.el7                base    459 k
 sudo                                  x86_64 1.8.19p2-13.el7           base    1.1 M
 sysstat                               x86_64 10.1.5-13.el7             base    310 k
 system-config-printer                 x86_64 1.4.1-21.el7              base    293 k
 system-config-printer-libs            noarch 1.4.1-21.el7              base    950 k
 system-config-printer-udev            x86_64 1.4.1-21.el7              base     93 k
 systemd                               x86_64 219-57.el7                base    5.0 M
 systemd-libs                          x86_64 219-57.el7                base    402 k
 systemd-python                        x86_64 219-57.el7                base    128 k
 systemd-sysv                          x86_64 219-57.el7                base     79 k
 systemtap-runtime                     x86_64 3.2-4.el7                 base    404 k
 tar                                   x86_64 2:1.26-34.el7             base    845 k
 tcpdump                               x86_64 14:4.9.2-3.el7            base    421 k
 teamd                                 x86_64 1.27-4.el7                base    112 k
 telepathy-glib                        x86_64 0.24.1-1.el7              base    719 k
 tigervnc-license                      noarch 1.8.0-5.el7               base     28 k
 tigervnc-server-minimal               x86_64 1.8.0-5.el7               base    1.0 M
 tracker                               x86_64 1.10.5-6.el7              base    1.4 M
 tuned                                 noarch 2.9.0-1.el7               base    244 k
 tzdata                                noarch 2018e-3.el7               updates 482 k
 tzdata-java                           noarch 2018e-3.el7               updates 185 k
 udisks2                               x86_64 2.7.3-6.el7               base    399 k
 unzip                                 x86_64 6.0-19.el7                base    170 k
 usb_modeswitch                        x86_64 2.5.1-1.el7               base    162 k
 usb_modeswitch-data                   noarch 20170806-1.el7            base    103 k
 usbredir                              x86_64 0.7.1-3.el7               base     47 k
 util-linux                            x86_64 2.23.2-52.el7             base    2.0 M
 vim-common                            x86_64 2:7.4.160-4.el7           base    5.9 M
 vim-enhanced                          x86_64 2:7.4.160-4.el7           base    1.0 M
 vim-filesystem                        x86_64 2:7.4.160-4.el7           base     10 k
 vim-minimal                           x86_64 2:7.4.160-4.el7           base    437 k
 vinagre                               x86_64 3.22.0-9.el7              base    1.4 M
 virt-what                             x86_64 1.18-4.el7                base     29 k
 webkitgtk4                            x86_64 2.16.6-6.el7              base     25 M
 webkitgtk4-jsc                        x86_64 2.16.6-6.el7              base    4.3 M
 webkitgtk4-plugin-process-gtk2        x86_64 2.16.6-6.el7              base    9.0 M
 wget                                  x86_64 1.14-15.el7_4.1           base    547 k
 wpa_supplicant                        x86_64 1:2.6-9.el7               base    1.2 M
 xdg-user-dirs                         x86_64 0.15-5.el7                base     59 k
 xfsdump                               x86_64 3.1.7-1.el7               base    308 k
 xfsprogs                              x86_64 4.5.0-15.el7              base    896 k
 xmlsec1                               x86_64 1.2.20-7.el7_4            base    177 k
 xmlsec1-openssl                       x86_64 1.2.20-7.el7_4            base     76 k
 xorg-x11-drv-ati                      x86_64 7.10.0-1.el7              base    161 k
 xorg-x11-drv-intel                    x86_64 2.99.917-27.20160929.el7  base    672 k
 xorg-x11-drv-wacom                    x86_64 0.34.2-4.el7              base    306 k
 xorg-x11-server-Xorg                  x86_64 1.19.5-5.el7              base    1.5 M
 xorg-x11-server-common                x86_64 1.19.5-5.el7              base     53 k
 xorg-x11-xinit                        x86_64 1.3.4-2.el7               base     58 k
Installing for dependencies:
 gnome-shell-extension-top-icons       noarch 3.26.2-3.el7              base     19 k
 ldns                                  x86_64 1.6.16-10.el7             base    476 k
 libblockdev                           x86_64 2.12-3.el7                base    105 k
 libblockdev-crypto                    x86_64 2.12-3.el7                base     55 k
 libblockdev-fs                        x86_64 2.12-3.el7                base     62 k
 libblockdev-loop                      x86_64 2.12-3.el7                base     51 k
 libblockdev-mdraid                    x86_64 2.12-3.el7                base     55 k
 libblockdev-part                      x86_64 2.12-3.el7                base     58 k
 libblockdev-swap                      x86_64 2.12-3.el7                base     50 k
 libblockdev-utils                     x86_64 2.12-3.el7                base     56 k
 libbytesize                           x86_64 1.2-1.el7                 base     52 k
 libinput                              x86_64 1.8.4-2.el7               base    142 k
 libwayland-client                     x86_64 1.14.0-2.el7              base     32 k
 libwayland-cursor                     x86_64 1.14.0-2.el7              base     20 k
 libwayland-server                     x86_64 1.14.0-2.el7              base     38 k
 llvm-private                          x86_64 5.0.0-3.el7               base     20 M
 lz4                                   x86_64 1.7.5-2.el7               base     98 k
 mesa-libwayland-egl                   x86_64 17.2.3-8.20171019.el7     base     17 k
 python-ipaddress                      noarch 1.0.16-2.el7              base     34 k
 samba-common-libs                     x86_64 4.7.1-6.el7               base    162 k
 unbound-libs                          x86_64 1.6.6-1.el7               base    405 k
 volume_key-libs                       x86_64 0.3.9-8.el7               base    140 k

Transaction Summary
======================================================================================
Install    5 Packages (+22 Dependent packages)
Upgrade  539 Packages

Total size: 596 M
Is this ok [y/d/N]: Exiting on user command
Your transaction was saved, rerun it with:
 yum load-transaction /tmp/yum_save_tx.2018-05-30.13-28.sXnWvm.yumtx

~~~
