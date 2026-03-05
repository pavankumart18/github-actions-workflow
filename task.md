# Repository Workflow

steps:
  - run: echo "Listing repository files"
  - run: ls

  - run: echo "Counting Python files"
  - run: find . -name "*.py" | wc -l