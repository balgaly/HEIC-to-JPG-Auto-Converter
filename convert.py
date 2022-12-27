import datetime
import os
import random
import subprocess
import time

# Set the directory containing the HEIC files
input_dir = "INPUT_DIR"

# Set the log file path
log_file = "LOG_FILE_PATH"

# Get a list of all HEIC files in the input directory
heic_files = [f for f in os.listdir(input_dir) if f.endswith(".heic") or f.endswith(".HEIC")]

# Calculate the total number of files to process
total_files = len(heic_files)

# Initialize a counter for the number of files processed
processed_files = 0

# Log the start of the run to the log file
with open(log_file, "a") as f:
  f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Started conversion of {total_files} HEIC files\n")

# Loop through each HEIC file
for file in heic_files:
  # Get the full path to the HEIC file
  file_path = os.path.join(input_dir, file)

  # Generate a random 6-digit suffix to add to the file name
  suffix = "".join([str(random.randint(0, 9)) for _ in range(6)])

  # Build the new file name by adding the suffix to the file name
  new_file_name = f"{file[:-5]}-{suffix}.jpg"

  # Build the full path to the new file
  new_file_path = os.path.join(input_dir, new_file_name)

  # Convert the HEIC file to JPG using the "convert" command from ImageMagick
  result = subprocess.run(["convert", file_path, new_file_path])

  # Check if the conversion was successful
  if result.returncode == 0:
    # Conversion was successful, so delete the original HEIC file
    os.remove(file_path)

    # Log the conversion to the log file
    with open(log_file, "a") as f:
      f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Converted {file} to {new_file_name} and deleted original HEIC file\n")
  else:
    # Conversion was not successful, log an error message to the log file
    with open(log_file, "a") as f:
      f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Error converting {file} to JPG\n")

  # Increment the counter for the number of processed files
  processed_files += 1

  # Calculate the progress in percent
  progress = int((processed_files / total_files) * 100)

  # Log the progress to the log file every 10 seconds
  if processed_files % 10 == 0:
    with open(log_file, "a") as f:
      f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Processed {processed_files} of {total_files} files ({progress}%)\n")

# Log the end of the run to the log file
with open(log_file, "a") as f:
  f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Finished conversion of {total_files} HEIC files\n")
