# Prism Data Intelligence Platform

An integrated, dependency-free reference platform for BI, analytics, reporting,
data warehouse, data lake, lakehouse, DBMS, integration, ETL/ELT, iPaaS,
catalog, governance, quality, MDM, observability, fabric, mesh, big data,
stream processing, CEP, OLAP and decision support.

It also includes a local-first AI/ML control plane: real tabular training and
serving, a versioned model registry, drift detection, a small neural network,
embeddings, persistent vector search, grounded conversational RAG, allowlisted
agents, NLP, Document AI, recommendation ranking and portable-graymap vision.

## What is implemented

- Persistent SQLite control plane with assets, versioned datasets, jobs, quality
  results, lineage, master records, events, alerts, metrics and audit logs.
- Executable ETL/ELT pipelines backed by a dynamically discovered capability catalog.
- Searchable data catalog, classification policies, RBAC primitives and audit trail.
- Data-quality rules, golden-record MDM, OLAP aggregation and recommendations.
- Stateful stream windows and complex-event rules that produce persisted alerts.
- Responsive BI portal and JSON REST API built entirely with the Python standard library.
- 1,020 executable capability modules across 34 data disciplines. Every module is
  imported and executed by the automated validation suite.

## Architecture

```text
Browser / CLI / REST clients
            |
       API + Portal
            |
 Catalog | Pipelines | Quality | MDM | OLAP | Streaming/CEP | Governance
            |
 Executable capability registry (1,020 modules / 34 families)
            |
 SQLite control plane + versioned JSON datasets + metrics + audit log
```

## Quick start

Requires Python 3.11 or newer. No package download is needed.

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
python -m dip validate
python -m dip demo
$env:DIP_API_KEY = "development-key"
python -m dip serve --port 8080
```

Open `http://127.0.0.1:8080`. The default local API key used by the portal is
`development-key`; set `DIP_API_KEY` and update the client for non-local use.

## CLI

```text
dip demo                         Seed all major platform flows
dip ai-demo                      Train, deploy, predict and run grounded RAG
dip ask "question"               Ask the local grounded assistant
dip status                       Show operational and business KPIs
dip validate                     Import and execute all capability modules
dip ingest data.json --name x    Register and version a JSON dataset
dip serve --host 0.0.0.0         Start the portal and REST API
```

## REST API

| Method | Route | Purpose | Authentication |
|---|---|---|---|
| GET | `/api/health` | Liveness and component counts | Public |
| GET | `/api/overview` | Executive KPIs and recommendations | API key |
| GET | `/api/assets` | Search catalog assets | API key |
| GET | `/api/lineage` | Read lineage edges | API key |
| GET | `/api/capabilities` | Inspect executable capability catalog | API key |
| POST | `/api/ingest` | Register a versioned dataset | API key |
| POST | `/api/query` | Execute grouped OLAP aggregation | API key |
| POST | `/api/demo` | Seed demonstrative end-to-end data | API key |
| GET | `/api/ai/models` | List registered models and deployments | API key |
| GET | `/api/ai/vector/collections` | List vector collections | API key |
| POST | `/api/ai/train` | Train and version a model | API key |
| POST | `/api/ai/automl` | Infer task/features and train a model | API key |
| POST | `/api/ai/deploy` | Deploy a model version | API key |
| POST | `/api/ai/predict` | Run model inference | API key |
| POST | `/api/ai/drift` | Measure feature drift | API key |
| POST | `/api/ai/vector/upsert` | Index a knowledge document | API key |
| POST | `/api/ai/vector/search` | Semantic vector search | API key |
| POST | `/api/ai/chat` | Grounded RAG assistant | API key |
| POST | `/api/ai/agent/run` | Execute an allowlisted agent plan | API key |
| POST | `/api/ai/expert/evaluate` | Evaluate explainable expert rules | API key |
| POST | `/api/ai/nlp` | NLP analysis | API key |
| POST | `/api/ai/document` | Intelligent document processing | API key |
| POST | `/api/ai/recommend` | Hybrid recommendation ranking | API key |
| POST | `/api/ai/vision/analyze` | Analyze a base64 PGM image | API key |

## AI/ML runtime

The bundled runtime is deliberately local and auditable. Regression,
classification and clustering use actual learned parameters; deployments point
to immutable versions and every prediction is persisted with latency. Vector
documents use deterministic normalized feature-hashing embeddings. The default
assistant is extractive and answers only from retrieved evidence, so it works
offline and does not pretend to be a frontier LLM. `LanguageModel` is the
provider boundary for plugging in a generative model when desired.

Agent plans are bounded, reject common prompt-injection patterns and can call
only registered tools. The Document AI path supports text, HTML, JSON and CSV;
the vision path supports dependency-free P2 PGM analysis. General-purpose OCR,
speech recognition and natural-voice TTS require a specialized model/provider
and are not falsely emulated by the core runtime.

Use the `X-API-Key` header. Roles are `viewer`, `analyst`, `engineer`, `steward`
and `admin`, configured through `DIP_API_ROLE` for the built-in HTTP adapter.

## Capability families

The registry includes 30 executable controls for each of these 34 families:
business intelligence, analytics, data visualization, reporting, warehouse,
lake, lakehouse, DBMS, integration, ETL, ELT, iPaaS, catalog, governance,
quality, MDM, observability, fabric, mesh, big data, stream processing, CEP,
OLAP, decision support, semantic layer, orchestration, connectors, privacy,
metadata, feature store, reverse ETL, MLOps, geospatial analytics and FinOps.

Each module declares metadata plus a real operation: profiling, filtering,
projection, derivation, aggregation, validation, deduplication, masking,
classification or timestamp enrichment. `dip.registry` discovers the modules,
rejects duplicate codes and exposes them to pipelines and the API.

## Data and security

The database defaults to `var/platform.db`; set `DIP_DATA_DIR` or pass
`--database` to move it. WAL mode and foreign keys are enabled. Inputs are
parameterized, catalog fields are JSON encoded, static paths are constrained to
the web root, API keys use constant-time comparison, and browser output escapes
untrusted values. The included authentication is intentionally lightweight; put
the server behind TLS and an identity-aware gateway for production deployment.

## Testing and validation

The tests cover the platform journey, every one of the 1,020 capability modules,
pipelines, OLAP, MDM, governance and access-control helpers. The validation CLI
is also suitable for packaging checks:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
python -m dip --database var/validation.db validate
```

## Project map

```text
src/dip/api.py             HTTP API and static portal
src/dip/service.py         Application facade and end-to-end orchestration
src/dip/storage.py         SQLite schema and safe data access
src/dip/pipeline.py        ETL/ELT execution with persisted jobs
src/dip/analytics.py       OLAP aggregation and decision support
src/dip/quality.py         Rule evaluation and quality scoring
src/dip/streaming.py       Stream windows and CEP alerts
src/dip/mdm.py             Golden-record consolidation
src/dip/governance.py      Classification and auditing
src/dip/observability.py   Health, metrics and operational counters
src/dip/capabilities/      1,020 executable domain capability modules
src/dip/web/               Accessible responsive BI portal
tests/                     Standard-library automated test suite
tools/scaffold.py          Reproducible source catalog generator
```

## License

MIT. See `LICENSE`.
