# facturació

## Requirements

- Install tesseract from https://github.com/UB-Mannheim/tesseract/wiki
- Install poppler from https://github.com/oschwartz10612/poppler-windows
- Install opencv https://sourceforge.net/projects/opencvlibrary/files/latest/download

## Model

### Initialise the model:

docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db

### When de model changes

docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade