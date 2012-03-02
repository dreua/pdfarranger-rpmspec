#!/bin/bash
DATE=$(date +%Y%m%d)

set -x

rm -rf pdfshuffler
svn export https://pdfshuffler.svn.sourceforge.net/svnroot/pdfshuffler/trunk pdfshuffler
tar cJf pdfshuffler-${DATE}svn.tar.xz pdfshuffler

rm -rf pershuffler
