from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASETS_DIR = PROJECT_ROOT / "datasets"
SRC_DIR = PROJECT_ROOT / "src"
SQL_DIR = PROJECT_ROOT / "sql"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"
LOGS_DIR = PROJECT_ROOT / "logs"

# Arquivos específicos
CUSTOMERS_CSV = DATASETS_DIR / "customers.csv"
ORDERS_CSV = DATASETS_DIR / "orders.csv"
PRODUCTS_CSV = DATASETS_DIR / "products.csv"