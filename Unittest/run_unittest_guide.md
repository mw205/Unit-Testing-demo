# Complete Python Testing Guide - unittest & coverage

## Running Your CLI Application

### Basic CLI Commands
```bash
# Display help and available commands
python main.py --help

# Create a new task
python main.py create "Grocery Shopping" "Buy milk, eggs, bread" "2024-03-15"

# List all tasks
python main.py list

# Get a specific task by ID
python main.py get 1

# Update an existing task
python main.py update 1 "Grocery Run" "Milk, eggs, bread, cheese" "2024-03-16" "In Progress"

# Delete a task
python main.py delete 1
```

## Running Tests with unittest

### Basic Test Execution

#### 1. Run a Specific Test File
```bash
# Basic execution
python -m unittest file.py

# Verbose output (shows each test method)
python -m unittest -v file.py

# Run specific test module
python -m unittest test_my_module.py

# Verbose output for specific module
python -m unittest -v test_my_module.py
```

#### 2. Test Discovery
```bash
# Discover and run all tests in current directory
python -m unittest discover

# Discover tests in specific directory
python -m unittest discover tests

# Discover tests with verbose output
python -m unittest discover -v

# Discover tests in specific directory with verbose output
python -m unittest discover -s tests -v
```

### Advanced unittest Options

#### Command Line Options
```bash
# Show help for unittest
python -m unittest -h

# Run with buffer (capture stdout/stderr during tests)
python -m unittest -b test_my_module.py

# Catch Ctrl+C and display results so far
python -m unittest -c test_my_module.py

# Stop on first failure
python -m unittest -f test_my_module.py

# Start directory for discovery (default: current directory)
python -m unittest discover -s tests

# Pattern to match test files (default: test*.py)
python -m unittest discover -p "*_test.py"

# Top level directory of project (default: start directory)
python -m unittest discover -t .

# Verbose output
python -m unittest discover -v

# Combine multiple options
python -m unittest discover -s tests -p "*_test.py" -v -b
```

#### Running Specific Test Cases and Methods
```bash
# Run specific test class
python -m unittest test_my_module.TestClassName

# Run specific test method
python -m unittest test_my_module.TestClassName.test_method_name

# Run multiple specific tests
python -m unittest test_my_module.TestClass1.test_method1 test_my_module.TestClass2.test_method2

# Run with verbose output
python -m unittest -v test_my_module.TestClassName.test_method_name
```

### Test Discovery Patterns

#### Directory Structure Examples
```
project/
├── main.py
├── my_module.py
├── tests/
│   ├── __init__.py
│   ├── test_my_module.py
│   ├── test_integration.py
│   └── unit/
│       ├── __init__.py
│       └── test_utils.py
└── integration_tests/
    ├── __init__.py
    └── test_api.py
```

#### Discovery Commands for Different Structures
```bash
# Standard tests/ directory
python -m unittest discover -s tests

# Custom test directory
python -m unittest discover -s integration_tests

# Recursive discovery with specific pattern
python -m unittest discover -s tests -p "test_*.py"

# Discovery with top-level directory specification
python -m unittest discover -s tests -t .
```

## Coverage Testing

### Installation
```bash
# Install coverage.py
pip install coverage
```

### Basic Coverage Commands

#### 1. Run Tests with Coverage
```bash
# Run all discovered tests with coverage
coverage run -m unittest discover

# Run tests in specific directory
coverage run -m unittest discover tests

# Run specific test file
coverage run -m unittest test_my_module.py

# Run with specific source inclusion
coverage run --source=. -m unittest discover tests
```

#### 2. Generate Coverage Reports
```bash
# Display coverage report in console
coverage report

# Display with missing line numbers
coverage report -m

# Generate HTML report
coverage html

# Generate XML report (useful for CI/CD)
coverage xml

# Generate JSON report
coverage json
```

### Advanced Coverage Options

#### Coverage Configuration
Create a `.coveragerc` file:
```ini
[run]
source = .
omit = 
    */tests/*
    */venv/*
    setup.py
    */site-packages/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError

[html]
directory = htmlcov
```

#### Coverage Commands with Options
```bash
# Run with specific source directories
coverage run --source=my_module,another_module -m unittest discover

# Include/exclude specific files
coverage run --include="*.py" --omit="*/tests/*" -m unittest discover

# Parallel execution support
coverage run --parallel-mode -m unittest discover

# Combine parallel data
coverage combine

# Erase previous coverage data
coverage erase

# Show coverage for specific files only
coverage report my_module.py another_module.py

# Set minimum coverage percentage (fails if below threshold)
coverage report --fail-under=80

# Skip covered files in report
coverage report --skip-covered

# Sort report by different criteria
coverage report --sort=cover    # Sort by coverage percentage
coverage report --sort=name     # Sort by filename
coverage report --sort=stmts    # Sort by number of statements
coverage report --sort=miss     # Sort by number of missing lines
```

### Complete Testing Workflow

#### 1. Development Workflow
```bash
# 1. Run tests during development
python -m unittest discover -v

# 2. Run specific failing test
python -m unittest -v test_my_module.TestClass.test_failing_method

# 3. Run with coverage after fixes
coverage run -m unittest discover

# 4. Check coverage report
coverage report -m

# 5. Generate HTML report for detailed analysis
coverage html
```

#### 2. CI/CD Pipeline Commands
```bash
# Complete CI pipeline
coverage erase                                    # Clear previous data
coverage run -m unittest discover tests          # Run tests with coverage
coverage report --fail-under=80                  # Ensure minimum coverage
coverage xml                                      # Generate XML for CI tools
coverage html                                     # Generate HTML report
```

#### 3. Multi-Module Testing
```bash
# Test multiple modules separately
coverage run --source=module1 -m unittest discover tests/test_module1
coverage run --source=module2 --append -m unittest discover tests/test_module2
coverage report

# Or test everything together
coverage run --source=module1,module2 -m unittest discover tests
coverage report
```

### Interpreting Coverage Reports

#### Console Report Format
```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
my_module.py            20      4    80%   23-26
another_module.py       15      0   100%
--------------------------------------------------
TOTAL                   35      4    89%
```

#### HTML Report Features
- Line-by-line coverage visualization
- Branch coverage (if enabled)
- Missing lines highlighted
- Sortable columns
- Search functionality

### Troubleshooting Common Issues

#### 1. Import Errors
```bash
# Add current directory to Python path
PYTHONPATH=. python -m unittest discover

# Or use explicit path
python -m unittest discover -s tests -t .
```

#### 2. Coverage Data Issues
```bash
# Clear coverage data if corrupted
coverage erase

# Check coverage data location
coverage debug data

# Debug configuration
coverage debug config
```

#### 3. Test Discovery Issues
```bash
# Ensure __init__.py files exist in test directories
touch tests/__init__.py

# Check test naming convention (must start with 'test')
ls tests/test_*.py

# Verify test class inherits from unittest.TestCase
```

### Best Practices

1. **Organize Tests**: Keep tests in separate `tests/` directory
2. **Naming Convention**: Use `test_*.py` for test files, `Test*` for classes, `test_*` for methods
3. **Coverage Goals**: Aim for 80-90% coverage, 100% for critical code
4. **Regular Testing**: Run tests frequently during development
5. **CI Integration**: Include coverage reporting in your CI/CD pipeline
6. **Documentation**: Document test cases and expected behaviors

### Example Makefile for Automation
```makefile
test:
	python -m unittest discover -v

test-coverage:
	coverage run -m unittest discover
	coverage report -m

test-html:
	coverage run -m unittest discover
	coverage html
	@echo "Open htmlcov/index.html in browser"

clean-coverage:
	coverage erase
	rm -rf htmlcov/

.PHONY: test test-coverage test-html clean-coverage
```

This comprehensive guide covers all the major options and use cases for running Python tests with unittest and generating coverage reports.