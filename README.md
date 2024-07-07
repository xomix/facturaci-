# facturació

## Requirements

- Install tesseract from https://github.com/UB-Mannheim/tesseract/wiki
- Install poppler from https://github.com/oschwartz10612/poppler-windows
- Install opencv https://sourceforge.net/projects/opencvlibrary/files/latest/download

## Model

### Initialise the model:

aerich init -t src.database.config.TORTOISE_ORM
aerich init-db

### When de model changes

aerich migrate
aerich upgrade