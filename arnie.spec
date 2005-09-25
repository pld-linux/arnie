
Summary:	Arnie
Summary(pl):	Arnie
Name:		arnie
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://furius.ca/downloads/arnie/%{name}-%{version}.tar.bz2
# Source0-md5:	ec7de82fd1ebb8bb7d3535308c2cee4b
URL:		http://furius.ca/arnie/
#Requires:	-
#Obsoletes:	-
#Conflicts:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arnie is a tremendously simple system for performing incremental
backups to remote untrusted hosts, with support for encrypted 
files on the remote host. While our scripts are simple and recent,
we believe they are robust and are in active use on the author's 
own servers, and we provide a comprehensive suite of tests to prove it.
In addition, the following features are provided (see options):

* Automatically compress archives in gzip or bzip2 format;
* Automatically encrypt archives using a GnuPG key (specify the key Id
  or name);
* Automatically send the archive file to a remote host using scp. This
  is just a convenience: alternatively you can capture the name of the
  archive and send it any way you like (ftp, other...);
* Tracks and restores permissions changes on directories and files;
* Works with empty directories;
* Works with symbolic links;
* An alternate location for the history file can be specified;
* Regexp patterns for excluding files in the backup can be provided;
* You can restore at any of the times the backups were made (the 
  restore script has an option);
* The archives are simply stored as GNU tar files, so you can open
  them manually if so desired.

%description -l pl

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install bin/arnie-archive $RPM_BUILD_ROOT%{_bindir}/arnie-archive 
install bin/arnie-restore $RPM_BUILD_ROOT%{_bindir}/arnie-restore
install doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%dir %attr(755,root,root) %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%attr(755,root,root) %{_bindir}/*
