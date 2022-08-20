
def responsesBot(response):

    response('Bienvenido al chatbot del ITLA, en qué le puedo ayudar?', ['hola', 'saludos', 'klk', 'buenas', 'buen dia'], single_message=True)
    response('El Instituto Tecnológico de las Américas (ITLA), es una institución técnica de estudios superiores especializada en educación tecnológica en la República Dominicana.', ['que', 'itla', 'es', ], required_word=['itla'])
    response('El ITLA fue fundada por el Estado Dominicano em el año 2000', ['cuando', 'fundada', 'año', 'creo', 'creada', 'crearon'], single_message=True)
    response('Su actual rector es el Ing. Omar Méndez Lluberes', ['quien', 'rector', 'dirige', 'director', 'manda'], single_message=True)
    response('El objetivo principal del itla es transformar a la juventud dominicana mediante la formacion académica especializada en la tecnología', ['cual', 'objetivo', 'fin', ], required_word=['objetivo'])
    response('Desarrollo de Software, Mecatrónica, Seguridad Informática, Multimedia, Análisis de Datos', ['carreras', 'cuales', 'dan'], required_word = ['carreras'])
    response('Sus periodos estudiantiles se basan en cuatrimestres (4 meses)', ['periodo', 'cuatrimestre', 'trimestre', 'semestre',], single_message=True)
    response('Las carrerras en el ITLA suelen durar 7 cuatrimestres, aunque eso va a depender de la carrera', ['cuanto duran', 'tiempo', 'carrera', 'terminan', 'se acaba', 'graduar'], required_word=['duran'])
    response('El ITLA está ubicado en el Km.27, calle 27, La Caleta',['donde', 'ubicados', 'ubicacion', 'location', 'oficina principal'], single_message=True)
    response('(809) 738-4852 ', ['numero', 'telefono', 'celular', 'contacto', 'movil', 'llamar', 'llamada'], single_message=True)