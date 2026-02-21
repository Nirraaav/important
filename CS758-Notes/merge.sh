#!/bin/bash

# Define the output filename
OUTPUT_FILE="Merged_Lectures_08_to_13.pdf"

# Initialize an empty array to hold the filenames
files=()

# Loop through the numbers 2 to 13
for i in {8..13}; do
    # Format the number to be exactly 2 digits (e.g., 02, 03... 10, 11)
    num=$(printf "%02d" $i)
    filename="Lecture - ${num}.pdf"
    
    # Verify the file actually exists before adding it to the list
    if [[ -f "$filename" ]]; then
        files+=("$filename")
    else
        echo "Warning: '$filename' not found. Skipping..."
    fi
done

# Check if we found any files to merge
if [ ${#files[@]} -eq 0 ]; then
    echo "Error: No files found to merge. Please check your current directory."
    exit 1
fi

echo "Found ${#files[@]} files. Starting merge with pdfunite..."

# Syntax: pdfunite input1.pdf input2.pdf ... output.pdf
pdfunite "${files[@]}" "$OUTPUT_FILE"

# Check if the command succeeded
if [ $? -eq 0 ]; then
    echo "Success! Files merged into: $OUTPUT_FILE"
else
    echo "Error: pdfunite encountered a problem."
fi
