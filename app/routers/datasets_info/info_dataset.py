from fastapi import APIRouter, File, Response, UploadFile, Form
from io import BytesIO

from app.metadata.tipo_arch import TipoArch
from app.parser.info_data_set_parser import validar_tipo_log


data_info_router = APIRouter(prefix='/info_dataset', tags=['info_data_set'])


@data_info_router.post('/obtener-informacion', status_code=200)
async def agregar_informacion(sep: str = Form(), file: UploadFile = File()
                        ) -> dict:
    """Obtiene la información general del dataset.

    Args:
        file: archivo cargado por el usuario
        sep: Separador del archivo

    Returns:
        información detallada del dataset.

    """
    file_name = file.filename
    extencion = validar_tipo_log(file_name.split('.')[-1])
    funcion_lectura = TipoArch.lectura.get(extencion)
    content = await file.read()
    if 'x' in extencion:
        dataset = funcion_lectura(BytesIO(content))
    else:
        dataset = funcion_lectura(BytesIO(content), sep=sep)

    info = dataset.describe()
    data = info.to_dict()

    return data
