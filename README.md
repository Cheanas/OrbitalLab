# OrbitalLab

**OrbitalLab** is an open-source Python project dedicated to orbital mechanics, numerical simulations, and scientific computing.

The goal is to build a reliable, modular simulation engine from the ground up, starting with Newtonian physics and progressively exploring numerical methods, distributed computing, and cloud infrastructure.

> **Project status:** Early development. The scientific simulation engine is not yet implemented.

## Objectives

OrbitalLab aims to:

- Implement a scientific simulation engine based on Newtonian mechanics.
- Model gravitational interactions between celestial bodies.
- Simulate orbital trajectories using numerical integration.
- Analyze numerical accuracy, stability, and conservation laws.
- Provide reproducible simulations and automated scientific tests.
- Expose simulation capabilities through APIs.
- Explore distributed execution and cloud infrastructure.

The project prioritizes **scientific correctness, clean architecture, reproducibility, and maintainability**.

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| Dependency management | uv |
| Scientific computing | NumPy |
| Testing | pytest |
| Coverage | pytest-cov |
| Linting and formatting | Ruff |
| Static type checking | mypy |
| Containerization | Docker and Docker Compose |
| Continuous integration | GitHub Actions |

Additional technologies may be introduced as the project evolves.

## Getting Started

### Prerequisites

For local development:

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- Git

For containerized development:

- Docker
- Docker Compose

### Clone the Repository

```bash
git clone https://github.com/Cheanas/OrbitalLab.git
cd OrbitalLab
```

### Install Dependencies

OrbitalLab uses `uv` to manage Python dependencies and virtual environments.

Install the dependencies:

```bash
uv sync --locked
```

This creates a virtual environment and installs the dependencies specified in `uv.lock`.

Run Python commands through uv:

```bash
uv run python --version
```

There is no need to activate the virtual environment manually.

## Development

### Run Tests

```bash
uv run pytest
```

Tests are located in the `tests/` directory.

### Run Linting

```bash
uv run ruff check .
```

To automatically fix supported linting issues:

```bash
uv run ruff check . --fix
```

### Check Formatting

```bash
uv run ruff format --check .
```

To format the code:

```bash
uv run ruff format .
```

### Run Static Type Checking

```bash
uv run mypy src tests
```

OrbitalLab uses strict type checking to help maintain reliable scientific code.

### Test Coverage

Coverage reporting is configured through pytest.

Run:

```bash
uv run pytest
```

The coverage report is displayed in the terminal.

> **Note:** During the initial project setup, coverage percentages may not be meaningful because the scientific engine has not yet been implemented.

## Docker

OrbitalLab provides a Docker-based environment for reproducible development and testing.

The Docker image uses a multi-stage build to install dependencies and package the application.

### Configure the Environment

Docker Compose requires the uv version to be provided through an environment variable.

Create a `.env` file at the project root:

```dotenv
UV_VERSION=0.13.0
```

The `.env` file is excluded from the Docker build context.

### Build the Image

```bash
docker compose build
```

Docker caches dependency installation layers to improve subsequent build performance.

### Run Tests

```bash
docker compose run --rm orbitallab
```

The default container command executes pytest.

### Run Linting

```bash
docker compose run --rm orbitallab ruff check .
```

### Check Formatting

```bash
docker compose run --rm orbitallab ruff format --check .
```

### Run Type Checking

```bash
docker compose run --rm orbitallab mypy src tests
```

### Open an Interactive Shell

```bash
docker compose run --rm -it orbitallab sh
```

### Clean Up

Remove Compose containers and networks:

```bash
docker compose down
```

This does not remove the Docker image.

## Project Structure

```text
OrbitalLab/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   └── orbitallab/
│       ├── __init__.py
│       └── core/
│           └── __init__.py
│
├── tests/
│   └── orbitallab/
│       └── test_package.py
│
├── .dockerignore
├── .gitignore
├── .python-version
├── Dockerfile
├── compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

### Scientific Core

The `src/orbitallab/core/` package will contain the scientific simulation engine.

Its initial responsibilities will include:

- Vector mathematics.
- Physical bodies and their properties.
- Gravitational force calculations.
- Numerical integration.
- Simulation state management.

The scientific core is intended to remain independent of HTTP APIs, databases, message brokers, and infrastructure-specific dependencies.

This separation allows the simulation engine to be tested and reused without requiring external services.

## Scientific Approach

OrbitalLab begins with a simplified physical model:

- Two-dimensional space.
- Newtonian gravitational interactions.
- Point-mass bodies.
- SI units.
- Deterministic simulation steps.

### Newtonian Gravitation

The magnitude of the gravitational force between two bodies is:

$$
F = G \frac{m_1 m_2}{r^2}
$$

Where:

- $F$ is the gravitational force.
- $G$ is the gravitational constant.
- $m_1$ and $m_2$ are the masses of the bodies.
- $r$ is the distance between their centers.

### Numerical Integration

The initial simulation engine will use the semi-implicit Euler method.

For a time step $\Delta t$:

$$
\vec{v}_{n+1} = \vec{v}_n + \vec{a}_n \Delta t
$$

$$
\vec{x}_{n+1} = \vec{x}_n + \vec{v}_{n+1} \Delta t
$$

Unlike explicit Euler integration, semi-implicit Euler updates the position using the new velocity.

This method provides a simple starting point for studying numerical stability in orbital simulations.

Future versions may explore more advanced integration methods.

## Roadmap

OrbitalLab is organized into six development milestones.

### Milestone 1 — Scientific Foundations

Establish the mathematical and physical foundations of the project.

Planned work includes:

- Python project initialization and quality tooling.
- Two-dimensional vector mathematics.
- Physical constants and units.
- Celestial body representation.
- Gravitational interactions.

### Milestone 2 — Two-Body Simulation

Develop the first functional orbital simulation.

Planned work includes:

- Simulation state representation.
- Semi-implicit Euler integration.
- Two-body gravitational simulation.
- Trajectory analysis.
- Scientific validation and regression testing.

### Milestone 3 — REST Engine Service

Expose the simulation engine through a REST API.

The API will remain separate from the scientific core.

### Milestone 4 — Distributed Execution

Explore asynchronous and distributed simulation execution.

Potential technologies include message brokers, background workers, and gRPC.

These technologies will be introduced only when justified by the project's requirements.

### Milestone 5 — Cloud and Observability

Explore deployment, monitoring, logging, and infrastructure automation.

### Milestone 6 — Advanced Scientific Research

Investigate more advanced physical models, numerical methods, and simulation capabilities.

This milestone represents longer-term research rather than the initial project scope.

## Continuous Integration

OrbitalLab uses GitHub Actions for automated quality checks.

The CI workflow is intended to run on:

- Pushes to the `main` branch.
- Pull requests targeting `main`.

The quality pipeline includes:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

All checks should pass before changes are merged.

## Contributing

Contributions, bug reports, and technical discussions are welcome.

When contributing:

1. Create a branch for your changes.
2. Keep changes focused and reasonably scoped.
3. Add or update tests when implementing functionality.
4. Run the quality checks locally.
5. Open a pull request describing the changes.

Scientific implementations should clearly document their assumptions, units, and numerical limitations.

## Design Principles

OrbitalLab follows several core principles:

**Scientific correctness**

Physical models and numerical methods should be validated against known results whenever possible.

**Separation of concerns**

Scientific calculations should not depend on transport protocols or infrastructure services.

**Reproducibility**

Simulation inputs, numerical methods, and dependencies should be explicit and reproducible.

**Incremental complexity**

The project starts with a simple, well-tested simulation engine before introducing more advanced infrastructure.

**Maintainability**

Readable code, type annotations, automated tests, and clear documentation are preferred over unnecessary abstraction.

## License

A license has not yet been selected.

Before accepting external contributions or distributing the project under an open-source license, an appropriate `LICENSE` file should be added.