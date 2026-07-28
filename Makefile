LATEXMK := latexmk
SOURCE_DATE_EPOCH ?= 1785081600
export SOURCE_DATE_EPOCH
export FORCE_SOURCE_DATE := 1

.PHONY: all proposal cdr check verify-archive clean

all: proposal cdr

proposal:
	mkdir -p build/proposal
	$(LATEXMK) -outdir=build/proposal proposal/main.tex

cdr:
	mkdir -p build/cdr
	$(LATEXMK) -outdir=build/cdr cdr/main.tex

verify-archive:
	cd archive/original_20260727 && shasum -a 256 -c SHA256SUMS

check: verify-archive all
	! grep -E "(Citation .* undefined|Reference .* undefined|There were undefined references|No file .*\\.bbl|File .* not found)" build/proposal/main.log build/cdr/main.log

clean:
	latexmk -C -outdir=build/proposal proposal/main.tex
	latexmk -C -outdir=build/cdr cdr/main.tex
	rmdir build/proposal build/cdr build 2>/dev/null || true
