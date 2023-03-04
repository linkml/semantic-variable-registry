RUN = poetry run
SRC = src
PROJECT_SRC = src/gsvr
SCHEMA_DIR = $(PROJECT_SRC)/schema
SCHEMA = $(SCHEMA_DIR)/gsvr.yaml
TESTS = tests
TEST_INPUT = $(TESTS)/input
EXAMPLES_SRC_DIR = $(TEST_INPUT)/examples
PUBLISHED_EXAMPLES = examples

all: project test

project: python
	$(RUN) gen-project $(SCHEMA) -d project

python: src/gsvr/datamodel/metamodel.py
src/gsvr/datamodel/metamodel.py:
	$(RUN) gen-pydantic $(SCHEMA) > $@.tmp && mv $@.tmp $@

test: test-examples test-normalized
test-examples:
	$(RUN) linkml-run-examples --no-use-type-designators -s $(SCHEMA) -e $(EXAMPLES_SRC_DIR) -d $(PUBLISHED_EXAMPLES) -t yaml -t json

unittest:
	$(RUN) python -m unittest
pytest:
	$(RUN) pytest

EXAMPLE_OBJECTS = Variable-person-name Variable-soil-depth-m VariableCollection-health VariableCollection-soil  VariableCollection-unstructured
test-normalized: $(patsubst %, normalized/%.yaml, $(EXAMPLE_OBJECTS))

normalized/VariableCollection-%.yaml: $(EXAMPLES_SRC_DIR)/VariableCollection-%.yaml
	$(RUN) linkml-normalize -s $(SCHEMA) -C VariableCollection $< -o $@
normalized/Variable-%.yaml: $(EXAMPLES_SRC_DIR)/Variable-%.yaml
	$(RUN) linkml-normalize -s $(SCHEMA) -C Variable $< -o $@

%.ofn: %.yaml
	$(RUN) linkml-data2owl -s $(SCHEMA) $< -o $@
