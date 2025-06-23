def crear_card(datos):
    cards = ''
    for dato in datos:
        cards += f'''
    <div class="card" style="width: 18rem;">
        <img src="{dato['images']['thumb']}" class="card-img-top" alt="{dato['name']['spanish']}">
        <div class="card-body">
            <h5 class="card-title">{dato['name']['spanish']}</h5>
            <p class="card-text">Una fascinante ave de Chile.</p>
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">**Nombre en Inglés:** {dato['name']['english']}</li>
            <li class="list-group-item">**Nombre en Latín:** *{dato['name']['latin']}*</li>
        </ul>
        <div class="card-footer text-center">
            <small class="text-muted">Más información próximamente</small>
        </div>
    </div>
    '''
    return cards