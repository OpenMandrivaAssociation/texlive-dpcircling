%global tl_name dpcircling
%global tl_revision 54994

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Decorated text boxes using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/dpcircling
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dpcircling.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dpcircling.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This simple package provides four types of text decorations using TikZ.
You can frame your text with circles, rectangles, jagged rectangles, and
fan-shapes. The baseline will be adjusted properly according to the
surroundings. You can use these decorations both in text mode and in
math mode. You can specify line color, line width, width, and height
using option keys. Note: The "DP" in the package name stands for
"Decorated Packets".

