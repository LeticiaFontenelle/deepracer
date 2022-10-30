agente - veículo - para seguir a linha central
    '''
    
    # Lê os parâmetros de entrada

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calcula os 3 marcadores - distâncias variadas da linha central

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Conceda uma recompensa maior se o carro estiver mais perto da linha central e vice-versa

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # provável queda/perto do caminho
    
    return float(reward)