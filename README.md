# Bacteria Speciation Process

An algorithm that detects bacterial and archaeal species based on the rates of gene flow across populations.

Bobay and Ochman. *Genome Biol Evol* 2017. 9(3): 491–501.

## Required Technologies

The following programs should be accessable from your command line (on your local path), or else the path to the program specified in `config.py`. Programs marked with a * must be on your local path.

- python*
- gunzip*
- wget*
- usearch https://www.drive5.com/usearch/
- mcl https://www.micans.org/mcl/index.html
- mafft http://mafft.cbrc.jp/alignment/software/
- RAxML https://sco.h-its.org/exelixis/web/software/raxml/index.html
- Rscript* https://cran.r-project.org/doc/manuals/r-release/R-admin.html

## Functionality

This branch is specified to allow the filepath to be passed as a command-line argument.

[**Analyze Your Own Genomes:**](https://github.com/Bobay-Ochman/ConSpeciFix/tree/forRelease/personalCompare) for use on a single folder of genomes to determine if they are all the same species.