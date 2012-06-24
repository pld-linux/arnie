Summary:	Arnie - simple incremental backup system
Summary(pl):	Arnie - prosty system przyrostowych kopii zapasowych
Name:		arnie
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://furius.ca/downloads/arnie/%{name}-%{version}.tar.bz2
# Source0-md5:	ec7de82fd1ebb8bb7d3535308c2cee4b
URL:		http://furius.ca/arnie/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arnie is a tremendously simple system for performing incremental
backups to remote untrusted hosts, with support for encrypted files on
the remote host. While these scripts are simple and recent, they are
believed to be robust and are in active use on the author's own
servers, and are provided a comprehensive suite of tests to prove it.
In addition, the following features are provided:

- Automatically compress archives in gzip or bzip2 format;
- Automatically encrypt archives using a GnuPG key (specify the key Id
  or name);
- Automatically send the archive file to a remote host using scp. This
  is just a convenience: alternatively you can capture the name of the
  archive and send it any way you like (ftp, other...);
- Tracks and restores permissions changes on directories and files;
- Works with empty directories;
- Works with symbolic links;
- An alternate location for the history file can be specified;
- Regexp patterns for excluding files in the backup can be provided;
- You can restore at any of the times the backups were made (the
  restore script has an option);
- The archives are simply stored as GNU tar files, so you can open
  them manually if so desired.

%description -l pl
arnie to bardzo prosty system do wykonywania przyrostowych kopii
zapasowych na zdalne, nie zaufane hosty z obs�ug� szyfrowanych plik�w
na zdalnym ho�cie. Chocia� skrypty s� proste i �wie�e, autorzy wierz�,
�e s� pot�ne, s� aktywnie u�ywane na w�asnych serwerach autor�w, a
ponadto istnieje zestaw test�w do udowodnienia tego. Ponadto dost�pne
s� nast�puj�ce mo�liwo�ci:

- automatyczna kompresja archiw�w w formacie gzip lub bzip2;
- automatyczne szyfrowanie archiw�w przy u�yciu klucza GnuPG (po
  podaniu identyfikatora klucza lub nazwy);
- automatyczne wysy�anie pliku archiwum na zdalny host przy u�yciu
  scp; opcja tylko dla wygody - zamiast niej mo�na przechwyci� nazw�
  archiwum i wys�a� je w dowolnie wybrany spos�b (np. ftp);
- �ledzenie i przywracanie zmian uprawnie� na katalogach i plikach;
- dzia�anie z pustymi katalogami;
- dzia�anie z dowi�zaniami symbolicznymi;
- mo�liwo�� podania alternatywnego po�o�enia pliku historii;
- mo�liwo�� u�ycia wyra�e� regularnych do wy��czania plik�w z kopii
  zapasowych;
- mo�liwo�� odtworzenia kopii zapasowych z dowolnej chwili;
- przechowywanie archiw�w jako zwyk�ych plik�w GNU tar, dzi�ki czemu
  mo�na je otwiera� r�cznie.
 
%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install bin/arnie-archive $RPM_BUILD_ROOT%{_bindir}/arnie-archive 
install bin/arnie-restore $RPM_BUILD_ROOT%{_bindir}/arnie-restore
install doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%attr(755,root,root) %{_bindir}/*
