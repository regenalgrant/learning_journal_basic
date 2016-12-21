"""Run startup learning_journal."""
#!/bin/bash
set -e
python setup.py develop
python runapp.py
