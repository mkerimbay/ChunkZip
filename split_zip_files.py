#!/usr/bin/env python3
"""
Split large zip files containing media into smaller chunks (max 1GB each).
"""

import os
import zipfile
import argparse
from pathlib import Path


# Maximum size for each output zip file (1 GB)
MAX_ZIP_SIZE = 1 * 1024 * 1024 * 1024  # 1 GB in bytes


def get_zip_files(input_folder):
    """Get all zip files from the input folder."""
    input_path = Path(input_folder)
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_folder}")

    zip_files = list(input_path.glob("*.zip"))
    return zip_files


def split_zip_file(zip_path, output_folder):
    """
    Split a zip file into multiple smaller zip files (max 1GB each).

    Args:
        zip_path: Path to the input zip file
        output_folder: Path to the output folder
    """
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    base_name = zip_path.stem  # Get filename without extension
    part_number = 1
    current_size = 0
    current_zip = None
    current_zip_path = None

    print(f"Processing: {zip_path.name}")

    try:
        with zipfile.ZipFile(zip_path, 'r') as source_zip:
            # Get all files sorted by name for consistent ordering
            file_list = sorted(source_zip.namelist())

            for file_name in file_list:
                file_info = source_zip.getinfo(file_name)
                file_size = file_info.file_size

                # Check if we need to create a new zip file
                if current_zip is None or (current_size + file_size > MAX_ZIP_SIZE and current_size > 0):
                    # Close previous zip if exists
                    if current_zip is not None:
                        current_zip.close()
                        print(f"  Created: {current_zip_path.name} ({current_size / (1024*1024):.2f} MB)")

                    # Create new zip file
                    current_zip_path = output_path / f"{base_name}_part{part_number}.zip"
                    current_zip = zipfile.ZipFile(current_zip_path, 'w', zipfile.ZIP_DEFLATED)
                    part_number += 1
                    current_size = 0

                # Add file to current zip
                file_data = source_zip.read(file_name)
                current_zip.writestr(file_info, file_data)
                current_size += file_size

            # Close the last zip file
            if current_zip is not None:
                current_zip.close()
                print(f"  Created: {current_zip_path.name} ({current_size / (1024*1024):.2f} MB)")

    except zipfile.BadZipFile:
        print(f"  Error: {zip_path.name} is not a valid zip file")
    except Exception as e:
        print(f"  Error processing {zip_path.name}: {str(e)}")
        if current_zip is not None:
            current_zip.close()


def main():
    parser = argparse.ArgumentParser(
        description="Split zip files into smaller chunks (max 1GB each)"
    )
    parser.add_argument(
        "-i", "--input",
        default="input",
        help="Input folder containing zip files (default: ./input)"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Output folder for split zip files (default: ./output)"
    )

    args = parser.parse_args()

    print(f"Input folder: {args.input}")
    print(f"Output folder: {args.output}")
    print(f"Max zip size: {MAX_ZIP_SIZE / (1024*1024*1024):.1f} GB\n")

    # Get all zip files from input folder
    try:
        zip_files = get_zip_files(args.input)

        if not zip_files:
            print(f"No zip files found in {args.input}")
            return

        print(f"Found {len(zip_files)} zip file(s)\n")

        # Process each zip file
        for zip_file in zip_files:
            split_zip_file(zip_file, args.output)

        print(f"\nDone! Check the '{args.output}' folder for results.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
