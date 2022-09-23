{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python39;
  package = pkgs.python39Packages;
  pythonPackages = python.buildEnv.override {
    extraLibs = [
      package.numpy
      package.matplotlib
      package.pandas
      package.jupyter
    ];
  };
  texPackages = pkgs.texlive.combined.scheme-full;
in
      
pkgs.mkShell {
  buildInputs = [
    pythonPackages
    texPackages
    pkgs.imagemagick
  ];
}
