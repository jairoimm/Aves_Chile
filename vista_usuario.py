def vista_usuario(cards):
    plantilla = f'''
    
    <!doctype html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        body {{
            background-color: #f8f9fa; /* Un color de fondo suave */
        }}
        .header-title {{
            margin-top: 40px;
            margin-bottom: 40px;
            color: #343a40; /* Un color oscuro para el título */
            font-weight: 700;
        }}
        .card-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px; /* Espacio entre las tarjetas */
            justify-content: center; /* Centrar las tarjetas en el contenedor */
            padding-bottom: 50px; /* Espacio al final de la página */
        }}
        .card {{
            border: none; /* Eliminar borde predeterminado */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Sombra suave para un efecto 3D */
            transition: transform 0.2s ease-in-out; /* Transición suave al pasar el mouse */
            border-radius: 10px; /* Bordes redondeados */
            overflow: hidden; /* Asegurar que la imagen no sobresalga */
        }}
        .card:hover {{
            transform: translateY(-5px); /* Pequeño levantamiento al pasar el mouse */
        }}
        .card-img-top {{
            height: 200px; /* Altura fija para las imágenes */
            object-fit: cover; /* Recortar la imagen para que cubra el espacio */
        }}
        .card-body {{
            text-align: center;
        }}
        .list-group-item {{
            font-size: 0.9em;
            color: #6c757d;
        }}
    </style>
    </head>

    <body>
        <div class="container">
            <h1 class="text-center header-title">Descubre las Aves de Chile</h1>
            <div class="card-container">
                {cards}
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    return plantilla