# parent image
FROM python

# cartella di lavoro nell'immagine --> container
WORKDIR home/isa

# copio il file locale isa-0.0.1-py3-none-any.whl il punto inidca che copio il file nella cartella corrente di destinazione (definita da workdir)
COPY dist/isa-0.0.1-py3-none-any.whl .

# python -m pip install isa-0.0.1-py3-none-any.whl 
RUN ["python", "-m", "pip", "install", "isa-0.0.1-py3-none-any.whl"]

# isa --predicted 1 2 3 --expected 1 2 4 --metrics MAE
# ENTRYPOINT ["isa", "--predicted", "1", "2", "3", "--expected", "1", "2", "4", "--metrics", "MAE"]
ENTRYPOINT ["isa"]