# differential-drive-excitation

## Français

Vérifier si des trajets identifient les paramètres des roues.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m differential_drive_excitation examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Empile équations distance et lacet de cinématique différentielle et résout les rayons par moindres carrés ; expose le rang insuffisant au lieu d’inventer un rayon.

### Limites

Voie connue, données indépendantes sans glissement supposées ; distance et lacet traités à poids égal dans leurs unités. Pas une calibration certifiée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Check whether trajectories identify wheel parameters.

Synthetic data; no network access or secret required.

```sh
python -m differential_drive_excitation examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Stacks differential-drive distance and yaw equations and solves wheel radii by least squares; exposes deficient excitation instead of inventing a radius.

### Limits

Known track width and independent slip-free data assumed; distance and yaw weighted equally in their units. Not certified calibration.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comprobar si trayectorias identifican parámetros de ruedas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m differential_drive_excitation examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Apila ecuaciones de distancia y giro diferencial y estima radios por mínimos cuadrados; expone excitación insuficiente sin inventar radios.

### Límites

Supone ancho conocido y datos independientes sin deslizamiento; distancia y giro ponderados igual en sus unidades. No calibración certificada.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://control.ros.org/rolling/doc/ros2_controllers/diff_drive_controller/doc/userdoc.html
