# ChunkZip - Split Large Zip Files

A Python script that splits large zip files containing media files into smaller chunks of maximum 1GB each.

## Features

- Automatically finds all zip files in the input folder
- Splits them into chunks not exceeding 1GB
- Preserves file integrity and structure
- Creates organized output with numbered parts

## Complete Workflow: Cloud Storage to Android Phone

This workflow helps you transfer large amounts of media from cloud storage to your Android phone:

### Step 1: Download from Cloud Storage
1. **Find the starting date** - Identify the date from where files are taking up storage
2. **Select files** - Select all files from that date till today
3. **Download** - Download the selected files
   - Note the item count and total size for reference
4. **Clean up cloud** - After download completes, delete files from cloud storage

### Step 2: Prepare and Chunk the Zip File
5. **Place in input folder** - Move or copy your downloaded zip file to the `input` folder of ChunkZip
6. **Run ChunkZip** - Execute the script to split the zip into 1GB chunks:
   ```bash
   python split_zip_files.py
   ```

### Step 3: Transfer to Android Phone
7. **Install Android File Transfer** (macOS):
   ```bash
   brew install android-file-transfer
   ```
8. **Transfer chunks** - Copy all chunk zip files from the `output` folder to your Android phone

### Step 4: Extract on Phone
9. **Extract and clean** - On your Android phone:
   - Extract each zip file one by one
   - Delete the zip file after extraction to free up storage space
   - Repeat for all chunks

### Result
Your phone storage is now populated with your media files without exceeding size limitations during transfer.

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
