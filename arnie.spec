Summary:	Arnie - simple incremental backup system
Summary(pl.UTF-8):	Arnie - prosty system przyrostowych kopii zapasowych
Name:		arnie
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://furius.ca/downloads/arnie/%{name}-%{version}.tar.bz2
# Source0-md5:	ec7de82fd1ebb8bb7d3535308c2cee4b
URL:		http://furius.ca/arnie/
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
arnie to bardzo prosty system do wykonywania przyrostowych kopii
zapasowych na zdalne, nie zaufane hosty z obsługą szyfrowanych plików
na zdalnym hoście. Chociaż skrypty są proste i świeże, autorzy wierzą,
że są potężne, są aktywnie używane na własnych serwerach autorów, a
ponadto istnieje zestaw testów do udowodnienia tego. Ponadto dostępne
są następujące możliwości:

- automatyczna kompresja archiwów w formacie gzip lub bzip2;
- automatyczne szyfrowanie archiwów przy użyciu klucza GnuPG (po
  podaniu identyfikatora klucza lub nazwy);
- automatyczne wysyłanie pliku archiwum na zdalny host przy użyciu
  scp; opcja tylko dla wygody - zamiast niej można przechwycić nazwę
  archiwum i wysłać je w dowolnie wybrany sposób (np. ftp);
- śledzenie i przywracanie zmian uprawnień na katalogach i plikach;
- działanie z pustymi katalogami;
- działanie z dowiązaniami symbolicznymi;
- możliwość podania alternatywnego położenia pliku historii;
- możliwość użycia wyrażeń regularnych do wyłączania plików z kopii
  zapasowych;
- możliwość odtworzenia kopii zapasowych z dowolnej chwili;
- przechowywanie archiwów jako zwykłych plików GNU tar, dzięki czemu
  można je otwierać ręcznie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install bin/arnie-* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
