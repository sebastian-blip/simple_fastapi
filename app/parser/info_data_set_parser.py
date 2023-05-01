from fastapi import HTTPException

from app.metadata.tipo_arch import TipoArch


def validar_tipo_log(tipo_arch: str) -> str:
    """ Válida que la extencion sea correcta.

    Args:
        tipo_arch: Tipo de log a validar.

    Returns:
        tipo de archivo validado.

    """
    if tipo_arch not in TipoArch.tipos:
        msg = (f'Tipo log invalido: {tipo_arch}. Las extensions' 
               f'validos son {TipoArch.tipos}')
        raise HTTPException(status_code=422, detail=msg)

    return tipo_arch
