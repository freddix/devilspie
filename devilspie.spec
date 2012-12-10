Summary:	Devil's Pie - window matching tool
Name:		devilspie
Version:	0.22
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	4190e12f99ab92c0427e457d9fbfe231
Patch0:		%{name}-no-disable-deprecated.patch
Patch1:		%{name}-link.patch
URL:		http://www.burtonini.com/blog/computers/devilspie
BuildRequires:	gtk+-devel
BuildRequires:	libwnck2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A window-matching utility, inspired by Sawfish's "Matched Windows"
option and the lack of the functionality in Metacity. Metacity lacking
window matching is not a bad thing - Metacity is a lean window
manager, and window matching does not have to be a window manager
task.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i "/GNOME_COMPILE_WARNINGS/d" configure.in
%{__sed} -i "/AM_CFLAGS/d" src/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}*

