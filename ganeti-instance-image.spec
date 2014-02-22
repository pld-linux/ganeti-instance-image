Summary:	System Image Guest OS definition for Ganeti
Name:		ganeti-instance-image
Version:	0.6
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	https://code.osuosl.org/attachments/download/3285/%{name}-%{version}.tar.gz
# Source0-md5:	6f1f50d23dd172921983c803a8286dc8
Patch0:		kpartx-sync.patch
URL:		https://code.osuosl.org/projects/ganeti-image
BuildRequires:	rpmbuild(macros) >= 1.647
Requires:	ganeti
Requires:	util-linux
Requires:	kpartx
Requires:	losetup
Requires:	e2fsprogs
Requires:	coreutils
Requires:	mount
Requires:	sed
Requires:	dump
Requires:	tar
Requires:	blockdev
Requires:	gawk
Requires:	parted
Requires:	/usr/bin/qemu-img
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ganeti Instance Image is guest OS definition for Ganeti that uses
either filesystem dumps or tar ball images to deploy instances.
The goal of this OS definition is to allow fast and flexible
installation of instances without the need for external tools
such as debootstrap.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# symlink points to buildroot
%{__rm} $RPM_BUILD_ROOT/usr/share/ganeti/os/image/variants.list
ln -s %{_sysconfdir}/ganeti/instance-image/variants.list $RPM_BUILD_ROOT/usr/share/ganeti/os/image/variants.list

%{__rm} -r $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
%dir %{_sysconfdir}/ganeti/instance-image
%dir %{_sysconfdir}/ganeti/instance-image/hooks
%attr(755,root,root) %{_sysconfdir}/ganeti/instance-image/hooks/grub
%attr(755,root,root) %{_sysconfdir}/ganeti/instance-image/hooks/interfaces
%attr(755,root,root) %{_sysconfdir}/ganeti/instance-image/hooks/overlays
%attr(755,root,root) %{_sysconfdir}/ganeti/instance-image/hooks/ssh
%attr(755,root,root) %{_sysconfdir}/ganeti/instance-image/hooks/zz_ddns
%dir %{_sysconfdir}/ganeti/instance-image/variants
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-image/variants/default.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-image/variants.list
%dir %{_datadir}/ganeti/os/image
%{_datadir}/ganeti/os/image/common.sh
%attr(755,root,root) %{_datadir}/ganeti/os/image/create
%attr(755,root,root) %{_datadir}/ganeti/os/image/export
%{_datadir}/ganeti/os/image/ganeti_api_version
%attr(755,root,root) %{_datadir}/ganeti/os/image/import
%attr(755,root,root) %{_datadir}/ganeti/os/image/rename
%{_datadir}/ganeti/os/image/variants.list
%dir %{_datadir}/ganeti/os/image/tools
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/ganeti-image
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/make-dump
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/make-image
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/make-qemu-img
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/mount-disks
%attr(755,root,root) %{_datadir}/ganeti/os/image/tools/umount-disks
