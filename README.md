# PoC Collector

* This is the little script to collect the proof-of-concept which is refered from [nomi-sec](https://github.com/nomi-sec/PoC-in-GitHub).
* The repository now is only develop for linux-based operating system

## Usage
* Initialize first
	```bash
	python3 Collector.py --init
	```
* Update the sources
	```bash
	python3 Collector.py --update
	```
* Find specified PoC of vulnerability
	```bash
	python3 Collector.py --search=[CVE Number]
	```
* Clone the PoC in Github
	```bash
	python3 Collector.py --clone=[CVE Number]
	```
