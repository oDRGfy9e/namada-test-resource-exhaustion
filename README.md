# Namada Testnet Node Vulnerability Test for Resource Exhaustion

## Introduction

This repository addresses a critical security concern involving a resource exhaustion vulnerability in the h2 library, which could potentially lead to a Denial of Service (DoS) attack on Namada testnet nodes. The vulnerability allows an attacker to cause excessive resource consumption by exploiting specific behaviors in the HTTP/2 implementation, potentially destabilizing the node or making it unresponsive.

The purpose of this project is to share a testing script designed to evaluate the resilience of Namada testnet nodes against such resource exhaustion attacks. By conducting this test, we aim to identify nodes that are susceptible to this vulnerability, enabling timely mitigation efforts to safeguard the network.

## Vulnerability Details

- **Nature of Vulnerability:** Resource Exhaustion in h2 Library
- **Impact:** Potential Denial of Service (DoS)
- **Affected Component:** RPC endpoints utilizing the h2 library for HTTP/2 communications

## Test Script

The `namada_rpc_exhaustion_test.py` script simulates an attack scenario by sending a large volume of HTTP/2 requests to the targeted RPC endpoint, aiming to trigger the resource exhaustion condition.

### Prerequisites

- Python 3.x
- `hyper` library (for HTTP/2 support)

To install the `hyper` library, run:

```bash
pip install hyper

### Results

Upon running the script, nodes vulnerable to the resource exhaustion issue might exhibit one or more of the following symptoms:

- Significant slowdown in response times
- Increased error rates for incoming requests
- Abnormal spikes in CPU or memory usage

### More tests
Stress enough to crash the node.
