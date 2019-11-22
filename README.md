# PingScan

This script performs a `ping` command to every single network host on an IP range. This uses the `subprocess`
Python module which presents as an OS API for Python. The whole idea is to evaluate if can be accessible from "the attacker" perspective

Internally, the `pingscan.py` script handles the program workflow and exceptions if occurs.

For each IP address, the script runs a `ping -c 1 [IP]` and attempts to get a `ECHO_REPLY` (ICMP Protocol response) to whatever IP is on the network segment available. The `ECHO_REPLY` is evaluated on a string comparison of the `stdout` Pipe.

The `ping` command uses the `ICMP protocol`, which basically is a message protocol to get to know if a machine is available/active or not. The client does a `ECHO_REQUEST` and the requested machine will respond to a `ECHO_REPLY` object to it.

## WorkFlow

Basically the subprocess module sets up like an interface (`Popen class`) to the terminal, this does the `ping` command and waits for the response. Any program product is handled by `pipes` for errors, input, and output.

## Usage

`python 192.168.1` or any of network segment reachable.

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
