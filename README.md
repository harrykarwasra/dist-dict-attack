# Distributed Dictionary Attack

A Distributed Dictionary Attack implemetation using Python, and detection using Scapy.

## Requirements

* Python 3.6+

## Usage

### Setup Instructions

* Clone this repository.
* Run `pip3 install -r requirements.txt` on repository root to install dependencies.
* Set up a local/remote MySQL server (database templete in `pass_dict.sql`, can be
  imported directly).
* Update the credentials of the SQL server in the first few lines of `sql.py`.

### Attack

* Run `python3 dict_attack.py`.

### Detect

* Generate a pcap file on FTP server host or use `test.pcap` provided with this repo.
* Run `python3 ftp_attack_report.py`.

## Development

* Please open an issue if you find a bug or would like to see a feature added to the
  project.
* Pull requests fixing issues or adding relevant features are welcome!

## Licence

This project is licensed under the MIT License.
