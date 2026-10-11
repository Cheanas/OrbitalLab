# Global build argument
ARG UV_VERSION

# Stage 1: Select the uv version
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

# Stage 2: Build OrbitalLab
FROM python:3.12-slim AS builder

COPY --from=uv /uv /uvx /bin/

WORKDIR /orbitallab

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync --locked --no-install-project

COPY . .

RUN uv sync --locked

# Stage 3: Runtime
FROM python:3.12-slim

WORKDIR /orbitallab

COPY --from=builder /orbitallab/.venv /orbitallab/.venv
COPY --from=builder /orbitallab/pyproject.toml /orbitallab/pyproject.toml
COPY --from=builder /orbitallab/src /orbitallab/src
COPY --from=builder /orbitallab/tests /orbitallab/tests

ENV PATH="/orbitallab/.venv/bin:$PATH"

CMD ["pytest"]