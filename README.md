
# HEIC to JPG Converter

A Python script that converts HEIC (High Efficiency Image Container) files to JPG and logs the conversion process to a log file.

## Requirements

- Python 3
- ImageMagick (installed and added to the system PATH)

## Usage

1. Clone the repository or download the script.
2. Edit the `input_dir` variable in the script to specify the directory containing the HEIC files.
3. Edit the `log_file` variable in the script to specify the path to the log file.
4. Run the script using `python /path/to/converter.py`.

### Cron Job

To set up a cron job to run the script at a specific time:

1. Open a terminal window and enter the following command to edit the crontab file for the current user:
   ```
   bash
   crontab -e
   ```
2. Add a line to the crontab file specifying when and how often to run the script. For example, to run the script every Sunday at 10 AM, add the following line (replacing /path/to/converter.py with the actual path to the script):
```
0 10 * * 0 python /path/to/converter.py
```
Save and close the crontab file.

## Credits
Script developed by [@balgaly](https://github.com/balgaly)

ImageMagick command line tool used for the conversion process.

I hope this helps! Let me know if you have any other questions.
