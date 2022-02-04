# -*- coding: utf-8 -*-

"""Para ver el contenido de archivos muy grandes se recomienda correr el siguiente comando desde la AWS CLI:


aws s3 cp s3://BUCKET-NAME/TARFILE.tar - | tar -tvf -


Para extraer archivos individuales intentar:

aws s3 cp s3://fastq-59samples/data_release2.tar - | tar -xvf - ./data_release2/China-NovoPM-Pharma-IM-PHUSC2019122101.tar.gz


"""

#Aquí se ingresan el bucket y el nombre del objeto que se quiere inspeccionar

bucket = 'fastq-59samples'
tarfile_key = 'data_release3.tar'

#Se importan las librerías necesarias

import boto3
from io import BytesIO
import tarfile
from botocore.client import Config

#Creamos un objeto de configuración para poder acceder a AWS

#config = Config(connect_timeout=5, retries={'max_attempts': 0})

config = Config(connect_timeout=900, read_timeout = 900, retries={'max_attempts': 0})

#Creamos el cliente Python boto3 para acceder a s3

s3 = boto3.client('s3', use_ssl=False, config =config)  # optional

#Creamos el objeto s3 en modo lectura

s3_object = BytesIO(s3.get_object(Bucket=bucket, Key=tarfile_key)['Body'].read())

#Se abre el archivo .tar a partir del objeto seleccionado

tarf = tarfile.open(fileobj=s3_object)

#Se obtienen los nombres de los archivos comprimidos dentro del .tar

names = tarf.getnames()
for name in names:
    print(name)

"""
Para extraer carpetas específicas intentar:

tarf.extract(member='China-Pharma-CAP-NovoPM-IM-PHUSC2020040201_M872-D713-E773.tar', path = './data_release3/')

"""
