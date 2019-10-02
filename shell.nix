with import <nixpkgs> {};
with python37Packages;

buildPythonPackage rec {
  name = "plover_czech";
  src = ".";
}
