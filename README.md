# Concussion Risk Monitor — ROS 2

A simulated real-time head impact monitoring pipeline built with ROS 2 Humble.
Models the kind of system used in professional sports helmet sensors (e.g. NFL, NHL).

## Architecture

helmet_sensor → /head_impact → impact_monitor → /alerts → session_logger

## Nodes

- **helmet_sensor** — publishes simulated g-force at 2Hz. Injects random hit events (~10% chance per reading)
- **impact_monitor** — flags single hits >80g and cumulative session exposure >300g (based on real concussion research thresholds)
- **session_logger** — maintains a timestamped event log of all alerts

## How to run

Requires Docker + ROS 2 Humble.

# terminal 1
python3 helmet_sensor.py

# terminal 2
python3 impact_monitor.py

# terminal 3
python3 session_logger.py

## Why this matters

Repeated sub-concussive impacts are linked to CTE (Chronic Traumatic Encephalopathy).
This pipeline models the cumulative exposure tracking used in real sports safety research.
