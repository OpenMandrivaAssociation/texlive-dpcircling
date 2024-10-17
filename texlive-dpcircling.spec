Name:		texlive-dpcircling
Version:	54994
Release:	2
Summary:	Decorated text boxes using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dpcircling
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpcircling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpcircling.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple package provides four types of text decorations
using TikZ. You can frame your text with circles, rectangles,
jagged rectangles, and fan-shapes. The baseline will be
adjusted properly according to the surroundings. You can use
these decorations both in text mode and in math mode. You can
specify line color, line width, width, and height using option
keys. Note: The "DP" in the package name stands for "Decorated
Packets".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dpcircling
%doc %{_texmfdistdir}/doc/latex/dpcircling

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
