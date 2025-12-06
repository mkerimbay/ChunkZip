# ChunkZip - Split Large Zip Files

A Python script that splits large zip files containing media files into smaller chunks of maximum 1GB each.

## Features

- Automatically finds all zip files in the input folder
- Splits them into chunks not exceeding 1GB
- Preserves file integrity and structure
- Creates organized output with numbered parts

## Usage

### Basic usage (with default folders):

```bash
python split_zip_files.py
```

This will:
- Look for zip files in `./input` folder
- Create split zip files in `./output` folder

### Custom input/output folders:

```bash
python split_zip_files.py -i /path/to/input -o /path/to/output
```

### Options:

- `-i, --input`: Input folder containing zip files (default: `./input`)
- `-o, --output`: Output folder for split zip files (default: `./output`)

## Example

```bash
# Create input folder and add your zip files
mkdir input
# Copy your large zip files to the input folder

# Run the script
python split_zip_files.py

# Check the output folder for results
ls output/
```

## Output Format

If you have a zip file named `vacation_photos.zip`, the script will create:
- `vacation_photos_part1.zip` (max 1GB)
- `vacation_photos_part2.zip` (max 1GB)
- `vacation_photos_part3.zip` (and so on...)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)
