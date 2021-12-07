# Repo for creating github action for running tests using Selenium- 
Test case is run using selenium+python and using headless-chrome.

# Test Framework-
I have used <a href="https://github.com/qxf2/qxf2-page-object-model">Qxf2's Page Object Model framework</a> to write test cases.

# GitHub action steps:

1. Install dependencies-

```
name: Run Python Tests on headless-chrome browser
on:
  push:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Python 3
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
      - name: Install dependencies
        run: |
          set -ex
          wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
          sudo apt install ./google-chrome-stable_current_amd64.deb
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install msedge-selenium-tools
 ```
 
 2. Run Tests

```
# Execute Test for headless chrome
      - name: Run test 
        run: python -m pytest tests/test_altoro_mutual_form.py --browser headless-chrome
```

