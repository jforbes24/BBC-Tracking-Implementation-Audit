# BBC Python Screaming Frog Extraction

This Python script processes a CSV file extracted from Screaming Frog for BBC iPlayer URLs. It limits the number of entries per container to 5 and saves the results in a new CSV file.

## Features

- Extracts data from Screaming Frog CSV files.
- Identifies columns based on specific patterns (`data-bbc-container`, `data-bbc-content-label`, `data-bbc-metadata`, `href`).
- Groups data by `data-bbc-container` and limits entries to 5 per container.
- Saves processed data to a new CSV file.

## Requirements

- Python 3.x
- Pandas library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jforbes24/BBC-Python.git
   cd BBC-Python
   ```

2. Install the required Python library:
   ```bash
   pip install pandas
   ```

## Usage

1. Place the Screaming Frog CSV file at the path:
   ```
   /Users/forbej02/Documents/Screaming Frog/web_iplayer_screamingFrog_extraction.csv
   ```

2. Run the script:
   ```bash
   python web_iplayer_screamingFrog_extraction.py
   ```

3. The processed data will be saved to:
   ```
   /Users/forbej02/Documents/Screaming Frog/web_iplayer_extractions_limited.csv
   ```

## File Structure

```
.gitattributes
web_iplayer_screamingFrog_extraction.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Visualization

The processed data can be visualized using a Tableau dashboard. Below are screenshots of the dashboard:

### Example Dashboarding Pipeline Flow:
![Tableau - Screaming Frog Web iPlayer Tracking Implementation - Doc 2025-07-07 12-44-25](https://github.com/user-attachments/assets/70203993-7c33-4c11-9522-2aa475e50f61)

### Detailed View of Screaming Frog data-pivot:
![Tableau - Screaming Frog Web iPlayer Tracking Implementation - ScreamingFrog pivot 2025-07-07 12-45-25](https://github.com/user-attachments/assets/0350e4ec-4c4b-415e-8652-03026d416e20)

### Example Use Cases to explore and Aggregate this data:
![Tableau - Screaming Frog Web iPlayer Tracking Implementation - Audit Use Cases 2025-07-07 12-46-08](https://github.com/user-attachments/assets/ca53d8aa-29ef-4de0-b43a-57bb57edd3a3)

### Next Steps..
<img width="1304" alt="Tableau - Screaming Frog Web iPlayer Tracking Implementation - Next Steps 2025-07-07 12-46-52" src="https://github.com/user-attachments/assets/0faa8336-5917-42e0-b2a4-e4175fbcde01" />


To recreate the dashboard, import the processed CSV file (`web_iplayer_extractions_limited.csv`) into Tableau and follow your preferred visualization steps.

## Author

Created by James Forbes.
