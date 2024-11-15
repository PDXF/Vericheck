# VeriCheck - Advanced CLI Validator

Welcome to **VeriCheck** - Your Advanced CLI Validator for a wide variety of input data types including email addresses, IP addresses, vehicle details, finance and identity information, technology identifiers, and more.

## Overview

**VeriCheck** is a command-line interface (CLI) tool designed to validate different types of data inputs using regular expressions. The tool allows you to validate data like IP addresses, email addresses, vehicle identification numbers, social media handles, and more.

This validator provides an interactive, page-based menu system to guide users in selecting the appropriate validation type, all presented in an intuitive way with color-coded feedback.

## Features

- Validate **40+ data types** across different categories including personal information, finance, health, and technology.
- Organized **multi-page menu** for easy navigation.
- **Color-coded outputs** for better readability.
- **Regex-based validation** to ensure input data meets required formats.

### Supported Data Types Include:

1. **General Information**: Email, IP Address, URL, Phone Number, etc.
2. **Vehicle Information**: VIN, License Plate, IMEI, etc.
3. **Finance & Identity**: Credit Card Number, SSN, IBAN, Bitcoin Address, etc.
4. **Social Media**: Discord Token, Instagram Handle, LinkedIn Profile URL, etc.
5. **Location**: Latitude/Longitude, Geohash, Postal Address, etc.
6. **Technology Identifiers**: UUID, IP Range (CIDR), GitHub URL, etc.
7. **Health Identifiers**: NPI, NHS Number, Medical Insurance Policy, etc.
8. **Document Identifiers**: ISBN, DOI, ISSN, etc.

## Prerequisites

- Python 3.x
- **colorama** for color-coded terminal output. To install it, run:

  ```sh
  pip install colorama
  ```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/vericheck.git
   cd vericheck
   ```

2. Install the necessary dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   > Note: The `requirements.txt` should contain `colorama`.

## Usage

To start VeriCheck, simply run:

```sh
python vericheck.py
```

### Navigating the Menu

- After launching VeriCheck, you will see a **menu** to choose the data type to validate.
- Use `<` or `>` to navigate between different **pages** of the menu.
- **Enter the number** corresponding to the data type you want to validate.
- **Input the data** when prompted.

### Example

- To validate an **email address**:
  1. Start the script using `python vericheck.py`.
  2. Select **1** for "Email Address".
  3. Enter the email you want to validate.

If the email is valid, you will see a **green success message**; if not, an **error message in red**.

## Directory Structure

```
vericheck/
|-- vericheck.py
|-- README.md
|-- requirements.txt
```

- **vericheck.py**: The main Python script for data validation.
- **README.md**: Documentation of the project.
- **requirements.txt**: List of dependencies.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. All contributions are welcome, whether it's fixing a bug or adding a new type of data validation!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Issues

If you encounter any issues while using VeriCheck, please submit an issue on the [GitHub repository](https://github.com/yourusername/vericheck/issues).

## Future Plans

- Add validation for more specialized fields.
- Improve user experience by adding more detailed feedback for validation failures.
- Add support for exporting the results to a file.

## Contact

If you have any questions or feedback, feel free to contact us at: 
- Email: **your-email@example.com**
- GitHub: [YourUsername](https://github.com/yourusername)

Enjoy using **VeriCheck** to make your data validation process easier and more efficient!
