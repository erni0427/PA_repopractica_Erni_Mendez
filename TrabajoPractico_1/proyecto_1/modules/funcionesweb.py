import datetime
def fechaHora():
    dataHora= datetime.datetime.now().time()
    
    dataFecha = datetime.datetime.now()
    dia=  str(dataFecha.day) if len(str(dataFecha.day))==2 else '0'+str(dataFecha.day)
    mes = str(dataFecha.month) if len(str(dataFecha.month))==2 else '0'+str(dataFecha.month)
    hora= str(dataHora.hour) if len(str(dataHora.hour))==2 else '0'+str(dataHora.hour)
    minutos= str(dataHora.minute)  if len(str(dataHora.minute))==2 else '0'+str(dataHora.minute) 
    
    fechaActual= str(dataFecha.year)+ "/"+ dia + "/"  + mes  
    horaActual= hora + ":" + minutos
    
    fecha=fechaActual + " " + horaActual
    return (fecha)