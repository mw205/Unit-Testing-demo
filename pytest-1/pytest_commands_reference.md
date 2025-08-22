# Complete pytest Run Commands Reference

## Basic Test Execution

| Command | Description |
|---------|-------------|
| `pytest` | Run all tests in current directory and subdirectories |
| `pytest path/to/test_file.py` | Run a specific test file |
| `pytest dir/` | Run all tests in a specific directory |
| `pytest test_file.py::test_function` | Run a specific test function |
| `pytest test_file.py::TestClass` | Run all tests in a specific class |
| `pytest test_file.py::TestClass::test_method` | Run a specific test method inside a class |
| `pytest tests/unit tests/integration` | Run tests from multiple directories |

## Test Selection Options

| Option | Description | Example |
|--------|-------------|---------|
| `-k "expression"` | Run tests matching substring/expression | `pytest -k "login"` |
| `-k "test_login or test_logout"` | Run tests matching OR condition | `pytest -k "login or logout"` |
| `-k "test_login and not slow"` | Run tests matching AND NOT condition | `pytest -k "login and not slow"` |
| `-m "marker"` | Run tests with specific marker | `pytest -m "slow"` |
| `-m "not slow"` | Run tests NOT marked with marker | `pytest -m "not slow"` |
| `-m "slow or integration"` | Run tests with multiple markers | `pytest -m "slow or integration"` |
| `--lf` / `--last-failed` | Run only last failed tests | `pytest --lf` |
| `--ff` / `--failed-first` | Run failed tests first, then the rest | `pytest --ff` |
| `--nf` / `--new-first` | Run new tests first | `pytest --nf` |

## Output and Verbosity Control

| Option | Description | Example |
|--------|-------------|---------|
| `-v` / `--verbose` | Verbose output (show test names) | `pytest -v` |
| `-vv` | Extra verbose output | `pytest -vv` |
| `-q` / `--quiet` | Quiet output (minimal) | `pytest -q` |
| `-s` / `--capture=no` | Show print statements and output | `pytest -s` |
| `--capture=sys` | Capture stdout/stderr (default) | `pytest --capture=sys` |
| `--capture=fd` | Capture file descriptors 1 and 2 | `pytest --capture=fd` |
| `--tb=auto` | Automatic traceback format (default) | `pytest --tb=auto` |
| `--tb=long` | Long traceback format | `pytest --tb=long` |
| `--tb=short` | Short traceback format | `pytest --tb=short` |
| `--tb=line` | One line per failure | `pytest --tb=line` |
| `--tb=native` | Python standard library format | `pytest --tb=native` |
| `--tb=no` | No traceback | `pytest --tb=no` |
| `--disable-warnings` | Hide warnings | `pytest --disable-warnings` |
| `--disable-warnings -q` | Hide warnings and minimize output | `pytest --disable-warnings -q` |

## Execution Control

| Option | Description | Example |
|--------|-------------|---------|
| `-x` / `--exitfirst` | Stop after first failure | `pytest -x` |
| `--maxfail=NUM` | Stop after N failures | `pytest --maxfail=3` |
| `--continue-on-collection-errors` | Continue even if collection errors occur | `pytest --continue-on-collection-errors` |
| `-n NUM` | Run tests in parallel (requires pytest-xdist) | `pytest -n 4` |
| `-n auto` | Auto-detect number of CPUs for parallel execution | `pytest -n auto` |
| `--dist=worksteal` | Distribute tests dynamically | `pytest -n 4 --dist=worksteal` |

## Debugging and Development

| Option | Description | Example |
|--------|-------------|---------|
| `--pdb` | Drop into debugger on failure | `pytest --pdb` |
| `--pdb-trace` | Drop into debugger at start of each test | `pytest --pdb-trace` |
| `--trace` | Drop into debugger at start of each test | `pytest --trace` |
| `--setup-show` | Show setup and teardown of fixtures | `pytest --setup-show` |
| `--setup-only` | Only run setup, don't execute tests | `pytest --setup-only` |
| `--setup-plan` | Show what fixtures will be executed | `pytest --setup-plan` |
| `--durations=N` | Show N slowest tests | `pytest --durations=10` |
| `--durations=0` | Show all test durations | `pytest --durations=0` |

## Collection and Discovery

| Option | Description | Example |
|--------|-------------|---------|
| `--collect-only` | Only collect tests, don't run them | `pytest --collect-only` |
| `--co` | Short form of --collect-only | `pytest --co` |
| `--ignore=path` | Ignore specific path during collection | `pytest --ignore=legacy_tests/` |
| `--ignore-glob=pattern` | Ignore paths matching glob pattern | `pytest --ignore-glob="*integration*"` |
| `--deselect=path` | Deselect specific tests | `pytest --deselect=test_slow.py::test_timeout` |

## Configuration and Environment

| Option | Description | Example |
|--------|-------------|---------|
| `-c FILE` / `--confcutdir=DIR` | Use specific config file | `pytest -c myconfig.ini` |
| `--rootdir=DIR` | Define root directory | `pytest --rootdir=/path/to/root` |
| `--override-ini=OPTION` | Override ini file options | `pytest --override-ini="python_files=check_*.py"` |
| `--assert=MODE` | Set assertion debugging mode | `pytest --assert=plain` |
| `--import-mode=MODE` | Set import mode (prepend, append, importlib) | `pytest --import-mode=importlib` |

## Coverage and Reporting (requires plugins)

| Option | Description | Example |
|--------|-------------|---------|
| `--cov=PATH` | Measure coverage for specified path | `pytest --cov=src` |
| `--cov-report=TYPE` | Coverage report type (term, html, xml, json) | `pytest --cov=src --cov-report=html` |
| `--cov-report=term-missing` | Show missing lines in terminal | `pytest --cov=src --cov-report=term-missing` |
| `--cov-config=FILE` | Coverage config file | `pytest --cov-config=.coveragerc` |
| `--cov-branch` | Include branch coverage | `pytest --cov=src --cov-branch` |
| `--cov-fail-under=MIN` | Fail if coverage is below minimum | `pytest --cov=src --cov-fail-under=90` |
| `--html=FILE` | Generate HTML report (requires pytest-html) | `pytest --html=report.html` |
| `--self-contained-html` | Create self-contained HTML report | `pytest --html=report.html --self-contained-html` |
| `--junitxml=FILE` | Generate JUnit XML report | `pytest --junitxml=report.xml` |
| `--resultlog=FILE` | Generate result log (deprecated) | `pytest --resultlog=result.log` |

## Plugin-Specific Options

### pytest-mock
| Option | Description | Example |
|--------|-------------|---------|
| `--mock-use-standalone-module` | Use standalone mock module | `pytest --mock-use-standalone-module` |

### pytest-xdist (parallel execution)
| Option | Description | Example |
|--------|-------------|---------|
| `--tx=SPEC` | Add transmission spec | `pytest --tx ssh=myhost//python` |
| `--rsyncdir=DIR` | Add directory for rsyncing | `pytest --rsyncdir=src` |
| `--rsyncignore=GLOB` | Add glob for rsync ignoring | `pytest --rsyncignore="*.log"` |
| `--looponfail` | Run tests in subprocess, restart on failure | `pytest --looponfail` |

### pytest-benchmark
| Option | Description | Example |
|--------|-------------|---------|
| `--benchmark-skip` | Skip benchmark tests | `pytest --benchmark-skip` |
| `--benchmark-only` | Run only benchmark tests | `pytest --benchmark-only` |
| `--benchmark-sort=COLUMN` | Sort benchmarks by column | `pytest --benchmark-sort=mean` |

## Common Command Combinations

| Command | Description |
|---------|-------------|
| `pytest -v -s` | Verbose output with print statements |
| `pytest -x -vv` | Stop on first failure with extra verbose output |
| `pytest -k "not slow" -v` | Run non-slow tests with verbose output |
| `pytest --lf -x` | Run last failed tests and stop on first failure |
| `pytest --cov=src --cov-report=html -v` | Run with coverage and generate HTML report |
| `pytest -n auto --dist=worksteal` | Parallel execution with dynamic distribution |
| `pytest --tb=short --disable-warnings -q` | Minimal output with short tracebacks |
| `pytest --durations=10 -v` | Show 10 slowest tests with verbose output |
| `pytest --pdb -s` | Debug mode with print statements |
| `pytest --collect-only -q` | Quietly show what tests would be collected |

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `PYTEST_ADDOPTS` | Additional command line options | `export PYTEST_ADDOPTS="-v --tb=short"` |
| `PYTEST_PLUGINS` | Plugins to load | `export PYTEST_PLUGINS="myproject.plugin,pytest_html"` |
| `PYTEST_DISABLE_PLUGIN_AUTOLOAD` | Disable plugin auto-loading | `export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1` |
| `PYTEST_CURRENT_TEST` | Current test being run (set by pytest) | Read-only during test execution |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All tests passed |
| 1 | Tests were collected and run but some of the tests failed |
| 2 | Test execution was interrupted by the user |
| 3 | Internal error happened while executing tests |
| 4 | pytest command line usage error |
| 5 | No tests were collected |

## Popular Plugin Commands

### pytest-cov (Coverage)
```bash
# Basic coverage
pytest --cov=src

# Coverage with HTML report
pytest --cov=src --cov-report=html

# Coverage with missing lines
pytest --cov=src --cov-report=term-missing

# Branch coverage
pytest --cov=src --cov-branch --cov-report=html
```

### pytest-xdist (Parallel)
```bash
# Run with 4 workers
pytest -n 4

# Auto-detect CPUs
pytest -n auto

# Distribute tests efficiently
pytest -n auto --dist=worksteal
```

### pytest-html (HTML Reports)
```bash
# Basic HTML report
pytest --html=report.html

# Self-contained HTML report
pytest --html=report.html --self-contained-html

# HTML report with extra info
pytest --html=report.html --self-contained-html -v
```

### pytest-mock (Mocking)
```bash
# Standard usage (no special flags needed)
pytest -v  # Mock fixtures available automatically
```

### pytest-benchmark (Performance)
```bash
# Run only benchmarks
pytest --benchmark-only

# Skip benchmarks
pytest --benchmark-skip

# Sort benchmarks by mean time
pytest --benchmark-sort=mean
```