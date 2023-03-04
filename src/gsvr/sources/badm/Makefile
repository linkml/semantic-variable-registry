MODULES = main enums explanations

all: $(patsubst %, schema/badm-soil-%.yaml, $(MODULES))

schema/%.yaml: curated/%.tsv
	poetry run sheets2linkml -C curated/$*.yaml $< > $@.tmp && mv $@.tmp $@
.PRECIOUS: schema/%.yaml

curated/badm-soil-main.tsv: downloads/BADM-Soil-v2021-Template-main.csv
	csvformat -T $< | ./utils/fix-main.pl > $@

gen-project:
	poetry run gen-project schema/badm-soil.yaml -d project

gendocs:
	poetry run gen-doc schema/badm-soil.yaml  -d docs
