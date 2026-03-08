# AI Context

## Project vision

Build a modular embodied AI home robot that combines conversation, memory, and physical interaction.

## System architecture

The platform follows Hexagonal Architecture and DDD bounded contexts, starting as a modular monolith in a monorepo.

## Robotics goals

Enable progressive integration with ROS2, hardware controllers, and sensor pipelines while preserving clean domain boundaries.

## Current development phase

Repository and architecture foundation are complete. Current work is an early phase-1 interaction slice:

- operational state model
- head expression mapping
- conversation turn model
- green unit tests for these domain elements

## Hardware

- Raspberry Pi 4 (core runtime and device control)
- Android phone (head device and interaction surface)
