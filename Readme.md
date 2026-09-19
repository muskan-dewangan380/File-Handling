# File Handling

## Overview

This assignment demonstrates the fundamental concepts of **Python File Handling** using a retail sales analytics scenario.

The programs cover creating files, writing data, reading data in different ways, appending new records, extracting numerical information from files, accepting user input, and safely checking whether a file exists before opening it.

The assignment is implemented using only **core Python file-handling features**.

---

## Topics Covered

* Opening files using different modes

  * `r` – Read
  * `w` – Write
  * `a` – Append
  * `r+` – Read and Write
  * `w+` – Write and Read
* `open()`
* `with open()`
* `read()`
* `readline()`
* `readlines()`
* `write()`
* File existence checking using `os.path.exists()`
* String cleanup using `strip()`
* Converting text data into integers
* Basic calculations using built-in Python functions

---

## Project Structure

```text
File_Handling/
│
├── write_sales.py
├── read_file.py
├── append_sales.py
├── sales_summary.py
├── product_info.py
├── safe_file_read.py
│
├── sales_data.txt
├── products.txt
└── README.md
```

---

# Task 1: Write Sales Records to a File

### File

`write_sales.py`

### Description

Creates a list of sales amounts and writes each sale to `sales_data.txt` on a separate line.

The program then reopens the file in read mode and displays its contents.

### Concepts Used

* List
* `open()`
* Write mode (`w`)
* `write()`
* Read mode (`r`)
* `read()`
* `with open()`

### Output File

`sales_data.txt`

---

# Task 2: Read File in Different Ways

### File

`read_file.py`

### Description

Reads the existing `sales_data.txt` file using three different file-reading methods:

1. `read()` – Reads the entire file.
2. `readline()` – Reads the first line.
3. `readlines()` – Reads all lines.

The newline characters are removed using `strip()`, and the sales values are converted into integers.

### Concepts Used

* `read()`
* `readline()`
* `readlines()`
* `strip()`
* List comprehension
* Integer conversion

### Dependency

This task requires:

```text
sales_data.txt
```

Run **Task 1 before Task 2** if the file does not already exist.

---

# Task 3: Append New Sales

### File

`append_sales.py`

### Description

Adds new sales values to the existing `sales_data.txt` file without deleting the previously stored records.

The program uses append mode (`a`) and then reads the complete updated file.

### New Sales Added

```text
5000
2500
1700
```

### Concepts Used

* Append mode (`a`)
* `write()`
* `read()`
* `readlines()`
* `with open()`

### Dependency

This task uses:

```text
sales_data.txt
```

Run **Task 1 before Task 3** if the file does not already exist.

---

# Task 4: Generate Sales Summary Report

### File

`sales_summary.py`

### Description

Reads all sales values from `sales_data.txt`, converts them into integers, and calculates:

* Total Sales
* Highest Sale
* Lowest Sale
* Average Sale

### Concepts Used

* File reading
* `readlines()`
* `strip()`
* Integer conversion
* `sum()`
* `max()`
* `min()`
* `len()`

### Dependency

This task requires:

```text
sales_data.txt
```

For the complete assignment flow, run Tasks 1–3 before Task 4.

---

# Task 5: Create Product Information File

### File

`product_info.py`

### Description

Accepts the names and prices of three products from the user.

The information is written to `products.txt` in the following format:

```text
ProductName | Price
```

The program then reads the file and displays each product record.

### Concepts Used

* User input
* `input()`
* Write mode (`w`)
* `write()`
* Read mode (`r`)
* File iteration
* `strip()`

### Output File

```text
products.txt
```

### Example

```text
Mouse | 500
Keyboard | 800
Monitor | 7000
```

---

# Task 6: Read File Safely

### File

`safe_file_read.py`

### Description

Asks the user to enter a filename and checks whether the file exists before attempting to open it.

The program uses:

```python
os.path.exists()
```

If the file exists, its contents are displayed.

If the file does not exist, the following message is displayed:

```text
File not found. Please check the filename.
```

### Concepts Used

* `os.path.exists()`
* Conditional statements
* `with open()`
* `read()`
* Basic file safety

---

# How to Run the Programs

## Step 1: Open the Project Folder

Open the `File_Handling` folder in your preferred Python IDE or terminal.

## Step 2: Run Task 1

```bash
python write_sales.py
```

This creates:

```text
sales_data.txt
```

## Step 3: Run Task 2

```bash
python read_file.py
```

## Step 4: Run Task 3

```bash
python append_sales.py
```

This adds the new sales to `sales_data.txt`.

## Step 5: Run Task 4

```bash
python sales_summary.py
```

## Step 6: Run Task 5

```bash
python product_info.py
```

Enter the names and prices of three products when prompted.

## Step 7: Run Task 6

```bash
python safe_file_read.py
```

Enter the name of a file when prompted.

---

# Important File Dependencies

| Task   | Python File         | Input File             | Output File              |
| ------ | ------------------- | ---------------------- | ------------------------ |
| Task 1 | `write_sales.py`    | None                   | `sales_data.txt`         |
| Task 2 | `read_file.py`      | `sales_data.txt`       | None                     |
| Task 3 | `append_sales.py`   | `sales_data.txt`       | Updated `sales_data.txt` |
| Task 4 | `sales_summary.py`  | `sales_data.txt`       | None                     |
| Task 5 | `product_info.py`   | User input             | `products.txt`           |
| Task 6 | `safe_file_read.py` | User-provided filename | None                     |

---

# File Modes Demonstrated

| Mode | Purpose                                         |
| ---- | ----------------------------------------------- |
| `r`  | Read an existing file                           |
| `w`  | Write to a file; creates or overwrites the file |
| `a`  | Append data to the end of a file                |
| `r+` | Read and write without truncating the file      |
| `w+` | Write and read; overwrites or creates the file  |

The implemented tasks primarily use `r`, `w`, and `a` because they directly match the requirements of the individual tasks.

---

# Restrictions Followed

This assignment follows the specified restrictions:

* No `pandas`
* No `csv` module
* No external libraries
* Uses core Python functionality
* Uses `with open()` for safe file handling
* Uses basic file-reading and writing operations
* Uses `os.path.exists()` only where required for file existence checking

---

# Expected Files After Execution

After running the required tasks, the project directory will contain:

```text
File_Handling/
│
├── write_sales.py
├── read_file.py
├── append_sales.py
├── sales_summary.py
├── product_info.py
├── safe_file_read.py
│
├── sales_data.txt
├── products.txt
└── README.md
```

---

## Conclusion

This assignment demonstrates the practical use of Python file handling for storing, reading, updating, and processing retail data. It also demonstrates safe file operations using `with open()` and basic file existence validation.
